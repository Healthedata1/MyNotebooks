## Sample Summary Markdown Template...

### All Required Coded Elements:


1. **[CareTeam.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-careteam-definitions.html#CareTeam.status)**
   - **required**
   - http://hl7.org/fhir/ValueSet/care-team-status
     (
     proposed, 
     active, 
     suspended, 
     inactive, 
     entered-in-error)
1. **[CareTeam.participant.role](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-careteam-definitions.html#CareTeam.participant.role)**
   - extensible
   - max binding = true
   - http://hl7.org/fhir/us/core/ValueSet/us-core-careteam-provider-roles
1. **[MedicationStatement.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-medicationstatement-definitions.html#MedicationStatement.status)**
   - **required**
   - http://hl7.org/fhir/ValueSet/medication-statement-status
     (
     active, 
     completed, 
     entered-in-error, 
     intended, 
     stopped, 
     on-hold, 
     **unknown**, 
     not-taken)
1. **[MedicationStatement.medication[x]](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-medicationstatement-definitions.html#MedicationStatement.medication[x])**
   - extensible
   - http://hl7.org/fhir/us/core/ValueSet/us-core-medication-codes
1. **[Device.type](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-device-definitions.html#Device.type)**
   - extensible
   - http://hl7.org/fhir/ValueSet/device-kind
     (
     156009, 
     271003, 
     287000, 
     291005, 
     678001, 
     739006, 
     793009, 
     882002, 
     972002, 
     989005, 
     994005, 
     1211003, 
     1333003, 
     1422002, 
     1579007, 
     1766001, 
     1941006, 
     1962007, 
     2248009, 
     2282003)
1. **[Patient.telecom.system](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-patient-definitions.html#Patient.telecom.system)**
   - **required**
   - http://hl7.org/fhir/ValueSet/contact-point-system
     (
     phone, 
     fax, 
     email, 
     pager, 
     url, 
     sms, 
     other)
1. **[Patient.gender](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-patient-definitions.html#Patient.gender)**
   - **required**
   - http://hl7.org/fhir/ValueSet/administrative-gender
     (
     male, 
     female, 
     other, 
     **unknown**)
1. **[Patient.communication.language](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-patient-definitions.html#Patient.communication.language)**
   - extensible
   - max binding = true
   - http://hl7.org/fhir/us/core/ValueSet/simple-language
1. **[Immunization.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-immunization-definitions.html#Immunization.status)**
   - **required**
   - http://hl7.org/fhir/ValueSet/immunization-status
     (
     completed, 
     entered-in-error, 
     not-done)
1. **[Immunization.vaccineCode](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-immunization-definitions.html#Immunization.vaccineCode)**
   - extensible
   - max binding = true
   - http://hl7.org/fhir/us/core/ValueSet/us-core-cvx
1. **[Observation.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-observation-definitions.html#Observation.status)**
   - **required**
   - http://hl7.org/fhir/ValueSet/observation-status
     (
     registered, 
     preliminary, 
     final, 
     amended, 
     corrected, 
     cancelled, 
     entered-in-error, 
     **unknown**)
1. **[Observation.code](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-observation-definitions.html#Observation.code)**
   - example
   - http://hl7.org/fhir/ValueSet/observation-codes
1. **[Observation.valueCodeableConcept](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-observation-definitions.html#Observation.valueCodeableConcept)**
   - extensible
   - max binding = true
   - http://hl7.org/fhir/us/core/ValueSet/us-core-observation-ccdasmokingstatus
1. **[DocumentReference.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-documentreference-definitions.html#DocumentReference.status)**
   - **required**
   - http://hl7.org/fhir/ValueSet/document-reference-status
     (
     current, 
     superseded, 
     entered-in-error)
1. **[DocumentReference.type](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-documentreference-definitions.html#DocumentReference.type)**
   - **required**
   - http://hl7.org/fhir/ValueSet/c80-doc-typecodes
     (
     55107-7, 
     74155-3, 
     51851-4, 
     67851-6, 
     34744-3, 
     34873-0, 
     68552-9, 
     67852-4, 
     68471-2, 
     68483-7, 
     64058-1, 
     64070-6, 
     64053-2, 
     64054-0, 
     34862-3, 
     64062-3, 
     64078-9, 
     64066-4, 
     64060-7, 
     64074-8)
1. **[DocumentReference.category](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-documentreference-definitions.html#DocumentReference.category)**
   - extensible
   - http://hl7.org/fhir/us/core/ValueSet/us-core-documentreference-category
1. **[DocumentReference.content.attachment.contentType](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-documentreference-definitions.html#DocumentReference.content.attachment.contentType)**
   - **required**
   - http://hl7.org/fhir/ValueSet/mimetypes|4.0.0
1. **[DiagnosticReport.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-diagnosticreport-definitions.html#DiagnosticReport.status)**
   - **required**
   - http://hl7.org/fhir/ValueSet/diagnostic-report-status
     (
     registered, 
     partial, 
     preliminary, 
     final, 
     amended, 
     corrected, 
     appended, 
     cancelled, 
     entered-in-error, 
     **unknown**)
1. **[DiagnosticReport.category](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-diagnosticreport-definitions.html#DiagnosticReport.category)**
   - extensible
   - http://hl7.org/fhir/us/core/ValueSet/us-core-diagnosticreport-category
1. **[DiagnosticReport.code](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-diagnosticreport-definitions.html#DiagnosticReport.code)**
   - extensible
   - http://hl7.org/fhir/ValueSet/report-codes
1. **[Extension.extension.valueCoding](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-extension-definitions.html#Extension.extension.valueCoding)**
   - **required**
   - http://hl7.org/fhir/us/core/ValueSet/omb-race-category
1. **[Extension.extension.valueCoding](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-extension-definitions.html#Extension.extension.valueCoding)**
   - **required**
   - http://hl7.org/fhir/us/core/ValueSet/detailed-race
1. **[MedicationRequest.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-medicationrequest-definitions.html#MedicationRequest.status)**
   - **required**
   - http://hl7.org/fhir/ValueSet/medicationrequest-status
     (
     active, 
     on-hold, 
     cancelled, 
     completed, 
     entered-in-error, 
     stopped, 
     draft, 
     **unknown**)
1. **[MedicationRequest.medication[x]](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-medicationrequest-definitions.html#MedicationRequest.medication[x])**
   - extensible
   - http://hl7.org/fhir/us/core/ValueSet/us-core-medication-codes
1. **[DiagnosticReport.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-diagnosticreport-definitions.html#DiagnosticReport.status)**
   - **required**
   - http://hl7.org/fhir/ValueSet/diagnostic-report-status
     (
     registered, 
     partial, 
     preliminary, 
     final, 
     amended, 
     corrected, 
     appended, 
     cancelled, 
     entered-in-error, 
     **unknown**)
1. **[DiagnosticReport.category](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-diagnosticreport-definitions.html#DiagnosticReport.category)**
   - example
   - http://hl7.org/fhir/ValueSet/diagnostic-service-sections
     (
     AU, 
     BG, 
     BLB, 
     CG, 
     CH, 
     CP, 
     CT, 
     CTH, 
     CUS, 
     EC, 
     EN, 
     GE, 
     HM, 
     ICU, 
     IMG, 
     IMM, 
     LAB, 
     MB, 
     MCB, 
     MYC)
1. **[DiagnosticReport.code](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-diagnosticreport-definitions.html#DiagnosticReport.code)**
   - extensible
   - http://hl7.org/fhir/ValueSet/report-codes
1. **[Condition.verificationStatus](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-condition-definitions.html#Condition.verificationStatus)**
   - **required**
   - http://hl7.org/fhir/ValueSet/condition-ver-status
     (
     unconfirmed, 
     provisional, 
     differential, 
     confirmed, 
     refuted, 
     entered-in-error)
1. **[Condition.category](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-condition-definitions.html#Condition.category)**
   - preferred
   - http://hl7.org/fhir/us/core/ValueSet/us-core-condition-category
1. **[Condition.code](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-condition-definitions.html#Condition.code)**
   - extensible
   - http://hl7.org/fhir/us/core/ValueSet/us-core-problem
1. **[Encounter.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-encounter-definitions.html#Encounter.status)**
   - **required**
   - http://hl7.org/fhir/ValueSet/encounter-status|4.0.0
     (
     planned, 
     arrived, 
     triaged, 
     in-progress, 
     onleave, 
     finished, 
     cancelled, 
     entered-in-error, 
     **unknown**)
1. **[Encounter.class](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-encounter-definitions.html#Encounter.class)**
   - extensible
   - http://terminology.hl7.org/ValueSet/v3-ActEncounterCode
     (
     AMB, 
     EMER, 
     FLD, 
     HH, 
     IMP, 
     ACUTE, 
     NONAC, 
     OBSENC, 
     PRENC, 
     SS, 
     VR)
1. **[Encounter.type](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-encounter-definitions.html#Encounter.type)**
   - extensible
   - http://hl7.org/fhir/us/core/ValueSet/us-core-encounter-type
1. **[Observation.code](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-observation-definitions.html#Observation.code)**
   - extensible
   - http://hl7.org/fhir/ValueSet/observation-vitalsignresult
     (
     85353-1, 
     9279-1, 
     8867-4, 
     2708-6, 
     8310-5, 
     8302-2, 
     9843-4, 
     29463-7, 
     39156-5, 
     85354-9, 
     8480-6, 
     8462-4, 
     8478-0)
1. **[Procedure.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-procedure-definitions.html#Procedure.status)**
   - **required**
   - http://hl7.org/fhir/ValueSet/event-status
     (
     preparation, 
     in-progress, 
     not-done, 
     on-hold, 
     stopped, 
     completed, 
     entered-in-error, 
     **unknown**)
1. **[Procedure.code](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-procedure-definitions.html#Procedure.code)**
   - extensible
   - max binding = true
   - http://hl7.org/fhir/us/core/ValueSet/us-core-procedure-code
1. **[Medication.code](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-medication-definitions.html#Medication.code)**
   - extensible
   - http://hl7.org/fhir/us/core/ValueSet/us-core-medication-codes
1. **[Observation.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-observation-definitions.html#Observation.status)**
   - **required**
   - http://hl7.org/fhir/ValueSet/observation-status
     (
     registered, 
     preliminary, 
     final, 
     amended, 
     corrected, 
     cancelled, 
     entered-in-error, 
     **unknown**)
1. **[Observation.category](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-observation-definitions.html#Observation.category)**
   - preferred
   - http://hl7.org/fhir/ValueSet/observation-category
     (
     social-history, 
     vital-signs, 
     imaging, 
     laboratory, 
     procedure, 
     survey, 
     exam, 
     therapy, 
     activity)
1. **[Observation.code](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-observation-definitions.html#Observation.code)**
   - extensible
   - http://hl7.org/fhir/ValueSet/observation-codes
1. **[PractitionerRole.code](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-practitionerrole-definitions.html#PractitionerRole.code)**
   - extensible
   - http://hl7.org/fhir/us/core/ValueSet/us-core-provider-role
1. **[PractitionerRole.specialty](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-practitionerrole-definitions.html#PractitionerRole.specialty)**
   - extensible
   - http://hl7.org/fhir/us/core/ValueSet/us-core-provider-specialty
1. **[PractitionerRole.telecom.system](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-practitionerrole-definitions.html#PractitionerRole.telecom.system)**
   - **required**
   - http://hl7.org/fhir/ValueSet/contact-point-system|4.0.0
     (
     phone, 
     fax, 
     email, 
     pager, 
     url, 
     sms, 
     other)
1. **[DocumentReference.category](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-documentreference-definitions.html#DocumentReference.category)**
   - extensible
   - http://hl7.org/fhir/us/core/ValueSet/us-core-documentreference-category
1. **[CarePlan.text.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-careplan-definitions.html#CarePlan.text.status)**
   - **required**
   - http://hl7.org/fhir/us/core/ValueSet/us-core-narrative-status
1. **[CarePlan.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-careplan-definitions.html#CarePlan.status)**
   - **required**
   - http://hl7.org/fhir/ValueSet/request-status
     (
     draft, 
     active, 
     on-hold, 
     revoked, 
     completed, 
     entered-in-error, 
     **unknown**)
1. **[CarePlan.intent](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-careplan-definitions.html#CarePlan.intent)**
   - **required**
   - http://hl7.org/fhir/ValueSet/care-plan-intent
     (
     proposal, 
     plan, 
     order, 
     option)
1. **[CarePlan.category](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-careplan-definitions.html#CarePlan.category)**
   - example
   - http://hl7.org/fhir/ValueSet/care-plan-category
1. **[Goal.lifecycleStatus](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-goal-definitions.html#Goal.lifecycleStatus)**
   - **required**
   - http://hl7.org/fhir/ValueSet/goal-status
     (
     proposed, 
     planned, 
     accepted, 
     active, 
     on-hold, 
     completed, 
     cancelled, 
     entered-in-error, 
     rejected)
1. **[Goal.description](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-goal-definitions.html#Goal.description)**
   - example
   - http://hl7.org/fhir/ValueSet/clinical-findings
     (
     109006, 
     122003, 
     127009, 
     129007, 
     134006, 
     140004, 
     144008, 
     147001, 
     150003, 
     151004, 
     162004, 
     165002, 
     168000, 
     171008, 
     172001, 
     175004, 
     177007, 
     179005, 
     181007, 
     183005)
1. **[Extension.extension.valueCoding](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-extension-definitions.html#Extension.extension.valueCoding)**
   - **required**
   - http://hl7.org/fhir/us/core/ValueSet/omb-ethnicity-category
1. **[Extension.extension.valueCoding](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-extension-definitions.html#Extension.extension.valueCoding)**
   - **required**
   - http://hl7.org/fhir/us/core/ValueSet/detailed-ethnicity
1. **[Observation.code](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-observation-definitions.html#Observation.code)**
   - extensible
   - http://hl7.org/fhir/ValueSet/observation-vitalsignresult
     (
     85353-1, 
     9279-1, 
     8867-4, 
     2708-6, 
     8310-5, 
     8302-2, 
     9843-4, 
     29463-7, 
     39156-5, 
     85354-9, 
     8480-6, 
     8462-4, 
     8478-0)
1. **[Observation.code](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-observation-definitions.html#Observation.code)**
   - extensible
   - http://hl7.org/fhir/ValueSet/observation-vitalsignresult
     (
     85353-1, 
     9279-1, 
     8867-4, 
     2708-6, 
     8310-5, 
     8302-2, 
     9843-4, 
     29463-7, 
     39156-5, 
     85354-9, 
     8480-6, 
     8462-4, 
     8478-0)
1. **[AllergyIntolerance.verificationStatus](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-allergyintolerance-definitions.html#AllergyIntolerance.verificationStatus)**
   - **required**
   - http://hl7.org/fhir/ValueSet/allergyintolerance-verification
     (
     unconfirmed, 
     confirmed, 
     refuted, 
     entered-in-error)
1. **[AllergyIntolerance.code](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-allergyintolerance-definitions.html#AllergyIntolerance.code)**
   - extensible
   - https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1186.8/expansion

### All Max Bindings for Required Coded Elements:


1. **[CareTeam.participant.role](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-careteam-definitions.html#CareTeam.participant.role)**  
    - http://hl7.org/fhir/us/core/ValueSet/us-core-careteam-provider-roles
1. **[Patient.communication.language](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-patient-definitions.html#Patient.communication.language)**  
    - http://hl7.org/fhir/us/core/ValueSet/simple-language
1. **[Immunization.vaccineCode](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-immunization-definitions.html#Immunization.vaccineCode)**  
    - http://hl7.org/fhir/us/core/ValueSet/us-core-cvx
1. **[Observation.valueCodeableConcept](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-observation-definitions.html#Observation.valueCodeableConcept)**  
    - http://hl7.org/fhir/us/core/ValueSet/us-core-observation-ccdasmokingstatus
1. **[Procedure.code](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-procedure-definitions.html#Procedure.code)**  
    - http://hl7.org/fhir/us/core/ValueSet/us-core-procedure-code


### All Required Bindings for Required Coded Elements:


1. **[CareTeam.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-careteam-definitions.html#CareTeam.status)**  
    - http://hl7.org/fhir/ValueSet/care-team-status
    (
     proposed, 
     active, 
     suspended, 
     inactive, 
     entered-in-error)
1. **[MedicationStatement.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-medicationstatement-definitions.html#MedicationStatement.status)**  
    - http://hl7.org/fhir/ValueSet/medication-statement-status
    (
     active, 
     completed, 
     entered-in-error, 
     intended, 
     stopped, 
     on-hold, 
     **unknown**, 
     not-taken)
1. **[Patient.telecom.system](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-patient-definitions.html#Patient.telecom.system)**  
    - http://hl7.org/fhir/ValueSet/contact-point-system
    (
     phone, 
     fax, 
     email, 
     pager, 
     url, 
     sms, 
     other)
1. **[Patient.gender](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-patient-definitions.html#Patient.gender)**  
    - http://hl7.org/fhir/ValueSet/administrative-gender
    (
     male, 
     female, 
     other, 
     **unknown**)
1. **[Immunization.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-immunization-definitions.html#Immunization.status)**  
    - http://hl7.org/fhir/ValueSet/immunization-status
    (
     completed, 
     entered-in-error, 
     not-done)
1. **[Observation.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-observation-definitions.html#Observation.status)**  
    - http://hl7.org/fhir/ValueSet/observation-status
    (
     registered, 
     preliminary, 
     final, 
     amended, 
     corrected, 
     cancelled, 
     entered-in-error, 
     **unknown**)
1. **[DocumentReference.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-documentreference-definitions.html#DocumentReference.status)**  
    - http://hl7.org/fhir/ValueSet/document-reference-status
    (
     current, 
     superseded, 
     entered-in-error)
1. **[DocumentReference.type](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-documentreference-definitions.html#DocumentReference.type)**  
    - http://hl7.org/fhir/ValueSet/c80-doc-typecodes
    (
     55107-7, 
     74155-3, 
     51851-4, 
     67851-6, 
     34744-3, 
     34873-0, 
     68552-9, 
     67852-4, 
     68471-2, 
     68483-7, 
     64058-1, 
     64070-6, 
     64053-2, 
     64054-0, 
     34862-3, 
     64062-3, 
     64078-9, 
     64066-4, 
     64060-7, 
     64074-8)
1. **[DocumentReference.content.attachment.contentType](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-documentreference-definitions.html#DocumentReference.content.attachment.contentType)**  
    - http://hl7.org/fhir/ValueSet/mimetypes|4.0.0
1. **[DiagnosticReport.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-diagnosticreport-definitions.html#DiagnosticReport.status)**  
    - http://hl7.org/fhir/ValueSet/diagnostic-report-status
    (
     registered, 
     partial, 
     preliminary, 
     final, 
     amended, 
     corrected, 
     appended, 
     cancelled, 
     entered-in-error, 
     **unknown**)
1. **[Extension.extension.valueCoding](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-extension-definitions.html#Extension.extension.valueCoding)**  
    - http://hl7.org/fhir/us/core/ValueSet/omb-race-category
1. **[Extension.extension.valueCoding](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-extension-definitions.html#Extension.extension.valueCoding)**  
    - http://hl7.org/fhir/us/core/ValueSet/detailed-race
1. **[MedicationRequest.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-medicationrequest-definitions.html#MedicationRequest.status)**  
    - http://hl7.org/fhir/ValueSet/medicationrequest-status
    (
     active, 
     on-hold, 
     cancelled, 
     completed, 
     entered-in-error, 
     stopped, 
     draft, 
     **unknown**)
1. **[DiagnosticReport.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-diagnosticreport-definitions.html#DiagnosticReport.status)**  
    - http://hl7.org/fhir/ValueSet/diagnostic-report-status
    (
     registered, 
     partial, 
     preliminary, 
     final, 
     amended, 
     corrected, 
     appended, 
     cancelled, 
     entered-in-error, 
     **unknown**)
1. **[Condition.verificationStatus](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-condition-definitions.html#Condition.verificationStatus)**  
    - http://hl7.org/fhir/ValueSet/condition-ver-status
    (
     unconfirmed, 
     provisional, 
     differential, 
     confirmed, 
     refuted, 
     entered-in-error)
1. **[Encounter.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-encounter-definitions.html#Encounter.status)**  
    - http://hl7.org/fhir/ValueSet/encounter-status|4.0.0
    (
     planned, 
     arrived, 
     triaged, 
     in-progress, 
     onleave, 
     finished, 
     cancelled, 
     entered-in-error, 
     **unknown**)
1. **[Procedure.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-procedure-definitions.html#Procedure.status)**  
    - http://hl7.org/fhir/ValueSet/event-status
    (
     preparation, 
     in-progress, 
     not-done, 
     on-hold, 
     stopped, 
     completed, 
     entered-in-error, 
     **unknown**)
1. **[Observation.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-observation-definitions.html#Observation.status)**  
    - http://hl7.org/fhir/ValueSet/observation-status
    (
     registered, 
     preliminary, 
     final, 
     amended, 
     corrected, 
     cancelled, 
     entered-in-error, 
     **unknown**)
1. **[PractitionerRole.telecom.system](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-practitionerrole-definitions.html#PractitionerRole.telecom.system)**  
    - http://hl7.org/fhir/ValueSet/contact-point-system|4.0.0
    (
     phone, 
     fax, 
     email, 
     pager, 
     url, 
     sms, 
     other)
1. **[CarePlan.text.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-careplan-definitions.html#CarePlan.text.status)**  
    - http://hl7.org/fhir/us/core/ValueSet/us-core-narrative-status
1. **[CarePlan.status](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-careplan-definitions.html#CarePlan.status)**  
    - http://hl7.org/fhir/ValueSet/request-status
    (
     draft, 
     active, 
     on-hold, 
     revoked, 
     completed, 
     entered-in-error, 
     **unknown**)
1. **[CarePlan.intent](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-careplan-definitions.html#CarePlan.intent)**  
    - http://hl7.org/fhir/ValueSet/care-plan-intent
    (
     proposal, 
     plan, 
     order, 
     option)
1. **[Goal.lifecycleStatus](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-goal-definitions.html#Goal.lifecycleStatus)**  
    - http://hl7.org/fhir/ValueSet/goal-status
    (
     proposed, 
     planned, 
     accepted, 
     active, 
     on-hold, 
     completed, 
     cancelled, 
     entered-in-error, 
     rejected)
1. **[Extension.extension.valueCoding](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-extension-definitions.html#Extension.extension.valueCoding)**  
    - http://hl7.org/fhir/us/core/ValueSet/omb-ethnicity-category
1. **[Extension.extension.valueCoding](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-extension-definitions.html#Extension.extension.valueCoding)**  
    - http://hl7.org/fhir/us/core/ValueSet/detailed-ethnicity
1. **[AllergyIntolerance.verificationStatus](https://build.fhir.org/ig/HL7/US-Core-R4/StructureDefinition-us-core-allergyintolerance-definitions.html#AllergyIntolerance.verificationStatus)**  
    - http://hl7.org/fhir/ValueSet/allergyintolerance-verification
    (
     unconfirmed, 
     confirmed, 
     refuted, 
     entered-in-error)