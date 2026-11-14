#!/usr/bin/env python3
"""Generate a by-actor conformance table for a narrative page, and audit the
hand-written quick-reference matrix against the rules found on the page.

WHERE THIS LIVES

This script is not in the IG repo. It sits with the other US Core generator
scripts in the MyNotebooks CapStatement folder, locally at
~/Documents/Python/Jupyter/MyNotebooks/CapStatement/gen_conformance_table.py
and published at
https://github.com/Healthedata1/MyNotebooks/blob/master/CapStatement/gen_conformance_table.py
It is listed in the US Core README under "US Core Python Scripts", in the table
that maps each page to the collection it renders and the script that writes it.

HOW TO RUN IT

It takes the IG repo from the current directory, so the normal invocation is
from the repo root:

    cd ~/Documents/FHIR/US-Core
    python3 ~/Documents/Python/Jupyter/MyNotebooks/CapStatement/gen_conformance_table.py

    ... --check         # write nothing; exit 1 if the page block is stale
    ... --page foo      # another page under input/pagecontent
    ... --repo PATH     # an IG repo other than the current directory

What it does

1. Parses the page for normative bullets: a "**Client Requirements**",
   "**Server Requirements**" or "**Requirements**" block sets the actor, and any
   bullet under it carrying a bolded RFC 2119 verb is a rule. Bullets in the
   per-mode "Additional Rules and Guidance for X" subsections use a different
   shape -- the verb sits mid-sentence -- so the actor is read from the sentence.
2. Assigns each rule a stable ID from an append-only registry
   (input/data/<page>-requirements.csv). IDs are never renumbered: a reworded
   rule keeps its ID through a close-match lookup, a deleted rule's row is kept
   and marked retired, and only an unseen rule draws a new number. Sequential
   numbering at generation time would silently invalidate every tracker or test
   plan citing an ID.
3. Rewrites the table between the generated markers in the page.
4. Audits the hand-written quick-reference matrix, which is deliberately NOT
   generated: deciding that a rule is solicited-only is judgment about scope,
   and nothing in the markup states it. The audit reports mode-specific rules
   with no matrix row, and matrix rows whose code tokens have left the page.

Table and matrix cells escape "|" because kramdown splits a table row on pipes
before inline code spans are parsed (see ../CLAUDE.md).
"""

import argparse
import csv
import difflib
import re
import sys
from pathlib import Path

# The repo root is the working directory (or --repo), not the script's own
# folder: the script lives outside the IG repo.
REPO = Path.cwd()


def find_repo(arg):
    base = Path(arg).resolve() if arg else Path.cwd()
    if not (base / "input" / "pagecontent").is_dir():
        sys.exit(
            "error: %s is not an IG repo root (no input/pagecontent). "
            "Run from the repo root or pass --repo." % base
        )
    return base

