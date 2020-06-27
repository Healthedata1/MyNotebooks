#! /usr/bin/env python3.7

qa_issues = {
    '"English"': '"English (Region=United States)"',
      '"Driver\'s License"': '"Driver\'s license Number"',
       '"display": "M"' : '"display": "Married"'
    }
    
org_npi = [
    {
      "use" : "official",
      "type" : {
        "coding" : [
          {
            "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",
            "code" : "PRN",
          }
        ]
      },
      "system" : "http://hl7.org/fhir/sid/us-npi",
      "value" : "9999999999"
    }
  ]

enc_type = [
               {
                  "coding": [
                     {
                        "code": "99221",
                        "display": "Initial hospital care",
                        "system": "http://www.ama-assn.org/go/cpt"
                     }
                  ],
                  "text": "Initial hospital care"
               }
            ]


summ = True
use_bundle=True
single_patient = False
use_task = False
uc = ''#'mrp'

base = '/Users/ehaas/Documents/FHIR/Davinci-DEQM'
source = 'source/examples'
#out_path ='r4'  #local output dir
out_path = f'{base}/{source}'  #DEQM source

mrs =

[
    'Practitioner/practitioner01',
    'Organization/organization01',
    'Organization/organization04',
    'Task/task01',
    'Organization/organization02',
    'Patient/patient01',
    'Encounter/encounter01',
    'Coverage/coverage01',
    'MeasureReport/measurereport01',
     'Observation/observation01',
]

mrp2_core_references = [
    'Practitioner/practitioner02',
    'Organization/organization01',
    'Organization/organization04',
    'Task/task02',
    'Organization/organization02',
    'Patient/patient02',
    'Encounter/encounter02',
    'Coverage/coverage02',
    'MeasureReport/measurereport02',
    'Observation/observation02',
]

mrp3_core_references = [
    'Practitioner/practitioner03',
    'Organization/organization01',
    'Organization/organization04',
    'Task/task03',
    'Organization/organization02',
    'Patient/patient03',
    'Encounter/encounter03',
    'Coverage/coverage03',
    'MeasureReport/measurereport03',
    'Observation/observation03',
]

