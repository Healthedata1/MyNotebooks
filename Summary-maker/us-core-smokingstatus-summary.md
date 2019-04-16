
### Summary of the Mandatory Requirements



1.  A  code  in `Observation.status`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [ObservationStatus](http://hl7.org/fhir/ValueSet/observation-status)

1.  A  CodeableConcept  in `Observation.code`
with a [example](http://hl7.org/fhir/R4/terminologies.html#example)
 binding to [LOINC Codes](http://hl7.org/fhir/ValueSet/observation-codes)

1.  A  Reference  in `Observation.subject`


1.  An  instant  in `Observation.issued`


1.  A  CodeableConcept  in `Observation.valueCodeableConcept`
with a [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)\+ [MaxValueSet](general-guidance.html#max-binding)
 binding to [Smoking Status](http://hl7.org/fhir/us/core/ValueSet/us-core-observation-ccdasmokingstatus)



