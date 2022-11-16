| Data Element | CDex Request Attachment Task Profile Element | Submit Attachments Comments |
|-----|-----|-------------------|
| Tracking ID (Provider or Payer Assigned) | Task.identifier | <span class="bg-success" markdown="1">For *unsolicited* attachments, this is the provider-assigned tracking/control number. For *solicited* attachments, this is the payer-assigned tracking/control number.</span><!-- new-content --> |
| Use | Task.reasonCode | Choice of "claim" or "preauthorization" |
| Payer ID | Task.requester.identifier | Payer ID |
| Payer URL | "payer-url" Task.input | Payer endpoint where the attachments are submitted using the $submit-operation |
| Organization ID | Task.owner.identifier | Organization of provider who submitted claim/prior authorization |
| Provider ID | Task.owner.identifier | Provider who submitted claim/prior authorization |
| Claim/PreAuth ID | Task.reasonReference.identifier | <span class="bg-success" markdown="1">Provider-assigned claim/prior authorization ID</span><!-- new-content --> |
| Line Item(s) | “code” Task.input.extension | Claim/prior-authorization line item numbers |
| LOINC Attachment Code | “code” Task.input | LOINC attachment codes |
| Due Date | Task.restriction.period | Deadline for submitting attachments to Payer |
| Date of Service | “service-date” Task.input | Date of service for claim/prior authorization |
| Member ID | Patient.identifier | Payer assigned patient identifier |
| Patient Name | Patient.name | Patient demographic information for patient matching |
| Patient Account No. | Patient.identifier | <span class="bg-success" markdown="1">Patient Account Number is a provider-assigned identifier</span><!-- new-content --> |
| Date of Birth | Patient.birthDate | Patient demographic information for patient matching |
{:.grid}