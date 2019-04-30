


#### Mandatory Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHALL be supported.  the  modifiers, comparators and chained parameters that are listed as optional SHOULD be supported.:


1. **SHALL** support searching using the combination of the **[`patient`](SearchParameter-us-core-observation-patient.html)** and **[`code`](SearchParameter-us-core-observation-code.html)** search parameters:

  `GET [base]/Observation?patient=[reference]&code=http://loinc.org\|72166-2`

    Example: GET [base]/Observation?patient=1032702&amp;code=http://loinc.org\|72166-2

  *Implementation Notes:* Fetches a bundle of all Observation resources for the specified patient and observation code. ([how to search by patient] and [how to search by code])



#### Optional Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHOULD be supported.


{% include link-list.md %}