mrp1=[
    {
  "id":"measurereport01",  
  "resourceType": "MeasureReport",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/indv-measurereport-deqm"
    ]
  },
  "extension": [
    {
      "url": "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/extension-certificationIdentifier",
      "valueIdentifier": {
        "system": "urn:oid:2.16.840.1.113883.3.2074.1",
        "value": "0015HQN9BD3304E"
      }
    },
    {
      "url": "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/extension-reportingVendor",
      "valueReference": {
        "reference": "Organization/organization02"
      }
    }
  ],
  "status": "complete",
  "type": "individual",
  "measure": "http://hl7.org/fhir/us/davinci-deqm/Measure/measure-mrp-example",
  "subject": {
    "reference": "Patient/patient01"
  },
  "date": "2018-09-05T16:59:52.404Z",
  "reporter": {
    "reference": "Organization/organization01"
  },
  "period": {
    "start": "2018-08-01",
    "end": "2018-09-01"
  },
  "group": [
    {
      "code": {
        "coding": [
          {
            "system": "http://hl7/example.org",
            "code": "112",
            "display": "112"
          }
        ]
      },
      "population": [
        {
          "code": {
            "coding": [
              {
                "system": "http://hl7/example.org",
                "code": "initial-population",
                "display": "Initial Population"
              }
            ]
          }
        }
      ],
      "measureScore": {
        "value": 100
      }
    }
  ],
  "evaluatedResource": [
    {
      "reference": "Task/task01"
    }
  ]
},
 {
  "id": "task01", 
  "resourceType" : "Task",
  "meta" : {
    "profile" : [
      "http://hl7.org/fhir/us/qicore/StructureDefinition/qicore-task"
    ]
  },

  "identifier" : [
    {
      "system" : "http://hl7/example.org",
      "value" : "19009"
    }
  ],
  "status" : "completed",
  "intent" : "plan",
  "priority" : "routine",
  "code" : {
    "coding" : [
      {
        "system" : "http://www.ama-assn.org/go/cpt",
        "code" : "1111F",
        "display" : "Medication Reconciliation"
      }
    ]
  },
  "for" : {
    "reference" : "Patient/patient01"
  },
  "encounter" : {
    "reference" : "Encounter/encounter01"
  },
  "executionPeriod" : {
    "start" : "2017-06-11",
    "end" : "2017-06-11"
  },
  "authoredOn" : "2018-09-25T14:24:23.584Z",
  "owner" : {
    "reference" : "Practitioner/practitioner01"
  }
},
{
   "id": "coverage01",
  "resourceType": "Coverage",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/coverage-deqm"
    ]
  },
  "status": "active",
  "policyHolder": {
    "reference": "Patient/patient01"
  },
  "subscriber": {
    "reference": "Patient/patient01"
  },
  "subscriberId": "A123456789",
  "beneficiary": {
    "reference": "Patient/patient01"
  },
  "relationship": {
    "coding": [
      {
        "code": "self"
      }
    ]
  },
  "payor": [
    {
      "reference": "Organization/organization04"
    }
  ]
},
    {
  "resourceType" : "Organization",
  "id" : "organization02",
  "meta" : {
    "profile" : [
      "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/organization-deqm"
    ]
  },
  "identifier" : [
    {
      "use" : "official",
      "type" : {
        "coding" : [
          {
            "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",
            "code" : "TAX",
            "display" : "Tax ID number"
          }
        ]
      },
      "system" : "urn:oid:2.16.840.1.113883.4.2",
      "value" : "456789124",
      "assigner" : {
        "display" : "www.irs.gov"
      }
    }
  ],
  "active" : True,
  "type" : [
    {
      "coding" : [
        {
          "system" : "http://terminology.hl7.org/CodeSystem/organization-type",
          "code" : "other",
          "display" : "Other"
        }
      ]
    }
  ],
  "name" : "DV Quality Measure Data Reporter",
  "telecom" : [
    {
      "system" : "phone",
      "value" : "(+1) 616-555-1212"
    }
  ],
  "address" : [
    {
      "line" : [
        "160 Glen Eagles Road"
      ],
      "city" : "Grand Rapids",
      "state" : "MI",
      "postalCode" : "49503",
      "country" : "USA"
    }
  ]
},
    {
  "resourceType" : "Organization",
  "id" : "organization04",
  "meta" : {
    "profile" : [
      "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/organization-deqm"
    ]
  },
  "identifier" : [
    {
      "use" : "official",
      "type" : {
        "coding" : [
          {
            "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",
            "code" : "TAX",
            "display" : "Tax ID number"
          }
        ]
      },
      "system" : "urn:oid:2.16.840.1.113883.4.2",
      "value" : "456789125",
      "assigner" : {
        "display" : "www.irs.gov"
      }
    }
  ],
  "active" : True,
  "type" : [
    {
      "coding" : [
        {
          "system" : "http://terminology.hl7.org/CodeSystem/organization-type",
          "code" : "ins",
          "display" : "Insurance Company"
        }
      ]
    }
  ],
  "name" : "DVPayer04",
  "telecom" : [
    {
      "system" : "phone",
      "value" : "(+1) 616-555-1212"
    }
  ],
  "address" : [
    {
      "line" : [
        "160 Glen Eagles Road"
      ],
      "city" : "Grand Rapids",
      "state" : "MI",
      "postalCode" : "49503",
      "country" : "USA"
    }
  ]
},
{
  "resourceType": "Observation",
  "id": "observation01",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/qicore/StructureDefinition/qicore-observation"
    ]
  },
  "status": "final",
  "category": [
    {
      "coding": [
        {
          "system": "http://hl7/example.org",
          "code": "measure",
          "display": "Measure"
        }
      ]
    }
  ],
  "code": {
    "coding": [
      {
        "system": "http://www.ama-assn.org/go/cpt",
        "code": "1111F",
        "display": "Medication Reconciliation"
      }
    ]
  },
  "subject": {
    "reference": "Patient/patient01"
  },
  "encounter": {
    "reference": "Encounter/encounter01"
  },
  "effectiveDateTime": "2018-09-29T14:15:04.424Z",
  "issued": "2018-09-29T14:15:04.424Z",
  "performer": [
    {
      "reference": "Practitioner/practitioner01"
    }
  ],
  "valueBoolean": True
}
]

