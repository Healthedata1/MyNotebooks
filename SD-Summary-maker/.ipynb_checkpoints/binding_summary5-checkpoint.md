## All Required Bindings for Required Coded Elements:


1. **[CareTeam.status](http://hl7.org/fhir/us/core//StructureDefinition-us-core-careteam.jsonCareTeam.status)**
    - [base](https://build.fhir.org/careteam-definitions.html#CareTeam.status) cardinality= 0..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/care-team-status|4.0.0](http://hl7.org/fhir/ValueSet/care-team-status|4.0.0)
    - base binding strength = required
    - http://hl7.org/fhir/ValueSet/care-team-status
    (
     entered-in-error, 
     inactive, 
     active, 
     suspended, 
     proposed)
1. **[MedicationStatement.status](http://hl7.org/fhir/us/core//StructureDefinition-us-core-medicationstatement.jsonMedicationStatement.status)**
    - [base](https://build.fhir.org/medicationstatement-definitions.html#MedicationStatement.status) cardinality= 1..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/medication-statement-status|4.0.0](http://hl7.org/fhir/ValueSet/medication-statement-status|4.0.0)
    - base binding strength = required
    - http://hl7.org/fhir/ValueSet/medication-statement-status
    (
     completed, 
     active, 
     entered-in-error, 
     on-hold, 
     **unknown**, 
     stopped, 
     intended, 
     not-taken)
1. **[Patient.telecom.system](http://hl7.org/fhir/us/core//StructureDefinition-us-core-patient.jsonPatient.telecom.system)**
    - [base](https://build.fhir.org/medicationstatement-definitions.html#MedicationStatement.status) cardinality= ..
    - http://hl7.org/fhir/ValueSet/contact-point-system
    (
     phone, 
     pager, 
     url, 
     fax, 
     other, 
     sms, 
     email)
1. **[Patient.gender](http://hl7.org/fhir/us/core//StructureDefinition-us-core-patient.jsonPatient.gender)**
    - [base](https://build.fhir.org/patient-definitions.html#Patient.gender) cardinality= 0..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/administrative-gender|4.0.0](http://hl7.org/fhir/ValueSet/administrative-gender|4.0.0)
    - base binding strength = required
    - http://hl7.org/fhir/ValueSet/administrative-gender
    (
     male, 
     female, 
     other, 
     **unknown**)
1. **[Immunization.status](http://hl7.org/fhir/us/core//StructureDefinition-us-core-immunization.jsonImmunization.status)**
    - [base](https://build.fhir.org/immunization-definitions.html#Immunization.status) cardinality= 1..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/immunization-status|4.0.0](http://hl7.org/fhir/ValueSet/immunization-status|4.0.0)
    - base binding strength = required
    - http://hl7.org/fhir/ValueSet/immunization-status
    (
     completed, 
     not-done, 
     entered-in-error)
1. **[Observation.status](http://hl7.org/fhir/us/core//StructureDefinition-us-core-smokingstatus.jsonObservation.status)**
    - [base](https://build.fhir.org/immunization-definitions.html#Immunization.status) cardinality= ..
    - http://hl7.org/fhir/ValueSet/observation-status
    (
     corrected, 
     amended, 
     final, 
     registered, 
     entered-in-error, 
     preliminary, 
     cancelled, 
     **unknown**)
1. **[DocumentReference.status](http://hl7.org/fhir/us/core//StructureDefinition-us-core-documentreference.jsonDocumentReference.status)**
    - [base](https://build.fhir.org/documentreference-definitions.html#DocumentReference.status) cardinality= 1..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/document-reference-status|4.0.0](http://hl7.org/fhir/ValueSet/document-reference-status|4.0.0)
    - base binding strength = required
    - http://hl7.org/fhir/ValueSet/document-reference-status
    (
     entered-in-error, 
     superseded, 
     current)
1. **[DocumentReference.type](http://hl7.org/fhir/us/core//StructureDefinition-us-core-documentreference.jsonDocumentReference.type)**
    - [base](https://build.fhir.org/documentreference-definitions.html#DocumentReference.type) cardinality= 0..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/c80-doc-typecodes](http://hl7.org/fhir/ValueSet/c80-doc-typecodes)
    - base binding strength = preferred
    - http://hl7.org/fhir/ValueSet/c80-doc-typecodes
    (
     36325-9, 
     39337-1, 
     42473-9, 
     47522-8, 
     43458-9, 
     39920-4, 
     34751-8, 
     37393-6, 
     38019-6, 
     46349-7, 
     57177-8, 
     39670-5, 
     30688-6, 
     24659-5, 
     37764-8, 
     58744-4, 
     24909-4, 
     39336-3, 
     43791-3, 
     51392-9)
1. **[DocumentReference.content.attachment.contentType](http://hl7.org/fhir/us/core//StructureDefinition-us-core-documentreference.jsonDocumentReference.content.attachment.contentType)**
    - [base](https://build.fhir.org/documentreference-definitions.html#DocumentReference.type) cardinality= ..
    - http://hl7.org/fhir/ValueSet/mimetypes|4.0.0
1. **[DiagnosticReport.status](http://hl7.org/fhir/us/core//StructureDefinition-new-us-core-diagnosticreport.jsonDiagnosticReport.status)**
    - [base](https://build.fhir.org/documentreference-definitions.html#DocumentReference.type) cardinality= ..
    - http://hl7.org/fhir/ValueSet/diagnostic-report-status
    (
     registered, 
     cancelled, 
     partial, 
     entered-in-error, 
     **unknown**, 
     appended, 
     final, 
     preliminary, 
     corrected, 
     amended)
1. **[Extension.extension.valueCoding](http://hl7.org/fhir/us/core//StructureDefinition-us-core-race.jsonExtension.extension.valueCoding)**
    - [base](https://build.fhir.org/documentreference-definitions.html#DocumentReference.type) cardinality= ..
    - http://hl7.org/fhir/us/core/ValueSet/omb-race-category
1. **[Extension.extension.valueCoding](http://hl7.org/fhir/us/core//StructureDefinition-us-core-race.jsonExtension.extension.valueCoding)**
    - [base](https://build.fhir.org/documentreference-definitions.html#DocumentReference.type) cardinality= ..
    - http://hl7.org/fhir/us/core/ValueSet/detailed-race
1. **[MedicationRequest.status](http://hl7.org/fhir/us/core//StructureDefinition-us-core-medicationrequest.jsonMedicationRequest.status)**
    - [base](https://build.fhir.org/medicationrequest-definitions.html#MedicationRequest.status) cardinality= 1..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/medicationrequest-status|4.0.0](http://hl7.org/fhir/ValueSet/medicationrequest-status|4.0.0)
    - base binding strength = required
    - http://hl7.org/fhir/ValueSet/medicationrequest-status
    (
     stopped, 
     active, 
     entered-in-error, 
     cancelled, 
     completed, 
     draft, 
     **unknown**, 
     on-hold)
1. **[DiagnosticReport.status](http://hl7.org/fhir/us/core//StructureDefinition-us-core-diagnosticreport.jsonDiagnosticReport.status)**
    - [base](https://build.fhir.org/diagnosticreport-definitions.html#DiagnosticReport.status) cardinality= 1..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/diagnostic-report-status|4.0.0](http://hl7.org/fhir/ValueSet/diagnostic-report-status|4.0.0)
    - base binding strength = required
    - http://hl7.org/fhir/ValueSet/diagnostic-report-status
    (
     registered, 
     cancelled, 
     partial, 
     entered-in-error, 
     **unknown**, 
     appended, 
     final, 
     preliminary, 
     corrected, 
     amended)
1. **[Condition.verificationStatus](http://hl7.org/fhir/us/core//StructureDefinition-us-core-condition.jsonCondition.verificationStatus)**
    - [base](https://build.fhir.org/condition-definitions.html#Condition.verificationStatus) cardinality= 0..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/condition-ver-status|4.0.0](http://hl7.org/fhir/ValueSet/condition-ver-status|4.0.0)
    - base binding strength = required
    - http://hl7.org/fhir/ValueSet/condition-ver-status
    (
     differential, 
     entered-in-error, 
     unconfirmed, 
     confirmed, 
     refuted, 
     provisional)
1. **[Encounter.status](http://hl7.org/fhir/us/core//StructureDefinition-us-core-encounter.jsonEncounter.status)**
    - [base](https://build.fhir.org/encounter-definitions.html#Encounter.status) cardinality= 1..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/encounter-status|4.0.0](http://hl7.org/fhir/ValueSet/encounter-status|4.0.0)
    - base binding strength = required
    - http://hl7.org/fhir/ValueSet/encounter-status|4.0.0
    (
     planned, 
     **unknown**, 
     in-progress, 
     finished, 
     cancelled, 
     triaged, 
     arrived, 
     onleave, 
     entered-in-error)
1. **[Procedure.status](http://hl7.org/fhir/us/core//StructureDefinition-us-core-procedure.jsonProcedure.status)**
    - [base](https://build.fhir.org/procedure-definitions.html#Procedure.status) cardinality= 1..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/event-status|4.0.0](http://hl7.org/fhir/ValueSet/event-status|4.0.0)
    - base binding strength = required
    - http://hl7.org/fhir/ValueSet/event-status
    (
     completed, 
     **unknown**, 
     not-done, 
     stopped, 
     entered-in-error, 
     on-hold, 
     preparation, 
     in-progress)
1. **[Observation.status](http://hl7.org/fhir/us/core//StructureDefinition-us-core-observationresults.jsonObservation.status)**
    - [base](https://build.fhir.org/procedure-definitions.html#Procedure.status) cardinality= ..
    - http://hl7.org/fhir/ValueSet/observation-status
    (
     corrected, 
     amended, 
     final, 
     registered, 
     entered-in-error, 
     preliminary, 
     cancelled, 
     **unknown**)
1. **[PractitionerRole.telecom.system](http://hl7.org/fhir/us/core//StructureDefinition-us-core-practitionerrole.jsonPractitionerRole.telecom.system)**
    - [base](https://build.fhir.org/procedure-definitions.html#Procedure.status) cardinality= ..
    - http://hl7.org/fhir/ValueSet/contact-point-system|4.0.0
    (
     phone, 
     pager, 
     url, 
     fax, 
     other, 
     sms, 
     email)
1. **[CarePlan.text.status](http://hl7.org/fhir/us/core//StructureDefinition-us-core-careplan.jsonCarePlan.text.status)**
    - [base](https://build.fhir.org/procedure-definitions.html#Procedure.status) cardinality= ..
    - http://hl7.org/fhir/us/core/ValueSet/us-core-narrative-status
1. **[CarePlan.status](http://hl7.org/fhir/us/core//StructureDefinition-us-core-careplan.jsonCarePlan.status)**
    - [base](https://build.fhir.org/careplan-definitions.html#CarePlan.status) cardinality= 1..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/request-status|4.0.0](http://hl7.org/fhir/ValueSet/request-status|4.0.0)
    - base binding strength = required
    - http://hl7.org/fhir/ValueSet/request-status
    (
     active, 
     draft, 
     completed, 
     entered-in-error, 
     **unknown**, 
     on-hold, 
     revoked)
1. **[CarePlan.intent](http://hl7.org/fhir/us/core//StructureDefinition-us-core-careplan.jsonCarePlan.intent)**
    - [base](https://build.fhir.org/careplan-definitions.html#CarePlan.intent) cardinality= 1..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/care-plan-intent|4.0.0](http://hl7.org/fhir/ValueSet/care-plan-intent|4.0.0)
    - base binding strength = required
    - http://hl7.org/fhir/ValueSet/care-plan-intent
    (
     proposal, 
     option, 
     plan, 
     order)
1. **[Goal.lifecycleStatus](http://hl7.org/fhir/us/core//StructureDefinition-us-core-goal.jsonGoal.lifecycleStatus)**
    - [base](https://build.fhir.org/goal-definitions.html#Goal.lifecycleStatus) cardinality= 1..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/goal-status|4.0.0](http://hl7.org/fhir/ValueSet/goal-status|4.0.0)
    - base binding strength = required
    - http://hl7.org/fhir/ValueSet/goal-status
    (
     active, 
     completed, 
     rejected, 
     cancelled, 
     planned, 
     entered-in-error, 
     accepted, 
     on-hold, 
     proposed)
1. **[Extension.extension.valueCoding](http://hl7.org/fhir/us/core//StructureDefinition-us-core-ethnicity.jsonExtension.extension.valueCoding)**
    - [base](https://build.fhir.org/goal-definitions.html#Goal.lifecycleStatus) cardinality= ..
    - http://hl7.org/fhir/us/core/ValueSet/omb-ethnicity-category
1. **[Extension.extension.valueCoding](http://hl7.org/fhir/us/core//StructureDefinition-us-core-ethnicity.jsonExtension.extension.valueCoding)**
    - [base](https://build.fhir.org/goal-definitions.html#Goal.lifecycleStatus) cardinality= ..
    - http://hl7.org/fhir/us/core/ValueSet/detailed-ethnicity
1. **[AllergyIntolerance.verificationStatus](http://hl7.org/fhir/us/core//StructureDefinition-us-core-allergyintolerance.jsonAllergyIntolerance.verificationStatus)**
    - [base](https://build.fhir.org/allergyintolerance-definitions.html#AllergyIntolerance.verificationStatus) cardinality= 0..1
    - base valueSet = [http://hl7.org/fhir/ValueSet/allergyintolerance-verification|4.0.0](http://hl7.org/fhir/ValueSet/allergyintolerance-verification|4.0.0)
    - base binding strength = required
    - http://hl7.org/fhir/ValueSet/allergyintolerance-verification
    (
     confirmed, 
     refuted, 
     entered-in-error, 
     unconfirmed)