<!-- PAS_Bundle_to_278.md
*****************************************************************************************************
*                                  WARNING: DO NOT EDIT THIS FILE                                   *
*                                                                                                   *
* This file is generated by csv_to_markdown_tabler.ipynb. Any edits you make to this file will be   *
* overwritten                                                                                       *
* To change the contents of this file, edit input/images/data-element-mapping.csv                     *
*****************************************************************************************************
-->

| Data Element | X12n 278 Response-v5010 | ClaimResponse (from PAS Response Bundle) | PAS Response Bundle |
|---|---------------|------------|------------|
| Tracking ID | Loop: 2000E Segment: TRN02 Notes: TRN01 = "1", patient event tracking number. or Loop: 2000F Segment: TRN02 Notes: TRN01 = "1" or TRN01 = "2", service level tracking number | ClaimResponse.identifier, ClaimResponse.item.commmunicationRequest: CommunicationRequest.identifier | ClaimResponse = Bundle.entry[0].resource, CommunicationRequest = Bundle.entry[n].resource referenced by ClaimResponse.communincationRequest |
| Use | Prior Auth | preauthorization | Fixed to "preauthorization" |
| Payer ID | Loop: 2010A Segment: NM109 Notes: NM108 = "PI" | ClaimResponse.insurer: Organization.identifier | ClaimResponse = Bundle.entry[0].resource, Organization = Bundle.entry[n].resource referenced by ClaimResponse.insurer |
| Payer URL | Loop: 2010A Segment: PER08 Notes: PER07 = "UR" | out of band | out of band |
| Organization ID | Loop: 2010B Segment: NM109 Notes: NM101 = id code qualifier, NM102 = "2" | ClaimResponse.requester: Organization.identifier, ClaimResponse.requester: PractitionerRole.organization: Organziation.identifier | ClaimResponse = Bundle.entry[0].resource, Organization,PractitionerRole = Bundle.entry[n].resource referenced by ClaimResponse.requester |
| Provider ID | Loop: 2010EA Segment: NM109 Notes: NM101 = id code qualifier , NM102 = "1" | ClaimResponse.requester: PractitionerRole.practitioner: Practitioner.identifier | ClaimResponse = Bundle.entry[0].resource, PractitionerRole = Bundle.entry[n].resource referenced by ClaimResponse.requester |
| Line Item(s) | Loop: 2000F Segment: TRN02 Notes: TRN01 = "1" | ClaimResponse.item.extension:itemTraceNumber Note: CommunicationRequest.payload.extension:serviceLineNumber references this item | ClaimResponse = Bundle.entry[0].resource |
| LOINC Attachment Code | Loop: 2000E Segment: HI?? or Loop: 2000F Segment: PWK?? Notes: Clarify! | ClaimResponse.item.commmunicationRequest: CommunicationRequest.payload.extension:contentModifier | ClaimResponse = Bundle.entry[0].resource |
| Date of Service | Loop: 2000E (event level) or 2000F (line level) Segment: DTP03 Notes: DTP01="742" DTP02 = date format code | ClaimResponse.item.extension:requestedServiceDate | ClaimResponse = Bundle.entry[0].resource |
| Member ID | Loop: 2010C Segment: NM109 Notes: NM108 = id code qualifier | ClaimResponse.patient: Patient.identifer | ClaimResponse = Bundle.entry[0].resource, Patient = Bundle.entry[n].resource referenced by ClaimResponse.patient |
{:.grid}

The data element mapping table is available as a [CSV](data-element-mapping.csv) and [Excel](data-element-mapping.xlsx) file.