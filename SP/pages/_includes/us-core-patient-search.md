
#### Mandatory Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHALL be supported.  the  modifiers, comparators and chained parameters that are listed as optional SHOULD be supported.:


1. **SHALL** support fetching a Patient using the **[`_id`](i.rel_url)** search parameter:

    `GET [base]/Patient[id]`

    Example: GET [base]/Patient/1032702

    *Implementation Notes:*  (how to search by the [logical id] of the resource)

1. **SHALL** support searching a Patient by an identifier such as a MPI using the **[`identifier`](i.rel_url)** search parameter:

  `GET [base]/Patient?identifier={[system]}|[code]`

    Example: GET [base]/Patient?identifier=http://hospital.smarthealthit.org\|1032702

    *Implementation Notes:*  (how to search by [token])

1. **SHALL** support searching using the **[`name`](i.rel_url)** search parameter:

  `GET [base]/Patient?name=[string]`

    Example: See combination searches below

    *Implementation Notes:* Search based on at least name and another patient element  (how to search by [string])

1. **SHOULD** support searching using the combination of the **[`birthdate`](SearchParameter-us-core-patient-birthdate.html)** and **[`name`](SearchParameter-us-core-patient-name.html)** search parameters:

    `GET [base]/Patient?birthdate=[date]&name=[string]`

    *Implementation Notes:*  (how to search by [birthdate] and [name])

1. **SHOULD** support searching using the combination of the **[`gender`](SearchParameter-us-core-patient-gender.html)** and **[`name`](SearchParameter-us-core-patient-name.html)** search parameters:

    `GET [base]/Patient?gender=[token]&name=[string]`

    *Implementation Notes:*  (how to search by [gender] and [name])



#### Optional Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHOULD be supported.

1. **SHOULD** support searching using the combination of the **[`birthdate`](SearchParameter-us-core-patient-birthdate.html)** and **[`family`](SearchParameter-us-core-patient-family.html)** search parameters:

    `GET [base]/Patient?birthdate=[date]&family=[string]`

    *Implementation Notes:*  (how to search by [date] and [string])

1. **SHOULD** support searching using the combination of the **[`family`](SearchParameter-us-core-patient-family.html)** and **[`gender`](SearchParameter-us-core-patient-gender.html)** search parameters:

    `GET [base]/Patient?family=[string]&gender=[token]`

    *Implementation Notes:*  (how to search by [string] and [token])


{% include link-list.md %}