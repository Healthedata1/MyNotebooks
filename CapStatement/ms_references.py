# %% [markdown]
# # Find all must support dependent profiles in StructureDefinitions
# 
# - see FHIR-39723
# - for hard coded path search all SD (in YAML) for:
#   -  all reference with must support = true profiles
#   -  all reference with must support = true and add't USCDI profiles when add add'l USCDI equal True
# - list of other profile that need to be supported
# - incorporate into narrative generator...
# - todo think about canonical too and !uscdi requirements as well! and inherited references from base. (such as Media) use snapshot instead?
#   - check if inherited reference if emopty ( e.g. Media )
# - associated url with title to publish  (see narrative generator)
# 

# %%
from pathlib import Path
from json import load, dumps
from yaml import load as y_load, dump as y_dump, FullLoader
from pprint import pprint
import pandas as pd
from IPython.display import display, HTML
yml_path = Path('/Users/ehaas/Documents/FHIR/US-Core/input/resources-yaml')
snapshot_path =  Path('/Users/ehaas/Documents/FHIR/US-Core/output')  # use this

my_path = snapshot_path

# %%
def get_my_dict(addl_uscdi = False):
    type_map={}
    title_map={}
    derived_map={}
    mydict = {}
    excludelist = []
    print(f'addl_uscdi={addl_uscdi}')
    whitelist = []

    count = 0
    cant_match_path = []

    for i in sorted(my_path.glob('Struct*.json')):
        my_urls = set() # MS only set
        my_uscdi_urls = set() # MS + USCDI set

        obj = y_load(i.read_text(),Loader=FullLoader) #dict
        if obj['id'] in excludelist or obj['type'] == 'Extension':
            continue
        type_map[obj['url']] = obj['type']
        title_map[obj['url']] = obj['title']
        derived_map[obj['url']] = obj['baseDefinition']
        # print(enum,i,)
        # print(obj['url'])
        #find references type elements in diff
        for element in obj['differential']['element']:
            # print(element['id'])
            # print()
        
            try:
                targetProfile = (type for type in element['type'] if type['code'] == 'Reference').__next__()['targetProfile']
            except KeyError:
                # find snapshot_element
                try:
                    snapshot_element =  (snapshot_element for snapshot_element in obj['snapshot']['element'] if snapshot_element['id'] == element['id']).__next__()
                    # check if snapshot_element has a type reference
                except StopIteration:
                    # print('id mismatch')
                    pass
                else:
                    try:
                        snapshot_reference = (type for type in snapshot_element['type'] if type['code'] == 'Reference').__next__()['targetProfile']
                        # print(f"++++++++++++++++snapshot_reference={snapshot_reference}+++++++++++++++++++++")
                        try:
                            if element['mustSupport']: # only Must Supports / no add;l uscdi elements
                                my_urls.update(snapshot_reference) #add list to set
                        except KeyError: # Must Supports + Add;l USCDI
                            my_uscdi_urls.update(snapshot_reference) #add list to set

                    except KeyError:
                        # print('not a type = reference')
                        pass
                    except StopIteration:
                        # print('not a type = reference')
                        pass
            except StopIteration:
                # print('no reference')
                pass
            else:
                ms_ext = None
                try:
                    ms_ext = (type for type in element['type'] if type['code'] == 'Reference').__next__()['_targetProfile']
                except KeyError:
                    # print('no  _targetProfile')
                    pass
                except StopIteration:
                    # print('stopIteration')
                    pass

                # print(targetProfile, ms_ext)
                
                # print(element['id'])
                # print(dict(zip(targetProfile,ms_ext)))
                # print()
                try:
                    zipped = dict(zip(targetProfile,ms_ext))
                    ms_targetProfile = [k for k,v in zipped.items() if v["extension"][0]['valueBoolean']]
                    # print(f"{element['id']} = {ms_targetProfile}\n")
                    try:
                        if element['mustSupport']: # only Must Supports / no add;l uscdi elements
                            my_urls.update(ms_targetProfile) #add list to set
                    except KeyError: # Must Supports + Add;l USCDI
                        my_uscdi_urls.update(ms_targetProfile) #add list to set
                except TypeError:
                    # print(f"{element['id']} = {targetProfile}\n")
                    try:
                        if element['mustSupport']: # only Must Supports / no add;l uscdi elements
                            my_urls.update(targetProfile) #add list to set
                    except KeyError: # Must Supports + Add;l USCDI
                        my_uscdi_urls.update(targetProfile) #add list to set             
        # print(f'{my_urls}\n')
        if addl_uscdi:
            mydict[obj['url']] = list(my_uscdi_urls)
        else:
            mydict[obj['url']] = list(my_urls)

    ### update profiles derived from other US Core profiles
    #
    #- iterate through and combine lists of profiles from parent profiles.   
    for k,v in derived_map.items():
        if v in mydict.keys():
            # print(k,v,mydict[k],mydict[v])
            mydict[k] = mydict[k] + mydict[v]
    # pprint(mydict)
    print('return mydict, type_map, title_map')
    return mydict, type_map, title_map


