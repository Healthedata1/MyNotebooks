**MessageHeader**

#### Summary of the Mandatory Requirements
1.  A  Coding  in `MessageHeader.eventCoding`
with an [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [Da Vinci Notification Event ValueSet](ValueSet-notification-event.html)
1. One or more Focus References  in `MessageHeader.focus`
      - which must have a  string value  in `MessageHeader.focus.reference`

#### Summary of the Must Support Requirements
1.  A  Destination  in `MessageHeader.destination`
1.  A Sender Reference  in `MessageHeader.sender`
1.  An Author Reference  in `MessageHeader.author`
1.  A Responsible Reference  in `MessageHeader.responsible`

#### Summary of the Unsupported Elements
1. `MessageHeader.response`