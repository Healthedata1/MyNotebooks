### Find all not must support modifier elements in FHIR US Core

A Python script to find all modifier elements in FHIR US Core that are not marked as "must support," you would need to first access the FHIR US Core specification. This can be done by downloading the specification from the HL7 website or by accessing it through a web API that provides access to the FHIR specification.

Once you have access to the specification, you would need to parse through the structure definitions for each resource and extract the elements that have the "modifier" flag set to "true." Then, for each of these elements, you would need to check if the "mustSupport" flag is set to "true." If the "mustSupport" flag is not set to "true," then you would add the element to a list of elements that are not marked as "must support."


```python

from pathlib import Path
from json import loads
import pandas as pd

mods = ['implicitRules', 'modifierExtension']
def find_not_must_support_modifiers(my_path):
    not_must_support = []
    
    # Get the structure definitions from the specification
    # response = requests.get(spec_url + "/StructureDefinition")
    # if response.status_code == 200:
    #     structure_definitions = response.json()["entry"]
        
        # Iterate through each structure definition
    for my_file in my_path.glob('StructureDefinition*.json'):
        structure_definition = loads(my_file.read_text())
        profile = structure_definition["title"]

        elements = structure_definition["snapshot"]["element"]
        
        # Iterate through each element in the structure definition
        for element in elements:
            # print(element["path"])
            # Check if the element is a modifier
            if element["isModifier"] and not any(mod in element["path"] for mod in mods):
                # print(f'{element["path"]} is a modifier!!!')
                # Check if the element is marked as must support
                try:
                    if not element["mustSupport"]:
                      not_must_support.append({"profile": profile, "element": element["path"]})
                except KeyError:
                    not_must_support.append({"profile": profile, "element": element["path"]})
    return not_must_support

my_path = Path(r"/Users/ehaas/.fhir/packages/hl7.fhir.us.core#dev/package")
my_path

not_must_support = find_not_must_support_modifiers(my_path=my_path)
# print(not_must_support)
df = pd.DataFrame(not_must_support)
markdown_table = df.to_markdown()
print(markdown_table)
```

|    | profile                                                                   | element                                   |
|---:|:--------------------------------------------------------------------------|:------------------------------------------|
|  0 | US Core Respiratory Rate Profile                                          | Observation.value[x].comparator           |
|  1 | US Core Heart Rate Profile                                                | Observation.value[x].comparator           |
|  2 | US Core Body Temperature Profile                                          | Observation.value[x].comparator           |
|  3 | US Core Practitioner Profile                                              | Practitioner.identifier.use               |
|  4 | US Core Practitioner Profile                                              | Practitioner.name.use                     |
|  5 | US Core Practitioner Profile                                              | Practitioner.telecom.use                  |
|  6 | US Core Practitioner Profile                                              | Practitioner.address.use                  |
|  7 | US Core Pediatric BMI for Age Observation Profile                         | Observation.value[x].comparator           |
|  8 | US Core Pediatric Weight for Height Observation Profile                   | Observation.value[x].comparator           |
|  9 | US Core Patient Profile                                                   | Patient.identifier.use                    |
| 10 | US Core Patient Profile                                                   | Patient.active                            |
| 11 | US Core Patient Profile                                                   | Patient.name.use                          |
| 12 | US Core Patient Profile                                                   | Patient.deceased[x]                       |
| 13 | US Core Patient Profile                                                   | Patient.address.use                       |
| 14 | US Core Patient Profile                                                   | Patient.link                              |
| 15 | US Core Pulse Oximetry Profile                                            | Observation.value[x].comparator           |
| 16 | US Core Pulse Oximetry Profile                                            | Observation.component.value[x].comparator |
| 17 | US Core Pulse Oximetry Profile                                            | Observation.component.value[x].comparator |
| 18 | US Core Immunization Profile                                              | Immunization.isSubpotent                  |
| 19 | US Core Head Circumference Profile                                        | Observation.value[x].comparator           |
| 20 | US Core MedicationRequest Profile                                         | MedicationRequest.doNotPerform            |
| 21 | US Core Specimen Profile                                                  | Specimen.status                           |
| 22 | US Core Encounter Profile                                                 | Encounter.identifier.use                  |
| 23 | US Core Body Height Profile                                               | Observation.value[x].comparator           |
| 24 | US Core BMI Profile                                                       | Observation.value[x].comparator           |
| 25 | US Core Organization Profile                                              | Organization.identifier.use               |
| 26 | US Core Organization Profile                                              | Organization.telecom.use                  |
| 27 | US Core Organization Profile                                              | Organization.address.use                  |
| 28 | US Core Medication Profile                                                | Medication.status                         |
| 29 | US Core Blood Pressure Profile                                            | Observation.component.value[x].comparator |
| 30 | US Core Blood Pressure Profile                                            | Observation.component.value[x].comparator |
| 31 | US Core PractitionerRole Profile                                          | PractitionerRole.telecom.use              |
| 32 | US Core CarePlan Profile                                                  | CarePlan.activity.detail.status           |
| 33 | US Core CarePlan Profile                                                  | CarePlan.activity.detail.doNotPerform     |
| 34 | US Core ServiceRequest Profile                                            | ServiceRequest.doNotPerform               |
| 35 | US Core Location Profile                                                  | Location.address.use                      |
| 36 | US Core Implantable Device Profile                                        | Device.status                             |
| 37 | US Core Pediatric Head Occipital Frontal Circumference Percentile Profile | Observation.value[x].comparator           |
| 38 | US Core Body Weight Profile                                               | Observation.value[x].comparator           |

