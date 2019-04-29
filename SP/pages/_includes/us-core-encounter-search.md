
#### Mandatory Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHALL be supported.  the  modifiers, comparators and chained parameters that are listed as optional SHOULD be supported.:


1. **SHALL** support fetching an Encounter using the **[`_id`](i.rel_url)** search parameter:

    `GET [base]/Encounter[id]`

    Example: GET [base]/Encounter/12354

    *Implementation Notes:*  (how to search by the [logical id] of the resource)

1. **SHALL** support searching for all encounters for a patient using the **[`patient`](i.rel_url)** search parameter:

  `GET [base]/Encounter?patient=[reference]`

    Example: GET [base]/Encounter?patient=1137192

    *Implementation Notes:* Fetches a bundle of all Encounter resources for the specified patient (how to search by [reference])

1. **SHOULD** support searching using the combination of the **[`date`](SearchParameter-us-core-encounter-date.html)** and **[`patient`](SearchParameter-us-core-encounter-patient.html)** search parameters:

    `GET [base]/Encounter?date={gt|lt|ge|le}[date]&patient=[reference]`

    *Implementation Notes:*  (how to search by [date] and [patient])



#### Optional Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHOULD be supported.

1. **SHOULD** support searching using the **[`identifier`](i.rel_url)** search parameter:

    `GET [base]/Encounter?identifier={[system]}|[code]`

    Example: GET [base]/Encounter?identifier=http://hospital.smarthealthit.org\|1032702

    *Implementation Notes:*  (how to search by [token])

1. **SHOULD** support searching using the combination of the **[`class`](SearchParameter-us-core-encounter-class.html)** and **[`date`](SearchParameter-us-core-encounter-date.html)** search parameters:

    `GET [base]/Encounter?class=[token]&date={gt|lt|ge|le}[date]`

    *Implementation Notes:*  (how to search by [date] and [token])

1. **SHOULD** support searching using the combination of the **[`class`](SearchParameter-us-core-encounter-class.html)** and **[`patient`](SearchParameter-us-core-encounter-patient.html)** search parameters:

    `GET [base]/Encounter?class=[token]&patient=[reference]`

    *Implementation Notes:*  (how to search by [reference] and [token])

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-encounter-patient.html)** and **[`status`](SearchParameter-us-core-encounter-status.html)** search parameters:

    `GET [base]/Encounter?patient=[reference]&status=[token]`

    *Implementation Notes:*  (how to search by [reference] and [token])

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-encounter-patient.html)** and **[`type`](SearchParameter-us-core-encounter-type.html)** search parameters:

    `GET [base]/Encounter?patient=[reference]&type=[token]`

    *Implementation Notes:*  (how to search by [reference] and [token])


{% include link-list.md %}