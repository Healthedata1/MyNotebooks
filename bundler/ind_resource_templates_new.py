summ = False
use_bundle=True
single_patient = False
use_task = False
uc = 'mrp'

base = '/Users/ehaas/Documents/FHIR/Davinci-DEQM'
source = 'source/examples'
out_path ='r4'  #local output dir
#out_path = f'{base}/{source}'  #DEQM source

mrs = [
    [
        'Practitioner/practitioner01',
        'Organization/organization01',
        'Organization/organization04',
        'Task/task01',
        'Organization/organization02',
        'Patient/patient01',
        'Encounter/encounter01',
        'Coverage/coverage01',
        'MeasureReport/indv-measurereport01',
        'Observation/observation01',
    ],
    [
        'Practitioner/practitioner02',
        'Organization/organization01',
        'Organization/organization04',
        'Task/task01',
        'Organization/organization02',
        'Patient/patient02',
        'Encounter/encounter02',
        'Coverage/coverage02',
        'MeasureReport/measurereport02',
        'Observation/observation02',
    ],
    [
        'Practitioner/practitioner03',
        'Organization/organization01',
        'Organization/organization04',
        'Task/task01',
        'Organization/organization02',
        'Patient/patient03',
        'Encounter/encounter03',
        'Coverage/coverage03',
        'MeasureReport/measurereport03',
        'Observation/observation03',
    ],
]