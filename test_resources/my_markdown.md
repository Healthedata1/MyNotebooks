|   No | Data Element                             | CDex #submit-attachment Parameter   | X12n 275   | Comments                                                |
|------|------------------------------------------|-------------------------------------|------------|---------------------------------------------------------|
|    1 | Tracking ID (Provider or Payer Assigned) | TrackingId                          | -          | Tracking ID (Provider or Payer Assigned)                |
|    2 | Use                                      | AttachTo                            | -          | Claim or Prior Authorization.                           |
|    3 | Payer ID                                 | PayerId                             | -          | Payer ID - should be a business ID -requester.reference |
|    4 | Payer URL                                | (operation endpoint)                | -          | Payer URL                                               |
|    5 | Organiztion ID                           | OrganizationId                      | -          | Organization of Provider who submitted Claim/Prior-Auth |
|    6 | Provider ID                              | ProviderId                          | -          | Provider who submitted Claim/Prior-Auth                 |
|    7 | Claim/PreAuth ID                         | -                                   | -          | Claim/Prior-Auth ID (Provider or Payer Assigned)        |
|    8 | line item(s)                             | Attachment.LineItem                 | -          | Claim/Prior-Auth line item # nos                        |
|    9 | LOINC Attachment code                    | Attachment.Code                     | -          | LOINCs                                                  |
|   10 | Due Date                                 | -                                   | -          | When attachments are Due                                |
|   11 | Date of Service                          | ServiceDate                         | -          | Claim/Prior-Auth Date of Service (encounter info)       |
|   12 | Member ID                                | MemberId                            | -          | Member ID (patient info)                                |
|   13 | Patient Name                             | -                                   | -          | Patient Name (patient info)                             |
|   14 | Patient Account No.                      | -                                   | -          | Patient Account No. PreAuth Only (patient info)         |
|   15 | Date of Birth                            | -                                   | -          | Date of Birth (patient info)                            |
{:.grid}