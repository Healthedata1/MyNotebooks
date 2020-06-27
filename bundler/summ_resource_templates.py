summ = True
use_bundle=True
single_patient = False
use_task = False
uc = ''#'mrp'

base = '/Users/ehaas/Documents/FHIR/Davinci-DEQM'
source = 'source/examples'
#out_path ='r4'  #local output dir
out_path = f'{base}/{source}'  #DEQM source

mrs = [
    [
        'MeasureReport/summ-measurereport01',
        'Organization/organization01', ],
    [
        'MeasureReport/summ-measurereport02',
        'Organization/organization01', ],
    [
        'MeasureReport/summ-medicare-stratification-example',
        'Organization/organization01', ],
]