VERB_RE = re.compile(r"\*\*(SHALL NOT|SHALL|SHOULD NOT|SHOULD|MAY NOT|MAY)\*\*")
BULLET_RE = re.compile(r"^\s*[-*]\s+(\S.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
REQ_BLOCK_RE = re.compile(r"^\*\*(?:(Client|Server)\s+)?Requirements\*\*\s*$")
BOLD_ONLY_RE = re.compile(r"^\*\*[^*].*?\*\*\s*$")
MODE_HEADING_RE = re.compile(r"^Additional Rules and Guidance for\s+(.*)$")
CODE_SPAN_RE = re.compile(r"`([^`]+)`")

# A statement is flagged conditional when its text carries a precondition: a
# "when"/"if"/"unless"/"where" clause, a purpose clause ("To supersede a
# document, clients SHOULD ..."), or a qualified subject ("Servers that allow
# status correction ... SHALL ..."). The flag is a seed, not an oracle -- it is
# written to the registry once and a hand-edited value there is never
# overwritten, so a wrong call is corrected in one place and stays corrected.
CONDITIONAL_RES = [
    re.compile(r"\bwhen\b", re.I),
    re.compile(r"\bif\b", re.I),
    re.compile(r"\bunless\b", re.I),
    re.compile(r"\bwhere\b", re.I),
    re.compile(r"^To\s+\w+", re.I),
    re.compile(r"\b(?:Servers?|Clients?)\s+that\b", re.I),
]


def detect_conditional(text):
    # Code spans first: "conditional create (`If-None-Exist`)" is not a
    # conditional statement, it just contains the word in a header name.
    bare = CODE_SPAN_RE.sub(" ", text)
    return any(rx.search(bare) for rx in CONDITIONAL_RES)

# Matches the green check already used for the IPA/IPS ratings on
# relationship-with-other-igs.md, so the glyph is consistent across the IG.
CHECK = '<span style="color:green; font-size:1.5em">&#10004;</span>'

# Short mode codes for the conformance table. A rule picks up a code only from
# the per-mode section it sits in; a rule stated in a general section is ALL
# even when a reader would scope it tighter, because nothing in the markup says
# so. Override "mode_code" in the registry to scope one by hand.
MODE_CODES = {
    "Provider Write": "PROV",
    "Solicited Patient Write": "SPAT",
    "Unsolicited Patient Write": "UPAT",
}

# PAT covers both patient modes. No section derives it -- a statement that
# spans the two patient modes always sits in a general section -- so it only
# ever arrives as a hand-set "mode_code" in the registry.
VALID_MODE_CODES = {"ALL", "PROV", "SPAT", "UPAT", "PAT"}

BEGIN = "<!-- BEGIN generated conformance table -- gen_conformance_table.py: edit the requirement bullets above, not this table -->"
END = "<!-- END generated conformance table -->"

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "for", "in", "on", "with", "that",
    "their", "they", "it", "its", "is", "are", "be", "been", "when", "whether",
    "both", "at", "least", "one", "by", "as", "not", "no", "any", "all", "from",
    "servers", "server", "clients", "client", "shall", "should", "may",
}


def link_defs():
    """Reference-style link definitions from input/includes/link-list.md.

    A requirement cell is rendered on its own through Liquid's markdownify, so a
    reference-style label has no definition in scope and would print as literal
    brackets. The labels are expanded to inline links on the way into the CSV.
    """
    out = {}
    # link-list.md includes requirements-, r4- and page-link-list.md, so every
    # one of them has to be read -- the label a requirement uses can be defined
    # in any of the four.
    for path in sorted((REPO / "input" / "includes").glob("*link-list*.md")):
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.match(r"^\[([^\]]+)\]:\s*(\S+)", line.strip())
            if m:
                out.setdefault(m.group(1), m.group(2))
    return out


def resolve_refs(text, defs):
    def sub(m):
        label = m.group(1)
        url = defs.get(label)
        return "[%s](%s)" % (label, url) if url else m.group(0)

    return re.sub(r"\[([^\]\[]+)\](?![(:\[])", sub, text)


def anchor(title):
    """kramdown's auto id: lowercase, drop punctuation, spaces to hyphens."""
    text = re.sub(r"[^a-z0-9 _-]", "", title.lower())
    return re.sub(r"-{2,}", "-", text.replace(" ", "-")).strip("-")


def norm(text):
    """Normalized key for registry lookup: wording-stable, markup-insensitive."""
    text = re.sub(r"[`*_\[\]]", "", text.lower())
    text = re.sub(r"\(#[^)]*\)", "", text)
    return re.sub(r"[^a-z0-9 ]", " ", text).strip()


def esc(cell):
    return cell.replace("|", r"\|")


def code_tokens(text):
    out = set()
    for span in CODE_SPAN_RE.findall(text):
        out.add(span.strip().lower())
    return out


def keywords(text):
    words = re.findall(r"[a-z0-9.]{3,}", norm(text))
    return {w for w in words if w not in STOPWORDS}


