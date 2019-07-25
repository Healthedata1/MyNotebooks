**Endpoint**

#### Summary of the Mandatory Requirements
1.  A  code  in `Endpoint.status`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [EndpointStatus](http://hl7.org/fhir/ValueSet/endpoint-status|4.0.0)
1.  A  Coding  in `Endpoint.connectionType`
with an [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [Endpoint Connection Type](http://hl7.org/fhir/ValueSet/endpoint-connection-type)
      - which must have a fixed `Endpoint.connectionType.system` = `http://terminology.hl7.org/CodeSystem/endpoint-connection-type`
      - which must have a fixed `Endpoint.connectionType.code` = `hl7-fhir-rest`
1.  A  CodeableConcept  in `Endpoint.payloadType`
with an [example](http://hl7.org/fhir/R4/terminologies.html#example)
 binding to [Endpoint Payload Type](http://hl7.org/fhir/ValueSet/endpoint-payload-type)
      - which should have one or more  Coding values  in `Endpoint.payloadType.coding`
      - which must have a  string value  in `Endpoint.payloadType.text`
1.  An  url  in `Endpoint.address`

#### Summary of the Must Support Requirements
1. One or more  strings  in `Endpoint.header`