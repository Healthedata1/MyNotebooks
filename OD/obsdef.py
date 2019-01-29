
# %%markdown
OperationDefinition for creating a spreadsheet based approach to generate Observations
See discussion on Zulip regarding the common and simple need for a way to use ObservationDefinition as table or spreadsheet to create Observation instances based on a few 'base' profiles.

This Gist walks through creating a Spreadsheet based on my ObservationDefinition Logical Model which is a major redo of the existing one. Then using the spreadsheet to create several Observation instances which are ready to be populated with lab data.

The idea id ObservationDefinition needs to be structured simply and flat enough to be able to directly transform the stuff you need for creating a table.
the table is like a Dictionary of Observations for use and is a shortcut to creating 100s or 1000s of profiles.
The following proof of concept Python script takes this spreadsheet as an Excel spreadsheet (not a google sheet) and generates profile types (in the output console).
# %%markdown

od table proof of concept:read obs-def from a spreadsheet ('Dictionary' or 'Lbrary')
and apply to Obs Profile instance "template" which is ready to be filled with the data to create an Observation instance



run in python 3.6


Outline:
1.read row from od spreadsheets as dict
2.apply od spreadsheet data to named profile (SD)
3. write/display profile

# %%

# imports
import json, os, sys
from csv import DictReader
from pandas import read_csv
import logging
# logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')
logging.info('The logging module is working.')

# %%
# global variables and templates

in_path = '/Users/ehaas/Documents/Python/Notebooks/OD - od.csv'
sheet_name = 'od'
logging.info('source spreadsheet = {}'.format(source_spreadsheet))
outfile = 'outfile'  # name of output file

# %%

#********************* get patient data **********************
# preview data from  csv file )
df1 = read_csv(in_path)
df1
# %%


def getitems():  # read rows from od spreadsheets...  ( row 0 = headers, row 1 = description )
    with open(in_path, mode='r',encoding='utf-8-sig') as csv_file:
        csv_reader = DictReader(csv_file)
    return(csv_reader)

for item in getitems():
    print(item)
# %%

def getobs(r):# apply od spreadsheet data to profile
    obs = '''{{
      "resourceType": "Observation",
      "meta": {{ "profile": ["http://hl7.org/fhir/us/core/StructureDefinition/us-core-observationresults"],
      }},
      "status": "{status}",
      "category": {{
        "coding": [
          {{
            "system": "http://hl7.org/fhir/observation-category",
            "code": "laboratory",
            "display": "Laboratory"
          }}
        ],
        "text": "Laboratory"
      }},
      "code": {{
        "coding": [
          {{
            "system": "http://loinc.org",
            "code": "{codeCoding_0_Code}",
            "display": "{codeCoding_0_Display}"
          }}
        ],
        "text": "{codeText}"
      }},
      "subject": {{
        "reference": "Patient/example","display": "Amy Shaw"
      }},
      "effectiveDateTime": "{effectiveDateTime}",
      "valueQuantity": {{
        "value": "{resultValue}",
        "unit": "{unitUnit}",
        "system": "{unitCodeSystem}"
        "code": "{unitCodeCode}"
          }},
      "referenceRange": [
        {{
          "low": {{
            "value": {refLow},
            "unit": "{unitUnit}",
            "system": "{unitCodeSystem}"
            "code": "{unitCodeCode}"
          }},
          "high": {{
            "value": {refHigh},
            "unit": "{unitUnit}",
            "system": "{unitCodeSystem}"
            "code": "{unitCodeCode}"
          }},
          "type": {{
            "coding": [
              {{
                "system": "http://hl7.org/fhir/referencerange-meaning",
                "code": "{refType}",
              }}
            ],
        }}
      ]
    }}'''

    new_obs = obs.format(status='{status}', effectiveDateTime='{effectiveDateTime}', resultValue='{resultValue}', **r)
    return(new_obs)

# %%
# get main

def main():
    logging.info('read rows from od spreadsheets')
    rows = getitems()
    for i, r in enumerate(rows[1:]): #skip first one
        logging.info('row {} from od spreadsheets = {}'.format(i,r))
        for d in r:
            logging.info('{} = {}'.format(d,r[d]))
        logging.info('apply od spreadsheet data to profile TODO fix decimal typing right now all as string')
        new_obs = getobs(r)
        logging.info('new_obs = {}'.format(new_obs))

# %%
if __name__ == '__main__':
    qr_json = main()
    logging.info('End of program')

    When used with the sample spreadsheet, the script output the following 3 Observations profiles which a fully specified except for the actual Observation 'instance' data. I.e, dates, patient, status, actual result value, comments, dataabsentreason etc.