class Rule:
    def __init__(self, text, actor, verb, section, section_anchor, mode, flagged, line):
        self.text = text
        self.actor = actor
        self.verb = verb
        self.section = section
        self.section_anchor = section_anchor
        self.mode = mode
        self.flagged = flagged      # inside a bg-warning / bg-info block
        self.line = line
        # Scoped key: the same sentence appears verbatim under more than one
        # section or mode (the PATAST rules, for example), and a text-only key
        # would hand both occurrences the same ID and retire a live row.
        self.key = norm(text) + " :: " + norm(mode or section)
        self.conditional_auto = "Yes" if detect_conditional(text) else ""
        self.conditional = self.conditional_auto
        self.text_rendered = text      # set once link definitions are loaded
        self.mode_code_auto = MODE_CODES.get(mode, "ALL")
        self.mode_code = self.mode_code_auto
        self.id = None


def parse(lines):
    """Walk the page, returning (rules, matrix_rows, heading_titles)."""
    rules, matrix_rows, titles = [], [], []
    headings = {}
    block_actor = None
    mode = None
    section = section_anchor = ""
    flagged = in_comment = in_mermaid = 0
    in_matrix = False

    for n, raw in enumerate(lines, start=1):
        line = raw.rstrip()
        stripped = line.strip()

        # --- raw-HTML and comment regions -------------------------------
        if in_comment:
            in_comment = 0 if "-->" in stripped else 1
            continue
        if stripped.startswith("<!--") and "-->" not in stripped:
            in_comment = 1
            continue
        if in_mermaid:
            if "</div>" in stripped:
                in_mermaid = 0
            continue
        if 'class="mermaid"' in stripped:
            in_mermaid = 1
            continue
        if 'class="bg-warning"' in stripped or 'class="bg-info"' in stripped:
            flagged = 1
            continue
        if stripped.startswith("</div>"):
            flagged = 0
            continue

        # --- headings ---------------------------------------------------
        m = HEADING_RE.match(line)
        if m:
            level, title = len(m.group(1)), m.group(2)
            headings[level] = title
            for deeper in [k for k in headings if k > level]:
                headings.pop(deeper)
            titles.append(title)
            block_actor = None
            in_matrix = title.lower().startswith("quick-reference")
            mm = MODE_HEADING_RE.match(title)
            mode = mm.group(1) if mm else None
            # Section cell: the deepest heading at h4 or h5 -- h6 is the
            # per-mode "Additional Rules" wrapper, whose h5 names the mode.
            for lvl in (5, 4, 3):
                if lvl in headings:
                    section = headings[lvl]
                    section_anchor = anchor(section)
                    break
            continue

        if in_matrix:
            if stripped.startswith("|") and not re.match(r"^\|[\s|:-]+\|?$", stripped):
                cells = [c.strip() for c in stripped.strip("|").split("|")]
                if cells and cells[0].lower() != "rule":
                    matrix_rows.append(cells)
            continue

        # Table rows and bold-only labels are never rules. A bold label such as
        # "**Guidance**" ends the current requirements block.
        if stripped.startswith("|") or stripped.startswith("{:"):
            continue
        if REQ_BLOCK_RE.match(stripped):
            block_actor = REQ_BLOCK_RE.match(stripped).group(1)
            continue
        if BOLD_ONLY_RE.match(stripped):
            block_actor = None
            continue
        if stripped in ("---", ""):
            continue

        b = BULLET_RE.match(line)
        if not b:
            continue
        text = b.group(1).strip()
        v = VERB_RE.search(text)
        if not v:
            continue

        actor = block_actor
        if actor is None:
            before = text[: v.start()]
            who = re.search(r"\b(Servers?|Clients?)\b", before, re.I) or re.search(
                r"\b(Servers?|Clients?)\b", text, re.I
            )
            actor = who.group(1).rstrip("s").capitalize() if who else "Unspecified"

        plain = VERB_RE.sub(lambda mo: mo.group(1), text)
        rules.append(
            Rule(plain, actor, v.group(1), section, section_anchor, mode, bool(flagged), n)
        )

    return rules, matrix_rows, titles


