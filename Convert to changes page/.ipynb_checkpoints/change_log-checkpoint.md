
### current
- url: http://build.fhir.org/ig/HL7/US-Core
- FHIR version : 4.0.1
#### Changes:
 Continuous Integration Build (latest in version control) - **Content subject to frequent changes**

---

### 4.1.0
- date: 2021-11-30
- url: http://hl7.org/fhir/us/core/2022Jan
- FHIR version : 4.0.1
#### Changes:
 **The January 2022 Ballot**

This Ballot addresses the following issues:
- Adds [United States Core Data for Interoperability (USCDI) V2](https://www.healthit.gov/sites/default/files/page/2021-07/Standards_Bulletin_2021-3.pdf) updates that the Office of the National Coordinator (ONC) published in July of 2021 with these new Data Elements and Classes:
  - **Applied**: [A Social Determinants Of Health (SDOH) Guidance page](http://hl7.org/fhir/us/core/2022Jan/sdoh.html) to document and provide guidance on using US Core to represent and access [SDOH Assessments](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-observation-screening-response.html) and [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-observation-social-history-assessment.html), [Goals](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-goal.html), Interventions represented by [ServiceRequest](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-servicerequest.html) + [Procedure](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-procedure.html), and [Problems/Health Concerns](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-condition.html)
  - **Applied**: [Clinical Tests](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-observation-clinical-test.html) and [Diagnostic Imaging](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-observation-imaging.html) [also see Changes Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-diagnosticreport-note.html)
  - **Applied**: [Patient Gender Identity](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-patient.html) and [Sexual Identity](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-observation-sexual-orientation.html#)
  - **Applied**: **Care Team Member:** Name, Identifier, Location, Telecom and Role [See Change Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-careteam.html) and [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-practitioner.html) and [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-relatedperson.html)
  - **Applied**: **Encounter:** Diagnosis, Disposition, Location, Time, Type [See Change Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-encounter.html)
  - **Applied**: **Problems:** Date of Diagnosis and Date of Resolution [See Change Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-condition.html)
- Continued efforts to link terminology directly to the FHIR® Terminology Service for VSAC Resources ([Value Set Authority Center (VSAC) - NIH](https://vsac.nlm.nih.gov/)) where applicable and as a result align terminology between US Core and [HL7 C-CDA](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=492).
- [Updated uscdii table](http://hl7.org/fhir/us/core/2022Jan/general-guidance.html) for easier browsing.
- Addition of consolidated [CSV and Excel File representations](http://hl7.org/fhir/us/core/2022Jan/downloads.html) of Profiles to  enable testers and analysts to review elements properties across profiles in a single table
- Addressed and applied over 30 trackers submitted by implementers since the previous STU2 ballot for US Core ver 4.0.0:

 **Tracker Status**: **Summary** **Jira Issue** **Link to Updated Content**
  1. **Applied**: Make values in direct and birth sex extensions min=1 [FHIR-26459](https://jira.hl7.org/browse/FHIR-26459) See Change:
     - [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-birthsex.html)
     - [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-direct.html)
  1. **Applied**: FIX imm-1.json NDC/CVX codes QA Error [FHIR-30104](https://jira.hl7.org/browse/FHIR-30104) See Change:
     - [Here](http://hl7.org/fhir/us/core/2022Jan/Immunization-imm-1.html)
     - [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-immunization.html)
  1. **Applied**: Fix patient search parameter definitions to only target Patient  [FHIR-32305](https://jira.hl7.org/browse/FHIR-32305) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/SearchParameter-us-core-allergyintolerance-patient.json.html)
  1. **Applied**: Provide a caution to the user that a query of MedicationRequest does not provide complete information. [FHIR-32720](https://jira.hl7.org/browse/FHIR-32720) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-medicationrequest.html#mandatory-and-must-support-data-elements)
  1. **Applied**: Make Condition.encounter 0..1 MS [FHIR-32844](https://jira.hl7.org/browse/FHIR-32844) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-condition.html)
  1. **Applied**: Correction on USCoreCarePlanProfile Binding [FHIR-32846](https://jira.hl7.org/browse/FHIR-32846) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-careplan.html)
  1. **Applied**: Fix title for BMI Profile [FHIR-32847](https://jira.hl7.org/browse/FHIR-32847) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-bmi.html)
  1. **Applied**: Remove unchanged elements from Differentials [FHIR-32848](https://jira.hl7.org/browse/FHIR-32848) [For example change see](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-diagnosticreport-lab.profile.json.html)
  1. **Applied**: Create US Core slices for category elements [FHIR-32857](https://jira.hl7.org/browse/FHIR-32857) See Change:
     -  [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-documentreference.html)
     -  [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-medicationrequest.html)
     -  [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-servicerequest.html)
     -  [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-condition.html)
  1. **Applied**: Change drug class value set for allergens to align with C-CDA [FHIR-32953](https://jira.hl7.org/browse/FHIR-32953) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-allergyintolerance.html)
  1. **Applied**: Referencing incorrect figure [FHIR-32961](https://jira.hl7.org/browse/FHIR-32961) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/basic-provenance.html#clinical-information-reconciliation-and-incorporation)
  1. **Applied**: Clarify Guidance for missing data for Coding data type element [FHIR-33048](https://jira.hl7.org/browse/FHIR-33048) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/general-guidance.html#missing-data)
  1. **Applied**: Fix us-core-1 Invariant for Observation [FHIR-33052](https://jira.hl7.org/browse/FHIR-33052) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-observation-lab.html#constraints)
  1. **Applied**: Remove requirement to use only 401 from capabiltystatement [FHIR-33069](https://jira.hl7.org/browse/FHIR-33069) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/CapabilityStatement-us-core-server.html#behavior)
  1. **Applied**: US Core to USCDI guidance page -- add patient email [FHIR-33079](https://jira.hl7.org/browse/FHIR-33079) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-patient.html)
  1. **Applied**: Utilize "use" field for patient previous name and previous address [FHIR-33080](https://jira.hl7.org/browse/FHIR-33080) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-patient.html)
  1. **Applied**: Fix search parameter list [FHIR-33123](https://jira.hl7.org/browse/FHIR-33123) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/search-parameters-and-operations.html)
  1. **Applied**: Clarify requirement on date searches without prefix [FHIR-33156](https://jira.hl7.org/browse/FHIR-33156) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/general-guidance.html#search-syntax.html)
  1. **Applied**: Clarify distinction between repeated search params and ""composite"" params [FHIR-33159](https://jira.hl7.org/browse/FHIR-33159) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-observation-lab.html#notes)
  1. **Applied**: Add content as mandatory element in narrative for documentreference [FHIR-33160](https://jira.hl7.org/browse/FHIR-33160) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-documentreference.html)
  1. **Applied**: Fix invalid elements in extensions [FHIR-33233](https://jira.hl7.org/browse/FHIR-33233) See Change:
     - [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-race.html)
     - [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-birthsex.html)
     - [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-direct.html)
  1. **Applied**: Make Procedure.performed conditionally mandatory [FHIR-33243](https://jira.hl7.org/browse/FHIR-33243) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-procedure.html)
  1. **Applied**: add same Null options to Race and Ethnicity [FHIR-34036](https://jira.hl7.org/browse/FHIR-34036) See Change
     - [Here](http://hl7.org/fhir/us/core/2022Jan/ValueSet-omb-ethnicity-category.html)
     - [Here](http://hl7.org/fhir/us/core/2022Jan/ValueSet-omb--detailed-ethnicity.html)
     - [Here](http://hl7.org/fhir/us/core/2022Jan/ValueSet-omb-race-category.html)
     - [Here](http://hl7.org/fhir/us/core/2022Jan/ValueSet-omb-detailed-race.html)
  1. **Applied**: Clarify MustSupport for Observation.component.value[x] vs dataAbsentReason [FHIR-34061](https://jira.hl7.org/browse/FHIR-34061) See Change:
     - [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-blood-pressure.html#mandatory-and-must-support-data-elements)
     - [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-vital-signs.html#mandatory-and-must-support-data-elements)
  1. **Applied**: Add  Null options to US Core Birth Sex Extension [FHIR-34133](https://jira.hl7.org/browse/FHIR-34133) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/ValueSet-birthsex.html)
  1. **Applied**: USCDI v2 update [FHIR-34231](https://jira.hl7.org/browse/FHIR-34231) SEE SECTION ABOVE
  1. **Applied**: Fix Observation Examples using `appliesTo` [FHIR-34286](https://jira.hl7.org/browse/FHIR-34286) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/Observation-serum-calcium.html)
  1. **Applied**: Correct CapabilityStatement SMART IG reference [FHIR-34281](https://jira.hl7.org/browse/FHIR-34281) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/CapabilityStatement-us-core-server.html#should_igs)
  1. **Applied**: Make DiagnosticReport.effective and DiagnosticReport.issued conditionally mandatory [FHIR-34330](https://jira.hl7.org/browse/FHIR-34330) See Change:
      - [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-diagnosticreport-lab.html)
      - [Here](http://hl7.org/fhir/us/core/2022Jan/StructureDefinition-us-core-diagnosticreport-note.html)
  1. **Applied**: Resolution of http://hl7.org/fhir/us/core/OperationDefinition/docref [FHIR-34044](https://jira.hl7.org/browse/FHIR-34044) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/search-parameters-and-operations.html#operations)
  1. **Applied**: US Core search page is not working [FHIR-34028](https://jira.hl7.org/browse/FHIR-34028) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/#) - Coordination with HL7 IG publishing team to Correct

  **The Following Trackers Will be Applied Following this Ballot**

  Due external dependencies and publication tooling limitations, the application of these resolutions have been deferred.

  **Tracker Status**: **Summary**: [**Jira Issue**](#) **Application Status**

  1. **Resolved - change required**: US Core Pulse Oximetry Profile noncomformant UCUM Unit for Oxygen Concentration [FHIR-27845](https://jira.hl7.org/browse/FHIR-27845) -  Awaiting FHIR-4b updates to update base FHIR Vitals Profile, STU Note Present
  1. **Resolved - change required**: Patient Examples QA Errors: CDCREC code system in VSAC [FHIR-30105](https://jira.hl7.org/browse/FHIR-30105) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/#) - Coordination with VSAC and IG publishing team to Correct and align Code System OIDS between FHIR, CCDA, and VSAC, Note To Balloters Present
  1. **Resolved - change required**: valueset-simple-language.xml QA Error [FHIR-30107](https://jira.hl7.org/browse/FHIR-30107) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/#) - Coordination with IG publishing team to Correct - Note To Balloters present
  1. **Resolved - change required**: Display only differential invariants and terminology tables in Differential View [FHIR-30780](https://jira.hl7.org/browse/FHIR-30780) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/#) - Coordination with HL7 IG publishing team to Correct
  1. **Resolved - change required**: Confusing to reads invariants and terminology tables in Differential View [FHIR-30783](https://jira.hl7.org/browse/FHIR-30783) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/#) - Coordination with HL7 IG publishing team to Correct
  1. **Resolved - change required**: Wrong link to IG homepage from package manifest [FHIR-33132](https://jira.hl7.org/browse/FHIR-33132) [See Change Here](http://hl7.org/fhir/us/core/2022Jan/#) - Coordination with HL7 IG publishing team to Correct


---

### 4.0.0
- date: 2021-06-28
- url: http://hl7.org/fhir/us/core/STU4
- FHIR version : 4.0.1
#### Changes:
 The changes in this annual update to US Core have been reviewed and commented upon by the public through the January 2021 HL7 balloting process.  The resolution of the community comments has been agreed to and voted on by the members of the sponsoring work group [HL7 International Cross-Group Projects](http://www.hl7.org/Special/committees/cgp/index.cfm).

The key changes are summarized below:

1. New *Conformance Expectations* page
  - Defining different ways to implement and conform to US Core.
  - Clarification of the Must Support definitions as it relates to various FHIR elements such a choice datatype and references.
2. Publishing a set US Core Vital Signs independent of the FHIR core profile upon which it is based
  - *US Core Vital Signs Profile*
    - *US Core Blood Pressure Profile*
    - *US Core BMI Profile*
    - *US Core Head Circumference Profile*
    - *US Core Body Height Profile*
    - *US Core Body Weight Profile*
    - *US Core Body Temperature Profile*
    - *US Core Heart Rate Profile*
    - *US Core Respiratory Rate Profile*
3. Linking terminology directly to the FHIR® Terminology Service for VSAC Resources ([Value Set Authority Center (VSAC) - NIH](https://vsac.nlm.nih.gov/)) where applicable:
**US Core Value Set, VSAC Value Set, VSAC OID, extensional?** 1. Detailed ethnicity, Detailed Ethnicity, 2.16.840.1.114222.4.11.877, No 1. OMB Ethnicity Categories, Ethnicity, 2.16.840.1.114222.4.11.837, Yes 1. US Core CareTeam Provider Roles, Care Team Member Function, 2.16.840.1.113762.1.4.1099.30, Yes 1. US Core Medication Codes (RxNorm), Medication Clinical Drug, 2.16.840.1.113762.1.4.1010.4, Yes 1. US Core Provider Specialty (NUCC), Healthcare Provider Taxonomy, 2.16.840.1.114222.4.11.1066, No 1. US Core Smoking Status, Smoking Status, 2.16.840.1.113883.11.20.9.38, Yes 1. US Core Vaccine Administered Value Set (CVX), CVX Vaccines Administered Vaccine Set, 2.16.840.1.113762.1.4.1010.6, Yes 1. US Core Common substances for allergy and intolerance documentation including refutations, Common substances for allergy and intolerance documentation including refutations, 2.16.840.1.113762.1.4.1186.8, No
4. Migrating to the standard set of HL7 FHIR IG templates for publishing. Although we strove to minimize the differences between this version and the previous versions of US Core, these changes are notable:
   - Additional Features include:
        - Addition of vocabulary and constraint tables to the profile pages
        - Addition of a summary table and to the profile page introduction
        - Addition of "Snapshot Table (Must Support)" Tab to profile views
   - Due to restrictions on customizable content, the full narrative text summaries of profiles is no longer available.

5. Addressing over 90 Januart 20201 Ballot related trackers resulting in the followed detailed changes.

Listed below are the resolved trackers for this version:

**Status**: **Summary**:(**Jira Issue**) **Link to Change**
1. **Applied**:Update PractitionerRole.practitioner to )..1 MS ([FHIR-29681](https://jira.hl7.org/browse/FHIR-29681)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-practitionerrole.html#profile)
1. **Applied**:Change CareTeam `status` search parameter compositeOR expectation to SHOULD ([FHIR-29768](https://jira.hl7.org/browse/FHIR-29768)) [See Change Here](http://hl7.org/fhir/us/core/STU4/SearchParameter-us-core-careteam-status.html)
1. **Applied**:Provide guidance on the population of narrative ([FHIR-29777](https://jira.hl7.org/browse/FHIR-29777)) [See Change Here](http://hl7.org/fhir/us/core/STU4/general-guidance.html#narrative)
1. **Applied**: Change $docref start and end input parameter types from `date` to `dateTime` ([FHIR-29825](https://jira.hl7.org/browse/FHIR-29825)) [See Change Here](http://hl7.org/fhir/us/core/STU4/OperationDefinition-docref.html)
1. **Applied**: The history file markdown rendering of the table ([FHIR-30100](https://jira.hl7.org/browse/FHIR-30100)) [See Change Here](http://hl7.org/fhir/us/core/history.html)
1. **Applied**:footnote rendering - pre-applied ([FHIR-30101](https://jira.hl7.org/browse/FHIR-30101)) [See Change Here](http://hl7.org/fhir/us/core/STU4/general-guidance.html#guidance-on-limiting-the-number-of-search-results)
1. **Applied**:Random Section Numbering (Reminder for tooling issue) ([FHIR-30102](https://jira.hl7.org/browse/FHIR-30102)) [See Change Here](http://hl7.org/fhir/us/core/STU4/toc.html)
1. **Applied**:Move section 1.5 US Core Conformance Requirements ([FHIR-30103](https://jira.hl7.org/browse/FHIR-30103)) [See Change Here](http://hl7.org/fhir/us/core/STU4/conformance-expectations.html)
1. **Applied**:Make custodian optional on document reference ([FHIR-30108](https://jira.hl7.org/browse/FHIR-30108)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-documentreference.html)
1. **Applied**:Remove required binding on procedure and condition ([FHIR-30109](https://jira.hl7.org/browse/FHIR-30109)) See Changes:
   - [Here](https://build.fhir.org/ig/HL7/US-Core/conformance-expectations.html#extensible-binding-for-codeableconcept-datatype)
   - [Here](https://build.fhir.org/ig/HL7/US-Core/StructureDefinition-us-core-condition.html#profile)
   - [Here](https://build.fhir.org/ig/HL7/US-Core/StructureDefinition-us-core-procedure.html#profile)
   
1. **Applied**:Update DocumentReference CCD operation ([FHIR-30110](https://jira.hl7.org/browse/FHIR-30110)) [See Change Here](http://hl7.org/fhir/us/core/STU4/OperationDefinition-docref.html)
1. **Applied**:Update DocumentReference MustSupport to choice of data or url ([FHIR-30111](https://jira.hl7.org/browse/FHIR-30111)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-documentreference.html#mandatory-and-must-support-data-elements)
1. **Applied**:Reference to 3 new document types - addressing corresponding metadat ([FHIR-30112](https://jira.hl7.org/browse/FHIR-30112)) [See Change Here](https://build.fhir.org/ig/HL7/US-Core/clinical-notes-guidance.html#clinical-notes) AND [See Change Here](https://build.fhir.org/ig/HL7/US-Core/clinical-notes-guidance.html#support-requirements)
1. **Applied**:Typo ([FHIR-30113](https://jira.hl7.org/browse/FHIR-30113))
1. **Applied**:Clarify Must Support of Complex elements ([FHIR-30321](https://jira.hl7.org/browse/FHIR-30321)) [See Change Here](http://hl7.org/fhir/us/core/STU4/conformance-expectations.html#must-support---complex-elements)
1. **Applied**:Clarify that VSAC FHIR API only retrieves a definition ([FHIR-30344](https://jira.hl7.org/browse/FHIR-30344)) [See Change Here](http://hl7.org/fhir/us/core/STU4/terminology.html#using-value-set-authority-center-vsac)
1. **Applied**:Allergy Intolerance example for UNKNOWN allergy status does not use unknown ([FHIR-30345](https://jira.hl7.org/browse/FHIR-30345)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-allergyintolerance.html#mandatory-and-must-support-data-elements)
1. **Applied**:Corrected allergy intolerance example SNOMED CT code ([FHIR-30346](https://jira.hl7.org/browse/FHIR-30346)) [See Change Here](http://hl7.org/fhir/us/core/STU4/AllergyIntolerance-example.html)
1. **Applied**:Allergy codes updated to snomed product hierarchy in VSAC([FHIR-30347](https://jira.hl7.org/browse/FHIR-30347)) [See Change Here](https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1186.8/expansion)
1. **Applied**:Clarify plans to align with Gender Harmony([FHIR-30350](https://jira.hl7.org/browse/FHIR-30350)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-patient.html#mandatory-and-must-support-data-elements)
1. **Applied**:Typos on Conformance Expectations Page ([FHIR-30353](https://jira.hl7.org/browse/FHIR-30353)) [See Change Here](http://hl7.org/fhir/us/core/STU4/conformance-expectations.html)
1. **Applied**:clarify use of additional codings ([FHIR-30354](https://jira.hl7.org/browse/FHIR-30354)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-vital-signs.html#mandatory-and-must-support-data-elements)
1. **Applied**:Clarify server requirements for Choice of Profile Elements scenario ([FHIR-30355](https://jira.hl7.org/browse/FHIR-30355)) [See Change Here](http://hl7.org/fhir/us/core/STU4/conformance-expectations.html#must-support---choice-of-profile-elements)
1. **Applied**:Add all options to Procedure.performed[x] ([FHIR-30391](https://jira.hl7.org/browse/FHIR-30391)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-procedure.html#profile)
1. **Applied**:Updated MedicationRequest.authoredOn from mandatory to must support([FHIR-30430](https://jira.hl7.org/browse/FHIR-30430)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-medicationrequest.html#mandatory-and-must-support-data-elements)
1. **Applied**:Typo ([FHIR-30460](https://jira.hl7.org/browse/FHIR-30460)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-vital-signs.html#mandatory-and-must-support-data-elements)
1. **Applied**: Update Encounter Type CPT Description ([FHIR-30470](https://jira.hl7.org/browse/FHIR-30470)) [See Change Here](http://hl7.org/fhir/us/core/STU4/ValueSet-us-core-encounter-type.html)
1. **Applied**: Clarify Missing Data language for coded data elements with required binding strength ([FHIR-30630](https://jira.hl7.org/browse/FHIR-30630)) [See Change Here](http://hl7.org/fhir/us/core/STU4/general-guidance.html#missing-data)
1. **Applied**:Note re language codes([FHIR-30654](https://jira.hl7.org/browse/FHIR-30654)) [See Change Here](http://hl7.org/fhir/us/core/STU4/ValueSet-simple-language.html#notes)
1. **Applied**:Change URL for Healthcare Common Procedure Coding System (HCPCS) level II alphanumeric codes([FHIR-30655](https://jira.hl7.org/browse/FHIR-30655)) See Changes [Here](http://hl7.org/fhir/us/core/STU4/terminology.html#using-value-set-authority-center-vsac) and [Here](http://hl7.org/fhir/us/core/ValueSet/us-core-procedure-code)
1. **Applied**:Typo ([FHIR-30656](https://jira.hl7.org/browse/FHIR-30656))
1. **Applied**: Explain the relationship between US CORE and an evolving USCDI. ([FHIR-30657](https://jira.hl7.org/browse/FHIR-30657)) [See Change Here](http://hl7.org/fhir/us/core/STU4/index.html)
1. **Applied**:Correct 2 bullet points in section 1.2. ([FHIR-30658](https://jira.hl7.org/browse/FHIR-30658)) [See Change Here](http://hl7.org/fhir/us/core/STU4/index.html)
1. **Applied**:Clarify actors ([FHIR-30659](https://jira.hl7.org/browse/FHIR-30659)) [See Change Here](http://hl7.org/fhir/us/core/STU4/index.html#us-core-actors)
1. **Applied**:Edit basic provenance ([FHIR-30660](https://jira.hl7.org/browse/FHIR-30660)) [See Change Here](http://hl7.org/fhir/us/core/STU4/basic-provenance.html#clinical-information-reconciliation-and-incorporation)
1. **Applied**:Clarify the duplication requirement for scanned documents in DocumentReference and DiagnosticReport. ([FHIR-30662](https://jira.hl7.org/browse/FHIR-30662)) [See Change Here](http://hl7.org/fhir/us/core/STU4/clinical-notes-guidance.html#fhir-resources-to-exchange-clinical-notes)
1. **Applied**:Clarify that clients should retain data visualization between DSTU2 to R4 upgrades. ([FHIR-30665](https://jira.hl7.org/browse/FHIR-30665)) [See Change Here](http://hl7.org/fhir/us/core/STU4/DSTU2-to-R4-conversion.html#expectation-that-dstu2-data-is-preserved-in-r4)
1. **Applied**:Add provenance to writing/updating guidance? ([FHIR-30666](https://jira.hl7.org/browse/FHIR-30666)) [See Change Here](http://hl7.org/fhir/us/core/STU4/future-of-US-core.html)
1. **Applied**:Clarify Code System section and update codesystem table ([FHIR-30667](https://jira.hl7.org/browse/FHIR-30667)) [See Change Here](http://hl7.org/fhir/us/core/STU4/terminology.html#code-systems)
1. **Applied**: Clarify guidance on implantable medical devices. ([FHIR-30669](https://jira.hl7.org/browse/FHIR-30669)) [[See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-implantable-device.html#mandatory-and-must-support-data-elements)
1. **Applied**: Make udi_HRF a *Must Support* element. ([FHIR-30670](https://jira.hl7.org/browse/FHIR-30670)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-implantable-device.html#mandatory-and-must-support-data-elements)
1. **Applied**: Clarify UDI information. ([FHIR-30672](https://jira.hl7.org/browse/FHIR-30672)) See Changes:
    - [Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-implantable-device.html#mandatory-and-must-support-data-elements)
    - [Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-implantable-device.html#profile)
1. **Applied**:Clarify text ([FHIR-30673](https://jira.hl7.org/browse/FHIR-30673)) [See Change Here](http://hl7.org/fhir/us/core/STU4/conformance-expectations.html#conformance-expectations)
1. **Applied**:Typos ([FHIR-30674](https://jira.hl7.org/browse/FHIR-30674))
1. **Applied**:Clarify prohibition on using contained resources. ([FHIR-30677](https://jira.hl7.org/browse/FHIR-30677)) [See Change Here](http://hl7.org/fhir/us/core/STU4/general-guidance.html#contained-resources)
1. **Applied**:Add guidance on suppressed data. ([FHIR-30678](https://jira.hl7.org/browse/FHIR-30678)) [See Change Here](http://hl7.org/fhir/us/core/STU4/general-guidance.html#suppressed-data)
1. **Applied**:Clarify what is meant by "support the other elements." ([FHIR-30680](https://jira.hl7.org/browse/FHIR-30680)) [See Change Here](http://hl7.org/fhir/us/core/STU4/conformance-expectations.html#must-support---choice-of-data-types)
1. **Applied**:Typo([FHIR-30681](https://jira.hl7.org/browse/FHIR-30681))
1. **Applied**:Fix typos ([FHIR-30683](https://jira.hl7.org/browse/FHIR-30683)) Various Changes
1. **Applied**:Update on Guidance on DataAbsentReason for Observations ([FHIR-30685](https://jira.hl7.org/browse/FHIR-30685)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-observation-lab.html#mandatory-and-must-support-data-elements)
1. **Applied**:Clarify use of qualifier LOINCs ([FHIR-30690](https://jira.hl7.org/browse/FHIR-30690)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-vital-signs.html#mandatory-and-must-support-data-elements)
1. **Applied**: Fix Typo ([FHIR-30695](https://jira.hl7.org/browse/FHIR-30695)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-immunization-definitions.html)
1. **Applied**: Update on Guidance on DataAbsentReason for Observations ([FHIR-30699](https://jira.hl7.org/browse/FHIR-30699)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-observation-lab.html#mandatory-and-must-support-data-elements)
1. **Applied**: Clarify what is intended with "additional observations"([FHIR-30772](https://jira.hl7.org/browse/FHIR-30772)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-vital-signs.html#mandatory-and-must-support-data-elements)
1. **Applied**: Add statement about clinical safety to the security page ([FHIR-30776](https://jira.hl7.org/browse/FHIR-30776)) [See Change Here](http://hl7.org/fhir/us/core/STU4/security.html)
1. **Applied**: Added clarification to vitals profile regarding use of additional codings and component observations. ([FHIR-30778](https://jira.hl7.org/browse/FHIR-30778)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-blood-pressure.html#mandatory-and-must-support-data-elements)
1. **Applied**: Typo grammar. All codes SHALL have an system value. Correction “a value system”. ([FHIR-30782](https://jira.hl7.org/browse/FHIR-30782)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-vital-signs.html#mandatory-and-must-support-data-elements)
1. **Applied**: Clarify resource search requirements CapabilityStatements and provide guidance on search for multiple patients using Bulk data ([FHIR-30787](https://jira.hl7.org/browse/FHIR-30787)) See Changes:
   - [Here](http://hl7.org/fhir/us/core/STU4/general-guidance.html#searching-multiple-patients)
   - [Here](http://hl7.org/fhir/us/core/STU4/CapabilityStatement-us-core-server.html#condition)
1. **Applied**: Add MedicationAdministration to the Future Page. ([FHIR-30788](https://jira.hl7.org/browse/FHIR-30788)) [See Change Here](http://hl7.org/fhir/us/core/STU4/future-of-US-core.html#future-candidate-requirements-under-consideration)
1. **Applied**: Fix text in $docref description ([FHIR-30810](https://jira.hl7.org/browse/FHIR-30810)) [See Change Here](https://build.fhir.org/ig/HL7/US-Core/OperationDefinition-docref.html)
1. **Applied**: Mandate that CapabilityStatement.instantiates refer to US Core ([FHIR-30889](https://jira.hl7.org/browse/FHIR-30889)) [See Change Here](http://hl7.org/fhir/us/core/STU4/CapabilityStatement-us-core-server.html#shall_css)
1. **Applied**: Add binding so Vitals will render it in differential view ([FHIR-31391](https://jira.hl7.org/browse/FHIR-31391)) [See Change Here](http://hl7.org/fhir/us/core/2021JAN/StructureDefinition-us-core-vital-signs.html#profile)
1. **Applied**: Update to URI from OID for CDT in Procedure Code ValueSet ([FHIR-31556](https://jira.hl7.org/browse/FHIR-31556)) [See Change Here](http://hl7.org/fhir/us/core/STU4/ValueSet-us-core-procedure-code.html)
1. **Applied**: Add DocumentReference.content is under "must have" list ([FHIR-31364](https://jira.hl7.org/browse/FHIR-31364)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-documentreference.html#mandatory-and-must-support-data-elements)
1. **Applied**: Update Must Support Bullet regarding missing data ([FHIR-31507](https://jira.hl7.org/browse/FHIR-31507)) [See Change Here](http://hl7.org/fhir/us/core/STU4/conformance-expectations.html#must-support-elements)
1. **Applied**: Update use context for Race and Ethnicity extensions ([FHIR-31008](https://jira.hl7.org/browse/FHIR-31008)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-race.html)
1. **Applied**: Add guidance on "POST based search" ([FHIR-31585](https://jira.hl7.org/browse/FHIR-31585)) See Changes:
   - [Here](http://hl7.org/fhir/us/core/STU4/general-guidance.html#search-syntax)
   - [Here](http://hl7.org/fhir/us/core/STU4/CapabilityStatement-us-core-server.html#behavior)
1. **Applied**: Add reference to Mapping from LOINC scale type to FHIR data type ([FHIR-31084](https://jira.hl7.org/browse/FHIR-31084)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-observation-lab.html#mandatory-and-must-support-data-elements)
1. **Applied**: Update Observation.value[x] definition ([FHIR-31083](https://jira.hl7.org/browse/FHIR-31083)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-observation-lab-definitions.html#Observation.value[x])
1. **Applied**: Add LOINC to procedure codes ([FHIR-31514](https://jira.hl7.org/browse/FHIR-31514)) [See Change Here](http://hl7.org/fhir/us/core/STU4/ValueSet-us-core-procedure-code.html)
1. **Applied**: Make PractitionerRole.organization must support and add invariant ([FHIR-29680](https://jira.hl7.org/browse/FHIR-29680)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-practitionerrole.html)
1. **Applied**: Fix FHIRPath constraint for provenance-1([FHIR-31020](https://jira.hl7.org/browse/FHIR-31020)) [See Change Here](https://build.fhir.org/ig/HL7/US-Core/StructureDefinition-us-core-provenance.html)
1. **Applied**: Add guidance to BMI Profile([FHIR-32658](https://jira.hl7.org/browse/FHIR-32658)) [See Change Here](https://build.fhir.org/ig/HL7/StructureDefinition-us-core-bmi.html)
1. **Applied**: Write usage note for non-vaccination CVX codes([FHIR-31899](https://jira.hl7.org/browse/FHIR-31899)) [See Change Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-immunization.html#mandatory-and-must-support-data-elements)
1. **Applied**: Clarify that Extensible binding can always provide a mapped code([FHIR-32010](https://jira.hl7.org/browse/FHIR-32010)) [See Change Here](http://hl7.org/fhir/us/core/STU4/conformance-expectations.html#extensible-binding-for-codeableconcept-datatype)
1. **Applied**: Clarify RESTFul requirements([FHIR-31490](https://jira.hl7.org/browse/FHIR-31490)) See Changes:
   - [Here](http://hl7.org/fhir/us/core/STU4/index.html#introduction)
   - [Here](http://hl7.org/fhir/us/core/STU4/index.html#how-to-read-this-guide)
   - [Here](http://hl7.org/fhir/us/core/STU4/conformance-expectations.html#conformance-expectations)
   - [Here](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-allergyintolerance.html#notes)
1. **Applied**: fix Procedure Example error ([FHIR-30106](https://jira.hl7.org/browse/FHIR-30106)) [See Change Here](http://hl7.org/fhir/us/core/STU4/Procedure-rehab.html)

**Known issues:**

We are working to fix these issues that may come up when using US CORE.  We will correct them in a future version of the guide

Publishing

- [ ] **Resolved - change required**:Confusing for commercial vendor. Reads very confusing. ([FHIR-30783](https://jira.hl7.org/browse/FHIR-30783)) proposal is to make the differential tab the default view, see publishing plans [here](https://github.com/HL7/ig-template-base/issues/161)  timeline unknown.
- [ ] **Resolved - change required**:In most of the data elements – “Binding is from base FHIR and US Core Vital Signs”  Need this to be one single combined listing ([FHIR-30780](https://jira.hl7.org/browse/FHIR-30780)) proposal is to limit the terminology and invariants to view shown. see [Zulip chat](https://chat.fhir.org/#narrow/stream/179252-IG-creation/topic/Different.20views.20for.20tables.20and.20invariants) timeline unknown.
- [ ] **Resolved - change required**:Why are there separate codes for USCoreVitalSigns and the Systolic.value and the diastolic value? ([FHIR-30779](https://jira.hl7.org/browse/FHIR-30779)) proposal is to work with publishing to "clean up" terminology and invariants to view shown. see: see [Zulip chat](https://chat.fhir.org/#narrow/stream/179252-IG-creation/topic/Different.20views.20for.20tables.20and.20invariants) timeline unknown.

Terminology

- [ ] **Resolved - change required**: valueset-simple-language.xml QA error "Error from server: Language valuesets cannot be expanded as they are based on a grammar" ([FHIR-30107](https://jira.hl7.org/browse/FHIR-30107)) this error is still extant from prior version of US Core and has yet to be resolved. Work with publishing to fix and created [STU note](http://hl7.org/fhir/us/core/STU4/ValueSet-simple-language.html#notes). see [Zulip chat](https://chat.fhir.org/#narrow/stream/179252-IG-creation/topic/language.20valueset.20expansion.20error)
- [ ] **Resolved - change required**: Patient Examples QA Errors: CDCREC code system in VSAC Patient ([FHIR-30105](https://jira.hl7.org/browse/FHIR-30105)) CDCREC codes and code system value not aligned with VSAC. Workaround is to publish the [CDCREC code system and valuesets in USCore](http://hl7.org/fhir/us/core/STU4/terminology.html) until this content is moved to [HL7 Terminology](https://terminology.hl7.org/) Add an STU Note. [Zulip chat1](https://chat.fhir.org/#narrow/stream/179252-IG-creation/topic/cdcrec.20code.20errors.20in.20US.20Core) and [Zulip chat2](https://chat.fhir.org/#narrow/stream/179252-IG-creation/topic/Race.20Code.20System) and [Zulip chat3](https://chat.fhir.org/#narrow/stream/179202-terminology/topic/US.20CDCREC.20codessystems.20in.20HTA)
- [ ] **Resolved - change required**:imm-1.json NDC/CVX codes QA Error ([FHIR-30104](https://jira.hl7.org/browse/FHIR-30104)) Work with terminology server team to correct. see [Zulip chat](https://chat.fhir.org/#narrow/stream/179252-IG-creation/topic/CVX.20and.20NDC.20warnings.20in.20US.20Core)
- [ ] **Resolved - change required**:Pulse Ox Example: observation-satO2-fiO2 ([FHIR-27845](https://jira.hl7.org/browse/FHIR-27845)) Proposed Jira ticket to resolve in base made an [STU note](http://hl7.org/fhir/us/core/STU4/StructureDefinition-us-core-pulse-oximetry.html#mandatory-and-must-support-data-elements) that is technically not conformant with the base FHIR vital profile. See [Zulip chat](https://chat.fhir.org/#narrow/stream/179252-IG-creation/topic/US.20Core.20QA.20Issue.20.233-.20nasty.20profiling.20error)

---

### 3.2.0
- date: 2021-1-30
- url: http://hl7.org/fhir/us/core/2021Jan
- FHIR version : 4.0.1
#### Changes:
 The changes in this version have been voted on by the members of the sponsoring work group [HL7 International Cross-Group Projects](http://www.hl7.org/Special/committees/cgp/index.cfm).  This version addresses the following key issues:

1. Clarification of the Must Support definitions as it relates to:
  - Polymorphic datatypes, which of the possible types must be supported
  - Reference datatype (Reference, canonical) which of the target types must be supported
  - The vital signs profile in the Core Specification which profiles must be supported
  - New [Conformance Expectations] page
  (see individual trackers below for details)
1. Publishing a set US Core Vital Signs independent of the FHIR core profile upon which it is based (see individual trackers below for details)
  - [US Core Vital Signs Profile]
    - [US Core Blood Pressure Profile]
    - [US Core BMI Profile]
    - [US Core Head Circumference Profile]
    - [US Core Body Height Profile]
    - [US Core Body Weight Profile]
    - [US Core Body Temperature Profile]
    - [US Core Heart Rate Profile]
    - [US Core Respiratory Rate Profile]
1. Linking terminology directly to the FHIR® Terminology Service for VSAC Resources ([Value Set Authority Center (VSAC) - NIH](https://vsac.nlm.nih.gov/)) where applicable

  - We are seeking to resolve several technical and policy glitches when using VSAC directly prior to publishing which include the requirement to log in using your own UMLS API Key requiring a current UMLS account to view the value sets. [VSAC UMLS Licensing information](https://www.nlm.nih.gov/vsac/support/usingvsac/requestumlslicense.html).
  - To view the VSAC value set, use the link `https://vsac.nlm.nih.gov/valueset/{OID}/expansion` in your browser replacing the {OID} with the OID from the table below.
  - Enumerated (extensional) value sets can also be downloaded as a FHIR ValueSet resource. To do this, use the link `https://cts.nlm.nih.gov/fhir/ValueSet/{OID}` in your browser replacing the {OID} with the OID from the table below.
  - **NOTE that the Code System value used in FHIR® Terminology Service for VSAC Resources for Race and Ethnicity (CDCREC) concepts *does not* align with historical and current usage of OIDs in C-CDA and US Core. This issue has not been resolved in time for publication of the ballot version of this guide. As a result validation errors may occur when validating against this version of the US Core Patient Profile. Feedback on which code system value to use is welcome.**

    1. **US Core Value Set, VSAC Value Set, VSAC OID, extensional?**
    1. Detailed ethnicity, Detailed Ethnicity, 2.16.840.1.114222.4.11.877, No
    1. Detailed Race, Race, 2.16.840.1.113883.1.11.14914, No
    1. OMB Ethnicity Categories, Ethnicity, 2.16.840.1.114222.4.11.837, Yes
    1. US Core CareTeam Provider Roles, Care Team Member Function, 2.16.840.1.113762.1.4.1099.30, Yes
    1. US Core Medication Codes (RxNorm), Medication Clinical Drug, 2.16.840.1.113762.1.4.1010.4, Yes
    1. US Core Provider Specialty (NUCC), Healthcare Provider Taxonomy, 2.16.840.1.114222.4.11.1066, No
    1. US Core Smoking Status, Smoking Status, 2.16.840.1.113883.11.20.9.38, Yes
    1. US Core Vaccine Administered Value Set (CVX), CVX Vaccines Administered Vaccine Set, 2.16.840.1.113762.1.4.1010.6, Yes
    1. US Core Common substances for allergy and intolerance documentation including refutations, Common substances for allergy and intolerance documentation including refutations, 2.16.840.1.113762.1.4.1186.8, No

4. Migrating to the standard set of HL7 FHIR IG templates for publishing. Although we strove to minimize the differences between this version and the previous versions of US Core, these changes are notable:
   - Additional Features include:
        - Addition of vocabulary and constraint tables to the profile pages
        - Addition of a summary table and to the profile page introduction
        - Addition of "Snapshot Table (Must Support)" Tab to profile views
   - Due to restrictions on customizable content, the following features of prior versions are no longer available:
       - Full narrative text summaries of profiles  **NOTE: We are seeking feedback on whether to retain these full narrative text summaries for this guide (an example can be seen [here](http://hl7.org/fhir/us/core/StructureDefinition-us-core-allergyintolerance.html#formal-views-of-profile-content) by clicking on the "Text Summary" tab)***

5. Addressing over 95 outstanding trackers.


**Trackers items and links to the updated content**
listed below are the resolved trackers for this version:

1. Must Support Over Interpreted ([FHIR-28375](https://jira.hl7.org/browse/FHIR-28375)) Changes throughout the profiles -- added conformance page [See Change Here](conformance-expectations.html)

1. Replace the US Core Update Allergy substances value set with VSAC reference ([FHIR-29322](https://jira.hl7.org/browse/FHIR-29322)) [See Change Here](StructureDefinition-us-core-allergyintolerance.html)

1. Update Organization Quick Start Example Search. ([FHIR-29269](https://jira.hl7.org/browse/FHIR-29269)) [See Change Here](StructureDefinition-us-core-organization.html#quick-start)

1. birthsex binding applied to the wrong element in US Core Patient StructuredDefinition/differential ([FHIR-29262](https://jira.hl7.org/browse/FHIR-29262)) [See Change Here](StructureDefinition-us-core-patient.profile.json.html)

1. us-core-12 invariant interpretation ([FHIR-28942](https://jira.hl7.org/browse/FHIR-28942)) [See Changes Here](StructureDefinition-us-core-implantable-device.html#FHIR-28942)

1. Incorrect Description Observation.component (Pulse Ox) ([FHIR-28934](https://jira.hl7.org/browse/FHIR-28934)) [See Change Here](StructureDefinition-us-core-pulse-oximetry.html)

1. References should be constrained to use `reference` not `identifier` ([FHIR-28573](https://jira.hl7.org/browse/FHIR-28573)) [See Change Here](general-guidance.html#FHIR-28573)

1. Update USCorePatientName search description for consistency ([FHIR-28540](https://jira.hl7.org/browse/FHIR-28540)) [See Change Here](StructureDefinition-us-core-patient.html#quick-start)

1. Make Provenance.author optional ([FHIR-28517](https://jira.hl7.org/browse/FHIR-28517)) [See Change Here](StructureDefinition-us-core-provenance.html#FHIR-28516)

1. Add must support type choices for US Core Goal.target.due[x]. ([FHIR-28477](https://jira.hl7.org/browse/FHIR-28477)) [See Change Here](StructureDefinition-us-core-goal.html)

1. Immunization Profile Mandatory and Must Support Intro is missing attributes ([FHIR-28452](https://jira.hl7.org/browse/FHIR-28452)) [See Change Here](StructureDefinition-us-core-immunization.html#FHIR-28452)

1. DiagnosticReport-cardiology-report JSON and XML samples contain invalid hashes ([FHIR-28408](https://jira.hl7.org/browse/FHIR-28408)) [See Change Here](DiagnosticReport-cardiology-report.json.html)

1. MedicationRequest.medication[x] ([FHIR-28395](https://jira.hl7.org/browse/FHIR-28395)) [See Change Here](StructureDefinition-us-core-medicationrequest.html#FHIR-28395)

1. Fix MedicationRequest.encounter reference ([FHIR-28258](https://jira.hl7.org/browse/FHIR-28258)) [See Change Here](StructureDefinition-us-core-medicationrequest.html)

1. Fix typo: "an another" -> "another" ([FHIR-28227](https://jira.hl7.org/browse/FHIR-28227)) [See Change Here](StructureDefinition-us-core-practitioner.html)

1. Declare mustSupport on Organization telecom children ([FHIR-28216](https://jira.hl7.org/browse/FHIR-28216)) [See Change Here](StructureDefinition-us-core-organization.html)

1. Resolve remaining discrepancies with FHIR R4 Search Parameters ([FHIR-28181](https://jira.hl7.org/browse/FHIR-28181)) See Changes Here:
    - [1 SearchParameter-us-core-condition-onset-date](SearchParameter-us-core-condition-onset-date.html)
    - [2 SearchParameter-us-core-organization-name](SearchParameter-us-core-organization-name.html)
    - [3 SearchParameter-us-core-location-name](SearchParameter-us-core-location-name.html)

1. Provenance without activity is not very useful ([FHIR-28179](https://jira.hl7.org/browse/FHIR-28179)) [See Change Here](StructureDefinition-us-core-provenance.html#FHIR-28179)

1. Make Provenance.target.reference mandatory ([FHIR-28165](https://jira.hl7.org/browse/FHIR-28165)) [See Change Here](StructureDefinition-us-core-provenance.html)

1. Missing narrative Element ([FHIR-28159](https://jira.hl7.org/browse/FHIR-28159)) [See Change Here](Patient-example.html)

1. "Updated guidance regarding gender and sex." ([FHIR-28138](https://jira.hl7.org/browse/FHIR-28138)) [See Change Here](StructureDefinition-us-core-patient.html#FHIR-28138)

1. Replace the US Core Smoking Status with VSAC reference ([FHIR-28123](https://jira.hl7.org/browse/FHIR-28123),[FHIR-26059](https://jira.hl7.org/browse/FHIR-26059)) [See Change Here](StructureDefinition-us-core-smokingstatus.html)

1. Timing association for smoking status changed from `issued` to `effectiveDateTime` ([FHIR-28090](https://jira.hl7.org/browse/FHIR-28090)) [See Change Here](StructureDefinition-us-core-smokingstatus.html)

1. Remove Must Support from Patient.telecom ([FHIR-27731](https://jira.hl7.org/browse/FHIR-27731)) [See Change Here](StructureDefinition-us-core-patient.html#FHIR-27731)

1. Remove Must Support from Patient.communication.language ([FHIR-27730](https://jira.hl7.org/browse/FHIR-27730)) [See Change Here](StructureDefinition-us-core-patient.html#FHIR-27731)

1. Remove Must Support from us-core-birthsex extension ([FHIR-27729](https://jira.hl7.org/browse/FHIR-27729)) [See Change Here](StructureDefinition-us-core-patient.html#FHIR-27731)

1. Remove Must Support from  us-core-ethnicity extension ([FHIR-27728](https://jira.hl7.org/browse/FHIR-27728)) [See Change Here](StructureDefinition-us-core-patient.html#FHIR-27731)

1. Remove Must Support from  us-core-race extension ([FHIR-27727](https://jira.hl7.org/browse/FHIR-27727)) [See Change Here](StructureDefinition-us-core-patient.html#FHIR-27731)

1. Expand US Core state value set to include US Military codes ([FHIR-26833](https://jira.hl7.org/browse/FHIR-26833)) [See Change Here](ValueSet-us-core-usps-state.html)

1. Fixed Value Set Expansion Operation examples ([FHIR-26625](https://jira.hl7.org/browse/FHIR-26625)) [See Change Here](clinical-notes-guidance.html#FHIR-26625)

1. Add must support reference type choices for US Core laboratory DiagnosticReport.performer ([FHIR-25120](https://jira.hl7.org/browse/FHIR-25120)) [See Change Here](StructureDefinition-us-core-diagnosticreport-lab.html)

1. Fix US-Core-1 constraint on Observation.effectivePeriod ([FHIR-29658](https://jira.hl7.org/browse/FHIR-29658)) [See Change Here](StructureDefinition-us-core-observation-lab.html)

1. Change bindings from extensible to required for Condition.code value set: US Core Condition Category Codes Procedure.code value set: US Core Procedure Codes ([FHIR-29563](https://jira.hl7.org/browse/FHIR-29563)) See Changes Here:
      - [1 StructureDefinition-us-core-condition-definitions](StructureDefinition-us-core-condition.html)
      - [2 StructureDefinition-us-core-procedure-definitions](StructureDefinition-us-core-procedure.html)

1. Remove text "an author responsible for the update". Keep author organization ([FHIR-28516](https://jira.hl7.org/browse/FHIR-28516)) [See Change Here](StructureDefinition-us-core-provenance.html#FHIR-28516)

1. "Clarify expectations when accessing "other endpoint" for DocumentReference.content.attachment.url" ([FHIR-28472](https://jira.hl7.org/browse/FHIR-28472)) [See Change Here](StructureDefinition-us-core-documentreference.html#FHIR-28472)

1. Add a required category to smoking status ([FHIR-28436](https://jira.hl7.org/browse/FHIR-28436)) [See Change Here](StructureDefinition-us-core-smokingstatus.html#FHIR-28436)

1. Use of US Core Profile when not explicitly referenced when using Contained resources ([FHIR-28396](https://jira.hl7.org/browse/FHIR-28396)) [See Change Here](general-guidance.html#FHIR-28396)

1. DocumentReference.custodian to be Optional ([FHIR-28393](https://jira.hl7.org/browse/FHIR-28393)) [See *Proposed* Change Here](StructureDefinition-us-core-documentreference.html#FHIR-28393)

1. Encounter.serviceProvider Must Support and Encounter.location.location Optional ([FHIR-28392](https://jira.hl7.org/browse/FHIR-28392)) [See Change Here](StructureDefinition-us-core-encounter.html#FHIR-28392)

1. Observation.hasMember Vital Signs Panel Profile Reference Choice ([FHIR-28391](https://jira.hl7.org/browse/FHIR-28391)) [See Change Here](profiles-and-extensions.html#FHIR-28391)

1. Add must support type choices for Observation.value[x] for Lab Observation Profile ([FHIR-28390](https://jira.hl7.org/browse/FHIR-28390)) [See Change Here](StructureDefinition-us-core-observation-lab.html)

1. Add must support type choices for Observation.effective[x] for Lab Observation Profile ([FHIR-28389](https://jira.hl7.org/browse/FHIR-28389)) [See Change Here](StructureDefinition-us-core-observation-lab.html)

1. Add must support type choices for Immunization.occurrence[x] ([FHIR-28388](https://jira.hl7.org/browse/FHIR-28388)) [See Change Here](StructureDefinition-us-core-immunization.html)

1. Add must support type choices for DiagnosticReport.effective[x] for Note Data ([FHIR-28387](https://jira.hl7.org/browse/FHIR-28387)) [See Change Here](StructureDefinition-us-core-diagnosticreport-note.html)

1. Add must support type choices for DiagnosticReport.effective[x] for Lab Data Type ([FHIR-28385](https://jira.hl7.org/browse/FHIR-28385)) [See Change Here](StructureDefinition-us-core-diagnosticreport-lab.html)

1. Add must support reference type choices for Provenance.agent.who Reference ([FHIR-28383](https://jira.hl7.org/browse/FHIR-28383)) [See Change Here](StructureDefinition-us-core-provenance.html)

1. Add must support reference type choices for MedicationRequest.requester Reference ([FHIR-28382](https://jira.hl7.org/browse/FHIR-28382)) [See Change Here](StructureDefinition-us-core-medicationrequest.html)

1. Add must support reference type choices for MedicationRequest.reported Choice ([FHIR-28381](https://jira.hl7.org/browse/FHIR-28381)) [See Change Here](StructureDefinition-us-core-medicationrequest.html#FHIR-28381)

1. Add must support reference type choices for  DocumentReference.author Reference ([FHIR-28380](https://jira.hl7.org/browse/FHIR-28380)) [See Change Here](StructureDefinition-us-core-documentreference.html)

1. Add must support reference type choices for DiagnosticReport.performer for Note ([FHIR-28379](https://jira.hl7.org/browse/FHIR-28379)) [See Change Here](StructureDefinition-us-core-diagnosticreport-note.html)

1. Add must support reference type choices for DiagnosticReport.performer for Lab ([FHIR-28378](https://jira.hl7.org/browse/FHIR-28378)) [See Change Here](StructureDefinition-us-core-diagnosticreport-lab.html)

1. Add must support reference type choices for CareTeam.participant.member Reference ([FHIR-28376](https://jira.hl7.org/browse/FHIR-28376)) [See Change Here](StructureDefinition-us-core-careteam.html)

1. Add choice for and type choices for Encounter.reasonReference ([FHIR-27951](https://jira.hl7.org/browse/FHIR-27951)) [See Change Here](StructureDefinition-us-core-encounter.html#FHIR-27951)

1. Add choice for Procedure.performed[x] ([FHIR-29695](https://jira.hl7.org/browse/FHIR-29695)) [See Change Here](StructureDefinition-us-core-procedure.html)

1. Clarify deleted resources requirements and guidance ([FHIR-28091](https://jira.hl7.org/browse/FHIR-28091)) [See Change Here](general-guidance.html#FHIR-28091)

1. Clarify search by date precision conformance expectations ([FHIR-27906](https://jira.hl7.org/browse/FHIR-27906)) [See Change Here](general-guidance.html#FHIR-27906)
   - [General Guidance](general-guidance.html#FHIR-27906)
   - [Example in QuickStart](StructureDefinition-us-core-careplan.html#optional-search-parameters)
   - [Example in CapabilityStatement](CapabilityStatement-us-core-server.html#careplan)

1. Clarify search by reference conformance expectations ([FHIR-27905](https://jira.hl7.org/browse/FHIR-27905)) See Changes Here:
   - [General Guidance](general-guidance.html#FHIR-27905)
   - [Example in QuickStart](StructureDefinition-us-core-careplan.html#optional-search-parameters)
   - [Example in CapabilityStatement](CapabilityStatement-us-core-server.html#careplan)

1. Add "Cause of Death" to category codes to meet the Public Health Use Case for VRDR ([FHIR-27904](https://jira.hl7.org/browse/FHIR-27904)) [See Change Here](ValueSet-us-core-condition-category.html)

1. Address non-implantable device and how to document usage ([FHIR-27896](https://jira.hl7.org/browse/FHIR-27896), [FHIR-23715](https://jira.hl7.org/browse/FHIR-23715), [FHIR-23715](https://jira.hl7.org/browse/FHIR-23715)) [See Change Here](future-of-US-core.html#FHIR-27896)

1. Resource constraints based on Jurisdiction which are not well documented ([FHIR-27810](https://jira.hl7.org/browse/FHIR-27810)) [See Change Here](StructureDefinition-us-core-implantable-device.html#FHIR-27810)

1. Updated CPT copyright to current year ([FHIR-27770](https://jira.hl7.org/browse/FHIR-27770)) [See Change Here](ValueSet-us-core-encounter-type.html)

1. Change binding for CareTeam.participant.role from NUCC to Care Team Member Function, replace the US Core Careteam Provider Roles Value Set with VSAC reference ([FHIR-27769](https://jira.hl7.org/browse/FHIR-27769)) [See Change Here](StructureDefinition-us-core-careteam.html)

1. Remove US Core Server Capability Statement *requires* support for HTTP status 410-deleted ([FHIR-26597](https://jira.hl7.org/browse/FHIR-26597)) [See Change Here](CapabilityStatement-us-core-server.html#behavior)

1. Change US Core Condition Code Value Set Logical Definition ([FHIR-26060](https://jira.hl7.org/browse/FHIR-26060)) [See Change Here](ValueSet-us-core-condition-code.html)

1. Recommend against using SSN for Patient.identifier ([FHIR-24903](https://jira.hl7.org/browse/FHIR-24903)) [See Change Here](StructureDefinition-us-core-patient.html#FHIR-24903)

1. Remove identifier (OID) from ValueSet: US Core Encounter Type ([FHIR-29691](https://jira.hl7.org/browse/FHIR-29691)) [See Change Here](ValueSet-us-core-encounter-type.html)

1. Review vocabulary to align with CCDA and use VSAC valueset where possible ([FHIR-22488](https://jira.hl7.org/browse/FHIR-22488)) [See Changes Here:
    - [Detailed ethnicity --> Detailed Ethnicity](StructureDefinition-us-core-ethnicity.html#profile)
    - [Detailed Race --> Race](StructureDefinition-us-core-race.html#profile)
    - [OMB Ethnicity --> Categories\|Ethnicity](StructureDefinition-us-core-ethnicity.html#profile)
    - [US Core Medication Codes (RxNorm) --> Medication Clinical Drug](StructureDefinition-us-core-medicationrequest.html) and [here](StructureDefinition-us-core-medication.html#Medication.code)
    - [US Core Provider Specialty (NUCC) --> Healthcare Provider Taxonomy](StructureDefinition-us-core-practitionerrole.html)
    - [US Core Vaccine Administered Value Set (CVX) --> CVX Vaccines Administered Vaccine Set](StructureDefinition-us-core-immunization.html)

1. Remove CVX-NDC mapping table ([FHIR-29745](https://jira.hl7.org/browse/FHIR-29745)) [See Change Here](StructureDefinition-us-core-immunization.html#FHIR-29745)

1. Since CarePlan.text.div is min== 1 add must support == true element to be consistent with US Core design ([FHIR-29765](https://jira.hl7.org/browse/FHIR-29765)) [See Change Here](StructureDefinition-us-core-careplan.html)

1. Remove unused US Core ICD-10-PCS Procedure Codes valueset ([FHIR-29822](https://jira.hl7.org/browse/FHIR-29822))

1. Remove Clinical Notes Guidance References to ONC 2019 NPRM and move requirements to main body ([FHIR-29824](https://jira.hl7.org/browse/FHIR-29824)) [See Change Here](clinical-notes-guidance.html)

---

### 3.1.1
- date: 2020-6-30
- url: http://hl7.org/fhir/us/core/STU3.1.1
- FHIR version : 4.0.1
#### Changes:
 This update addresses several technical corrections and errata and clarifications. They have been reviewed and voted on by the members of the [HL7 International Cross-Group Projects WorkGroup](http://www.hl7.org/Special/committees/cgp/index.cfm) who is sponsoring this errata release and reconciliation of the comments.:
1. Add guidance for representing patient name suffix and previous patient name to the [US Core Patient Profile](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-patient.html#mandatory-and-must-support-data-elements) ([FHIR-28129](https://jira.hl7.org/browse/FHIR-28129))
1. Correct copy/paste error in [Goal Profile](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-goal-definitions.html#Goal.lifecycleStatus) ([FHIR-28109](https://jira.hl7.org/browse/FHIR-28109))
1. Correct [US Core Provider Specialty (NUCC) ValueSet ](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-provider-specialty.html) to hide abstract grouping codes ([FHIR-27975](https://jira.hl7.org/browse/FHIR-27975))
1. Added example of US Core Direct Extension to [Practitioner-2 Example](http://hl7.org/fhir/us/core/STU3.1.1/Practitioner-practitioner-2.html) ([FHIR-27947](https://jira.hl7.org/browse/FHIR-27947))
1. Corrected technical errors in [pediatric profiles StructureDefinitions](http://hl7.org/fhir/us/core/STU3.1.1/profiles.html#profiles) ([FHIR-27946](https://jira.hl7.org/browse/FHIR-27946))
1. Corrected errors in [DiagnosticReport Cardiology Example](http://hl7.org/fhir/us/core/STU3.1.1/DiagnosticReport-cardiology-report.html) ([FHIR-27913](https://jira.hl7.org/browse/FHIR-27913))
1. Update [Federal Register link](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-omb-race-category.html) for OMB race and ethnicity category classifications. ([FHIR-27907](https://jira.hl7.org/browse/FHIR-27907))
1. Clarified [token search syntax](http://hl7.org/fhir/us/core/STU3.1.1/general-guidance.html#search-syntax) ([FHIR-27897](https://jira.hl7.org/browse/FHIR-27897)).
1. Corrected [US Core DocumentReference Profile](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-documentreference-definitions.html#DocumentReference.content) to support multiple attachments ([FHIR-25778](https://jira.hl7.org/browse/FHIR-25778)).
1. Fix FHIRPath Expression in [USCoreGoalTargetDate](http://hl7.org/fhir/us/core/STU3.1.1/SearchParameter-us-core-goal-target-date.html) ([FHIR-27892](https://jira.hl7.org/browse/FHIR-27892)).
1. Fix FHIRPath Expression in [USCoreProcedureDate](http://hl7.org/fhir/us/core/STU3.1.1/SearchParameter-us-core-procedure-date.html)([FHIR-27887](https://jira.hl7.org/browse/FHIR-27887)).
1. Add omitted ["ge" comparators to SearchParameters](http://hl7.org/fhir/us/core/STU3.1.1/SearchParameter-us-core-goal-target-date.html) ([FHIR-27893](https://jira.hl7.org/browse/FHIR-27893)).
1. [Remove Must Support References](http://hl7.org/fhir/us/core/STU3.1.1/general-guidance.html#referencing-us-core-profiles) to non US Core Profiles ([FHIR-27876](https://jira.hl7.org/browse/FHIR-27876))
1. Add missing [reaction](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-allergyintolerance-definitions.html#AllergyIntolerance.reaction) to the US Core AllergyIntolerance Profile ([FHIR-27867](https://jira.hl7.org/browse/FHIR-27867)).
1. Clarify [reference to US Core Patient](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-pediatric-bmi-for-age.html#mandatory-and-must-support-data-elements) in Vitals Signs Profiles ([FHIR-27857](https://jira.hl7.org/browse/FHIR-27857)).
1. Corrected [US Core Pulse Oximetry Profile](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-pulse-oximetry.html#formal-views-of-profile-content) component.valueQuantity.code and component.valueQuantity.unit min from 0 to 1 to be consistent with the valueQuantity constraints within US Core ([FHIR-27846](https://jira.hl7.org/browse/FHIR-27846))
1. Correct UCUM Unit in [US Core Pulse Oximetry Profile Text Summary](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-pulse-oximetry.html#summary-of-the-must-support-requirements) ([FHIR-27845](https://jira.hl7.org/browse/FHIR-27845))
1. Update [Procedure Codes Value Set](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-procedure-code.html) to include ICD-10 PCS codes ([FHIR-27836](https://jira.hl7.org/browse/FHIR-27836))
1. Update [Procedure Codes Value Set](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-procedure-code.html) to include CDT codes ([FHIR-27737](https://jira.hl7.org/browse/FHIR-27737))
1. Clarify that pediatric vital sign percentile Observations should [reference growth chart](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-pediatric-bmi-for-age.html#mandatory-and-must-support-data-elements) ([FHIR-27549](https://jira.hl7.org/browse/FHIR-27549)),
1. Added Missing [US core Head Occipital-frontal Circumference Percentile Profile](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-head-occipital-frontal-circumference-percentile.html) ([FHIR-27542](https://jira.hl7.org/browse/FHIR-27542)).
1. Correct requirements for supporting [CLIA identifiers](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-organization.html#mandatory-and-must-support-data-elements) ([FHIR-27158](https://jira.hl7.org/browse/FHIR-27158))
1. Change Description of [ICD-10-PCS Value Set](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-procedure-icd10pcs.html) ([FHIR-27116](https://jira.hl7.org/browse/FHIR-27116))
1. Correct [AllergyIntolerance guidance](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-allergyintolerance.html#mandatory-and-must-support-data-elements) for verificationStatus ([FHIR-27096](https://jira.hl7.org/browse/FHIR-27096))
1. Fix example [US Core heart-rate example](http://hl7.org/fhir/us/core/STU3.1.1/Observation-heart-rate.html) ([FHIR-27086](https://jira.hl7.org/browse/FHIR-27086))
1. **review period comments** Update [smoking status codes](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-smokingstatus-definitions.html#Observation.value[x]:valueCodeableConcept) to align with USCDI ([FHIR-27082](https://jira.hl7.org/browse/FHIR-27082)).
1. Fix invariant [provenance-1](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-provenance-definitions.html#who) ([FHIR-27065](https://jira.hl7.org/browse/FHIR-27065))
1. Fix invalid [json snippet](http://hl7.org/fhir/us/core/STU3.1.1/general-guidance.html#missing-data) ([FHIR-27001](https://jira.hl7.org/browse/FHIR-27001))
1. **review period comments** Remove Provenance requirement from Medication, Location, Practitioner, PractitionerRole, and Organization and correct copy and paste error to Medication and Provenance searchType support in [CapabilityStatement](http://hl7.org/fhir/us/core/STU3.1.1/CapabilityStatement-us-core-server.html#resource--details) ([FHIR-26840](https://jira.hl7.org/browse/FHIR-26840), [FHIR-28161](https://jira.hl7.org/browse/FHIR-28161)).
1. Correction on [USCDI Table](http://hl7.org/fhir/us/core/STU3.1.1/general-guidance.html#us-core-data-for-interoperability-and-2015-edition-common-clinical-data-set) change "MedicationStatement" to "MedicationRequest" and remove references to MedicationStatement in the Medication Profile and CapabilityStatements ([FHIR-26840](https://jira.hl7.org/browse/FHIR-26840)).
1. Clarify that US Core Location/PractitionerRole are [not being referenced](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-encounter.html#mandatory-and-must-support-data-elements) by other resources ([FHIR-26840](https://jira.hl7.org/browse/FHIR-26840)).
1. Correct editing error restoring Write and Operation capability guidance into [DocumentReference QuickStart](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-documentreference.html#quick-start) ([FHIR-26840](https://jira.hl7.org/browse/FHIR-26840)).
1. Clarify [guidance](http://hl7.org/fhir/us/core/STU3.1.1/general-guidance.html#search-for-servers-requiring-status) that servers SHALL support search with status if status required ([FHIR-26840](https://jira.hl7.org/browse/FHIR-26840)).
1. Correct canonical url for ImplementationGuide ([FHIR-26686](https://jira.hl7.org/browse/FHIR-26686)).
1. Correct system URI for [ICD-10 procedure codes](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-procedure-icd10pcs.html) ([FHIR-26679](https://jira.hl7.org/browse/FHIR-26679)).
1. Fix invariant [us-core-1](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-condition-definitions.html#Condition) ([FHIR-26605](https://jira.hl7.org/browse/FHIR-26605)).
1. Change valueCode min from 0 to 1 for [US Core Birth Sex Extension](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-birthsex-definitions.html#Extension.valueCode) and valueBoolean min from 0 to 1 for[US Core Direct email Extension](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-direct-definitions.html#Extension.valueBoolean) ([FHIR-26459](https://jira.hl7.org/browse/FHIR-26459)).
1. Change valueQuantity min from 1 to 0 for [US Core Pediatric BMI for Age Observation Profile](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-pediatric-bmi-for-age-definitions.html#Observation.valueQuantity) and [US Core Pediatric Weight for Height Observation Profile](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-pediatric-weight-for-height-definitions.html#Observation.valueQuantity) ([FHIR-26363](https://jira.hl7.org/browse/FHIR-26363)).
1. Add page contents to [Clinical Notes](http://hl7.org/fhir/us/core/STU3.1.1/clinical-notes-guidance.html) and [Basic Provenance](basic-provenance.html) pages ([FHIR-25785](https://jira.hl7.org/browse/FHIR-25785)).
1. Fix duplicate URL causing validation failure. ([FHIR-25536](https://jira.hl7.org/browse/FHIR-25536)).
1. Fix Invariant [us-core-8](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-patient-definitions.html#Patient.name) ([FHIR-25459](https://jira.hl7.org/browse/FHIR-25459)).
1. Corrected the wording "should support" to "shall support" in [Clinical Notes Guidance](http://hl7.org/fhir/us/core/STU3.1.1/clinical-notes-guidance.html#clinical-notes) ([FHIR-25455](https://jira.hl7.org/browse/FHIR-25455)).
1. Fix Invariant [us-core-8](http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-patient-definitions.html#Patient.name) to allow for Data Absent Reason Extension on Patient name.([FHIR-25249](https://jira.hl7.org/browse/FHIR-25249)).
1. Fix Link to LOINC LP29708-2 ([FHIR-25213](https://jira.hl7.org/browse/FHIR-25213)).
1. Corrected [guidance](http://hl7.org/fhir/us/core/STU3.1.1/all-meds.html#fetching-all-medications-active-medications-and-all-medications-for-an-encounter) for conveying "Patient-Reported medications" ([FHIR-25035](https://jira.hl7.org/browse/FHIR-25035))

---

### 3.1.0
- date: 2019-10-31
- url: http://hl7.org/fhir/us/core/STU3.1
- FHIR version : 4.0.1
#### Changes:
 In order meet the proposed *ONC U.S. Core Data for Interoperability** (USCDI) regulatory requirements for access to patient data, this STU Update of the US Core Implementation Guide has added new content. Structured Documents and the [Argonaut Project Team](https://argonautwiki.hl7.org/Argonaut_2019_Projects#Argonaut_R4) have spent the last several months reviewing, testing and providing invaluable feedback on these and other topics including most notably:
1) A US Core Provenance Profile and Basic Provenance guidance on fetching Provenance for patient data.
2) Medication List Guidance for fetching a patient medications
3) Recasting the US Core Device profile into a US Core Implantable Device Profile
4) A US Core spO2 by US Core Pulse Oximetry Profile
5) Updated search to support requiring search by multiple statuses
6) Guidance when the source has no data
7) General guidelines and considerations for DSTU2 to R4 Conversion
8) Guidance for language support
9) Considerations for fetching data for multiple patients]
10) Future considerations for times offset and timezone guidelines
11) Future Considerations for writing and updating data
12) Update security pageto reflect current testing.
13) Clarify definition of MustSupport to reflect the intent that the server must be able to populate a MustSupport element in order to claim conformance to the profile.
14) Expanding bindings for Procedure and Condition codes for quality measures and other purposes.
These sections as well as several other clarifications, corrections and technical changes that are listed in the sections below have been reviewed and voted on by the members of the [HL7 International Structured Documents WorkGroup](http://www.hl7.org/Special/committees/structure/index.cfm) who is sponsoring this STU Update comment period and reconciliation of the comments.


---

### 3.0.1
- date: 2019-09-01
- url: http://hl7.org/fhir/us/core/2019Sep
- FHIR version : 4.0.0
#### Changes:
 In order meet the proposed ONC U.S. Core Data for Interoperability (USCDI) regulatory requirements for access to patient data, this STU Update for Comment Version of the US Core Implementation Guide has added new content. The Argonaut Project Team has spent the last several months reviewing, testing and providing invaluable feedback on these and other topics including most notably:
1) A US Core Provenance Profile and guidance on fetching Provenance for patient data.
2) Guidance on fetching a patient’s medications
3) A US Core spO2 by Pulse Oximetry profile
4) Recasting the US Core Device profile into a US Core Implantable Device profile
5) Making server search requirements less opaque and requiring search by multiple statuses.
6) Guidance when the source has no data
7) General guidelines and considerations for DSTU2 to R4 Conversion
8) Guidance for language support
9) Considerations for Fetching data for multiple patients
10) Future considerations for times offset and timezone guidelines
These sections as well as several other clarifications, corrections and technical changes that are listed in the sections below have been reviewed and voted on by the members of the HL7 International Structured Documents WorkGroup who is sponsoring this STU Update comment period and reconciliation of the comments.

---

### 3.0.0
- date: 2019-06-15
- url: http://hl7.org/fhir/us/core/STU3
- FHIR version : 4.0.0
#### Changes:
 FHIR R4 version of US Core which added profiles for exchanging Clinical Notes, expanded search expectations, and updated guidance as a results of comments from balloters.

---

### 2.1.0
- date: 2018-12-04
- url: http://hl7.org/fhir/us/core/2019Jan
- FHIR version : 4.0.0
#### Changes:
 STU 3 Ballot #1. First ballot on FHIR R4.

---

### 2.0.0
- date: 2018-12-04
- url: http://hl7.org/fhir/us/core/STU2
- FHIR version : 3.0.1
#### Changes:
 Publication added the following profiles:
1)US Core DocumentReference Profile
2)US Core Encounter Profile
3)US Core PractitionerRole Profile


---

### 1.1.0
- date: 2017-12-20
- url: http://hl7.org/fhir/us/core/2108Jan
- FHIR version : 3.0.1
#### Changes:
 STU2 Ballot

---

### 1.0.1
- date: 2017-11-02
- url: http://hl7.org/fhir/us/core/1.0.1
- FHIR version : 3.0.1
#### Changes:
 This version corrects technical errata from the original publication and for FHIR R3.

---

### 1.0.0
- date: 2017-03-21
- url: http://hl7.org/fhir/us/core/STU1
- FHIR version : 3.0.1
#### Changes:
 The first official published version of this IG published immediately following the release of FHIR STU3

---

### 0.0.0
- date: 2017-12-06
- url: http://hl7.org/fhir/us/core/2017Jan
- FHIR version : 1.8.0
#### Changes:
 STU1 Ballot

---