mrp2=[
    {
  "id":"measurereport02",  
  "resourceType": "MeasureReport",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/indv-measurereport-deqm"
    ]
  },
  "extension": [
    {
      "url": "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/extension-certificationIdentifier",
      "valueIdentifier": {
        "system": "urn:oid:2.16.840.1.113883.3.2074.1",
        "value": "0015HQN9BD3304E"
      }
    },
    {
      "url": "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/extension-reportingVendor",
      "valueReference": {
        "reference": "Organization/organization02"
      }
    }
  ],
  "status": "complete",
  "type": "individual",
  "measure": "http://hl7.org/fhir/us/davinci-deqm/Measure/measure-mrp-example",
  "subject": {
    "reference": "Patient/patient02"
  },
  "date": "2018-09-05T16:59:52.404Z",
  "reporter": {
    "reference": "Organization/organization01"
  },
  "period": {
    "start": "2018-08-01",
    "end": "2018-09-01"
  },
  "group": [
    {
      "code": {
        "coding": [
          {
            "system": "http://hl7/example.org",
            "code": "112",
            "display": "112"
          }
        ]
      },
      "population": [
        {
          "code": {
            "coding": [
              {
                "system": "http://hl7/example.org",
                "code": "initial-population",
                "display": "Initial Population"
              }
            ]
          }
        }
      ],
      "measureScore": {
        "value": 100
      }
    }
  ],
  "evaluatedResource": [
    {
      "reference": "Task/task02"
    }
  ]
},
 {
  "id": "task02", 
  "resourceType" : "Task",
  "meta" : {
    "profile" : [
      "http://hl7.org/fhir/us/qicore/StructureDefinition/qicore-task"
    ]
  },

  "identifier" : [
    {
      "system" : "http://hl7/example.org",
      "value" : "19009"
    }
  ],
  "status" : "completed",
  "intent" : "plan",
  "priority" : "routine",
  "code" : {
    "coding" : [
      {
        "system" : "http://www.ama-assn.org/go/cpt",
        "code" : "1111F",
        "display" : "Medication Reconciliation"
      }
    ]
  },
  "for" : {
    "reference": "Patient/patient02"
  },
  "encounter" : {
    "reference": "Encounter/encounter02"
  },
  "executionPeriod" : {
    "start" : "2017-06-11",
    "end" : "2017-06-11"
  },
  "authoredOn" : "2018-09-25T14:24:23.584Z",
  "owner" : {
    "reference" : "Practitioner/practitioner02"
  }
},
{
   "id": "coverage02",
  "resourceType": "Coverage",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/coverage-deqm"
    ]
  },
  "status": "active",
  "policyHolder": {
    "reference": "Patient/patient02"
  },
  "subscriber": {
    "reference": "Patient/patient02"
  },
  "subscriberId": "A123456790",
  "beneficiary": {
    "reference": "Patient/patient02"
  },
  "relationship": {
    "coding": [
      {
        "code": "self"
      }
    ]
  },
  "payor": [
    {
      "reference": "Organization/organization04"
    }
  ]
},
    {
  "resourceType" : "Organization",
  "id" : "organization02",
  "meta" : {
    "profile" : [
      "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/organization-deqm"
    ]
  },
  "identifier" : [
    {
      "use" : "official",
      "type" : {
        "coding" : [
          {
            "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",
            "code" : "TAX",
            "display" : "Tax ID number"
          }
        ]
      },
      "system" : "urn:oid:2.16.840.1.113883.4.2",
      "value" : "456789124",
      "assigner" : {
        "display" : "www.irs.gov"
      }
    }
  ],
  "active" : True,
  "type" : [
    {
      "coding" : [
        {
          "system" : "http://terminology.hl7.org/CodeSystem/organization-type",
          "code" : "other",
          "display" : "Other"
        }
      ]
    }
  ],
  "name" : "DV Quality Measure Data Reporter",
  "telecom" : [
    {
      "system" : "phone",
      "value" : "(+1) 616-555-1212"
    }
  ],
  "address" : [
    {
      "line" : [
        "160 Glen Eagles Road"
      ],
      "city" : "Grand Rapids",
      "state" : "MI",
      "postalCode" : "49503",
      "country" : "USA"
    }
  ]
},
    {
  "resourceType" : "Organization",
  "id" : "organization04",
  "meta" : {
    "profile" : [
      "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/organization-deqm"
    ]
  },
  "identifier" : [
    {
      "use" : "official",
      "type" : {
        "coding" : [
          {
            "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",
            "code" : "TAX",
            "display" : "Tax ID number"
          }
        ]
      },
      "system" : "urn:oid:2.16.840.1.113883.4.2",
      "value" : "456789125",
      "assigner" : {
        "display" : "www.irs.gov"
      }
    }
  ],
  "active" : True,
  "type" : [
    {
      "coding" : [
        {
          "system" : "http://terminology.hl7.org/CodeSystem/organization-type",
          "code" : "ins",
          "display" : "Insurance Company"
        }
      ]
    }
  ],
  "name" : "DVPayer04",
  "telecom" : [
    {
      "system" : "phone",
      "value" : "(+1) 616-555-1212"
    }
  ],
  "address" : [
    {
      "line" : [
        "160 Glen Eagles Road"
      ],
      "city" : "Grand Rapids",
      "state" : "MI",
      "postalCode" : "49503",
      "country" : "USA"
    }
  ]
},
{
  "resourceType": "Observation",
  "id": "observation02",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/qicore/StructureDefinition/qicore-observation"
    ]
  },
  "status": "final",
  "category": [
    {
      "coding": [
        {
          "system": "http://hl7/example.org",
          "code": "measure",
          "display": "Measure"
        }
      ]
    }
  ],
  "code": {
    "coding": [
      {
        "system": "http://www.ama-assn.org/go/cpt",
        "code": "1111F",
        "display": "Medication Reconciliation"
      }
    ]
  },
  "subject": {
    "reference": "Patient/patient02"
  },
  "encounter": {
    "reference": "Encounter/encounter02"
  },
  "effectiveDateTime": "2018-09-29T14:15:04.424Z",
  "issued": "2018-09-29T14:15:04.424Z",
  "performer": [
    {
      "reference": "Practitioner/practitioner02"
    }
  ],
  "valueBoolean": True
}

]