def load_registry(path):
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def assign_ids(rules, registry, prefix):
    """Append-only ID assignment. Exact key, then close match, then a new number."""
    by_key = {r["key"]: r for r in registry}
    used = set()
    seen_ids = set()
    report = {"new": [], "reworded": [], "retired": []}

    for rule in rules:
        row = by_key.get(rule.key)
        if row is not None and row["key"] in used:
            row = None
        if row is None:
            pool = [
                r for r in registry
                if r["actor"] == rule.actor and r["key"] not in used
            ]
            match = difflib.get_close_matches(
                rule.key, [r["key"] for r in pool], n=1, cutoff=0.9
            )
            if match:
                row = next(r for r in pool if r["key"] == match[0])
                report["reworded"].append((row["id"], row["requirement"], rule.text))
        if row is not None:
            rule.id = row["id"]
            # The registry keeps both the effective flag and the value the
            # detector produced when the row was written. Equal means nobody
            # touched it, so it is re-seeded from the current detection;
            # different means a human edited "conditional", and that edit wins
            # for good. No "manual" bookkeeping column for the author to set.
            stored = (row.get("conditionality") or "").strip()
            stored_auto = (row.get("conditionality_auto") or "").strip()
            if stored != stored_auto:
                rule.conditional = (
                    "" if stored.lower() in ("no", "-", "none", "") else stored
                )
            m_stored = (row.get("mode_code") or "").strip().upper()
            m_auto = (row.get("mode_code_auto") or "").strip().upper()
            if m_stored and m_stored != m_auto:
                rule.mode_code = m_stored
            used.add(row["key"])
            seen_ids.add(row["id"])

    letter = {"Client": "C", "Server": "S"}
    nums = []
    for r in registry:
        m = re.search(r"-(\d+)$", r["id"])
        if m:
            nums.append(int(m.group(1)))
    nxt = max(nums, default=0) + 1
    for rule in rules:
        if rule.id is None:
            rule.id = f"{prefix}-{letter.get(rule.actor, 'X')}-{nxt:02d}"
            nxt += 1
            report["new"].append((rule.id, rule.text))
            seen_ids.add(rule.id)

    rows = []
    for rule in rules:
        rows.append({
            "id": rule.id,
            "actor": rule.actor,
            "conformance": rule.verb,
            "conditionality": rule.conditional,
            "conditionality_auto": rule.conditional_auto,
            "mode_code": rule.mode_code,
            "mode_code_auto": rule.mode_code_auto,
            "requirement": rule.text_rendered,
            "section": rule.section,
            "section_anchor": rule.section_anchor,
            "unresolved": "yes" if rule.flagged else "",
            "mode": rule.mode or "",
            "status": "active",
            "key": rule.key,
        })
    for r in registry:
        if r["id"] not in seen_ids:
            r["status"] = "retired"
            rows.append(r)
            report["retired"].append((r["id"], r["requirement"]))
    return rows, report


