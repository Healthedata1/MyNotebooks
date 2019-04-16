
### Summary of the Mandatory Requirements



1.  A  Reference  in `PractitionerRole.practitioner`


1.  A  Reference  in `PractitionerRole.organization`


1.  A  CodeableConcept  in `PractitionerRole.code`
with a [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [US Core Provider Role (NUCC)](http://hl7.org/fhir/us/core/ValueSet/us-core-provider-role)

1.  A  CodeableConcept  in `PractitionerRole.specialty`
with a [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [US Core Provider Speciality (NUCC)](http://hl7.org/fhir/us/core/ValueSet/us-core-provider-specialty)

### Summary of the Must Support Requirements



1. One or more References  in `PractitionerRole.location`


1. One or more ContactPoints  in `PractitionerRole.telecom`

   - which must have a  code value  in `PractitionerRole.telecom.system`with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [](http://hl7.org/fhir/ValueSet/contact-point-system|4.0.0)
   - which must have a  string value  in `PractitionerRole.telecom.value`

1. One or more References  in `PractitionerRole.endpoint`
