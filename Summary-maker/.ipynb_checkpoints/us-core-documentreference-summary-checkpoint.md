
### Summary of the Mandatory Requirements



1.  A  code  in `DocumentReference.status`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [DocumentReferenceStatus](http://hl7.org/fhir/ValueSet/document-reference-status)

1.  A  CodeableConcept  in `DocumentReference.type`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [US Core DocumentReference Type Value Set](http://hl7.org/fhir/us/core/ValueSet/us-core-documentreference-type)

1. One or more CodeableConcepts  in `DocumentReference.category`
with a [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [US Core DocumentReference Category Value Set](http://hl7.org/fhir/us/core/ValueSet/us-core-documentreference-category)

1.  A  Reference  in `DocumentReference.subject`


1.  A  BackboneElement  in `DocumentReference.content`

    - which must have an  Attachment value  in `DocumentReference.content.attachment`

    - which must have a  code value  in `DocumentReference.content.attachment.contentType`with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [](http://hl7.org/fhir/ValueSet/mimetypes|4.0.0)

    - which should have a  base64Binary value  in `DocumentReference.content.attachment.data`

    - which should have an  url value  in `DocumentReference.content.attachment.url`

    - which should have a  Coding value  in `DocumentReference.content.format`with a [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [DocumentReference Format Code Set](http://hl7.org/fhir/ValueSet/formatcodes)


### Summary of the Must Support Requirements



1.  An  Identifier  in `DocumentReference.identifier`


1.  An  instant  in `DocumentReference.date`


1. One or more References  in `DocumentReference.author`


1.  A  Reference  in `DocumentReference.custodian`


1.  A  BackboneElement  in `DocumentReference.context`

   - which should have a  Reference value  in `DocumentReference.context.encounter`
