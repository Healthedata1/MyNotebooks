
#### Mandatory Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHALL be supported.  the  modifiers, comparators and chained parameters that are listed as optional SHOULD be supported.:


1. **SHALL** support searching for all conditions including problems, health concerns, and encounter diagnosis for a patient using the **`patient`** search parameter:

  `GET [base]/Condition?patient=[reference]`

    Example: GET [base]/Condition?patient=1137192

    *Implementation Notes:* Fetches a bundle of all Condition resources for the specified patient (how to search by [reference])



#### Optional Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHOULD be supported.

1. **SHOULD** support searching using the combination of the **`patient`** and **`clinical-status`** search parameters:

    `GET [base]/Condition?patient=[reference]&clinical-status=[token]`

    Example: GET [base/Condition?patient=[id]&amp;clinical-status=active,recurrance,remission

    *Implementation Notes:* Fetches a bundle of all Condition resources for the specified patient and all “active” statuses (active,relapse,remission). This will not return any “entered in error” resources because of the conditional presence of the clinicalStatus element. (how to search by [reference] and [token])

1. **SHOULD** support searching using the combination of the **`patient`** and **`category`** search parameters:

    `GET [base]/Condition?patient=[reference]&category=[token]`

    Example: GET [base]/Condition?patient=1032702&amp;category=problem,GET [base]/Condition?patient=1032702&amp;category=health-concern,GET [base]/Condition?patient=1032702&amp;category=encounter-diagnosis

    *Implementation Notes:* Fetches a bundle of all Condition resources for the specified patient and category. (how to search by [reference] and [token])

1. **SHOULD** support searching using the combination of the **`patient`** and **`code`** search parameters:

    `GET [base]/Condition?patient=[reference]&code=[token]`

    Example: GET [base]/Condition?patient=[id]&amp;code=[system|code]

    *Implementation Notes:* Fetches a bundle of all Condition resources for the specified patient and code. (how to search by [reference] and [token])

1. **SHOULD** support searching using the combination of the **`patient`** and **`onset-date`** search parameters:

    `GET [base]/Condition?patient=[reference]&onset-date={gt|lt|ge|le}[date]`

    Example: GET [base]Condition?patient=555580&amp;date=ge2018-01-14

    *Implementation Notes:* Fetches a bundle of all Condition resources for the specified patient and date.  (how to search by [reference] and [date])


{% include link-list.md %}