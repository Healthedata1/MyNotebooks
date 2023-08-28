def get_condition_resource(_title,_id,_datetime,_code,_status,_display):
    return {
    "resourceType": "Condition",
    "id": _id,
    "meta": {
        "profile": ["http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition"],
        "tags": [
            {
                "system": "http://example.org/fhir/tags",
                "code": f'Sept23_Connectathon_{_title.replace(" ","_")}_example',
            }
        ]
        },
    "extension": [
        {
            "url": "http://hl7.org/fhir/StructureDefinition/condition-assertedDate",
            "valueDateTime": _datetime
        }
    ],
    "clinicalStatus": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                "code": _status,
                "display": f'{_status.title()}'
            }
        ],
        "text": "Active"
    },
    "verificationStatus": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
                "code": "confirmed",
                "display": "Confirmed"
            }
        ],
        "text": "Confirmed"
    },
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/condition-category",
                    "code": "problem-list-item",
                    "display": "Problem List Item"
                }
            ],
            "text": "Problem List Item"
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": _code,
                "display": _display,
                "version": "http://snomed.info/sct/731000124108"
            }
        ],
        "text": _display.title()
    },
    "subject": {
        "reference": "Patient/example",
        "display": "Amy V. Shaw"
    },
    "recordedDate": _datetime
}