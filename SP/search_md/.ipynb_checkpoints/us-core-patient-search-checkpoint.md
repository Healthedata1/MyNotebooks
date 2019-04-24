
#### Mandatory Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHALL be supported.  the  modifiers, comparators and chained parameters that are listed as optional SHOULD be supported.:


1. **SHALL** support searching using the **`_id`** search parameter:

  `GET [base]/Patient?_id={[system]}|[code]`

  *Implementation Notes:* example for testing. (how to search by [token])

1. **SHALL** support searching using the **`identifier`** search parameter:

  `GET [base]/Patient?identifier={[system]}|[code]`

  *Implementation Notes:* example for testing. (how to search by [token])

1. **SHALL** support searching using the **`name`** search parameter:

  `GET [base]/Patient?name=[string]`

  *Implementation Notes:* example for testing. (how to search by [string])

1. **SHALL** support searching using the **`birthdate`** search parameter:

  `GET [base]/Patient?birthdate=[date]`

  *Implementation Notes:* example for testing. (how to search by [date])

1. **SHALL** support searching using the **`gender`** search parameter:

  `GET [base]/Patient?gender={[system]}|[code]`

  *Implementation Notes:* example for testing. (how to search by [token])

1. **SHALL**  using the combination of the  **`birthdate and name`** search parameters:

  `GET [base]/Patient?birthdate=[date]&name=[string]`

  Example: 

  *Implementation Notes:* . (how to search by [string] and [date])

1. **SHALL**  using the combination of the  **`gender and name`** search parameters:

  `GET [base]/Patient?gender=[token]&name=[string]`

  Example: 

  *Implementation Notes:* . (how to search by [string] and [token])

1. **SHALL**  using the combination of the  **`birthdate and name`** search parameters:

  `GET [base]/Patient?birthdate=[date]&name=[string]`

  Example: 

  *Implementation Notes:* . (how to search by [string] and [date])

1. **SHALL**  using the combination of the  **`gender and name`** search parameters:

  `GET [base]/Patient?gender=[token]&name=[string]`

  Example: 

  *Implementation Notes:* . (how to search by [string] and [token])



#### Optional Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHOULD be supported.

1. **SHOULD** support searching using the **`family`** search parameter:
  `GET [base]/Patient?family=[string]`

  *Implementation Notes:* . (how to search by [string])

1. **SHOULD** support searching using the **`given`** search parameter:
  `GET [base]/Patient?given=[string]`

  *Implementation Notes:* . (how to search by [string])


1. **SHOULD** support searching using the combination of the  **`family and gender`** search parameters:

  `GET [base]/Patient?family=[string]&gender=[token]`

  Example: 
  *Implementation Notes:* . (how to search by [string] and [token])
1. **SHOULD** support searching using the combination of the  **`gender and given`** search parameters:

  `GET [base]/Patient?gender=[token]&given=[string]`

  Example: 
  *Implementation Notes:* . (how to search by [string] and [token])
1. **SHOULD** support searching using the combination of the  **`family and gender`** search parameters:

  `GET [base]/Patient?family=[string]&gender=[token]`

  Example: 
  *Implementation Notes:* . (how to search by [string] and [token])
1. **SHOULD** support searching using the combination of the  **`gender and given`** search parameters:

  `GET [base]/Patient?gender=[token]&given=[string]`

  Example: 
  *Implementation Notes:* . (how to search by [string] and [token])

{% include link-list.md %}