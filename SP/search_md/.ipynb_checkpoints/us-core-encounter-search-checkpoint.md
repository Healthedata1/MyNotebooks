
#### Mandatory Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHALL be supported.  the  modifiers, comparators and chained parameters that are listed as optional SHOULD be supported.:


1. **SHALL** support fetching an Encounter using the **`_id`** search parameter:

  `GET [base]/Encounter[id]`

  Example: GET [base]/Encounter/12354

  *Implementation Notes:*  (how to search by the [logical id] of the resource)

1. **SHALL** support searching for all encounters for a patient using the **`patient`** search parameter:

  `GET [base]/Encounter?patient=[url]`

  Example: GET [base]/Encounter?patient=1137192

  *Implementation Notes:* Fetches a bundle of all Encounter resources for the specified patient (how to search by [reference])

1. **SHALL** support searching for all encounters by date using the **`period`** search parameter:
  - including support for these comparators: `ge, le, gt, lt`

  `GET [base]/Encounter?period=[date]`

  Example: See combination searches below

  *Implementation Notes:* Search based on date and patient parameter (how to search by [date])

1. **SHALL**  using the combination of the  **`patient and period`** search parameters:

  `GET [base]/Encounter?patient=[reference]&period=[date]`

  Example: 

  *Implementation Notes:*  (how to search by [date] and [reference])





{% include link-list.md %}