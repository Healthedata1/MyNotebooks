
# Get wt data from csv using Pandas

- loop through rows and create observations for each one and validate and save


```python
import pandas as pd

df = pd.read_csv('wt_data.csv', skip_blank_lines=True)
df.dropna(how="all", inplace=True)
df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>instance_name</th>
      <th>instance_description</th>
      <th>source</th>
      <th>identifier</th>
      <th>assigner</th>
      <th>value</th>
      <th>Unnamed: 6</th>
      <th>effective_datetime</th>
      <th>patient_fhirid</th>
      <th>patient_identifier</th>
      <th>...</th>
      <th>encounter_fhirid</th>
      <th>encounter_identifier</th>
      <th>encounter_display</th>
      <th>device_fhirid</th>
      <th>device_identifier</th>
      <th>device_display</th>
      <th>servicerequest_fhirid</th>
      <th>servicerequest_identifier</th>
      <th>servicerequest_display</th>
      <th>modality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Patient Supplied WT Example 1</td>
      <td>This is a simple patient entered weight exampl...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>167.0</td>
      <td>7/7/21 15:02</td>
      <td>2021-07-07T15:02:35Z</td>
      <td>Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Patient Supplied WT Example 2</td>
      <td>This is a simple patient entered weight exampl...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>162.0</td>
      <td>7/8/21 3:02</td>
      <td>2021-07-08T03:02:35Z</td>
      <td>Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>ServiceRequest/123</td>
      <td>SR123456</td>
      <td>Provider X Home weight monitoring</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Patient Supplied WT Example 3</td>
      <td>This is a simple patient entered weight exampl...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>164.0</td>
      <td>7/8/21 15:02</td>
      <td>2021-07-08T15:02:35Z</td>
      <td>Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Device/123</td>
      <td>Dev123456</td>
      <td>WiTscale S200 Bluetooth scale</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 21 columns</p>
</div>




```python
df.dtypes
```




    instance_name                 object
    instance_description          object
    source                        object
    identifier                    object
    assigner                      object
    value                        float64
    Unnamed: 6                    object
    effective_datetime            object
    patient_fhirid                object
    patient_identifier           float64
    patient_display               object
    encounter_fhirid             float64
    encounter_identifier         float64
    encounter_display             object
    device_fhirid                 object
    device_identifier             object
    device_display                object
    servicerequest_fhirid         object
    servicerequest_identifier     object
    servicerequest_display        object
    modality                      object
    dtype: object




```python
for i,row in df[0:].iterrows():
    print(row)
    %run ./obs_maker.ipynb