def render_block(rules, csv_stem):
    """The whole generated block: the legend, the inline documentation of the
    CSV, and the Liquid that renders it.

    The table is Liquid over site.data rather than literal markdown rows, in the
    same shape as the us_core_requirements table on requirements.md, so the
    statements live in one place -- the CSV -- and the page carries only the
    rendering. The legend and the column documentation are generated with the
    table because a hand-kept copy would survive a column change and start
    lying about it.
    """
    data_name = csv_stem
    out = [
        "**Legend**",
        "",
        "* **Mode** - `ALL` applies to every submission mode. "
        "`PROV` [Provider Write](#provider-write), "
        "`SPAT` [Solicited Patient Write](#solicited-patient-write), "
        "`UPAT` [Unsolicited Patient Write](#unsolicited-patient-write), "
        "`PAT` both patient modes. "
        "A statement in a general section is `ALL` unless it is scoped tighter.",
        "* **Conformance** - the RFC 2119 verb as written in the statement.",
        "* **Conditional** - " + CHECK + " marks a statement with a precondition "
        "in its text, for example \"when it is held for review\". A \"-\" means "
        "the statement applies whenever its mode applies.",
    ]
    if any(r.flagged for r in rules):
        out.append(
            "* &dagger; - the statement sits in an unresolved block on this page "
            "and is not settled."
        )
    out += [
        "",
        "<!-- ========================================================",
        "The liquid syntax below generates the conformance requirements table.",
        "The source is a csv file at input/data/%s.csv, which is" % data_name,
        "generated from the requirement bullets on this page by the python script",
        "at https://github.com/Healthedata1/MyNotebooks/blob/master/CapStatement/",
        "gen_conformance_table.py (locally ~/Documents/Python/Jupyter/MyNotebooks/",
        "CapStatement/gen_conformance_table.py), run from the repo root. The",
        "bullets are the thing to edit, then rerun the script. See the README",
        "section \"US Core Python Scripts\".",
        "Two columns are meant to be hand-edited and are preserved: mode_code and",
        "conditionality (see below).",
        "",
        "%s.csv columns:" % data_name,
        "- id: stable requirement id, \"WD-<C|S>-<nn>\". Assigned once from this",
        "  append-only csv and never renumbered, so a tracker or test plan can cite",
        "  it. A reworded statement keeps its id through a close-match lookup; a",
        "  deleted one keeps its row with status = retired.",
        "- actor: Client or Server. From the \"**Client Requirements**\" or",
        "  \"**Server Requirements**\" block the bullet sits under, or from the",
        "  subject of the sentence in the per-mode sections, which do not use those",
        "  block headers.",
        "- mode_code: the submission mode the statement applies to. ALL, PROV",
        "  (Provider Write), SPAT (Solicited Patient Write), UPAT (Unsolicited",
        "  Patient Write), or PAT (both patient modes). Derived from the enclosing",
        "  per-mode section, so a statement in a general section derives ALL.",
        "  EDITABLE: a hand-set value wins permanently. PAT is only ever hand-set,",
        "  since no single section spans the two patient modes.",
        "- conformance: the RFC 2119 verb as written in the statement: SHALL,",
        "  SHALL NOT, SHOULD, MAY.",
        "- conditionality: \"Yes\" when the statement carries a precondition in its",
        "  text, for example \"when it is held for review\". Detected from a",
        "  when/if/unless/where clause, a purpose clause, or a qualified subject",
        "  (\"Servers that allow ...\"), ignoring code spans. EDITABLE: a hand-set",
        "  value wins permanently, which is how a wrong guess is corrected.",
        "- requirement: a direct quote of the statement from this page. Markdown.",
        "  Reference-style links are expanded to inline links, because the cell is",
        "  rendered on its own by markdownify and link-list.md is not in scope.",
        "- section: the title of the section the statement came from.",
        "- section_anchor: that section's generated id, used for the link back.",
        "- unresolved: \"yes\" when the statement sits in an unresolved block on",
        "  this page. Rendered as a dagger beside the id.",
        "- mode: the full name of the per-mode section, empty in a general section.",
        "- mode_code_auto, conditionality_auto: what the script derived when the row",
        "  was written. Equal to the editable column means nobody overrode it and",
        "  the script re-derives it; different means a hand edit, which the script",
        "  keeps and reports on every run.",
        "- status: active or retired. Retired rows are kept for their ids only and",
        "  are not published in the table.",
        "- key: normalized statement text plus section. Used to match a row to its",
        "  bullet across rewording. Internal to the script.",
        "",
        "The script retrieves, sorts, and selects the table data.",
        "==============================================================-->",
        "",
        "{% assign rows = site.data." + data_name + " -%}",
        '{% assign actors = "Client,Server" | split: "," %}',
        '<table class="grid">',
        "<thead>",
        "  <tr>",
        "    <th>ID</th>",
        "    <th>Actor</th>",
        "    <th>Mode</th>",
        "    <th>Conformance</th>",
        "    <th>Conditional</th>",
        "    <th>Requirement</th>",
        "    <th>Section</th>",
        "  </tr>",
        "</thead>",
        "<tbody>",
        "{% for actor in actors -%}",
        '{% assign actor_rows = rows | where: "actor", actor '
        '| where: "status", "active" | sort: "id" -%}',
        "{% for item in actor_rows -%}",
        '  <tr id="{{ item.id }}">',
        '    <td>{{ item.id }}{% if item.unresolved == "yes" %} &dagger;{% endif %}</td>',
        "    <td>{{ item.actor }}</td>",
        "    <td>{{ item.mode_code }}</td>",
        "    <td><strong>{{ item.conformance }}</strong></td>",
        '    <td style="text-align: center;">{% if item.conditionality == "Yes" %}'
        + CHECK
        + "{% else %}-{% endif %}</td>",
        "    <td>{{ item.requirement | markdownify }}</td>",
        '    <td><a href="#{{ item.section_anchor }}">{{ item.section }}</a></td>',
        "  </tr>",
        "{% endfor -%}",
        "{% endfor -%}",
        "</tbody>",
        "</table>",
        "",
        "<!-- =============================== end liquid "
        "=================================== -->",
    ]
    return "\n".join(out)


