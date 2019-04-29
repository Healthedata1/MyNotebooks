
#### Mandatory Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHALL be supported.  the  modifiers, comparators and chained parameters that are listed as optional SHOULD be supported.:


1. **SHALL** support searching for all immunizations for a patient using the **[`patient`](i.rel_url)** search parameter:

  `GET [base]/Immunization?patient=[reference]`

    Example: GET [base]/Immunization?patient=1137192

    *Implementation Notes:* Fetches a bundle of all Immunization resources for the specified patient (how to search by [reference])



#### Optional Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHOULD be supported.

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-immunization-patient.html)** and **[`date`](SearchParameter-us-core-immunization-date.html)** search parameters:

    `GET [base]/Immunization?patient=[reference]&date={gt|lt|ge|le}[date]`

    Example: GET [base]/Immunization?patient=1137192&amp;date=ge2019-01-14

    *Implementation Notes:* Fetches a bundle of all Immunization resources for the specified patient and date.  (how to search by [date] and [reference])

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-immunization-patient.html)** and **[`status`](SearchParameter-us-core-immunization-status.html)** search parameters:

    `GET [base]/Immunization?patient=[reference]&status=[token]`

    Example: GET [base]/Immunization?patient=1137192&amp;status=completed

    *Implementation Notes:* Fetches a bundle of all Immunization resources for the specified patient and date (how to search by [reference] and [token])


{% include link-list.md %}