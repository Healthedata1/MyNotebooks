#!/usr/bin/env python
# coding: utf-8

# ## Make Profile summaries using Jinja2 and Python Modele
# 
# *USE Python 3.7 to maintain order of Json files*
# 
# - Fetch SD file from IG
# - Spec_internals from IG Package.tgz
# - Create and use import Title map from ?Package?
# - Transform to Python model
# - use Jinja2 template to create a summary markdown file
# - save markdown file
# 
# 
# 
# *Note need a successful build to generate since based on ig output local file
# alternatively use package.files to generate*

# ### import python modules including R4 fhirclient models

# In[23]:


from fhirclient.r4models import structuredefinition as SD
from fhirclient.r4models import narrative as N
from fhirclient.r4models import valueset as VS
import fhirclient.r4models.identifier as I
import fhirclient.r4models.coding as C
import fhirclient.r4models.codeableconcept as CC
import fhirclient.r4models.fhirdate as D
import fhirclient.r4models.extension as X
import fhirclient.r4models.contactdetail as CD
import fhirclient.r4models.fhirreference as FR
from json import dumps, loads, load
from pprint import pprint
from jinja2 import Environment, FileSystemLoader, select_autoescape
from commonmark import commonmark
from IPython.display import display, HTML, Markdown
import title_map as tm
import os
from stringcase import snakecase, titlecase
from pathlib import Path


# ### Get file and return as dict

# In[24]:


#ig_package_path =  "//ERICS-AIR-2/ehaas/Documents/FHIR/US-Core-R4/output"
ig_package_path =  "/Users/ehaas/Documents/FHIR/US-Core-R4/output"
#ig_source_path = "//ERICS-AIR-2/ehaas/Documents/FHIR/US-Core-R4/source/"
ig_source_path = "/Users/ehaas/Documents/FHIR/US-Core-R4/source/"
#ig_source_path = ''

def open_file(in_path, f_name): # get files
    with open(f'{in_path}/{f_name}', encoding="utf8") as f:
        r = f.read()
        return(loads(r))
   


# ### Get spec_internal from package.tgz a json file which includes canonical to local relative page links

# In[25]:


import tarfile

def get_si(path):
    with tarfile.open(name=os.path.join(path,'package.tgz'), mode='r') as tf:
        #pprint(tf.getnames())
        f = tf.extractfile('other/spec.internals')
        r = f.read()
        return(loads(r))
    
       
si = get_si(ig_package_path) #spec internals
path_map = si['paths']

#  map  VS url to titles
title_map = {}

vs_files = [x for x in os.listdir(ig_package_path) if x.startswith("ValueSet") and x.endswith('.json')]
for i in vs_files:
    path = Path.cwd() / ig_package_path / i
    vs_json = path.read_text(encoding='utf8')
    vs = VS.ValueSet(loads(vs_json))
    title_map[vs.url]= vs.title if vs.title else 'None' # save in pages folder
     
title_map.update(tm.title_map) #add core to ig title maps

#path_map
title_map


# ### Using Jinja2 Template create md file for summary view 
# *using Markdown instead of html for easier hand editing, the line spacing is resolved after template is rendered.*
# 
# uses these elements:
#  -   'label',
#  -   'short',
#  -  'min',
#  -  'max',
#  -   'type',
#  -   'binding',
#  
#  plus:
#  an invariant list
#  a hash table of value set urls to valueset titles.
# 

# In[26]:


def get_summary(profile_id,diff,constraints):

    in_path = ''
    template_path = 'summary-template.j2'
    core_path = 'http://hl7.org/fhir/R4/'

    bindings = dict(
        required = f'{core_path}terminologies.html#required',
        extensible = f'{core_path}terminologies.html#extensible',
        preferred =f'{core_path}terminologies.html#preferred',
        example = f'{core_path}terminologies.html#example',
    )
    


    def markdown(text, *args, **kwargs):
        return commonmark(text, *args, **kwargs)

    env = Environment(
        loader=FileSystemLoader(searchpath = in_path),
        autoescape=select_autoescape(['html','xml','xhtml','j2','md'])
        )

    env.filters['markdown'] = markdown

    template = env.get_template(template_path)
    d = template.render(elements = diff, title_map=title_map, bindings=bindings, constraints=constraints, path_map = path_map)

    print(f'============== file_name = {profile_id}-summary.md ================')
    display(Markdown(d))
    return d


