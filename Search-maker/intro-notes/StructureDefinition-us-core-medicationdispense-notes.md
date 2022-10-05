{% include quickstart-intro.md %}



1. {:.new-content}**SHALL** support searching using the **[`patient`](SearchParameter-us-core-medicationdispense-patient.html)** search parameter:

    `GET [base]/MedicationDispense?patient=FOO`

    *Implementation Notes:*  ([how to search by reference])


#### Optional Search Parameters:

The following search parameter combinations SHOULD be supported:

1. {:.new-content}**SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-medicationdispense-patient.html)** and **[`status`](SearchParameter-us-core-medicationdispense-status.html)** search parameters:
    - including support for *OR* search on `status` (e.g.`status={system|}[code],{system|}[code],...`)

    `GET [base]/MedicationDispense?patient={Type/}[id]&status={system|}[code]{,{system|}[code],...}`

    Example:
    
      1. foo

    *Implementation Notes:* Fetches a bundle of all MedicationDispense resources for the specified patient that have a given dispense status (e.g., dispensed, not dispensed)). ([how to search by reference] and [how to search by token])

1. {:.new-content}**SHOULD** support searching using the combination of the **[`patient`](SearchParameter-us-core-medicationdispense-patient.html)** and **[`status`](SearchParameter-us-core-medicationdispense-status.html)** and **[`type`](SearchParameter-us-core-medicationdispense-type.html)** search parameters:
    - including support for *OR* search on `status` (e.g.`status={system|}[code],{system|}[code],...`)
    - including support for *OR* search on `type` (e.g.`type={system|}[code],{system|}[code],...`)

    `GET [base]/MedicationDispense?patient={Type/}[id]&status={system|}[code]{,{system|}[code],...}&type={system|}[code]{,{system|}[code],...}`

    Example:
    
      1. foo

    *Implementation Notes:* Fetches a bundle of all MedicationDispense resources for the specified patient that have a given dispense status (e.g., dispensed, not dispensed) and type of dispense (e.g., partially dispensed). ([how to search by reference] and [how to search by token])



{% include link-list.md %}