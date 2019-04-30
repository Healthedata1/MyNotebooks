


#### Mandatory Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHALL be supported.  the  modifiers, comparators and chained parameters that are listed as optional SHOULD be supported.:


1. **SHALL** support searching for all prescriptions for a patient. The server application represents the medication using either an inline code or a contained or external reference to the Medication resource. using the **[`patient`](SearchParameter-us-core-medicationrequest-patient.html)** search parameter:

  - support the use the `_include` parameter to indicate that these resources be included in the results: `MedicationRequest:medication`
    `GET [base]/MedicationRequest?patient=[reference]`

  Example: GET [base]/MedicationRequest?patient=14676,GET [base]/MedicationRequest?patient=14676&amp;_include=MedicationRequest:medication

  *Implementation Notes:* Fetches a bundle of all MedicationRequest resources for the specified patient. Mandatory for client to support the _include parameter. Optional for server to support the _include parameter. ([how to search by reference])

1. **SHALL** support searching using the combination of the **[`patient`](SearchParameter-us-core-medicationrequest-patient.html)** and **[`status`](SearchParameter-us-core-medicationrequest-status.html)** search parameters:
  - support the use the `_include` parameter to indicate that these resources be included in the results: `MedicationRequest:medication`

  `GET [base]/MedicationRequest?patient=[reference]&status=[token]`

    Example: GET [base]/MedicationRequest?patient=1137192&amp;status=active

  *Implementation Notes:* Fetches a bundle of all MedicationRequest resources for the specified patient and status ([how to search by patient] and [how to search by status])



#### Optional Search Parameters:

The following search parameters, search parameter combinations and search parameter [modifiers], [comparators] and [chained parameters] SHOULD be supported.

1. **SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-medicationrequest-patient.html)** and **[`authoredon`](SearchParameter-us-core-medicationrequest-authoredon.html)** search parameters:
  - support the use the `_include` parameter to indicate that these resources be included in the results: `MedicationRequest:medication`
  - including support for these comparators: `gt, lt, ge, le`

  `GET [base]/MedicationRequest?patient=[reference]&authoredon={gt|lt|ge|le}[date]`

   Example: GET [base]/MedicationStatement?patient=1137192&amp;effective=ge2019

   *Implementation Notes:* Fetches a bundle of all MedicationRequest resources for the specified patient and date ([how to search by reference] and [how to search by date])


{% include link-list.md %}