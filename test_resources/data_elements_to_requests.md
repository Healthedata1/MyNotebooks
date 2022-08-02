| Data Element | CDex Request Attachment Task Profile Element | Comments |
|-----|-----|-------|
| Tracking ID (Provider or Payer Assigned) | Task.identifier | Provider or Payer assigned tracking control number |
| Use | Task.reasonCode | Choice of "claim" or "preauthorization" |
| Payer ID | Task.reasonReference.identifier | Payer ID |
| Payer URL | "payer-url" Task.input | Payer endpoint where the attachments are submitted using the $submit-operation |
| Organization ID | - | Organization of Provider who submitted claim/prior authorization |
| Provider ID | Task.owner.identifier | Provider who submitted claim/prior authorization |
| Claim/PreAuth ID | Task.reasonReference.identifier | claim/prior authorization ID (Provider or Payer Assigned) |
| Line Item(s) | “code” Task.input.extension | claim/prior authorization line item numbers |
| LOINC Attachment Code | “code” Task.input | LOINC attachment codes |
| Due Date | Task.restriction.period | Deadline form submitting attachments to Payer |
| Date of Service | “service-date” Task.input | Date of Service for claim/prior authorization |
| Member ID | Patient.identifier | Payer assigned patient identifier |
| Patient Name | Patient.name | Patient Demographic information for patient matching |
| Patient Account No. | Patient.identifier | Provider assigned patient identifer only for prior authorizatons |
| Date of Birth | Patient.birthDate | Patient Demographic information for patient matching |
{:.grid}