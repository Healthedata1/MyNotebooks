


#### Mandatory Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators], [chains] and [composites] SHALL be supported.  the  modifiers, comparators, chains and composites that are listed as optional SHOULD be supported.:


1. **SHALL** support searching using the combination of the **[`patient`](SearchParameter-us-core-observation-patient.html)** and **[`category`](SearchParameter-us-core-observation-category.html)** search parameters:

    `GET [base]/Observation?patient=[reference]&category=http://hl7.org/fhir/observation-category|laboratory`

    Example:
    
    1. GET [base]/Observation?patient=1134281&amp;category=http://hl7.org/fhir/observation-category\|laboratory

    *Implementation Notes:* Fetches a bundle of all Observation resources for the specified patient and a category code = `laboratory` ([how to search by reference] and [how to search by token])

1. **SHALL** support searching using the combination of the **[`patient`](SearchParameter-us-core-observation-patient.html)** and **[`code`](SearchParameter-us-core-observation-code.html)** search parameters:
    - optional support for composite *OR* search on `code` (e.g.`code=,,...`)

    `GET [base]/Observation?patient=[reference]&code={[system]}|[code]{,,...}`

    Example:
    
    1. GET [base]/Observation?patient=1134281&amp;code=http://loinc.org\|2339-0
    1. GET [base]/Observation?patient=1134281&amp;code=http://loinc.org\|2339-0,http://loinc.org\|25428-4,2514-8

    *Implementation Notes:* Fetches a bundle of all Observation resources for the specified patient and observation code(s).  SHOULD support search by multiple report codes. The Observation `code` parameter searches `Observation.code only. ([how to search by reference] and [how to search by token])

1. **SHALL** support searching using the combination of the **[`patient`](SearchParameter-us-core-observation-patient.html)** and **[`category`](SearchParameter-us-core-observation-category.html)** and **[`date`](SearchParameter-us-core-observation-date.html)** search parameters:
    - including support for these `date` comparators: `gt,lt,ge,le`
    - optional support for composite *AND* search on `date` (e.g.`date=[date]&date=[date]&...`)

    `GET [base]/Observation?patient=[reference]&category=http://hl7.org/fhir/observation-category|laboratory&date={gt|lt|ge|le}[date]{&date={gt|lt|ge|le}[date]&...}`

    Example:
    
    1. GET [base]Observation?patient=555580&amp;category=http://hl7.org/fhir/observation-category\|laboratory&amp;date=ge2018-03-14

    *Implementation Notes:* Fetches a bundle of all Observation resources for the specified patient and date and a category code = `laboratory` ([how to search by reference] and [how to search by token] and [how to search by date])



#### Optional Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators], [chains] and [composites] SHOULD be supported.

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-observation-patient.html)** and **[`category`](SearchParameter-us-core-observation-category.html)** and **[`status`](SearchParameter-us-core-observation-status.html)** search parameters:

    `GET [base]/Observation?patient=[reference]&category=http://hl7.org/fhir/observation-category|laboratory&status={[system]}|[code]`

    Example:
    
    1. GET [base]/Observation?patient=1134281&amp;category=http://hl7.org/fhir/observation-category\|laboratory&amp;status=final

    *Implementation Notes:* Fetches a bundle of all Observation resources for the specified patient and category = `laboratory` and status ([how to search by reference] and [how to search by token])

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-observation-patient.html)** and **[`code`](SearchParameter-us-core-observation-code.html)** and **[`date`](SearchParameter-us-core-observation-date.html)** search parameters:
    - optional support for composite *OR* search on `code` (e.g.`code=,,...`)
    - including support for these `date` comparators: `gt,lt,ge,le`
    - optional support for composite *AND* search on `date` (e.g.`date=[date]&date=[date]&...`)

    `GET [base]/Observation?patient=[reference]&code={[system]}|[code]{,,...}&date={gt|lt|ge|le}[date]{&date={gt|lt|ge|le}[date]&...}`

    Example:
    
    1. GET [base]Observation?patient=555580&amp;code=http://loinc.org\|2339-0&amp;date=ge2019

    *Implementation Notes:* Fetches a bundle of all Observation resources for the specified patient and date and report code(s).  SHOULD support search by multiple report codes. ([how to search by reference] and [how to search by token] and [how to search by date])


{% include link-list.md %}