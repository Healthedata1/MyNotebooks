
# step 1 get MR increment id, Observation, patient to create new MRs save in memory

def reftofile(ref):
    return(ref.replace('/','-'))

from pathlib import Path
base = '/Users/ehaas/Documents/FHIR/Davinci-DEQM/input/examples/'
ref = 'MeasureReport/indv-measurereport02'
p = Path(rf'{base}{reftofile(ref)}.json')

print(p)

# print(p.is_file())

from json import loads
mr_dict = {}
MR1 = loads(p.read_text())

from pprint import pprint

#pprint(document)

from nested_lookup import nested_lookup
pprint(nested_lookup('reference', MR1))

from nested_lookup import get_all_keys
keys = get_all_keys(MR1)

pprint(keys)

mr_dict[MR1['id']] = MR1

from nested_lookup import nested_update

#help(nested_update)
MR2 = nested_update(
     MR1,
     key='reference',
     value=['Organization/organization02',
     'Patient/patient02',
     'Organization/organization01',
     'Observation/observation02'],
     in_place=False,
     treat_as_element=False,
   )

MR2['id'] = 'indv-measurereport02a'
mr_dict[MR2['id']] = MR2
MR3 = nested_update(
     MR1,
     key='reference',
     value=['Organization/organization02',
     'Patient/patient03',
     'Organization/organization01',
     'Observation/observation03'],
     in_place=False,
     treat_as_element=False,
   )

MR3['id'] = 'indv-measurereport02b'

#pprint(MR3)
mr_dict[MR3['id']] = MR3

# step 2 create a set of all references from the MR and referenced resources
ref_list = []
for mr in mr_dict.values():
    new_refs = nested_lookup('reference', mr)
    ref_list = ref_list + new_refs
    for ref in new_refs:
        #fetch resource
        p = Path(rf'{base}{reftofile(ref)}.json')
        r_dict = loads(p.read_text())
        new_refs2 = nested_lookup('reference', r_dict)
        pprint(f'ref = {ref}, new_refs = {new_refs2}')
        ref_list = ref_list + new_refs2
        for ref2 in new_refs2:
            #fetch resource
            p = Path(rf'{base}{reftofile(ref2)}.json')
            r_dict = loads(p.read_text())
            new_refs3 = nested_lookup('reference', r_dict)
            pprint(f'ref = {ref2}, new_refs = {new_refs3}')
            ref_list = ref_list + new_refs3

ref_list = ref_list + ['MeasureReport/indv-measurereport02', 'MeasureReport/indv-measurereport02a','MeasureReport/indv-measurereport02b',]
pprint(set(ref_list))

print(mr_dict)


# step 3 iterate through the set and get resources and Bundle
