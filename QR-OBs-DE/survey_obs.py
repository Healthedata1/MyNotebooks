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

docref = {
  "resourceType" : "DocumentReference",
  "id" : "docref",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.19.5.99999.1"
  }],
  "status" : "current",
  "type" : {
    "coding" : [{
      "system" : "http://loinc.org",
      "code" : "34133-9",
      "display" : "Summary of episode note"
    }],
    "text" : "CCD Document"
  },
  "category" : [{
    "coding" : [{
      "system" : "http://hl7.org/fhir/us/core/CodeSystem/us-core-documentreference-category",
      "code" : "clinical-note",
      "display" : "Clinical Note"
    }],
    "text" : "Clinical Note"
  }],
    "subject": {
        "reference": "Patient/example"
    },
    "created": "2022-01-01T12:00:00Z",
    "indexed": "2022-01-01T12:00:00Z",
    "author": [
        {
            "reference": "Practitioner/example"
        }
    ],
    "content": [
        {
            "attachment": {
                "contentType": "application/pdf",
                "data": "JVBERi0xLjQKJ...",
                "title": "PatientHealthQuestionnaire-2_v1.0_2014Jul2"
            }
        }
    ]
}