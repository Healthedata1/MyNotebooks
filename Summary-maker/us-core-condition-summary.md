
### Summary of the Mandatory Requirements



1. One or more CodeableConcepts  in `Condition.category`
with a [preferred](http://hl7.org/fhir/R4/terminologies.html#preferred)
 binding to [US Core Condition Category Codes](http://hl7.org/fhir/us/core/ValueSet/us-core-condition-category)

1.  A  CodeableConcept  in `Condition.code`
with a [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [Problem Value Set](http://hl7.org/fhir/us/core/ValueSet/us-core-problem)

1.  A  Reference  in `Condition.subject`






1.  A  CodeableConcept  in `Condition.clinicalStatus`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [Condition Clinical Status Codes](http://hl7.org/fhir/ValueSet/condition-clinical)

1.  A  CodeableConcept  in `Condition.verificationStatus`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [ConditionVerificationStatus](http://hl7.org/fhir/ValueSet/condition-ver-status)