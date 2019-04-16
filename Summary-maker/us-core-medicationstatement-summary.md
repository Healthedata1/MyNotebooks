
### Summary of the Mandatory Requirements



1.  A  code  in `MedicationStatement.status`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [Medication  status  codes](http://hl7.org/fhir/ValueSet/medication-statement-status)

1.  A  CodeableConcept  in `MedicationStatement.medication[x]`
with a [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [Medication Clinical Drug (RxNorm)](http://hl7.org/fhir/us/core/ValueSet/us-core-medication-codes)

1.  A  Reference  in `MedicationStatement.subject`


1.  A  dateTime  in `MedicationStatement.dateAsserted`


### Summary of the Must Support Requirements



1.  A  dateTime  in `MedicationStatement.effective[x]`


1. One or more References  in `MedicationStatement.derivedFrom`
