



## Sample Summary Markdown Template...

### Summary of the Mandatory Requirements



1. 
One or more   Identifiers
 in `Patient.identifier`

    - 
which must  have
an   uri value in `Patient.identifier.system`

    - 
which must  have
a   string value in `Patient.identifier.value`


1. 
One or more   HumanNames
 in `Patient.name`

    - 
which must  have
a   string value in `Patient.name.family`

    - 
which must  have one or more  string values in `Patient.name.given`


1. 

A  code 
 in `Patient.gender`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
binding to [AdministrativeGender](http://hl7.org/fhir/ValueSet/administrative-gender)


### Summary of the Must Support Requirements



1. 

A 
[Race]([&#39;http://hl7.org/fhir/us/core/StructureDefinition/us-core-race&#39;]) Extension 
 in `Patient.extension`


1. 

An 
[Ethnicity]([&#39;http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity&#39;]) Extension 
 in `Patient.extension`


1. 

A 
[Birthsex]([&#39;http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex&#39;]) Extension 
 in `Patient.extension`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
binding to [Birth Sex](http://hl7.org/fhir/us/core/ValueSet/birthsex)


1. 
One or more   ContactPoints
 in `Patient.telecom`

   - 
which must  have
a   code value in `Patient.telecom.system`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
binding to [ContactPointSystem](http://hl7.org/fhir/ValueSet/contact-point-system)

   - 
which must  have
a   string value in `Patient.telecom.value`


1. 

A  date 
 in `Patient.birthDate`


1. 
One or more   Addresses
 in `Patient.address`

   - 
which should  have one or more  string values in `Patient.address.line`

   - 
which should  have
a   string value in `Patient.address.city`

   - 
which should  have
a   string value in `Patient.address.state`
with a [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
binding to [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/ValueSet/us-core-usps-state)

   - 
which should  have
a   string value in `Patient.address.postalCode`


1. 
One or more   BackboneElements
 in `Patient.communication`

   - 
which must  have
a   CodeableConcept value in `Patient.communication.language`
with a [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 \+ [MaxValueSet](general-guidance.html#max-binding)
binding to [Language codes with language and optionally a region modifier](http://hl7.org/fhir/us/core/ValueSet/simple-language)
