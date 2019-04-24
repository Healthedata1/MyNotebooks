### Quick Start
Below is an overview of the required set of RESTful FHIR interactions - for
example, search and read operations - for this profile. See the [Conformance requirements]
for a complete list of supported RESTful interactions for this IG.


#### Mandatory Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHALL be supported.  the  modifiers, comparators and chained parameters that are listed as optional SHOULD be supported.:





1. **SHALL** support searching using the **`_id`** search parameter:

`GET [base]/Questionnaire?_id={[system]}|[code]`



  *Implementation Notes:* example for testing. (how to search by [token])
1. **SHALL** support searching using the **`url`** search parameter:

`GET [base]/Questionnaire?url=[uri]`



  *Implementation Notes:* example for testing. (how to search by [uri])
1. **SHALL** support searching using the **`status`** search parameter:

`GET [base]/Questionnaire?status={[system]}|[code]`



  *Implementation Notes:* example for testing. (how to search by [token])
1. **SHALL** support searching using the **`title`** search parameter:
  - including optional support these modifiers: `foo, bar2`
  - including support for these comparators: `contains, foo, bar`
    - and optional support these comparators: `foo, bar2`
  - including support for these chained parameters: `contains, foo, bar`
    - and optional support these chained parameter: `foo, bar2`

`GET [base]/Questionnaire?title{:foo|bar2|foo|bar2}={foo|bar2}[string]`



  *Implementation Notes:* example for testing. (how to search by [string])
1. **SHALL** support searching using the **`publisher`** search parameter:
  - including support for these modifiers: `contains`

`GET [base]/Questionnaire?publisher={contains}[string]`



  *Implementation Notes:* example for testing. (how to search by [string])

1. **SHALL**  using the combination of the  **`publisher and status`** search parameters:

  `GET [base]/Questionnaire?publisher={contains}[string]&status=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [token] and [string])
1. **SHALL**  using the combination of the  **`publisher and status`** search parameters:

  `GET [base]/Questionnaire?publisher={contains}[string]&status=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [token] and [string])


#### Optional Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHOULD be supported.

1. **SHOULD** support searching using the **`version`** search parameter:

  `GET [base]/Questionnaire?version={[system]}|[code]`


  *Implementation Notes:* . (how to search by [S] and [H] and [O] and [U] and [L] and [D])
1. **SHOULD** support searching using the **`context-type-value`** search parameter:

  `GET [base]/Questionnaire?context-type-value=`


  *Implementation Notes:* . (how to search by [S] and [H] and [O] and [U] and [L] and [D])

1. **SHOULD** support searching using the combination of the  **`context-type-value and publisher`** search parameters:

  `GET [base]/Questionnaire?context-type-value=[composite]&publisher={contains}[string]`

  Example: 

  *Implementation Notes:* . (how to search by [composite] and [string])
1. **SHOULD** support searching using the combination of the  **`context-type-value and publisher and status`** search parameters:

  `GET [base]/Questionnaire?context-type-value=[composite]&publisher={contains}[string]&status=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [composite] and [token] and [string])
1. **SHOULD** support searching using the combination of the  **`context-type-value and status`** search parameters:

  `GET [base]/Questionnaire?context-type-value=[composite]&status=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [composite] and [token])
1. **SHOULD** support searching using the combination of the  **`publisher and status and version`** search parameters:

  `GET [base]/Questionnaire?publisher={contains}[string]&status=[token]&version=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [token] and [string])
1. **SHOULD** support searching using the combination of the  **`publisher and version`** search parameters:

  `GET [base]/Questionnaire?publisher={contains}[string]&version=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [token] and [string])
1. **SHOULD** support searching using the combination of the  **`status and title and version`** search parameters:

  `GET [base]/Questionnaire?status=[token]&title{:foo|bar2|foo|bar2}={foo|bar2}[string]&version=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [token] and [string])
1. **SHOULD** support searching using the combination of the  **`status and version`** search parameters:

  `GET [base]/Questionnaire?status=[token]&version=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [token])
1. **SHOULD** support searching using the combination of the  **`title and version`** search parameters:

  `GET [base]/Questionnaire?title{:foo|bar2|foo|bar2}={foo|bar2}[string]&version=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [token] and [string])
1. **SHOULD** support searching using the combination of the  **`context-type-value and publisher`** search parameters:

  `GET [base]/Questionnaire?context-type-value=[composite]&publisher={contains}[string]`

  Example: 

  *Implementation Notes:* . (how to search by [composite] and [string])
1. **SHOULD** support searching using the combination of the  **`context-type-value and publisher and status`** search parameters:

  `GET [base]/Questionnaire?context-type-value=[composite]&publisher={contains}[string]&status=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [composite] and [token] and [string])
1. **SHOULD** support searching using the combination of the  **`context-type-value and status`** search parameters:

  `GET [base]/Questionnaire?context-type-value=[composite]&status=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [composite] and [token])
1. **SHOULD** support searching using the combination of the  **`publisher and status and version`** search parameters:

  `GET [base]/Questionnaire?publisher={contains}[string]&status=[token]&version=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [token] and [string])
1. **SHOULD** support searching using the combination of the  **`publisher and version`** search parameters:

  `GET [base]/Questionnaire?publisher={contains}[string]&version=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [token] and [string])
1. **SHOULD** support searching using the combination of the  **`status and title and version`** search parameters:

  `GET [base]/Questionnaire?status=[token]&title{:foo|bar2|foo|bar2}={foo|bar2}[string]&version=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [token] and [string])
1. **SHOULD** support searching using the combination of the  **`status and version`** search parameters:

  `GET [base]/Questionnaire?status=[token]&version=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [token])
1. **SHOULD** support searching using the combination of the  **`title and version`** search parameters:

  `GET [base]/Questionnaire?title{:foo|bar2|foo|bar2}={foo|bar2}[string]&version=[token]`

  Example: 

  *Implementation Notes:* . (how to search by [token] and [string])

{% include link-list.md %}