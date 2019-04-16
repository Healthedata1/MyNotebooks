
### Summary of the Mandatory Requirements



1.  A  code  in `Observation.status`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [ObservationStatus](http://hl7.org/fhir/ValueSet/observation-status)

1. One or more CodeableConcepts  in `Observation.category`
with a [preferred](http://hl7.org/fhir/R4/terminologies.html#preferred)
 binding to [Observation Category Codes](http://hl7.org/fhir/ValueSet/observation-category)

1.  A  CodeableConcept  in `Observation.code`
with a [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [LOINC Codes](http://hl7.org/fhir/ValueSet/observation-codes)

1.  A  Reference  in `Observation.subject`


### Summary of the Must Support Requirements



1.  A  dateTime  in `Observation.effective[x]`


1.  A  Quantity  in `Observation.value[x]`


1.  A  CodeableConcept  in `Observation.dataAbsentReason`
with a [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [DataAbsentReason](http://hl7.org/fhir/ValueSet/data-absent-reason)