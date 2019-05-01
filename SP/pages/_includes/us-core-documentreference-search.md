


#### Mandatory Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHALL be supported.  the  modifiers, comparators and chained parameters that are listed as optional SHOULD be supported.:


1. **SHALL** support fetching a DocumentReference using the **[`_id`](SearchParameter-us-core-documentreference-_id.html)** search parameter:

    `GET [base]/DocumentReference[id]`

    Example:
    
    1. GET [base]/DocumentReference/2169591
    1. GET [base]/DocumentReference?_id=2169591

    *Implementation Notes:* Fetches a single DocumentReference. The document itself is represented as a base64 encoded binary data element or retrieved using the link provided by the resource. If the document is a  relative link to a [Binary] resource like a resource reference, it can be subsequently retrieved using: `GET [base]/Binary/[id]`. ([how to search by the logical id] of the resource)

1. **SHALL** support searching for all documentreferences for a patient using the **[`patient`](SearchParameter-us-core-documentreference-patient.html)** search parameter:

    `GET [base]/DocumentReference?patient=[reference]`

    Example:
    
    1. GET [base]/DocumentReference?patient=1137192

    *Implementation Notes:* Fetches a bundle of all DocumentReference resources for the specified patient. See the implementation notes above for how to access the actual document. ([how to search by reference])

1. **SHALL** support searching practitioner role by specialty using the **[`specialty`](SearchParameter-us-core-practitionerrole-specialty.html)** search parameter:

  - including optional support of the `_include` parameter to indicate that these resources be included in the results: `PractitionerRole:endpoint, PractitionerRole:practitioner`

    `GET [base]/PractitionerRole?specialty={[system]}|[code]`

    Example:
    
    1. GET [base]/PractitionerRole?specialty=http://nucc.org/provider-taxonomy\|208D0000X

    *Implementation Notes:* Fetches a bundle containing  PractitionerRole resources matching the specialty ([how to search by token])

1. **SHALL** support searching practitioner role by practitioner name and identifier using chained parameters using the **[`practitioner`](SearchParameter-us-core-practitionerrole-practitioner.html)** search parameter:

  - including support for these chained parameters: `identifier, name`
  - including optional support of the `_include` parameter to indicate that these resources be included in the results: `PractitionerRole:endpoint, PractitionerRole:practitioner`

    `GET [base]/PractitionerRole?practitioner=[reference]`

    Example:
    
    1. GET [base]/PractitionerRole?practitioner.identifier=http://hl7.org/fhir/sid/us-npi\|97860456&amp;_include=PractitionerRole:practitioner&amp;_include=PractitionerRole?endpoint
    1. GET [base]/PractitionerRole?practitioner.name=Henry&amp;_include=PractitionerRole:practitioner&amp;_include=PractitionerRole?endpoint

    *Implementation Notes:* Fetches a bundle containing  PractitionerRole resources matching the chained parameter practitioner.name or practitioner.identifier. SHOULD support the _include for PractionerRole.practitioner and PractitionerRole.endpoint. ([how to search by reference])

1. **SHALL** support searching using the combination of the **[`patient`](SearchParameter-us-core-documentreference-patient.html)** and **[`category`](SearchParameter-us-core-documentreference-category.html)** search parameters:

    `GET [base]/DocumentReference?patient=[reference]&category=http://hl7.org/fhir/us/core/CodeSystem/us-core-documentreference-category|clinical-note`

    Example:
    
    1. GET [base]/DocumentReference?patient=1235541&amp;category=http://hl7.org/fhir/us/core/CodeSystem/us-core-documentreference-category\|clinical-note

    *Implementation Notes:* Fetches a bundle of all DocumentReference resources for the specified patient and category = `clinical-note`.  See the implementation notes above for how to access the actual document. ([how to search by reference] and [how to search by token])

1. **SHALL** support searching using the combination of the **[`patient`](SearchParameter-us-core-documentreference-patient.html)** and **[`category`](SearchParameter-us-core-documentreference-category.html)** and **[`date`](SearchParameter-us-core-documentreference-date.html)** search parameters:
  - including support for these comparators: `gt, lt, ge, le`

    `GET [base]/DocumentReference?patient=[reference]&category=http://hl7.org/fhir/us/core/CodeSystem/us-core-documentreference-category|clinical-note&date={gt|lt|ge|le}[date]`

    Example:
    
    1. GET [base]/DocumentReference?patient=1235541&amp;category=http://hl7.org/fhir/us/core/CodeSystem/us-core-documentreference-category\|clinical-note&amp;date=ge2019

    *Implementation Notes:* Fetches a bundle of all DocumentReference resources for the specified patient and category = `clinical=note` and date. See the implementation notes above for how to access the actual document. ([how to search by reference] and [how to search by token] and [how to search by date])

1. **SHALL** support searching using the combination of the **[`patient`](SearchParameter-us-core-documentreference-patient.html)** and **[`type`](SearchParameter-us-core-documentreference-type.html)** search parameters:

    `GET [base]/DocumentReference?patient=[reference]&type={[system]}|[code]`

    Example:
    
    1. GET [base]/DocumentReference?patient=1316024&amp;type=http://loinc.org 18842-5

    *Implementation Notes:* Fetches a bundle of all DocumentReference resources for the specified patient and type. See the implementation notes above for how to access the actual document. ([how to search by reference] and [how to search by token])



#### Optional Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHOULD be supported.

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-documentreference-patient.html)** and **[`status`](SearchParameter-us-core-documentreference-status.html)** search parameters:

    `GET [base]/DocumentReference?patient=[reference]&status={[system]}|[code]`

    Example:
    
    1. GET [base]/DocumentReference?patient=1235541

    *Implementation Notes:* Fetches a bundle of all DocumentReference resources for the specified patient and status. See the implementation notes above for how to access the actual document. ([how to search by reference] and [how to search by token])

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-documentreference-patient.html)** and **[`type`](SearchParameter-us-core-documentreference-type.html)** and **[`period`](SearchParameter-us-core-documentreference-period.html)** search parameters:
  - including support for these comparators: `gt, lt, ge, le`

    `GET [base]/DocumentReference?patient=[reference]&type={[system]}|[code]&period={gt|lt|ge|le}[date]`

    Example:
    
    1. GET [base]/DocumentReference?patient=2169591&amp;type=34133-9&amp;period=ge2019

    *Implementation Notes:* Fetches a bundle of all DocumentReference resources for the specified patient and type and period. See the implementation notes above for how to access the actual document. ([how to search by reference] and [how to search by token] and [how to search by date])


{% include link-list.md %}