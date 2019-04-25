




#### Optional Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHOULD be supported.

1. **SHOULD** support searching using the **`address`** search parameter:

  `GET [base]/!Patient?address=[string]`

  Example: GET [base]/Organization?address=1183 Mountain View C

  *Implementation Notes:*  (how to search by [string])

1. **SHOULD** support searching using the **`telecom`** search parameter:

  `GET [base]/!Patient?telecom=[string]`

  Example: GET [base]/Organization?telecom=(707)555-5555

  *Implementation Notes:*  (how to search by [string])


{% include link-list.md %}