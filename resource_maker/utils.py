#!/usr/bin/env python
# coding: utf-8

from fhir.resources.observation import Observation
from fhir.resources import construct_fhir_element
from requests import post
from IPython.display import display as Display, HTML
from pathlib import Path
from yaml import load, FullLoader

def get_template(r_type):
    #/Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/Provenance.yml
    path = Path.cwd() / 'fhir_templates' /f'{r_type}.yml'
    r_dict = load(path.read_text(), Loader=FullLoader)
    r_obj = construct_fhir_element(r_type,r_dict)
    return r_obj

def get_element_type(resource,element):
    try:
        element_type = next(i.type_.__resource_type__ for i in resource.element_properties() if i.name == element)
    except AttributeError as e:
        print(e)
    return element_type

def new_dict(**kwargs):
    '''
    Functions to create fhir type dicts from data

    scrubs null from data too

    return only if object not empty else return None

    datatypes covered:

    - Identifier
    - Reference
    - Coding
    - Extension
    '''
    none_list = [None,{}]
    new_dict = {}
    for k,v in kwargs.items():
        #print(k,v)
        new_dict[k] = v
        #print(new_dict)
    new_dict = {k: v for k, v in new_dict.items() if v==v and v not in none_list} # scrub dict of None   
    if new_dict:
        return new_dict


def update_obj(element,element_dict,resource,replace=False):
    ### function to add complex elements to resource
    element_type = get_element_type(resource,element)
    if element_dict:
        new_element=construct_fhir_element(element_type,element_dict)
    else:
        return
    if not replace:
        try: # assume not a list 
            setattr(resource,element,new_element) # not a list 
            #print(getattr(resource,element).yaml())
        except: # treat as list
            try: # assume list already exists
                getattr(resource,element).append(new_element)
            except: # list does not exist
                setattr(resource,element,[new_element])
            #print(getattr(resource,element)[0].yaml())
    else:
        setattr(resource,element,[new_element])

        
def validate(pyfhir):
    print(pyfhir.resource_type)
    # validate fhir resource as fhir.resource object
    #fhir_test_server = 'http://test.fhir.org/r4'
    #fhir_test_server = 'http://hapi.fhir.org/baseR4'
    fhir_test_server = 'http://wildfhir4.aegis.net/fhir4-0-1'   
    headers = {
    'Accept':'application/fhir+json',
    'Content-Type':'application/fhir+json'
    }
    r = post(f'{fhir_test_server}/{pyfhir.resource_type}/$validate', headers = headers, data = pyfhir.json())
    print('...validating')
    r.status_code, r.json()
    Display(HTML(f'<h1>Validation output</h1><h3>Status Code = {r.status_code}</h3> {r.json()["text"]["div"]}'))

        
if __name__ == '__main__':
    obs_obj = Observation.parse_file("Observation_wt.yml")
    element = 'encounter'
    element_dict = new_dict(
            reference = "row.encounter_fhirid",
            identifier = new_dict(value = "row.encounter_identifier"),  # business identifier
            display = "row.encounter_display",
            )
    update_obj(element,element_dict,obs_obj)
    print(obs_obj.yaml())
    validate(obs_obj)

