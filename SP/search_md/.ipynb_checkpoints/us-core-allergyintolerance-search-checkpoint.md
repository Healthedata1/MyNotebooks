### Quick Start
Below is an overview of the required set of RESTful FHIR interactions - for
example, search and read operations - for this profile. See the [Conformance requirements]
for a complete list of supported RESTful interactions for this IG.






1. **SHALL** support searching for all allergies for a patient using the **`_id`** search parameter:

  `GET [base]/AllergyIntolerance?_id={[system]}|[code]`

  Example: GET [base]/AllergyIntolerance?patient=1137192

  *Implementation Notes:* Fetches a bundle of all AllergyIntolerance resources for the specified patient. (how to search by [token])






{% include link-list.md %}