```

    instance_name                                    Patient Supplied WT Example 1
    instance_description         This is a simple patient entered weight exampl...
    source                                                                     NaN
    identifier                                                                 NaN
    assigner                                                                   NaN
    value                                                                      167
    Unnamed: 6                                                        7/7/21 15:02
    effective_datetime                                        2021-07-07T15:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                                          NaN
    device_fhirid                                                              NaN
    device_identifier                                                          NaN
    device_display                                                             NaN
    servicerequest_fhirid                                                      NaN
    servicerequest_identifier                                                  NaN
    servicerequest_display                                                     NaN
    modality                                                                   NaN
    Name: 0, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 1
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 1
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project without any identifier, submission key, sensed/entered modality, or
          encounter data
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    effectiveDateTime: 2021-07-07 15:02:35+00:00
    valueQuantity:
      value: 167.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 1_tagged.yaml............
    instance_name                                    Patient Supplied WT Example 2
    instance_description         This is a simple patient entered weight exampl...
    source                                                                     NaN
    identifier                                                                 NaN
    assigner                                                                   NaN
    value                                                                      162
    Unnamed: 6                                                         7/8/21 3:02
    effective_datetime                                        2021-07-08T03:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                                          NaN
    device_fhirid                                                              NaN
    device_identifier                                                          NaN
    device_display                                                             NaN
    servicerequest_fhirid                                       ServiceRequest/123
    servicerequest_identifier                                             SR123456
    servicerequest_display                       Provider X Home weight monitoring
    modality                                                                   NaN
    Name: 1, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 2
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 2
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with a submission key
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    basedOn:
    - reference: ServiceRequest/123
      identifier:
        value: SR123456
      display: Provider X Home weight monitoring
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    effectiveDateTime: 2021-07-08 03:02:35+00:00
    valueQuantity:
      value: 162.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 2_tagged.yaml............
    instance_name                                    Patient Supplied WT Example 3
    instance_description         This is a simple patient entered weight exampl...
    source                                                                     NaN
    identifier                                                                 NaN
    assigner                                                                   NaN
    value                                                                      164
    Unnamed: 6                                                        7/8/21 15:02
    effective_datetime                                        2021-07-08T15:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                                          NaN
    device_fhirid                                                       Device/123
    device_identifier                                                    Dev123456
    device_display                                   WiTscale S200 Bluetooth scale
    servicerequest_fhirid                                                      NaN
    servicerequest_identifier                                                  NaN
    servicerequest_display                                                     NaN
    modality                                                                   NaN
    Name: 2, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 3
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 3
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with a device provided for simple provenance
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    effectiveDateTime: 2021-07-08 15:02:35+00:00
    valueQuantity:
      value: 164.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    device:
      reference: Device/123
      identifier:
        value: Dev123456
      display: WiTscale S200 Bluetooth scale
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 3_tagged.yaml............
    instance_name                                    Patient Supplied WT Example 4
    instance_description         This is a simple patient entered weight exampl...
    source                                    cdda928b-2d61-3a57-2eee-2d57336c9771
    identifier                                                                 NaN
    assigner                                                                   NaN
    value                                                                      167
    Unnamed: 6                                                         7/9/21 3:02
    effective_datetime                                        2021-07-09T03:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                                          NaN
    device_fhirid                                                              NaN
    device_identifier                                                          NaN
    device_display                                                             NaN
    servicerequest_fhirid                                                      NaN
    servicerequest_identifier                                                  NaN
    servicerequest_display                                                     NaN
    modality                                                                   NaN
    Name: 3, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 4
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 4
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with a meta.source identifier/string provided for simple provenance
      source: cdda928b-2d61-3a57-2eee-2d57336c9771
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    effectiveDateTime: 2021-07-09 03:02:35+00:00
    valueQuantity:
      value: 167.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 4_tagged.yaml............
    instance_name                                    Patient Supplied WT Example 5
    instance_description         This is a simple patient entered weight exampl...
    source                                                                     NaN
    identifier                                a9b492be-19e0-5018-4823-37781e420397
    assigner                                         WiTscale S200 Bluetooth scale
    value                                                                      165
    Unnamed: 6                                                        7/9/21 15:02
    effective_datetime                                        2021-07-09T15:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                                          NaN
    device_fhirid                                                              NaN
    device_identifier                                                          NaN
    device_display                                                             NaN
    servicerequest_fhirid                                                      NaN
    servicerequest_identifier                                                  NaN
    servicerequest_display                                                     NaN
    modality                                                                   NaN
    Name: 4, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 5
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 5
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with an identifier provided for simple provenance
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    identifier:
    - value: a9b492be-19e0-5018-4823-37781e420397
      assigner:
        display: WiTscale S200 Bluetooth scale
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    effectiveDateTime: 2021-07-09 15:02:35+00:00
    valueQuantity:
      value: 165.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 5_tagged.yaml............
    instance_name                                    Patient Supplied WT Example 6
    instance_description         This is a simple patient entered weight exampl...
    source                                                                     NaN
    identifier                                                                 NaN
    assigner                                                                   NaN
    value                                                                      168
    Unnamed: 6                                                        7/10/21 3:02
    effective_datetime                                        2021-07-10T03:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                           At Home Monitoring
    device_fhirid                                                              NaN
    device_identifier                                                          NaN
    device_display                                                             NaN
    servicerequest_fhirid                                                      NaN
    servicerequest_identifier                                                  NaN
    servicerequest_display                                                     NaN
    modality                                                                   NaN
    Name: 5, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 6
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 6
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with encounter data provided
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    encounter:
      display: At Home Monitoring
    effectiveDateTime: 2021-07-10 03:02:35+00:00
    valueQuantity:
      value: 168.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 6_tagged.yaml............
    instance_name                                    Patient Supplied WT Example 7
    instance_description         This is a simple patient entered weight exampl...
    source                                                                     NaN
    identifier                                                                 NaN
    assigner                                                                   NaN
    value                                                                      160
    Unnamed: 6                                                       7/10/21 15:02
    effective_datetime                                        2021-07-10T15:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                                          NaN
    device_fhirid                                                              NaN
    device_identifier                                                          NaN
    device_display                                                             NaN
    servicerequest_fhirid                                                      NaN
    servicerequest_identifier                                                  NaN
    servicerequest_display                                                     NaN
    modality                                                                sensed
    Name: 6, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 7
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 7
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with modality = sensed
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    extension:
    - url: http://www.fhir.org/guides/omhtofhir/StructureDefinition/extension-modality
      valueCode: sensed
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    effectiveDateTime: 2021-07-10 15:02:35+00:00
    valueQuantity:
      value: 160.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 7_tagged.yaml............
    instance_name                                    Patient Supplied WT Example 8
    instance_description         This is a simple patient entered weight exampl...
    source                                                                     NaN
    identifier                                                                 NaN
    assigner                                                                   NaN
    value                                                                      160
    Unnamed: 6                                                        7/11/21 3:02
    effective_datetime                                        2021-07-11T03:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                                          NaN
    device_fhirid                                                              NaN
    device_identifier                                                          NaN
    device_display                                                             NaN
    servicerequest_fhirid                                       ServiceRequest/123
    servicerequest_identifier                                             SR123456
    servicerequest_display                       Provider X Home weight monitoring
    modality                                                         self-reported
    Name: 7, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 8
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 8
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with a submission key and  modality = self-reported.
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    extension:
    - url: http://www.fhir.org/guides/omhtofhir/StructureDefinition/extension-modality
      valueCode: self-reported
    basedOn:
    - reference: ServiceRequest/123
      identifier:
        value: SR123456
      display: Provider X Home weight monitoring
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    effectiveDateTime: 2021-07-11 03:02:35+00:00
    valueQuantity:
      value: 160.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 8_tagged.yaml............
    instance_name                                    Patient Supplied WT Example 9
    instance_description         This is a simple patient entered weight exampl...
    source                                    1fb7cd90-9d9d-6334-133d-adfc5832484f
    identifier                                                                 NaN
    assigner                                                                   NaN
    value                                                                      166
    Unnamed: 6                                                       7/11/21 15:02
    effective_datetime                                        2021-07-11T15:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                                          NaN
    device_fhirid                                                              NaN
    device_identifier                                                          NaN
    device_display                                                             NaN
    servicerequest_fhirid                                       ServiceRequest/123
    servicerequest_identifier                                             SR123456
    servicerequest_display                       Provider X Home weight monitoring
    modality                                                                   NaN
    Name: 8, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 9
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 9
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with a submission key and source.
      source: 1fb7cd90-9d9d-6334-133d-adfc5832484f
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    basedOn:
    - reference: ServiceRequest/123
      identifier:
        value: SR123456
      display: Provider X Home weight monitoring
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    effectiveDateTime: 2021-07-11 15:02:35+00:00
    valueQuantity:
      value: 166.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 9_tagged.yaml............
    instance_name                                   Patient Supplied WT Example 10
    instance_description         This is a simple patient entered weight exampl...
    source                                                                     NaN
    identifier                                                                 NaN
    assigner                                                                   NaN
    value                                                                      168
    Unnamed: 6                                                        7/12/21 3:02
    effective_datetime                                        2021-07-12T03:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                                          NaN
    device_fhirid                                                       Device/123
    device_identifier                                                    Dev123456
    device_display                                   WiTscale S200 Bluetooth scale
    servicerequest_fhirid                                       ServiceRequest/123
    servicerequest_identifier                                             SR123456
    servicerequest_display                       Provider X Home weight monitoring
    modality                                                                   NaN
    Name: 9, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 10
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 10
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with a submission key and device data.
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    basedOn:
    - reference: ServiceRequest/123
      identifier:
        value: SR123456
      display: Provider X Home weight monitoring
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    effectiveDateTime: 2021-07-12 03:02:35+00:00
    valueQuantity:
      value: 168.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    device:
      reference: Device/123
      identifier:
        value: Dev123456
      display: WiTscale S200 Bluetooth scale
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 10_tagged.yaml............
    instance_name                                   Patient Supplied WT Example 11
    instance_description         This is a simple patient entered weight exampl...
    source                                    0dcdd41f-844f-290a-39e2-c9e2af22878d
    identifier                                ef138f8e-32f1-10ca-921f-72c1bbc825ee
    assigner                                         WiTscale S200 Bluetooth scale
    value                                                                      161
    Unnamed: 6                                                       7/12/21 15:02
    effective_datetime                                        2021-07-12T15:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                           At Home Monitoring
    device_fhirid                                                       Device/123
    device_identifier                                                    Dev123456
    device_display                                   WiTscale S200 Bluetooth scale
    servicerequest_fhirid                                       ServiceRequest/123
    servicerequest_identifier                                             SR123456
    servicerequest_display                       Provider X Home weight monitoring
    modality                                                                sensed
    Name: 10, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 11
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 11
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with source, identifier, submission key, sensed/entered modality, and
          encounter data
      source: 0dcdd41f-844f-290a-39e2-c9e2af22878d
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    extension:
    - url: http://www.fhir.org/guides/omhtofhir/StructureDefinition/extension-modality
      valueCode: sensed
    identifier:
    - value: ef138f8e-32f1-10ca-921f-72c1bbc825ee
      assigner:
        display: WiTscale S200 Bluetooth scale
    basedOn:
    - reference: ServiceRequest/123
      identifier:
        value: SR123456
      display: Provider X Home weight monitoring
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    encounter:
      display: At Home Monitoring
    effectiveDateTime: 2021-07-12 15:02:35+00:00
    valueQuantity:
      value: 161.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    device:
      reference: Device/123
      identifier:
        value: Dev123456
      display: WiTscale S200 Bluetooth scale
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 11_tagged.yaml............
    instance_name                                   Patient Supplied WT Example 12
    instance_description         This is a simple patient entered weight exampl...
    source                                    b3392a3a-0f95-49d9-1ea7-a79579ca4a1d
    identifier                                ad42644f-7f4f-14c5-6eec-ff9459540b51
    assigner                                         WiTscale S200 Bluetooth scale
    value                                                                      160
    Unnamed: 6                                                        7/13/21 3:02
    effective_datetime                                        2021-07-13T03:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                           At Home Monitoring
    device_fhirid                                                       Device/123
    device_identifier                                                    Dev123456
    device_display                                   WiTscale S200 Bluetooth scale
    servicerequest_fhirid                                       ServiceRequest/123
    servicerequest_identifier                                             SR123456
    servicerequest_display                       Provider X Home weight monitoring
    modality                                                                sensed
    Name: 11, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 12
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 12
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with source, identifier, submission key, sensed/entered modality, and
          encounter data
      source: b3392a3a-0f95-49d9-1ea7-a79579ca4a1d
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    extension:
    - url: http://www.fhir.org/guides/omhtofhir/StructureDefinition/extension-modality
      valueCode: sensed
    identifier:
    - value: ad42644f-7f4f-14c5-6eec-ff9459540b51
      assigner:
        display: WiTscale S200 Bluetooth scale
    basedOn:
    - reference: ServiceRequest/123
      identifier:
        value: SR123456
      display: Provider X Home weight monitoring
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    encounter:
      display: At Home Monitoring
    effectiveDateTime: 2021-07-13 03:02:35+00:00
    valueQuantity:
      value: 160.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    device:
      reference: Device/123
      identifier:
        value: Dev123456
      display: WiTscale S200 Bluetooth scale
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 12_tagged.yaml............
    instance_name                                   Patient Supplied WT Example 13
    instance_description         This is a simple patient entered weight exampl...
    source                                    e224e3c4-699f-2f7a-544d-d202301b35d5
    identifier                                08d57e91-1bce-68ed-6244-f7955ae3857e
    assigner                                         WiTscale S200 Bluetooth scale
    value                                                                      163
    Unnamed: 6                                                       7/13/21 15:02
    effective_datetime                                        2021-07-13T15:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                           At Home Monitoring
    device_fhirid                                                       Device/123
    device_identifier                                                    Dev123456
    device_display                                   WiTscale S200 Bluetooth scale
    servicerequest_fhirid                                       ServiceRequest/123
    servicerequest_identifier                                             SR123456
    servicerequest_display                       Provider X Home weight monitoring
    modality                                                                sensed
    Name: 12, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 13
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 13
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with source, identifier, submission key, sensed/entered modality, and
          encounter data
      source: e224e3c4-699f-2f7a-544d-d202301b35d5
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    extension:
    - url: http://www.fhir.org/guides/omhtofhir/StructureDefinition/extension-modality
      valueCode: sensed
    identifier:
    - value: 08d57e91-1bce-68ed-6244-f7955ae3857e
      assigner:
        display: WiTscale S200 Bluetooth scale
    basedOn:
    - reference: ServiceRequest/123
      identifier:
        value: SR123456
      display: Provider X Home weight monitoring
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    encounter:
      display: At Home Monitoring
    effectiveDateTime: 2021-07-13 15:02:35+00:00
    valueQuantity:
      value: 163.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    device:
      reference: Device/123
      identifier:
        value: Dev123456
      display: WiTscale S200 Bluetooth scale
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 13_tagged.yaml............
    instance_name                                   Patient Supplied WT Example 14
    instance_description         This is a simple patient entered weight exampl...
    source                                    911f886e-3e4e-a3a7-99d4-927b4b262efa
    identifier                                d26e9041-13c5-2612-14e4-8108d47d7f02
    assigner                                         WiTscale S200 Bluetooth scale
    value                                                                      163
    Unnamed: 6                                                        7/14/21 3:02
    effective_datetime                                        2021-07-14T03:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                           At Home Monitoring
    device_fhirid                                                       Device/123
    device_identifier                                                    Dev123456
    device_display                                   WiTscale S200 Bluetooth scale
    servicerequest_fhirid                                       ServiceRequest/123
    servicerequest_identifier                                             SR123456
    servicerequest_display                       Provider X Home weight monitoring
    modality                                                                sensed
    Name: 13, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 14
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 14
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with source, identifier, submission key, sensed/entered modality, and
          encounter data
      source: 911f886e-3e4e-a3a7-99d4-927b4b262efa
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    extension:
    - url: http://www.fhir.org/guides/omhtofhir/StructureDefinition/extension-modality
      valueCode: sensed
    identifier:
    - value: d26e9041-13c5-2612-14e4-8108d47d7f02
      assigner:
        display: WiTscale S200 Bluetooth scale
    basedOn:
    - reference: ServiceRequest/123
      identifier:
        value: SR123456
      display: Provider X Home weight monitoring
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    encounter:
      display: At Home Monitoring
    effectiveDateTime: 2021-07-14 03:02:35+00:00
    valueQuantity:
      value: 163.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    device:
      reference: Device/123
      identifier:
        value: Dev123456
      display: WiTscale S200 Bluetooth scale
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 14_tagged.yaml............
    instance_name                                   Patient Supplied WT Example 15
    instance_description         This is a simple patient entered weight exampl...
    source                                    6576859f-3286-7aa9-a1fa-c8f12b638ac1
    identifier                                6ea7ba5d-8f38-9454-4c16-864d345580c9
    assigner                                         WiTscale S200 Bluetooth scale
    value                                                                      168
    Unnamed: 6                                                       7/14/21 15:02
    effective_datetime                                        2021-07-14T15:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                           At Home Monitoring
    device_fhirid                                                       Device/123
    device_identifier                                                    Dev123456
    device_display                                   WiTscale S200 Bluetooth scale
    servicerequest_fhirid                                       ServiceRequest/123
    servicerequest_identifier                                             SR123456
    servicerequest_display                       Provider X Home weight monitoring
    modality                                                                sensed
    Name: 14, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 15
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 15
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with source, identifier, submission key, sensed/entered modality, and
          encounter data
      source: 6576859f-3286-7aa9-a1fa-c8f12b638ac1
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    extension:
    - url: http://www.fhir.org/guides/omhtofhir/StructureDefinition/extension-modality
      valueCode: sensed
    identifier:
    - value: 6ea7ba5d-8f38-9454-4c16-864d345580c9
      assigner:
        display: WiTscale S200 Bluetooth scale
    basedOn:
    - reference: ServiceRequest/123
      identifier:
        value: SR123456
      display: Provider X Home weight monitoring
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    encounter:
      display: At Home Monitoring
    effectiveDateTime: 2021-07-14 15:02:35+00:00
    valueQuantity:
      value: 168.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    device:
      reference: Device/123
      identifier:
        value: Dev123456
      display: WiTscale S200 Bluetooth scale
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 15_tagged.yaml............
    instance_name                                   Patient Supplied WT Example 16
    instance_description         This is a simple patient entered weight exampl...
    source                                    f573bd5e-a5ca-7193-7269-fc84eb845c50
    identifier                                0d2d3690-6683-0baf-3cdd-fe414ec80aa3
    assigner                                         WiTscale S200 Bluetooth scale
    value                                                                      166
    Unnamed: 6                                                        7/15/21 3:02
    effective_datetime                                        2021-07-15T03:02:35Z
    patient_fhirid                    Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
    patient_identifier                                                         NaN
    patient_display                                          Eldon718 Halvorson124
    encounter_fhirid                                                           NaN
    encounter_identifier                                                       NaN
    encounter_display                                           At Home Monitoring
    device_fhirid                                                       Device/123
    device_identifier                                                    Dev123456
    device_display                                   WiTscale S200 Bluetooth scale
    servicerequest_fhirid                                       ServiceRequest/123
    servicerequest_identifier                                             SR123456
    servicerequest_display                       Provider X Home weight monitoring
    modality                                                                sensed
    Name: 15, dtype: object
    /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker
    *******************************************************************************
    Patient Supplied WT Example 16
    *******************************************************************************
    resourceType: Observation
    meta:
      extension:
      - url: http://hl7.org/fhir/StructureDefinition/instance-name
        valueString: Patient Supplied WT Example 16
      - url: http://hl7.org/fhir/StructureDefinition/instance-description
        valueMarkdown: This is a simple patient entered weight example for the Argo Write
          project with source, identifier, submission key, sensed/entered modality, and
          encounter data
      source: f573bd5e-a5ca-7193-7269-fc84eb845c50
      profile:
      - http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight
      tag:
      - system: http://www.fhir.org/guides/argonaut/argo-write/CodeSystem/tags
        code: patient-supplied
    extension:
    - url: http://www.fhir.org/guides/omhtofhir/StructureDefinition/extension-modality
      valueCode: sensed
    identifier:
    - value: 0d2d3690-6683-0baf-3cdd-fe414ec80aa3
      assigner:
        display: WiTscale S200 Bluetooth scale
    basedOn:
    - reference: ServiceRequest/123
      identifier:
        value: SR123456
      display: Provider X Home weight monitoring
    status: final
    category:
    - coding:
      - system: http://terminology.hl7.org/CodeSystem/observation-category
        code: vital-signs
        display: Vital Signs
      text: Vital Signs
    code:
      coding:
      - system: http://loinc.org
        code: 29463-7
        display: Body Weight
      text: weight
    subject:
      reference: Patient/06e1f0dd-5fbe-4480-9bb4-6b54ec02d31b
      display: Eldon718 Halvorson124
    encounter:
      display: At Home Monitoring
    effectiveDateTime: 2021-07-15 03:02:35+00:00
    valueQuantity:
      value: 166.0
      unit: pounds
      system: http://unitsofmeasure.org
      code: '[lb_av]'
    device:
      reference: Device/123
      identifier:
        value: Dev123456
      display: WiTscale S200 Bluetooth scale
    
    ...validating



<h1>Validation output</h1><h3>Status Code = 200</h3> <div><p><b>Operation Outcome for :Validate resource </b></p><table class="grid"><tr><td><b>Severity</b></td><td><b>Location</b></td><td><b>Details</b></td><td><b>Diagnostics</b></td><td><b>Type</b></td></tr><tr><td>warning</td><td/><td>StructureDefinition reference "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight" could not be resolved</td><td/><td>invalid</td></tr><tr><td>warning</td><td/><td>A resource should have narrative for robust management () text.`div`.exists()</td><td/><td>invariant</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>information</td><td/><td>Could not verify slice for profile for profile http://hl7.org/fhir/StructureDefinition/Meta</td><td/><td>not-supported</td></tr><tr><td>warning</td><td/><td>Error Access violation at address 0000000000EDD9D3 in module 'FHIRServer.exe'. Read of address 0000000000000048 validating Coding</td><td/><td>code-invalid</td></tr></table></div>


    ...........saving to file /Users/ehaas/Documents/Python/MyNotebooks/Obs_maker/examples/Patient Supplied WT Example 16_tagged.yaml............



```python

```


```python

```
