


#### Mandatory Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHALL be supported.  the  modifiers, comparators and chained parameters that are listed as optional SHOULD be supported.:


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

1. **SHALL** support searching using the combination of the **[`patient`](SearchParameter-us-core-careplan-patient.html)** and **[`category`](SearchParameter-us-core-careplan-category.html)** search parameters:

    `GET [base]/CarePlan?patient=[reference]&category=http://hl7.org/fhir/us/core/CodeSystem/careplan-category|assess-plan`

    Example:
    
    1. GET [base]/CarePlan?patient=1137192&amp;category=http://hl7.org/fhir/us/core/CodeSystem/careplan-category\|assess-plan

    *Implementation Notes:* Fetches a bundle of all CarePlan resources for the specified patient and category=`assess-plan` ([how to search by reference] and [how to search by token])



#### Optional Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHOULD be supported.

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-careplan-patient.html)** and **[`category`](SearchParameter-us-core-careplan-category.html)** and **[`date`](SearchParameter-us-core-careplan-date.html)** search parameters:
  - including support for these comparators: `gt, lt, ge, le`

    `GET [base]/CarePlan?patient=[reference]&category=http://hl7.org/fhir/us/core/CodeSystem/careplan-category|assess-plan&date={gt|lt|ge|le}[date]`

    Example:
    
    1. GET [base]/CarePlan?patient=1137192&amp;category=http://hl7.org/fhir/us/core/CodeSystem/careplan-category\|assess-plan&amp;date=ge2019

    *Implementation Notes:* Fetches a bundle of all CarePlan resources for the specified patient and category=`assess-plan` and date ([how to search by reference] and [how to search by token] and [how to search by date])

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-careplan-patient.html)** and **[`category`](SearchParameter-us-core-careplan-category.html)** and **[`status`](SearchParameter-us-core-careplan-status.html)** search parameters:

    `GET [base]/CarePlan?patient=[reference]&category=http://hl7.org/fhir/us/core/CodeSystem/careplan-category|assess-plan&status={[system]}|[code]`

    Example:
    
    1. GET [base]/CarePlan?patient=1137192&amp;category=http://hl7.org/fhir/us/core/CodeSystem/careplan-category\|assess-plan&amp;status=active

    *Implementation Notes:* Fetches a bundle of all CarePlan resources for the specified patient and category=`assess-plan` and status=`active` ([how to search by reference] and [how to search by token])

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-careplan-patient.html)** and **[`category`](SearchParameter-us-core-careplan-category.html)** and **[`status`](SearchParameter-us-core-careplan-status.html)** and **[`date`](SearchParameter-us-core-careplan-date.html)** search parameters:
  - including support for these comparators: `gt, lt, ge, le`

    `GET [base]/CarePlan?patient=[reference]&category=http://hl7.org/fhir/us/core/CodeSystem/careplan-category|assess-plan&status={[system]}|[code]&date={gt|lt|ge|le}[date]`

    Example:
    
    1. GET [base]/CarePlan?patient=1137192&amp;category=http://hl7.org/fhir/us/core/CodeSystem/careplan-category\|assess-plan&amp;status=active&amp;date=ge2019

    *Implementation Notes:* Fetches a bundle of all CarePlan resources for the specified patient and category=`assess-plan` and status=`active` and date ([how to search by reference] and [how to search by token] and [how to search by date])


{% include link-list.md %}