# ### Loop through profiles and update missing stuff in Differential with Snapshot then generate Markdown summary file and save

# In[27]:


#in_path = '/Users/ehaas/Documents/FHIR/US-Core-R4/output/StructureDefinition-'
#f_name = 'us-core-patient'
#in_path = '/Users/ehaas/.fhir/packages/hl7.fhir.us.core.r4#dev/package/' # package file keeps disappearing
in_path = '/Users/ehaas/Documents/FHIR/US-Core-R4/output'  # use local build dir.
# in_path ='//ERICS-AIR-2/ehaas/Documents/FHIR/US-Core-R4/output'  # when working on PC
#files = [x for x in os.listdir(in_path) if x.startswith("StructureDefinition") and x.endswith('json')]
files = [x for x in os.listdir(in_path) if x.startswith("StructureDefinition") and x.endswith('json')]
files


# In[28]:


summ_elements =[
       'label',
       'short',
       'min',
       'max',
       'type',
       'binding',
       'sliceName',
        ]

choice_types = {'valueQuantity': 'value[x]',
                'valueCodeableConcept': 'value[x]',
                'valueString': 'value[x]',
                'valueInteger': 'value[x]',
                'valueDecimal': 'value[x]',
                'valueDateTime': 'value[x]',
                'valueRange': 'value[x]',
                'valuePeriod': 'value[x]',
                'dueDuration': 'due[x]',
                'dueDate': 'due[x]',
                'effectivedateTime': 'effective[x]',
                'effectivePeriod': 'effective[x]',
               } 


# In[29]:


#files = [i for i in files if i =='StructureDefinition-us-core-practitioner.json']
for i in files:
    
    constraints = {}
    sd_dict = open_file(in_path,i)
    sd = SD.StructureDefinition(sd_dict)
    profile_id = sd.id
    print(f'========{profile_id}=======')
    for i in sd.differential.element:
        path = i.path
        #print(f'====Path = {path} =====')
        # GET Invariant Dict  path: human readable invariant list.
        try:
            k = next((k for k in sd.snapshot.element if k.path == path))
            constraint = [j.human for j in k.constraint if 'dom-' not in j.key and 'ele-' not in j.key  and 'ext-' not in j.key]
        except TypeError:
            constraint = []
        except StopIteration:
            constraint = []
        if constraint:
            constraints[path]=constraint         

        for k in summ_elements:
            #print(f'differential = {path}.{k} = {getattr(i,k)}')
            if getattr(i,k) == None:
                try:
                    snap_element = (s for s in sd.snapshot.element if s.path == path)           
                    new_val = getattr(next(snap_element),k)
                    #print(f'snapshot = {path}.{k} = {new_val}')
                    setattr(i,k,new_val)
                except StopIteration: # assume is an choice data type
                    print(f'no snapshot element for {path}.{k} = {getattr(i,k)} assume is an choice data type')
                    new_plist = []
                    for p in path.split('.'):
                        try:
                            new_plist.append(choice_types[p])
                        except KeyError:
                            new_plist.append(p)
                    new_path = '.'.join(new_plist)
                    #print(path,new_path)
                    snap_element = (s for s in sd.snapshot.element if s.path == new_path)           
                    new_val = getattr(next(snap_element),k)
                    #print(f'snapshot = {path}.{k} = {new_val}')
                    setattr(i,k,new_val)
            #print(f'differential post if = {path}.{k} = {getattr(i,k)}')
    summ_file = get_summary(profile_id,sd.differential.element,constraints)
    summ_file = os.linesep.join([s for s in summ_file.splitlines() if s]) # remove empty lines
    summ_file = summ_file.replace('####', '\n####')  #add a line before Must Supports

    f_name = f'{profile_id}-summary.md'
    # save in pages folder
    #ig_source_path = ''  # temp folder
    path = Path.cwd() / ig_source_path / 'pages' / '_includes' / f_name
    path.write_text(summ_file, encoding='utf8')

