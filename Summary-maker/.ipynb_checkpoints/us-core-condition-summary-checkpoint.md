
### Summary of the Mandatory Requirements
1. One or more CodeableConcepts  in `Condition.category`
with a [preferred](http://hl7.org/fhir/R4/terminologies.html#preferred)
 binding to [US Core Condition Category Codes](http://hl7.org/fhir/us/core/ValueSet/us-core-condition-category) with the following constraints: **Condition.clinicalStatus SHALL NOT be present if verification Status is entered-in-error, If condition is abated, then clinicalStatus must be either inactive, resolved, or remission, Condition.clinicalStatus SHALL be present if verificationStatus is not entered-in-error and category is problem-list-item, A code in Condition.category SHOULD be from US Core Condition Category Codes value set.**
1.  A  CodeableConcept  in `Condition.code`
with an [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [Problem Value Set](http://hl7.org/fhir/us/core/ValueSet/us-core-problem) with the following constraints: **Condition.clinicalStatus SHALL NOT be present if verification Status is entered-in-error, If condition is abated, then clinicalStatus must be either inactive, resolved, or remission, Condition.clinicalStatus SHALL be present if verificationStatus is not entered-in-error and category is problem-list-item, A code in Condition.category SHOULD be from US Core Condition Category Codes value set.**
1.  A Patient Reference  in `Condition.subject`
 with the following constraints: **Condition.clinicalStatus SHALL NOT be present if verification Status is entered-in-error, If condition is abated, then clinicalStatus must be either inactive, resolved, or remission, Condition.clinicalStatus SHALL be present if verificationStatus is not entered-in-error and category is problem-list-item, A code in Condition.category SHOULD be from US Core Condition Category Codes value set.**

### Summary of the Must Support Requirements
1.  A  CodeableConcept  in `Condition.clinicalStatus`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [Condition Clinical Status Codes](http://hl7.org/fhir/ValueSet/condition-clinical) with the following constraints: **Condition.clinicalStatus SHALL NOT be present if verification Status is entered-in-error, If condition is abated, then clinicalStatus must be either inactive, resolved, or remission, Condition.clinicalStatus SHALL be present if verificationStatus is not entered-in-error and category is problem-list-item, A code in Condition.category SHOULD be from US Core Condition Category Codes value set.**
1.  A  CodeableConcept  in `Condition.verificationStatus`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [ConditionVerificationStatus](http://hl7.org/fhir/ValueSet/condition-ver-status) with the following constraints: **Condition.clinicalStatus SHALL NOT be present if verification Status is entered-in-error, If condition is abated, then clinicalStatus must be either inactive, resolved, or remission, Condition.clinicalStatus SHALL be present if verificationStatus is not entered-in-error and category is problem-list-item, A code in Condition.category SHOULD be from US Core Condition Category Codes value set.**