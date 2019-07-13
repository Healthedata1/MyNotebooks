**Communication**

#### Summary of the Mandatory Requirements
1.  A  code  in `Communication.status`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [EventStatus](http://hl7.org/fhir/ValueSet/event-status|4.0.0)
1. One or more  CodeableConcepts  in `Communication.category`
with an [example](http://hl7.org/fhir/R4/terminologies.html#example)
 binding to [CommunicationCategory](http://hl7.org/fhir/ValueSet/communication-category)
   - which must have at least  a  CodeableConcept value  in `Communication.category`
with an [example](http://hl7.org/fhir/R4/terminologies.html#example)
 binding to [CommunicationCategory](http://hl7.org/fhir/ValueSet/communication-category)
      - which must have a  Coding value  in `Communication.category.coding`
         - which must have a fixed `Communication.category.coding.system` = `http://terminology.hl7.org/CodeSystem/communication-category`
         - which must have a fixed `Communication.category.coding.code` = `alert`
1.  A Patient Reference  in `Communication.subject`
1.  A  CodeableConcept  in `Communication.topic`
with an [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [Da Vinci Communication Topic ValueSet](ValueSet-communication-topic.html)
1.  A Encounter Reference  in `Communication.encounter`
1.  A Sender Reference  in `Communication.sender`

#### Summary of the Must Support Requirements
1. One or more  Identifiers  in `Communication.identifier`
1.  A  code  in `Communication.priority`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [Request priority](http://hl7.org/fhir/ValueSet/request-priority|4.0.0)
1. One or more About References  in `Communication.about`
1.  A About Reference  in `Communication.about`
1.  A  dateTime  in `Communication.sent`
1. One or more Recipient References  in `Communication.recipient`
1. One or more  Payloads  in `Communication.payload`
   - which must have a  string value  in `Communication.payload.content[x]`