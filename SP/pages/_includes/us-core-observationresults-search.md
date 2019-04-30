


#### Mandatory Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHALL be supported.  the  modifiers, comparators and chained parameters that are listed as optional SHOULD be supported.:


1. **SHALL** support searching using the combination of the **[`patient`](SearchParameter-us-core-observation-patient.html)** and **[`category`](SearchParameter-us-core-observation-category.html)** search parameters:

  `GET [base]/Observation?patient=[reference]&category=http://hl7.org/fhir/observation-category\|laboratory`

    Example: GET [base]/Observation?patient=1134281&amp;category=http://hl7.org/fhir/observation-category\|laboratory

  *Implementation Notes:* Fetches a bundle of all Observation resources for the specified patient and a category code = `laboratory` ([how to search by patient] and [how to search by category])

1. **SHALL** support searching using the combination of the **[`patient`](SearchParameter-us-core-observation-patient.html)** and **[`code`](SearchParameter-us-core-observation-code.html)** search parameters:

  `GET [base]/Observation?patient=[reference]&code=[token]`

    Example: GET [base]/Observation?patient=1134281&amp;code=http://loinc.org\|2339-0,GET [base]/Observation?patient=1134281&amp;code=http://loinc.org\|2339-0,http://loinc.org\|25428-4,2514-8

  *Implementation Notes:* Fetches a bundle of all Observation resources for the specified patient and observation code(s).  SHOULD support search by multiple report codes. The Observation �code� parameter searches `Observation.code only. ([how to search by patient] and [how to search by code])

1. **SHALL** support searching using the combination of the **[`patient`](SearchParameter-us-core-observation-patient.html)** and **[`category`](SearchParameter-us-core-observation-category.html)** and **[`date`](SearchParameter-us-core-observation-date.html)** search parameters:
  - including support for these comparators: `gt, lt, ge, le`

  `GET [base]/Observation?patient=[reference]&category=http://hl7.org/fhir/observation-category\|laboratorydate={gt|lt|ge|le}[date]`

    Example: GET [base]Observation?patient=555580&amp;category=http://hl7.org/fhir/observation-category\|laboratory&amp;date=ge2018-03-14

  *Implementation Notes:* Fetches a bundle of all Observation resources for the specified patient and date and a category code = `laboratory` ([how to search by patient] and [how to search by category] and [how to search by date])



#### Optional Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHOULD be supported.

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-observation-patient.html)** and **[`category`](SearchParameter-us-core-observation-category.html)** and **[`status`](SearchParameter-us-core-observation-status.html)** search parameters:

  `GET [base]/Observation?patient=[reference]&category=[token]&status=[token]`

   Example: GET [base]/Observation?patient=1134281&amp;category=http://hl7.org/fhir/observation-category\|laboratory&amp;status=final

   *Implementation Notes:* Fetches a bundle of all Observation resources for the specified patient and category and status ([how to search by reference] and [how to search by token])

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-observation-patient.html)** and **[`code`](SearchParameter-us-core-observation-code.html)** and **[`date`](SearchParameter-us-core-observation-date.html)** search parameters:
  - including support for these comparators: `gt, lt, ge, le`

  `GET [base]/Observation?patient=[reference]&code=[token]&date={gt|lt|ge|le}[date]`

   Example: GET [base]Observation?patient=555580&amp;code=http://loinc.org\|2339-0&amp;date=ge2019

   *Implementation Notes:* Fetches a bundle of all Observation resources for the specified patient and date and report code(s).  SHOULD support search by multiple report codes. ([how to search by reference] and [how to search by token] and [how to search by date])

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-observation-patient.html)** and **[`status`](SearchParameter-us-core-observation-status.html)** search parameters:

  `GET [base]/Observation?patient=[reference]&status=[token]`

   Example: GET [base]/Observation?patient=1137192&amp;status=final

   *Implementation Notes:* Fetches a bundle of all !Observation resources for the specified patient and status ([how to search by reference] and [how to search by token])


{% include link-list.md %}