mrp3=[
    {
  "id":"measurereport03",  
  "resourceType": "MeasureReport",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/indv-measurereport-deqm"
    ]
  },
  "extension": [
    {
      "url": "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/extension-certificationIdentifier",
      "valueIdentifier": {
        "system": "urn:oid:2.16.840.1.113883.3.2074.1",
        "value": "0015HQN9BD3304E"
      }
    },
    {
      "url": "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/extension-reportingVendor",
      "valueReference": {
        "reference": "Organization/organization02"
      }
    }
  ],
  "status": "complete",
  "type": "individual",
  "measure": "http://hl7.org/fhir/us/davinci-deqm/Measure/measure-mrp-example",
  "subject": {
    "reference": "Patient/patient03"
  },
  "date": "2018-09-05T16:59:52.404Z",
  "reporter": {
    "reference": "Organization/organization01"
  },
  "period": {
    "start": "2018-08-01",
    "end": "2018-09-01"
  },
  "group": [
    {
      "code": {
        "coding": [
          {
            "system": "http://hl7/example.org",
            "code": "112",
            "display": "112"
          }
        ]
      },
      "population": [
        {
          "code": {
            "coding": [
              {
                "system": "http://hl7/example.org",
                "code": "initial-population",
                "display": "Initial Population"
              }
            ]
          }
        }
      ],
      "measureScore": {
        "value": 100
      }
    }
  ],
  "evaluatedResource": [
    {
      "reference": "Task/task01"
    }
  ]
},
 {
  "id": "task03", 
  "resourceType" : "Task",
  "meta" : {
    "profile" : [
      "http://hl7.org/fhir/us/qicore/StructureDefinition/qicore-task"
    ]
  },

  "identifier" : [
    {
      "system" : "http://hl7/example.org",
      "value" : "19009"
    }
  ],
  "status" : "completed",
  "intent" : "plan",
  "priority" : "routine",
  "code" : {
    "coding" : [
      {
        "system" : "http://www.ama-assn.org/go/cpt",
        "code" : "1111F",
        "display" : "Medication Reconciliation"
      }
    ]
  },
  "for" : {
    "reference": "Patient/patient03"
  },
  "encounter" : {
    "reference": "Encounter/encounter03"
  },
  "executionPeriod" : {
    "start" : "2017-06-11",
    "end" : "2017-06-11"
  },
  "authoredOn" : "2018-09-25T14:24:23.584Z",
  "owner" : {
    "reference" : "Practitioner/practitioner03"
  }
},
{
   "id": "coverage03",
  "resourceType": "Coverage",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/coverage-deqm"
    ]
  },
  "status": "active",
  "policyHolder": {
    "reference": "Patient/patient03"
  },
  "subscriber": {
    "reference": "Patient/patient03"
  },
  "subscriberId": "A123456795",
  "beneficiary": {
    "reference": "Patient/patient03"
  },
  "relationship": {
    "coding": [
      {
        "code": "self"
      }
    ]
  },
  "payor": [
    {
      "reference": "Organization/organization04"
    }
  ]
},
    {
  "resourceType" : "Organization",
  "id" : "organization02",
  "meta" : {
    "profile" : [
      "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/organization-deqm"
    ]
  },
  "identifier" : [
    {
      "use" : "official",
      "type" : {
        "coding" : [
          {
            "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",
            "code" : "TAX",
            "display" : "Tax ID number"
          }
        ]
      },
      "system" : "urn:oid:2.16.840.1.113883.4.2",
      "value" : "456789124",
      "assigner" : {
        "display" : "www.irs.gov"
      }
    }
  ],
  "active" : True,
  "type" : [
    {
      "coding" : [
        {
          "system" : "http://terminology.hl7.org/CodeSystem/organization-type",
          "code" : "other",
          "display" : "Other"
        }
      ]
    }
  ],
  "name" : "DV Quality Measure Data Reporter",
  "telecom" : [
    {
      "system" : "phone",
      "value" : "(+1) 616-555-1212"
    }
  ],
  "address" : [
    {
      "line" : [
        "160 Glen Eagles Road"
      ],
      "city" : "Grand Rapids",
      "state" : "MI",
      "postalCode" : "49503",
      "country" : "USA"
    }
  ]
},
    {
  "resourceType" : "Organization",
  "id" : "organization04",
  "meta" : {
    "profile" : [
      "http://hl7.org/fhir/us/davinci-deqm/StructureDefinition/organization-deqm"
    ]
  },
  "identifier" : [
    {
      "use" : "official",
      "type" : {
        "coding" : [
          {
            "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",
            "code" : "TAX",
            "display" : "Tax ID number"
          }
        ]
      },
      "system" : "urn:oid:2.16.840.1.113883.4.2",
      "value" : "456789125",
      "assigner" : {
        "display" : "www.irs.gov"
      }
    }
  ],
  "active" : True,
  "type" : [
    {
      "coding" : [
        {
          "system" : "http://terminology.hl7.org/CodeSystem/organization-type",
          "code" : "ins",
          "display" : "Insurance Company"
        }
      ]
    }
  ],
  "name" : "DVPayer04",
  "telecom" : [
    {
      "system" : "phone",
      "value" : "(+1) 616-555-1212"
    }
  ],
  "address" : [
    {
      "line" : [
        "160 Glen Eagles Road"
      ],
      "city" : "Grand Rapids",
      "state" : "MI",
      "postalCode" : "49503",
      "country" : "USA"
    }
  ]
},
    {
  "resourceType": "Observation",
  "id": "observation03",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/qicore/StructureDefinition/qicore-observation"
    ]
  },
  "status": "final",
  "category": [
    {
      "coding": [
        {
          "system": "http://hl7/example.org",
          "code": "measure",
          "display": "Measure"
        }
      ]
    }
  ],
  "code": {
    "coding": [
      {
        "system": "http://www.ama-assn.org/go/cpt",
        "code": "1111F",
        "display": "Medication Reconciliation"
      }
    ]
  },
  "subject": {
    "reference": "Patient/patient03"
  },
  "encounter": {
    "reference": "Encounter/encounter03"
  },
  "effectiveDateTime": "2018-09-29T14:15:04.424Z",
  "issued": "2018-09-29T14:15:04.424Z",
  "performer": [
    {
      "reference": "Practitioner/practitioner03"
    }
  ],
  "valueBoolean": True
}

]