# %% [markdown]
# ### Create A Dependency Table Using DataFrames ******DISABLED*******

# %% [markdown]
# #### Map The Url To Types
# 
# - fetch US Core profile types from SD - done above
# - otherwise use the deduce the type from the fhir url  e.g.  uri = http://hl7.org/fhir/StructureDefinition/Observation -> uri.split('/')[-1]

# %% [markdown]
# #### Create A Markdown Table
# 
# - create a dataframe
#   - split the dict into keys and values
#   - create DF form a dict of list of keys, key types, values, value-types

# %%
mydict,type_map,title_map = get_my_dict()
keys = list(mydict.keys())
r_types_keys = [type_map[k] for k in keys]

t_types_values = []
t_profile_values = []
for v in list(mydict.values()):
    target_type = []
    for i,j in enumerate(v):
        # print(i,j)
        try:
            target_type.append(type_map[j])
        except KeyError:
            t_types_value = j.split('/')[-1]
            if t_types_value == 'Resource':
                target_type.append("Any Resource")
            else:
                target_type.append(t_types_value)
                
    # print(target_type)
    t_types_values.append('<br />'.join(target_type))
    t_profile_values.append('<br />'.join(v))

df = pd.DataFrame({'US Core Profile': keys, 'Resource Type':r_types_keys, 'Target US Core Profile or FHIR Resource': t_profile_values,  'Target Resource Type':t_types_values})
# my_md_table = df.to_markdown(index=False)
# display.Markdown(my_md_table)
# display.Markdown("foo<br />bar")
# df.to_dict('records')



# %% [markdown]
# ### map in the the links to US Core IG

# %%
def get_references_summary(addl_uscdi=False):
    mydict,type_map,title_map = get_my_dict(addl_uscdi=addl_uscdi)
    keys = list(mydict.keys())
    r_types_keys = [type_map[k] for k in keys]
    # uscore_profile_links
    uscore_profile_links = [f'<a href="{k}">{title_map[k]}</a>' for k in keys]
    # resource_links
    resource_links = [f'<a href="#{k.lower()}">{k}</a>' for k in r_types_keys]
    # target profile links
    values = list(mydict.values())
    t_profile_links = []
    t_types_links = []
    for v in values:
        p_links=[]
        r_links=[]
        for t in v:
            try:
                p_links.append(f'<a href="{t}">{title_map[t]}</a>')
                r_links.append(f'<a href="#{type_map[t].lower()}">{type_map[t]}</a>')
            except KeyError:
                if t == "http://hl7.org/fhir/StructureDefinition/Resource":
                    p_links.append(f'<a href="#">Any Resource</a>')
                    r_links.append(f'<a href="#">Any Resource</a>')
                else:
                    p_links.append(f'<a href="#{t.split("/")[-1].lower()}">{t.split("/")[-1]}</a>')
                    r_links.append(f'<a href="#{t.split("/")[-1].lower()}">{t.split("/")[-1]}</a>')

        t_profile_links.append('<br />'.join(p_links))
        t_types_links.append(' <br />'.join(r_links))
  

    #t_types_values
    references_summary = {'US Core Profile': uscore_profile_links, 'Resource Type':resource_links, 'Target US Core Profile or FHIR Resource': t_profile_links,  'Target Resource Type':t_types_links}
    # for i, v in enumerate(references_summary["US Core Profile"]):
    #     for r in references_summary:
    #         print(references_summary[r][i])
    #     print("---")
    print( "return references_summary")
    return references_summary


# %% [markdown]
# # create a table in jinja with links etc

# %%

def main(addl_uscdi=False):
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    in_path = ''
    in_file = 'test.j2'
    def markdown(text, *args, **kwargs):
        return commonmark(text, *args, **kwargs)

    env = Environment(
        loader=FileSystemLoader(searchpath = in_path),
        autoescape=select_autoescape(['html','xml','xhtml','j2','md'],),
        trim_blocks = True,
        lstrip_blocks = True,
        )
    env.filters['markdown'] = markdown
    template = env.get_template(in_file)

    references_summary = get_references_summary(addl_uscdi=addl_uscdi)
    print(references_summary['US Core Profile'][0])
    rendered = template.render(references_summary=references_summary)
    return (rendered)

# %%
if __name__ == '__main__':
    # from IPython.display import display, HTML
    print("main")
    # global addl_uscdi
    addl_uscdi = False
    my_table = main(addl_uscdi=addl_uscdi)
    display(HTML(my_table))


