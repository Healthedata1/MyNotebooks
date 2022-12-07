survey_obs = {
    "resourceType": "Observation",
    "id": "id",
    "meta": {
        "extension": [
            {
                "url": "http://hl7.org/fhir/StructureDefinition/instance-name",
                "valueString": "Prapare Example [loinc]"
            },
            {
                "url": "http://hl7.org/fhir/StructureDefinition/instance-description",
                "valueMarkdown": "This is a Prapare Multiselect Example for the *US Core Screening Response Observation Profile*."
            }
        ],
        "profile": [
            "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-screening-assessment"
        ]
    },
    "status": "final",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "survey",
                    "display": "Survey"
                }
            ]
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "code",
                "display": "display]"
            }
        ]
    },
    "subject": {
        "reference": "Patient/example"
    },
    "effectiveDateTime": "2022-03-28T18:30:40-07:00",
    "performer": [
        {
            "reference": "Patient/example"
        }
    ],
    "hasMember": [
      {
          "reference": "reference",
          "display": "display"
      }
    ],
    "derivedFrom": [
        {
            "reference": "reference",
            "display": "display"
        }
    ]
}