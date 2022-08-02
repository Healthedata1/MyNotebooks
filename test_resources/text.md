| Data Element                             | CDex Request Attachment Task Profile Element   | CDex #submit-attachment Parameter   |
|------------------------------------------|------------------------------------------------|-------------------------------------|
| Tracking ID (Provider or Payer Assigned) | Task.identifier                                | TrackingId                          |
| Use                                      | Task.reasonCode                                | AttachTo                            |
| Payer URL                                | "payer-url" Task.input                         | (operation endpoint)                |
| Organiztion ID                           | -                                              | OrganizationId                      |
| Provider ID                              | Task.owner.identifier                          | ProviderId                          |
| line item(s)                             | “code” Task.input.extension                    | Attachment.LineItem                 |
| LOINC Attachment code                    | “code” Task.input                              | Attachment.Code                     |
| Date of Service                          | “service-date” Task.input                      | ServiceDate                         |
| Member ID                                | Patient.identifier                             | MemberId                            |
{:.grid}