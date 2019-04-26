
#### Mandatory Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHALL be supported.  the  modifiers, comparators and chained parameters that are listed as optional SHOULD be supported.:


1. **SHALL** support searching for all allergies for a patient using the **`patient`** search parameter:

  `GET [base]/AllergyIntolerance?patient=[reference]`

  Example: GET [base]/AllergyIntolerance?patient=1137192

  *Implementation Notes:* Fetches a bundle of all AllergyIntolerance resources for the specified patient (how to search by [reference])



#### Optional Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHOULD be supported.

1. **SHOULD** support searching using the combination of the **`patient`** and **`clinical-status`** search parameters:

  `GET [base]/AllergyIntolerance?patient=[reference]&clinical-status=[token]`

  Example: GET [base]/AllergyIntolerance?patient=[id]&amp;clinical-status=active

  *Implementation Notes:* Fetches a bundle of all Condition resources for the specified patient and status code.  This will not return any “entered in error” resources because of the conditional presence of the clinicalStatus element. (how to search by [reference] and [token])


{% include link-list.md %}