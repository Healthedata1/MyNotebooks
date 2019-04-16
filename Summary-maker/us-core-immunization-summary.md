
### Summary of the Mandatory Requirements



1.  A  code  in `Immunization.status`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [Immunization Status Codes](http://hl7.org/fhir/ValueSet/immunization-status)

1.  A  CodeableConcept  in `Immunization.vaccineCode`
with a [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)\+ [MaxValueSet](general-guidance.html#max-binding)
 binding to [Vaccine Administered Value Set (CVX)](http://hl7.org/fhir/us/core/ValueSet/us-core-cvx)

1.  A  Reference  in `Immunization.patient`


1.  A  dateTime  in `Immunization.occurrence[x]`


1.  A  boolean  in `Immunization.primarySource`






1.  A  CodeableConcept  in `Immunization.statusReason`
with a [example](http://hl7.org/fhir/R4/terminologies.html#example)
 binding to [Immunization Status Reason Codes](http://hl7.org/fhir/ValueSet/immunization-status-reason)