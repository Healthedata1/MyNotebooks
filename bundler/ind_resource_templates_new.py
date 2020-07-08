summ = False
use_bundle=True
single_patient = False
use_task = True
uc = 'mrp'

base = '/Users/ehaas/Documents/FHIR/Davinci-DEQM'
source = 'input/examples'
out_path ='r4'  #local output dir
#out_path = f'{base}/{source}'  #DEQM source

 refs = {'Encounter/encounter01',
 'Encounter/encounter02',
 'Encounter/encounter03',
 'MeasureReport/indv-measurereport02',
 'MeasureReport/indv-measurereport02a',
 'MeasureReport/indv-measurereport02b',
 'Observation/observation01',
 'Observation/observation02',
 'Observation/observation03',
 'Organization/organization01',
 'Organization/organization02',
 'Organization/organization03',
 'Patient/patient01',
 'Patient/patient02',
 'Patient/patient03',
 'Practitioner/practitioner01',
 'Practitioner/practitioner02'}