def splice(lines, table):
    """Replace the generated block, or create it in place of the stub."""
    text = "\n".join(lines)
    block = f"{BEGIN}\n\n{table}\n\n{END}"
    if BEGIN in text and END in text:
        head, rest = text.split(BEGIN, 1)
        _, tail = rest.split(END, 1)
        return (head + block + tail).split("\n")

    out, i, done = [], 0, False
    while i < len(lines):
        line = lines[i]
        out.append(line)
        m = HEADING_RE.match(line)
        if not done and m and m.group(2).strip().lower() == "conformance requirements":
            i += 1
            # keep the intro prose; drop a stub blockquote and stub table
            while i < len(lines):
                nxt = lines[i].strip()
                if HEADING_RE.match(lines[i]) or nxt == "---":
                    break
                if nxt.startswith(">") or nxt.startswith("|") or nxt.startswith("{:"):
                    i += 1
                    continue
                out.append(lines[i])
                i += 1
            while out and out[-1].strip() == "":
                out.pop()
            out += ["", block, ""]
            done = True
            continue
        i += 1
    if not done:
        sys.exit("error: no '#### Conformance Requirements' heading and no markers")
    return out


def audit(rules, matrix_rows, titles, page_text, preview):
    """Check the hand-written matrix against the rules, by cited ID.

    The matrix cites the IDs this script assigns, so coverage is an exact set
    comparison: every mode-scoped rule has to appear in the matrix, and every
    ID the matrix cites has to still exist. Nothing here infers which mode a
    rule belongs to -- that call stays with the author.
    """
    msgs = []
    by_id = {r.id: r for r in rules}
    cited = set()
    matrix_text = " ".join(" ".join(row) for row in matrix_rows)
    for token in re.findall(r"\b[A-Z]{2,4}-[A-Z]-\d+\b", matrix_text):
        cited.add(token)

    for rule in rules:
        if rule.mode_code != "ALL" and rule.id not in cited:
            msgs.append(
                "matrix: %s (%s) is mode-specific but the matrix does not cite it: %s"
                % (rule.id, rule.mode_code, rule.text[:70])
            )
    for token in sorted(cited):
        if token not in by_id:
            msgs.append(
                "matrix: cites %s, which no longer matches a rule on the page" % token
            )

    # Compare against the whole page with the matrix section itself removed --
    # a token that appears only inside the matrix is a stale citation.
    body = page_text
    head = body.find("#### Quick-reference Matrix")
    if head != -1:
        tail = body.find("\n---\n", head)
        body = body[:head] + (body[tail:] if tail != -1 else "")
    body_codes = code_tokens(body)
    for row in matrix_rows:
        for cell in row[1:]:
            stale = [t for t in code_tokens(cell) if t not in body_codes]
            if stale:
                msgs.append(
                    "matrix: row '%s' cites %s, not found elsewhere on the page"
                    % (row[1][:44], stale)
                )
                break

    for rule in rules:
        if rule.mode_code not in VALID_MODE_CODES:
            msgs.append(
                "invalid mode code '%s' on %s: expected one of %s"
                % (rule.mode_code, rule.id, ", ".join(sorted(VALID_MODE_CODES))))

    flagged_n = sum(1 for r in rules if r.conditional)
    msgs.append("conditional flags: %d of %d rules" % (flagged_n, len(rules)))
    for rule in rules:
        if rule.mode_code != rule.mode_code_auto:
            msgs.append(
                "mode override kept for %s (registry '%s', derived '%s')"
                % (rule.id, rule.mode_code, rule.mode_code_auto))
    for rule in rules:
        if rule.conditional != rule.conditional_auto:
            msgs.append(
                "conditional override kept for %s (registry '%s', detected '%s')"
                % (rule.id, rule.conditional or "-", rule.conditional_auto or "-"))

    seen_text = {}
    for rule in rules:
        seen_text.setdefault(norm(rule.text), []).append(rule)
    for text, group in sorted(seen_text.items()):
        if len(group) > 1:
            where = ", ".join("%s line %d" % (r.section, r.line) for r in group)
            msgs.append(
                "duplicate statement in %d places (%s): %s"
                % (len(group), where, group[0].text[:70]))

    for rule in rules:
        if rule.actor == "Unspecified":
            msgs.append("actor unresolved at line %d: %s" % (rule.line, rule.text[:80]))

    if preview.exists():
        html = preview.read_text(encoding="utf-8", errors="replace")
        for a in sorted(set(r.section_anchor for r in rules)):
            if 'id="%s"' % a not in html:
                msgs.append("anchor #%s is not in the rendered page" % a)
    else:
        msgs.append("note: no rendered page at %s, anchors unverified" % preview)
    return msgs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--page", default="writing-documents")
    ap.add_argument("--prefix", default=None)
    ap.add_argument("--check", action="store_true", help="write nothing; exit 1 if stale")
    ap.add_argument("--no-audit", action="store_true")
    ap.add_argument("--repo", default=None,
                    help="IG repo root (default: the current directory)")
    args = ap.parse_args()

    global REPO
    REPO = find_repo(args.repo)

    page = REPO / "input" / "pagecontent" / f"{args.page}.md"
    registry_path = (
        REPO / "input" / "data" / f"{args.page.replace('-', '_')}_requirements.csv"
    )
    preview = REPO / "temp" / "jekyll-preview" / f"{args.page}.html"
    prefix = args.prefix or "".join(p[0] for p in args.page.split("-")).upper()

    data = page.read_bytes()
    eol = b"\r\n" if b"\r\n" in data else b"\n"
    lines = data.decode("utf-8").replace("\r\n", "\n").split("\n")

    rules, matrix_rows, titles = parse(lines)
    if not rules:
        sys.exit(f"error: no normative bullets found in {page}")

    defs = link_defs()
    for rule in rules:
        rule.text_rendered = resolve_refs(rule.text, defs)

    registry = load_registry(registry_path)
    rows, report = assign_ids(rules, registry, prefix)
    table = render_block(rules, registry_path.stem)
    new_lines = splice(lines, table)
    new_page = eol.join(l.encode("utf-8") for l in new_lines)

    out = ["\n".join(f"{k}: {len(v)}" for k, v in report.items())]
    counts = {}
    for r in rules:
        counts[(r.actor, r.verb)] = counts.get((r.actor, r.verb), 0) + 1
    print(f"{len(rules)} rules: " + ", ".join(
        f"{a} {v} x{n}" for (a, v), n in sorted(counts.items())))
    for kind in ("new", "reworded", "retired"):
        for item in report[kind]:
            print(f"  {kind}: {item[0]} {str(item[1])[:70]}")

    stale = new_page != data
    if args.check:
        print("stale: table would change" if stale else "up to date")
    else:
        if stale:
            page.write_bytes(new_page)
            print(f"wrote {page}")
        else:
            print(f"{page} already current")
        fields = ["id", "actor", "mode_code", "conformance", "conditionality",
                  "requirement", "section", "section_anchor", "unresolved",
                  "mode", "mode_code_auto", "conditionality_auto", "status",
                  "key"]
        with registry_path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
            w.writeheader()
            for row in sorted(rows, key=lambda r: r["id"]):
                w.writerow({k: row.get(k, "") for k in fields})
        print(f"wrote {registry_path} ({len(rows)} rows)")

    if not args.no_audit:
        msgs = audit(rules, matrix_rows, titles, "\n".join(lines), preview)
        print(f"\naudit: {len(msgs)} item(s)")
        for m in msgs:
            print(f"  {m}")

    if args.check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
