Logical: CathPCI_Submission_Map_detailed
Id: ACCNCDRCathPCIDetailed
Title: "Cath-PCI Submission Map"
Description: """This is an example of the data that would be used for a Cath-PCI Submission.
The full map is a logical model as that allows conformance to the FHIR Standard the way a custom Resource would not.
Each element has the short name of the data, a full description and the paths to fetch and place the information, by data standard type, for each.
A section (such as Demographics) is a BackboneElement (holds no values).  All subordinate elements are CREDSElementDefinitions.
Each mapping includes the following:
* identity = standard used for the mapping (e.g., FHIR)
* language = mime type that matches identity
* map = FHIRPath expression of the path to the data
* comment = *Output mapping only* Profile for inclusion in the Submission Bundle if not the Core resource

Environment Variables used:
%patient (Patient resource for the subject of the procedure)
%period (Encounter period i.e. Encounter.period)
%procedure (Cath PCI Procedure resource)
%procedure.period (CathPCI Procedure period i.e., Procedure.performedPeriod)

"""
* ^baseDefinition = "http://hl7.org/fhir/us/fhir-registry-protocols-ig/StructureDefinition/CREDSStructureDefinition"
* ^version = "5.0"
* ^identifier.use = #official
* ^date = "2021-11-01"
* ^publisher = "American College of Cardiology"
* ^contact.name = "Jane Smith"
* ^contact.telecom.system = #email
* ^contact.telecom.value = "mailto:noreply@acc.org"
* ^kind = #logical
//Mappings so that things show up in the mappings page on the IG
* ^mapping[+].identity = "FHIR"
* ^mapping[=].uri = "http://fhir.hl7.org"
* ^mapping[=].name = "Fast Health Interoperability Resources"
* ^mapping[=].comment = "Path to where in a FHIR Resource the data element is found"
* ^mapping[+].identity = "CDA"
* ^mapping[=].uri = "http://build.fhir.org/ig/HL7/cda-core-2.0/"
* ^mapping[=].name = "Clinical Document Architecture"
* ^mapping[=].comment = "Path to where in a CDA 2.0/CCDA 2.1 Document the data element is found"
* ^mapping[+].identity = "HL7V2"
* ^mapping[=].uri = "http://www.hl7.eu/refactored/index.html"
* ^mapping[=].name = "HL7 V2 Messages"
* ^mapping[=].comment = "Path to where in a HL7 V2 Message the data element is found"
* ^mapping[+].identity = "Output"
* ^mapping[=].uri = "http://hl7.org/fhir/us/core"
* ^mapping[=].name = "Submission Data Output location"
* ^mapping[=].comment = "Location within the requirements profile to place the data for submission in US Core or FHIR Core Resources"

* administration 1..1 BackboneElement "Adminstrative Data"

* administration.event 1..1 CREDSElementDefinition "EventCode" "Code used for reason of submission"
* administration.event ^fixedCode = $message-events#CathPCI-Discharge
* administration.event ^mapping[+].identity = "Output"
* administration.event ^mapping[=].language = #application/fhir
* administration.event ^mapping[=].map = "MessageHeader.eventCoding"

* administration.participantId 1..1 CREDSElementDefinition "Facility ID" "ACC Assigned Facilty ID"
* administration.participantId ^mapping[+].identity = "Output"
* administration.participantId ^mapping[=].language = #application/fhir
* administration.participantId ^mapping[=].map = "MessageHeader.source.name"

* administration.vendorIdentifier 1..1 CREDSElementDefinition "Vendor Identifier" "Software Vendor ID"
* administration.vendorIdentifier ^mapping[+].identity = "Output"
* administration.vendorIdentifier ^mapping[=].language = #application/fhir
* administration.vendorIdentifier ^mapping[=].map = "MessageHeader.source.software"

* administration.vendorSoftwareVersion 1..1 CREDSElementDefinition "Software Version" "Vendor Software Version"
* administration.vendorSoftwareVersion ^mapping[+].identity = "Output"
* administration.vendorSoftwareVersion ^mapping[=].language = #application/fhir
* administration.vendorSoftwareVersion ^mapping[=].map = "MessageHeader.source.version"

* administration.status  1..1 CREDSElementDefinition "Submission Status" "Status of the Submission, always final"
* administration.status ^fixedCode = $loinc#11516-2 "Physician Episode of care medical records"
* administration.status ^mapping[+].identity = "Output"
* administration.status ^mapping[=].language = #application/fhir
* administration.status ^mapping[=].map = "Composition.type"
 
* administration.type  1..1 CREDSElementDefinition "Submission Status" "Status of the Submission, always final"
* administration.type ^fixedCode = #final
* administration.type ^mapping[+].identity = "Output"
* administration.type ^mapping[=].language = #application/fhir
* administration.type ^mapping[=].map = "Composition.status"

* administration.timeFrameOfDataSubmission 1..1 CREDSElementDefinition "Submission Period" "Time Frame of Data Submission quarter start (e.g., Q2 start date Apr 1)"
* administration.timeFrameOfDataSubmission ^mapping[+].identity = "Output"
* administration.timeFrameOfDataSubmission ^mapping[=].language = #application/fhir
* administration.timeFrameOfDataSubmission ^mapping[=].map = "Composition.event.period.start"

* administration.registryIdentifier 1..1 CREDSElementDefinition "Registry Identifier"
* administration.registryIdentifier ^fixedString = "ACC-NCDR-CathPCI-5.0"
* administration.registryIdentifier ^mapping[+].identity = "Output"
* administration.registryIdentifier ^mapping[=].language = #application/fhir
* administration.registryIdentifier ^mapping[=].map = "Composition.title"

* administration.submissionType  1..1 CREDSElementDefinition "Submission Type"
* administration.submissionType ^mapping[+].identity = "Output"
* administration.submissionType ^mapping[=].language = #application/fhir
* administration.submissionType ^mapping[=].map = "MessageHeader.reason.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/SubmissionType)"

* administration.date 1..1 CREDSElementDefinition "Submission DateTime " "Date and Time of the Submission"
* administration.date ^mapping[+].identity = "FHIR"
* administration.date ^mapping[=].language = #application/fhir
* administration.date ^mapping[=].map = "now()"
* administration.date ^mapping[+].identity = "Output"
* administration.date ^mapping[=].language = #application/fhir
* administration.date ^mapping[=].map = "Composition.date"

* administration.author 1..1 CREDSElementDefinition "Submission Organization " "Organization Submitting the Record"
* administration.author ^mapping[+].identity = "FHIR"
* administration.author ^mapping[=].language = #application/fhir
* administration.author ^mapping[=].map = "Organization"
* administration.author ^mapping[+].identity = "Output"
* administration.author ^mapping[=].language = #application/fhir
* administration.author ^mapping[=].map = "Composition.author"

* demographics 1..1 CREDSElementDefinition "The Patient who is the subject of this record"
* demographics ^mapping[+].identity = "FHIR"
* demographics ^mapping[=].language = #application/fhir 
* demographics ^mapping[=].map = "Patient"
* demographics ^mapping[+].identity = "Output"
* demographics ^mapping[=].language = #application/fhir 
* demographics ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient and %patient" 

* episodeInformation 1..1 BackboneElement "Episode information"

* episodeInformation.episodeUniqueKey 1..1 CREDSElementDefinition "Episode Unique Key" "Indicate the unique key associated with each patient episode record as assigned by the EMR/EHR or your software application."
* episodeInformation.episodeUniqueKey ^type.code = Identifier 
* episodeInformation.episodeUniqueKey ^patternIdentifier.system  = "http://cathpci.acc.org/episodeUniqueKey"
* episodeInformation.episodeUniqueKey ^mapping[+].identity = "FHIR"
* episodeInformation.episodeUniqueKey ^mapping[=].language = #application/fhir
* episodeInformation.episodeUniqueKey ^mapping[=].map = "Encounter.where(reason.resolve().is(FHIR.Procedure) and reason.resolve().code.codable.code=415070008 )"
* episodeInformation.episodeUniqueKey ^mapping[+].identity = "Output"
* episodeInformation.episodeUniqueKey ^mapping[=].language = #application/fhir
* episodeInformation.episodeUniqueKey ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter and %encounter"

* episodeInformation.healthInsurancePaymentSource  1..* CREDSElementDefinition "Health Insurers"
* episodeInformation.healthInsurancePaymentSource ^mapping[+].identity = "FHIR"
* episodeInformation.healthInsurancePaymentSource ^mapping[=].language = #application/fhir
* episodeInformation.healthInsurancePaymentSource ^mapping[=].map = "Coverage"
* episodeInformation.healthInsurancePaymentSource ^mapping[+].identity = "Output"
* episodeInformation.healthInsurancePaymentSource ^mapping[=].language = #application/fhir
* episodeInformation.healthInsurancePaymentSource ^mapping[=].map = "Coverage"

* episodeInformation.healthInsuranceClaimNumber 1..* CREDSElementDefinition "Health Insurance Claim Number" "Medicare Claim Number"
* episodeInformation.healthInsuranceClaimNumber ^mapping[+].identity = "FHIR"
* episodeInformation.healthInsuranceClaimNumber ^mapping[=].language = #application/fhir
* episodeInformation.healthInsuranceClaimNumber ^mapping[=].map = "ClaimResponse.where(type = medi).identifier.value"
* episodeInformation.healthInsuranceClaimNumber ^mapping[+].identity = "Output"
* episodeInformation.healthInsuranceClaimNumber ^mapping[=].language = #application/fhir
* episodeInformation.healthInsuranceClaimNumber ^mapping[=].map = "ClaimResponse"

* episodeInformation.patientRestriction 0..1 CREDSElementDefinition "Patient Restriction" "patient requested for their information not to be used for any research or studies for the associated episode of care."
* episodeInformation.patientRestriction ^mapping[+].identity = "FHIR"
* episodeInformation.patientRestriction ^mapping[=].language = #application/fhir
* episodeInformation.patientRestriction ^mapping[=].map = "Consent.where(scope = research)"
* episodeInformation.patientRestriction ^mapping[+].identity = "Output"
* episodeInformation.patientRestriction ^mapping[=].language = #application/fhir
* episodeInformation.patientRestriction ^mapping[=].map = "Consent"

* episodeInformation.admittingProvider 1..1 CREDSElementDefinition "Admitting Provider"
* episodeInformation.admittingProvider ^mapping[+].identity = "FHIR"
* episodeInformation.admittingProvider ^mapping[=].language = #application/fhir
* episodeInformation.admittingProvider ^mapping[=].map = "Encounter.participant.where( type.coding.code = 'ADM' ).individual.resolve()"
* episodeInformation.admittingProvider ^mapping[+].identity = "Output"
* episodeInformation.admittingProvider ^mapping[=].language = #application/fhir
* episodeInformation.admittingProvider ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner"

* episodeInformation.attendingProvider 1..1 CREDSElementDefinition "Attending Provider"
* episodeInformation.attendingProvider ^mapping[+].identity = "FHIR"
* episodeInformation.attendingProvider ^mapping[=].language = #application/fhir
* episodeInformation.attendingProvider ^mapping[=].map = "Encounter.participant.where( type.coding.code = 'ATND' ).individual.resolve()"
* episodeInformation.attendingProvider ^mapping[+].identity = "Output"
* episodeInformation.attendingProvider ^mapping[=].language = #application/fhir
* episodeInformation.attendingProvider ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner"

* researchStudy 0..* CREDSElementDefinition "ACC Research Study" "ACC study the patient is currently enrolled"
* researchStudy ^mapping[+].identity = "Output"
* researchStudy ^mapping[=].language = #application/fhir
* researchStudy ^mapping[=].map = "ResearchStudy"

* historyAndRiskFactors 1..1 BackboneElement "History and Risk Factors"

* historyAndRiskFactors.familyHistoryOfPrematureCoronaryArteryDisease 0..1 CREDSElementDefinition "Family History of Premature Coronary Artery Disease"
* historyAndRiskFactors.familyHistoryOfPrematureCoronaryArteryDisease ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.familyHistoryOfPrematureCoronaryArteryDisease ^mapping[=].language = #application/fhir
* historyAndRiskFactors.familyHistoryOfPrematureCoronaryArteryDisease ^mapping[=].map = "Observation.where(code.coding.code = '80985-5')"
* historyAndRiskFactors.familyHistoryOfPrematureCoronaryArteryDisease ^mapping[+].identity = "Output"
* historyAndRiskFactors.familyHistoryOfPrematureCoronaryArteryDisease ^mapping[=].language = #application/fhir
* historyAndRiskFactors.familyHistoryOfPrematureCoronaryArteryDisease ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation"

* historyAndRiskFactors.priorMyocardialInfarction  0..1 CREDSElementDefinition "Prior MI Incidence"
* historyAndRiskFactors.priorMyocardialInfarction ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.priorMyocardialInfarction ^mapping[=].language = #application/fhir
* historyAndRiskFactors.priorMyocardialInfarction ^mapping[=].map = "Condition.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PriorMyocardialInfarction) and %encounter.actualPeriod.start > (occurrenceDateTime - 1 day))"
* historyAndRiskFactors.priorMyocardialInfarction ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.priorMyocardialInfarction ^mapping[=].language = #application/fhir
* historyAndRiskFactors.priorMyocardialInfarction ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PriorMyocardialInfarction) and %encounter.actualPeriod.start > (effectiveDateTime - 1 day))"
* historyAndRiskFactors.priorMyocardialInfarction ^mapping[+].identity = "Output"
* historyAndRiskFactors.priorMyocardialInfarction ^mapping[=].language = #application/fhir
* historyAndRiskFactors.priorMyocardialInfarction ^mapping[=].map = "http://hl7.org/fhir/us/core//StructureDefinition/us-core-condition-problems-health-concerns.where(category = 'problem-list-item')"

* historyAndRiskFactors.priorPercutaneousCoronaryIntervention  0..1 CREDSElementDefinition "Prior PCI Incidence"
* historyAndRiskFactors.priorPercutaneousCoronaryIntervention ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.priorPercutaneousCoronaryIntervention ^mapping[=].language = #application/fhir
* historyAndRiskFactors.priorPercutaneousCoronaryIntervention ^mapping[=].map = "Procedure.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/priorPercutaneousCoronaryIntervention) and %encounter.actualPeriod.start > (occurrenceDateTime - 1 day))"
* historyAndRiskFactors.priorPercutaneousCoronaryIntervention ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.priorPercutaneousCoronaryIntervention ^mapping[=].language = #application/fhir
* historyAndRiskFactors.priorPercutaneousCoronaryIntervention ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/priorPercutaneousCoronaryIntervention) and %encounter.actualPeriod.start > (effectiveDateTime - 1 day))"
* historyAndRiskFactors.priorPercutaneousCoronaryIntervention ^mapping[+].identity = "Output"
* historyAndRiskFactors.priorPercutaneousCoronaryIntervention ^mapping[=].language = #application/fhir
* historyAndRiskFactors.priorPercutaneousCoronaryIntervention ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation"

* historyAndRiskFactors.priorCoronaryArteryBypassGraft  0..1 CREDSElementDefinition "Prior CABG Incidence"
* historyAndRiskFactors.priorCoronaryArteryBypassGraft ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.priorCoronaryArteryBypassGraft ^mapping[=].language = #application/fhir
* historyAndRiskFactors.priorCoronaryArteryBypassGraft ^mapping[=].map = "Procedure.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PriorCABG) and %encounter.actualPeriod.start > (occurrenceDateTime - 1 day))"
* historyAndRiskFactors.priorCoronaryArteryBypassGraft ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.priorCoronaryArteryBypassGraft ^mapping[=].language = #application/fhir
* historyAndRiskFactors.priorCoronaryArteryBypassGraft ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PriorCABG) and %encounter.actualPeriod.start > (effectiveDateTime - 1 day))"
* historyAndRiskFactors.priorCoronaryArteryBypassGraft ^mapping[+].identity = "Output"
* historyAndRiskFactors.priorCoronaryArteryBypassGraft ^mapping[=].language = #application/fhir
* historyAndRiskFactors.priorCoronaryArteryBypassGraft ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation"

* historyAndRiskFactors.cerebrovascularDisease 0..1 CREDSElementDefinition "Current Cerebrovascual Disease"
* historyAndRiskFactors.cerebrovascularDisease ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.cerebrovascularDisease ^mapping[=].language = #application/fhir
* historyAndRiskFactors.cerebrovascularDisease ^mapping[=].map = "Condition.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PriorCerebrovascularDisease) and %encounter.actualPeriod.start > (effectiveDateTime - 1 day))"
* historyAndRiskFactors.cerebrovascularDisease ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.cerebrovascularDisease ^mapping[=].language = #application/fhir
* historyAndRiskFactors.cerebrovascularDisease ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PriorCerebrovascularDisease) and %encounter.actualPeriod.start > (effectiveDateTime - 1 day))"
* historyAndRiskFactors.cerebrovascularDisease ^mapping[+].identity = "Output"
* historyAndRiskFactors.cerebrovascularDisease ^mapping[=].language = #application/fhir
* historyAndRiskFactors.cerebrovascularDisease ^mapping[=].map = "http://hl7.org/fhir/us/core//StructureDefinition/us-core-condition-problems-health-concerns.where(category = 'problem-list-item')"

* historyAndRiskFactors.diabetesMellitus 0..1 CREDSElementDefinition "Current Diabetes Mellitus"
* historyAndRiskFactors.diabetesMellitus ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.diabetesMellitus ^mapping[=].language = #application/fhir
* historyAndRiskFactors.diabetesMellitus ^mapping[=].map = "Condition.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PriorOrCurrentDiabetesMellitus) and %encounter.actualPeriod.start > (effectiveDateTime - 1 day))"
* historyAndRiskFactors.diabetesMellitus ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.diabetesMellitus ^mapping[=].language = #application/fhir
* historyAndRiskFactors.diabetesMellitus ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PriorOrCurrentDiabetesMellitus) and %encounter.actualPeriod.start > (effectiveDateTime - 1 day))"
* historyAndRiskFactors.diabetesMellitus ^mapping[+].identity = "Output"
* historyAndRiskFactors.diabetesMellitus ^mapping[=].language = #application/fhir
* historyAndRiskFactors.diabetesMellitus ^mapping[=].map = "http://hl7.org/fhir/us/core//StructureDefinition/us-core-condition-problems-health-concerns.where(category = 'problem-list-item')"

* historyAndRiskFactors.currentlyOnDialysis 0..1 CREDSElementDefinition "Patient on Dialysis"
* historyAndRiskFactors.currentlyOnDialysis ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.currentlyOnDialysis ^mapping[=].language = #application/fhir
* historyAndRiskFactors.currentlyOnDialysis ^mapping[=].map = "Condition.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/HemodialysisOrPeritonealDialysis) and %encounter.actualPeriod.start > (effectiveDateTime - 1 day))"
* historyAndRiskFactors.currentlyOnDialysis ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.currentlyOnDialysis ^mapping[=].language = #application/fhir
* historyAndRiskFactors.currentlyOnDialysis ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/HemodialysisOrPeritonealDialysis) and %encounter.actualPeriod.start > (effectiveDateTime - 1 day))"
* historyAndRiskFactors.currentlyOnDialysis ^mapping[+].identity = "Output"
* historyAndRiskFactors.currentlyOnDialysis ^mapping[=].language = #application/fhir
* historyAndRiskFactors.currentlyOnDialysis ^mapping[=].map = "http://hl7.org/fhir/us/core//StructureDefinition/us-core-condition-problems-health-concerns.where(category = 'problem-list-item')"

* historyAndRiskFactors.canadianStudyOfHealthAndAgingClinicalFrailtyScale 0..1 CREDSElementDefinition "Frailty Scale"
* historyAndRiskFactors.canadianStudyOfHealthAndAgingClinicalFrailtyScale ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.canadianStudyOfHealthAndAgingClinicalFrailtyScale ^mapping[=].language = #application/fhir
* historyAndRiskFactors.canadianStudyOfHealthAndAgingClinicalFrailtyScale ^mapping[=].map = "Observation.where(code.coding.code = '763264000' ) and %encounter.actualPeriod.start > (effectiveDateTime - 1 day))"
* historyAndRiskFactors.canadianStudyOfHealthAndAgingClinicalFrailtyScale ^mapping[+].identity = "Output"
* historyAndRiskFactors.canadianStudyOfHealthAndAgingClinicalFrailtyScale ^mapping[=].language = #application/fhir
* historyAndRiskFactors.canadianStudyOfHealthAndAgingClinicalFrailtyScale ^mapping[=].map = "http://hl7.org/fhir/us/core//StructureDefinition/us-core-observation"

* historyAndRiskFactors.chronicLungDisease  0..1 CREDSElementDefinition "Current Chronic Lung Disease"
* historyAndRiskFactors.chronicLungDisease ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.chronicLungDisease ^mapping[=].language = #application/fhir
* historyAndRiskFactors.chronicLungDisease ^mapping[=].map = "Condition.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/ChronicLungDisease) and %encounter.actualPeriod.start > (effectiveDateTime - 1 day))"
* historyAndRiskFactors.chronicLungDisease ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.chronicLungDisease ^mapping[=].language = #application/fhir
* historyAndRiskFactors.chronicLungDisease ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/ChronicLungDisease) and %encounter.actualPeriod.start > (effectiveDateTime - 1 day))"
* historyAndRiskFactors.chronicLungDisease ^mapping[+].identity = "Output"
* historyAndRiskFactors.chronicLungDisease ^mapping[=].language = #application/fhir
* historyAndRiskFactors.chronicLungDisease ^mapping[=].map = "http://hl7.org/fhir/us/core//StructureDefinition/us-core-condition-problems-health-concerns.where(category = 'problem-list-item')"

* historyAndRiskFactors.peripheralArterialDisease  0..1 CREDSElementDefinition "Peripheral Arterial Disease Instance"
* historyAndRiskFactors.peripheralArterialDisease ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.peripheralArterialDisease ^mapping[=].language = #application/fhir
* historyAndRiskFactors.peripheralArterialDisease ^mapping[=].map = "Condition.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PeripheralArterialOcclusiveDisease) and %encounter.actualPeriod.start > (effectiveDateTime - 1 day))"
* historyAndRiskFactors.peripheralArterialDisease ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.peripheralArterialDisease ^mapping[=].language = #application/fhir
* historyAndRiskFactors.peripheralArterialDisease ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PeripheralArterialOcclusiveDisease) and %encounter.actualPeriod.start > (effectiveDateTime - 1 day))"
* historyAndRiskFactors.peripheralArterialDisease ^mapping[+].identity = "Output"
* historyAndRiskFactors.peripheralArterialDisease ^mapping[=].language = #application/fhir
* historyAndRiskFactors.peripheralArterialDisease ^mapping[=].map = "http://hl7.org/fhir/us/core//StructureDefinition/us-core-condition-problems-health-concerns.where(category = 'problem-list-item')"

* historyAndRiskFactors.hypertension 0..1 CREDSElementDefinition "Hypertension Instance"
* historyAndRiskFactors.hypertension ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.hypertension ^mapping[=].language = #application/fhir
* historyAndRiskFactors.hypertension ^mapping[=].map = "Condition.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/Hypertension))"
* historyAndRiskFactors.hypertension ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.hypertension ^mapping[=].language = #application/fhir
* historyAndRiskFactors.hypertension ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/Hypertension))"
* historyAndRiskFactors.hypertension ^mapping[+].identity = "Output"
* historyAndRiskFactors.hypertension ^mapping[=].language = #application/fhir
* historyAndRiskFactors.hypertension ^mapping[=].map = "http://hl7.org/fhir/us/core//StructureDefinition/us-core-condition-problems-health-concerns.where(category = 'problem-list-item')"

* historyAndRiskFactors.dyslipidemia 0..1 CREDSElementDefinition "Dyslipidemia Instance"
* historyAndRiskFactors.dyslipidemia ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.dyslipidemia ^mapping[=].language = #application/fhir
* historyAndRiskFactors.dyslipidemia ^mapping[=].map = "Condition.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/Dyslipidemia))"
* historyAndRiskFactors.dyslipidemia ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.dyslipidemia ^mapping[=].language = #application/fhir
* historyAndRiskFactors.dyslipidemia ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/Dyslipidemia))"
* historyAndRiskFactors.dyslipidemia ^mapping[+].identity = "Output"
* historyAndRiskFactors.dyslipidemia ^mapping[=].language = #application/fhir
* historyAndRiskFactors.dyslipidemia ^mapping[=].map = "http://hl7.org/fhir/us/core//StructureDefinition/us-core-condition-problems-health-concerns.where(category = 'problem-list-item')"

* historyAndRiskFactors.tobaccoUse 1..1 CREDSElementDefinition "Smoking status and usage"  "This is for encoding all smoking status, including quantity"
* historyAndRiskFactors.tobaccoUse ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.tobaccoUse ^mapping[=].language = #application/fhir
* historyAndRiskFactors.tobaccoUse ^mapping[=].map = "Condition.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/Dyslipidemia))"
* historyAndRiskFactors.tobaccoUse ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.tobaccoUse ^mapping[=].language = #application/fhir
* historyAndRiskFactors.tobaccoUse ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/Dyslipidemia))"
* historyAndRiskFactors.tobaccoUse ^mapping[+].identity = "Output"
* historyAndRiskFactors.tobaccoUse ^mapping[=].language = #application/fhir
* historyAndRiskFactors.tobaccoUse ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-smokingstatus"

* historyAndRiskFactors.height  1..1 CREDSElementDefinition "Patient Height"
* historyAndRiskFactors.height ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.height ^mapping[=].language = #application/fhir
* historyAndRiskFactors.height ^mapping[=].map = "Observation.where(code.coding.code = '8302-2')"
* historyAndRiskFactors.height ^mapping[+].identity = "Output"
* historyAndRiskFactors.height ^mapping[=].language = #application/fhir
* historyAndRiskFactors.height ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-height"

* historyAndRiskFactors.weight 1..1 CREDSElementDefinition "Patient Weight"
* historyAndRiskFactors.weight ^mapping[+].identity = "FHIR"
* historyAndRiskFactors.weight ^mapping[=].language = #application/fhir
* historyAndRiskFactors.weight ^mapping[=].map = "Observation.where(code.coding.code = '3141-9')"
* historyAndRiskFactors.weight ^mapping[+].identity = "Output"
* historyAndRiskFactors.weight ^mapping[=].language = #application/fhir
* historyAndRiskFactors.weight ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight"

* cardiacStatus 1..1 BackboneElement "Cardiac Status"
* cardiacStatus.cardiacArrestOutofHealthcareFacility 0..1 CREDSElementDefinition "Cardiac Arrest Out of Healthcare Facility" "Indicate if a cardiac arrest event occurred outside of any healthcare facility."
* cardiacStatus.cardiacArrestOutofHealthcareFacility ^mapping[+].identity = "Output"
* cardiacStatus.cardiacArrestOutofHealthcareFacility ^mapping[=].language = #application/fhir
* cardiacStatus.cardiacArrestOutofHealthcareFacility ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=10001424808 andvalueBoolean.exists())"

* cardiacStatus.cardiacArrestWitnessed 0..1 CREDSElementDefinition "Cardiac Arrest Witnessed" "Indicate if the out-of-hospital cardiac arrest was witnessed by another person."
* cardiacStatus.cardiacArrestWitnessed ^mapping[+].identity = "Output"
* cardiacStatus.cardiacArrestWitnessed ^mapping[=].language = #application/fhir
* cardiacStatus.cardiacArrestWitnessed ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/Observation.where(code.coding.system = 'http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014082 and valueBoolean.exists())"

* cardiacStatus.cardiacArrestAfterArrivalofEMS 0..1 CREDSElementDefinition "Cardiac Arrest After Arrival of Emergency Medical Services" "Indicate if the out-of-hospital cardiac arrest occurred after arrival of Emergency Medical Services (EMS)."
* cardiacStatus.cardiacArrestAfterArrivalofEMS ^mapping[+].identity = "Output"
* cardiacStatus.cardiacArrestAfterArrivalofEMS ^mapping[=].language = #application/fhir
* cardiacStatus.cardiacArrestAfterArrivalofEMS ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014081 and valueBoolean.exists())"

* cardiacStatus.firstCardiacArrestRhythm 0..1 CREDSElementDefinition "First Cardiac Arrest Rhythm" "Indicate if the out-of-hospital cardiac arrest occurred after arrival of Emergency Medical Services (EMS)."
* cardiacStatus.firstCardiacArrestRhythm ^mapping[+].identity = "Output"
* cardiacStatus.firstCardiacArrestRhythm ^mapping[=].language = #application/fhir
* cardiacStatus.firstCardiacArrestRhythm ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014081 and valueCode.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/FirstCardiacArrestRhythm))"

* cardiacStatus.cardiacArrestatTransferringHealthcareFacility 0..1 CREDSElementDefinition "Cardiac Arrest at Transferring Healthcare Facility" "Indicate if the patient had cardiac arrest at the transferring healthcare facility prior to arrival at the current facility."
* cardiacStatus.cardiacArrestatTransferringHealthcareFacility ^mapping[+].identity = "Output"
* cardiacStatus.cardiacArrestatTransferringHealthcareFacility ^mapping[=].language = #application/fhir
* cardiacStatus.cardiacArrestatTransferringHealthcareFacility ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=000000 and valueBoolean.exists())"

* procedureInformation 1..1 BackboneElement "CathPCI Procedure Information" 

* procedureInformation.systolicBloodPressure 1..1 CREDSElementDefinition "Blood Pressure (Systolic)"
* procedureInformation.systolicBloodPressure ^mapping[+].identity = "FHIR"
* procedureInformation.systolicBloodPressure ^mapping[=].language = #application/fhir
* procedureInformation.systolicBloodPressure ^mapping[=].map = "Observation.where(code.coding.code = '8480-6')"
* procedureInformation.systolicBloodPressure ^mapping[+].identity = "Output"
* procedureInformation.systolicBloodPressure ^mapping[=].language = #application/fhir
* procedureInformation.systolicBloodPressure ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-blood-pressure"

* procedureInformation.PCIprocedure  1..1 CREDSElementDefinition "PCI Procedure" "Results of this query will fill the %Procedure and %procedure.period environment variables"
* procedureInformation.PCIprocedure ^mapping[+].identity = "FHIR"
* procedureInformation.PCIprocedure ^mapping[=].language = #application/fhir
* procedureInformation.PCIprocedure ^mapping[=].map = "Procedure.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/'PercutaneousCoronaryIntervention') and performedPeriod.exists() )"
* procedureInformation.PCIprocedure ^mapping[+].identity = "Output"
* procedureInformation.PCIprocedure ^mapping[=].language = #application/fhir
* procedureInformation.PCIprocedure ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure"

* procedureInformation.diagnosticCoronaryAngiographyProcedure  0..1 CREDSElementDefinition "Diagnostic Coronary Angiography"
* procedureInformation.diagnosticCoronaryAngiographyProcedure ^mapping[+].identity = "FHIR"
* procedureInformation.diagnosticCoronaryAngiographyProcedure ^mapping[=].language = #application/fhir
* procedureInformation.diagnosticCoronaryAngiographyProcedure ^mapping[=].map = "Procedure.where(code.coding.code = '80994-7' and performedPeriod.start >= %period.start and performedPeriod.end <= %period.end )"
* procedureInformation.diagnosticCoronaryAngiographyProcedure ^mapping[+].identity = "Output"
* procedureInformation.diagnosticCoronaryAngiographyProcedure ^mapping[=].language = #application/fhir
* procedureInformation.diagnosticCoronaryAngiographyProcedure ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure"

* procedureInformation.diagnosticCatheterizationOperator  0..1 CREDSElementDefinition "Diagnostic Catheterization Operator" 
* procedureInformation.diagnosticCatheterizationOperator ^mapping[+].identity = "FHIR"
* procedureInformation.diagnosticCatheterizationOperator ^mapping[=].language = #application/fhir
* procedureInformation.diagnosticCatheterizationOperator ^mapping[=].map = "Procedure.where(code.coding.code = '80994-7' and performedPeriod.start >= %period.start and performedPeriod <= %period.end ).performer.actor.resolve())"
* procedureInformation.diagnosticCatheterizationOperator ^mapping[+].identity = "Output"
* procedureInformation.diagnosticCatheterizationOperator ^mapping[=].language = #application/fhir
* procedureInformation.diagnosticCatheterizationOperator ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitoner"

* procedureInformation.diagnosticLeftHeartCath 0..1 CREDSElementDefinition "Instance of Left Heart Diagnostic Catheterization"
* procedureInformation.diagnosticLeftHeartCath ^mapping[+].identity = "FHIR"
* procedureInformation.diagnosticLeftHeartCath ^mapping[=].language = #application/fhir
* procedureInformation.diagnosticLeftHeartCath ^mapping[=].map = "Procedure.where(code.coding.code = '67629009' and performedPeriod.start >= %period.start and performedPeriod.end <= %period.end)"
* procedureInformation.diagnosticLeftHeartCath ^mapping[+].identity = "Output"
* procedureInformation.diagnosticLeftHeartCath ^mapping[=].language = #application/fhir
* procedureInformation.diagnosticLeftHeartCath ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure"

* procedureInformation.lvefPercentDiagnosticLeftHeartCath 1..1 CREDSElementDefinition "Diagnositic Left Heart Cath LVEF%"
* procedureInformation.lvefPercentDiagnosticLeftHeartCath ^mapping[+].identity = "FHIR"
* procedureInformation.lvefPercentDiagnosticLeftHeartCath ^mapping[=].language = #application/fhir
* procedureInformation.lvefPercentDiagnosticLeftHeartCath ^mapping[=].map = "Observation.where(code.coding.code = '10230-1' and effectiveDate ge %period.start)"
* procedureInformation.lvefPercentDiagnosticLeftHeartCath ^mapping[+].identity = "Output"
* procedureInformation.lvefPercentDiagnosticLeftHeartCath ^mapping[=].language = #application/fhir
* procedureInformation.lvefPercentDiagnosticLeftHeartCath ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-clinical-test"

* procedureInformation.concomitantProceduresPerformed 0..* CREDSElementDefinition "Concomitant Procedures Performed" 
* procedureInformation.concomitantProceduresPerformed ^mapping[+].identity = "Output"
* procedureInformation.concomitantProceduresPerformed ^mapping[=].language = #application/fhir
* procedureInformation.concomitantProceduresPerformed ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/ConcomitantProceduresPerformedType))"

* procedureInformation.cumulativeAirKerma  1..* CREDSElementDefinition "Cumulative Air Kerma" 
* procedureInformation.cumulativeAirKerma ^mapping[+].identity = "FHIR"
* procedureInformation.cumulativeAirKerma ^mapping[=].language = #application/fhir
* procedureInformation.cumulativeAirKerma ^mapping[=].map = "Observation.where(code.coding.code = '228850003' and (effectivePeriod.start >= %period.start and effectivePeriod.end <= %period.end)"
* procedureInformation.cumulativeAirKerma ^mapping[+].identity = "Output"
* procedureInformation.cumulativeAirKerma ^mapping[=].language = #application/fhir
* procedureInformation.cumulativeAirKerma ^mapping[=].map = "Observation"

* procedureInformation.fluoroscopyTime 1..* CREDSElementDefinition "Total Flouroscopy Time"  "Indicate the total fluoroscopy time recorded to the nearest 0.1-minute."
* procedureInformation.fluoroscopyTime ^mapping[+].identity = "Output"
* procedureInformation.fluoroscopyTime ^mapping[=].language = #application/fhir
* procedureInformation.fluoroscopyTime ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014077 and valueTime.exists()"

* procedureInformation.doseAreaProduct 1..* CREDSElementDefinition "Total Flouroscopy Dose"  "Indicate the total fluoroscopy dose to the nearest integer. The value recorded should include the total dose for the lab visit."
* procedureInformation.doseAreaProduct ^mapping[+].identity = "Output"
* procedureInformation.doseAreaProduct ^mapping[=].language = #application/fhir
* procedureInformation.doseAreaProduct ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100000994 and valueQuantity.exists()"

* procedureInformation.arterialCrossOver 1..* CREDSElementDefinition "Arterial Cross Over" "Indicate if the procedure involved a crossover to a different access site."
* procedureInformation.arterialCrossOver ^mapping[+].identity = "Output"
* procedureInformation.arterialCrossOver ^mapping[=].language = #application/fhir
* procedureInformation.arterialCrossOver ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014075 and valueBoolean.exists()"

* procedureInformation.venousAccess 1..* CREDSElementDefinition "Venous Access" "Indicate if a venous access was obtained for the purpose of the diagnostic or PCI procedure."
* procedureInformation.venousAccess ^mapping[+].identity = "Output"
* procedureInformation.venousAccess ^mapping[=].language = #application/fhir
* procedureInformation.venousAccess ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014075 and valueBoolean.exists("

* procedureInformation.cardiacArrestAtThisFacility  1..* CREDSElementDefinition "Cardiac Arrest at this Facility" "Indicate if a cardiac arrest event occurred at this facility PRIOR to the cath lab visit."
* procedureInformation.cardiacArrestAtThisFacility ^mapping[+].identity = "FHIR"
* procedureInformation.cardiacArrestAtThisFacility ^mapping[=].language = #application/fhir
* procedureInformation.cardiacArrestAtThisFacility ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/CardiacArrest) and (effectivePeriod.start> %period.start and effectivePeriod.start < %procedure.period.start))"
* procedureInformation.cardiacArrestAtThisFacility ^mapping[+].identity = "Output"
* procedureInformation.cardiacArrestAtThisFacility ^mapping[=].language = #application/fhir
* procedureInformation.cardiacArrestAtThisFacility ^mapping[=].map = "Observation"

* procedureInformation.preprocedureInformation  1..1 BackboneElement "Pre-procedure Information"
* procedureInformation.preprocedureInformation.heartFailure  1..* CREDSElementDefinition "Heart Failure" "Indicate if the patient has been diagnosed with heart failure, diagnosis date and the Heart Failure type."
* procedureInformation.preprocedureInformation.heartFailure ^mapping[+].identity = "FHIR"
* procedureInformation.preprocedureInformation.heartFailure ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.heartFailure ^mapping[=].map = "Condition.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/HeartFailure) and recordedDate.exists())"
* procedureInformation.preprocedureInformation.heartFailure ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.heartFailure ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.heartFailure ^mapping[=].map = "Condition"

* procedureInformation.preprocedureInformation.newYorkHeartAssociationClassification 1..* CREDSElementDefinition "New York Heart Association Classification" "Indicate the patient's latest dyspnea or functional class, coded as the New York Heart Association (NYHA) classification."
* procedureInformation.preprocedureInformation.newYorkHeartAssociationClassification ^mapping[+].identity = "FHIR"
* procedureInformation.preprocedureInformation.newYorkHeartAssociationClassification ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.newYorkHeartAssociationClassification ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/NewYorkHeartAssociationQuery))"
* procedureInformation.preprocedureInformation.newYorkHeartAssociationClassification ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.newYorkHeartAssociationClassification ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.newYorkHeartAssociationClassification ^mapping[=].map = "Observation.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/NewYorkHeartAssociationAnswers)"

* procedureInformation.preprocedureInformation.diagnosticTest  1..1 BackboneElement "Pre-procedure Diagnostic Tests"

* procedureInformation.preprocedureInformation.diagnosticTest.electrocardiacAssessment 0..* CREDSElementDefinition "Electrocardiac Assessment" "Indicate the results of the electrocardiac assessment." 
* procedureInformation.preprocedureInformation.diagnosticTest.electrocardiacAssessment ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.diagnosticTest.electrocardiacAssessment ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.electrocardiacAssessment ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142467 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/ElectrocardiacAssessmentResults) and Observation.method.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/ElectrocardiacAssessmentMethod)"

* procedureInformation.preprocedureInformation.diagnosticTest.newAntiarrhythmicTherapyInitiatedPriorToCathLab 1..* CREDSElementDefinition "New Antiarrhythmic Therapy Initiated Prior to Cath Lab" "Indicate if the patient received a NEW antiarrhythmic therapy PRIOR to evaluation within the cath lab."
* procedureInformation.preprocedureInformation.diagnosticTest.newAntiarrhythmicTherapyInitiatedPriorToCathLab ^mapping[+].identity = "FHIR"
* procedureInformation.preprocedureInformation.diagnosticTest.newAntiarrhythmicTherapyInitiatedPriorToCathLab ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.newAntiarrhythmicTherapyInitiatedPriorToCathLab ^mapping[=].map = "MedicationStatement.where(medicationCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/Antiarrhythmics) and effectiveDateTime < %Encounter.period.start and effeciveDateTime < %Encounter.period.start - 30 days)"
* procedureInformation.preprocedureInformation.diagnosticTest.newAntiarrhythmicTherapyInitiatedPriorToCathLab ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.diagnosticTest.newAntiarrhythmicTherapyInitiatedPriorToCathLab ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.newAntiarrhythmicTherapyInitiatedPriorToCathLab ^mapping[=].map = "MedicationStatement"

* procedureInformation.preprocedureInformation.diagnosticTest.electrocardiacAbnormalityType 0..* CREDSElementDefinition "Electrocardiac Assessment Abnormality Type" "Indicate the findings of the electrocardiac assessment."
* procedureInformation.preprocedureInformation.diagnosticTest.electrocardiacAbnormalityType ^mapping[+].identity = "FHIR"
* procedureInformation.preprocedureInformation.diagnosticTest.electrocardiacAbnormalityType ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.electrocardiacAbnormalityType ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/AbnormalElectrocardiacAssessment)"
* procedureInformation.preprocedureInformation.diagnosticTest.electrocardiacAbnormalityType ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.diagnosticTest.electrocardiacAbnormalityType ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.electrocardiacAbnormalityType ^mapping[=].map = "Observation.where(valueCodeableConcept.exists() or valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/ElectrocardiacAbnormalityType)"

* procedureInformation.preprocedureInformation.diagnosticTest.nonSustainedVentricularTachycardiaType 0..* CREDSElementDefinition "Non-Sustained Ventricular Tachycardia Type" "Last value between 30 days prior to 1st procedure (or previous procedure) and current procedure"
* procedureInformation.preprocedureInformation.diagnosticTest.nonSustainedVentricularTachycardiaType ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.diagnosticTest.nonSustainedVentricularTachycardiaType ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.nonSustainedVentricularTachycardiaType ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142475 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/NonSustainedVentricularTachycardiaType)"

* procedureInformation.preprocedureInformation.diagnosticTest.lvef 1..* CREDSElementDefinition "LVEF % (Pre-Procedure)" "Indicate the best estimate of the most recent left ventricular ejection fraction within 6 months of procedure."
* procedureInformation.preprocedureInformation.diagnosticTest.lvef ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.diagnosticTest.lvef ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.lvef ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100001027 and valueQuantity.exists())"

* procedureInformation.preprocedureInformation.diagnosticTest.cardiacCta 0..* CREDSElementDefinition "Cardiac CTA"
* procedureInformation.preprocedureInformation.diagnosticTest.cardiacCta ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.diagnosticTest.cardiacCta ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.cardiacCta ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100001257 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/CardiacCTAResults)"

* procedureInformation.preprocedureInformation.diagnosticTest.agatstonCalciumScore 0..* CREDSElementDefinition "Agatston Calcium Score"
* procedureInformation.preprocedureInformation.diagnosticTest.agatstonCalciumScore ^mapping[+].identity = "FHIR"
* procedureInformation.preprocedureInformation.diagnosticTest.agatstonCalciumScore ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.agatstonCalciumScore ^mapping[=].map = "Observation.where(code.coding.code = '450360000')"
* procedureInformation.preprocedureInformation.diagnosticTest.agatstonCalciumScore ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.diagnosticTest.agatstonCalciumScore ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.agatstonCalciumScore ^mapping[=].map = "Observation"

* procedureInformation.preprocedureInformation.diagnosticTest.priorDcapWithoutIntervention 0..* CREDSElementDefinition "Prior Diagnostic Coronary Angiography Procedure without intervention" "Indicate if the patient had a prior diagnostic coronary angiography procedure without a subsequent intervention." 
* procedureInformation.preprocedureInformation.diagnosticTest.priorDcapWithoutIntervention ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.diagnosticTest.priorDcapWithoutIntervention ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.priorDcapWithoutIntervention ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=10001424782 and valueBoolean.exists())"

* procedureInformation.preprocedureInformation.diagnosticTest.priorDcapResults 0..* CREDSElementDefinition "Prior Diagnostic Coronary Angiography Procedure results" "Indicate the results of the prior diagnostic coronary angiography."
* procedureInformation.preprocedureInformation.diagnosticTest.priorDcapResults ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.diagnosticTest.priorDcapResults ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.priorDcapResults ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=10001424784 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PriorDiagnosticCoronaryAngiographyProcedureResults))"

* procedureInformation.preprocedureInformation.diagnosticTest.heartRate 0..* CREDSElementDefinition "Heart Rate"
* procedureInformation.preprocedureInformation.diagnosticTest.heartRate ^mapping[+].identity = "FHIR"
* procedureInformation.preprocedureInformation.diagnosticTest.heartRate ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.heartRate ^mapping[=].map = "Observation.where(code.coding.code = '8867-4')"
* procedureInformation.preprocedureInformation.diagnosticTest.heartRate ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.diagnosticTest.heartRate ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.heartRate ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-heart-rate"

* procedureInformation.preprocedureInformation.diagnosticTest.stressTest 0..* CREDSElementDefinition "Indicate Stress Test Performed and results"
* procedureInformation.preprocedureInformation.diagnosticTest.stressTest ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.diagnosticTest.stressTest ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.stressTest ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142432 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/StressTestResults) and Observation.method.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/StressTest))" 

* procedureInformation.preprocedureInformation.diagnosticTest.stressTest.riskOrExtentOfIschemia 0..* CREDSElementDefinition  "Stress Test Risk/Extent of Ischemia" "Indicate the risk or extent of ischemia for the non-invasive stress test."
* procedureInformation.preprocedureInformation.diagnosticTest.stressTest.riskOrExtentOfIschemia ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.diagnosticTest.stressTest.riskOrExtentOfIschemia ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.diagnosticTest.stressTest.riskOrExtentOfIschemia ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142434 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/StressTestRiskExtentofIschemia))"

* procedureInformation.preprocedureInformation.preprocedureMedication 0..* CREDSElementDefinition "PreProcedure Medication" "Indicate the assigned identification number associated with the medications the patient was prescribed or received." 
* procedureInformation.preprocedureInformation.preprocedureMedication ^mapping[+].identity = "FHIR"
* procedureInformation.preprocedureInformation.preprocedureMedication ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.preprocedureMedication ^mapping[=].map = "MedicationAdministration.where(effectiveDateTime >= %period.start - 2 weeks and effeciveDateTime < %procedure.period.start)"
* procedureInformation.preprocedureInformation.preprocedureMedication ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.preprocedureMedication ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.preprocedureMedication ^mapping[=].map = "MedicationAdministration"

* procedureInformation.preprocedureInformation.saQuestionnaire  7..* CREDSElementDefinition  "Responses to the Seattle Angina Questionnaire"
* procedureInformation.preprocedureInformation.saQuestionnaire ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.saQuestionnaire ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.saQuestionnaire ^mapping[=].map = "Observation.where(code.coding.system='http://loinc.org' and code.coding.code=88479-1 and component.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/SeattleAnginaQs) and component.valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/SeattleAnginaAs))"

* procedureInformation.preprocedureInformation.roseDyspneaScale  4..* CREDSElementDefinition  "Responses to the Rose Dyspnea Scale Questionnaire"
* procedureInformation.preprocedureInformation.roseDyspneaScale ^mapping[+].identity = "Output"
* procedureInformation.preprocedureInformation.roseDyspneaScale ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureInformation.roseDyspneaScale ^mapping[=].map = "Observation.where(code.coding.system='http://loinc.org' and code.coding.code=89440-2 and component.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/RoseDyspneaQ) and component.valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/YesNo))"

* procedureInformation.closureMethods 1..1 BackboneElement "Method and Device used for procedure closures"

* procedureInformation.closureMethods.arterialAccessClosureMethod 0..* CREDSElementDefinition  "Arterial Access Closure Method"
* procedureInformation.closureMethods.arterialAccessClosureMethod ^mapping[+].identity = "Output"
* procedureInformation.closureMethods.arterialAccessClosureMethod ^mapping[=].language = #application/fhir
* procedureInformation.closureMethods.arterialAccessClosureMethod ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014074 and valueString.exists())"

* procedureInformation.closureMethods.closureMethodUdi 0..* CREDSElementDefinition  "Arterial Access Closure Devices"
* procedureInformation.closureMethods.closureMethodUdi ^mapping[+].identity = "FHIR"
* procedureInformation.closureMethods.closureMethodUdi ^mapping[=].language = #application/fhir
* procedureInformation.closureMethods.closureMethodUdi ^mapping[=].map = "%procedure.focalDevice.manipulated.resolve()"
* procedureInformation.closureMethods.closureMethodUdi ^mapping[+].identity = "Output"
* procedureInformation.closureMethods.closureMethodUdi ^mapping[=].language = #application/fhir
* procedureInformation.closureMethods.closureMethodUdi ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-implantable-device"

* procedureInformation.preprocedureLabs 1..1 BackboneElement "Preprocedure Lab Results"

* procedureInformation.preprocedureLabs.hemoglobin 1..* CREDSElementDefinition "Hemoglobin" "Indicate the hemoglobin (Hgb) value in g/dL."
* procedureInformation.preprocedureLabs.hemoglobin ^mapping[+].identity = "FHIR"
* procedureInformation.preprocedureLabs.hemoglobin ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureLabs.hemoglobin ^mapping[=].map = "Observation.where(code.coding.code = '718-7' and effectiveDateTime >= %procedure.period.end - 30 days and effectiveDateTime < %procedure.period.start)"
* procedureInformation.preprocedureLabs.hemoglobin ^mapping[+].identity = "Output"
* procedureInformation.preprocedureLabs.hemoglobin ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureLabs.hemoglobin ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab"

* procedureInformation.preprocedureLabs.creatinine 1..* CREDSElementDefinition "Creatinine" "Indicate the creatinine (Cr) level in mg/dL."
* procedureInformation.preprocedureLabs.creatinine ^mapping[+].identity = "FHIR"
* procedureInformation.preprocedureLabs.creatinine ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureLabs.creatinine ^mapping[=].map = "Observation.where(code.coding.code = '2160-0' and effectiveDateTime >= %period.start and effectiveDateTime < %procedure.period.start)"
* procedureInformation.preprocedureLabs.creatinine ^mapping[+].identity = "Output"
* procedureInformation.preprocedureLabs.creatinine ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureLabs.creatinine ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab"

* procedureInformation.preprocedureLabs.troponinI  1..* CREDSElementDefinition "PreProcedure Troponin I" "Indicate the Troponin I result in ng/mL."
* procedureInformation.preprocedureLabs.troponinI ^mapping[+].identity = "FHIR"
* procedureInformation.preprocedureLabs.troponinI ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureLabs.troponinI ^mapping[=].map = "Observation.where(code.coding.code = '10839-9' and effectiveDateTime >= %period.start and effectiveDateTime < %procedure.period.start)"
* procedureInformation.preprocedureLabs.troponinI ^mapping[+].identity = "Output"
* procedureInformation.preprocedureLabs.troponinI ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureLabs.troponinI ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab"

* procedureInformation.preprocedureLabs.troponinT  1..* CREDSElementDefinition "PreProcedure Troponin T" "Indicate the Troponin I result in ng/mL."
* procedureInformation.preprocedureLabs.troponinI ^mapping[+].identity = "FHIR"
* procedureInformation.preprocedureLabs.troponinI ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureLabs.troponinI ^mapping[=].map = "Observation.where(code.coding.code = '6598-7' and effectiveDateTime >= %period.start and effectiveDateTime < %procedure.period.start)"
* procedureInformation.preprocedureLabs.troponinI ^mapping[+].identity = "Output"
* procedureInformation.preprocedureLabs.troponinI ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureLabs.troponinI ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab"

* procedureInformation.preprocedureLabs.totalCholesterol  1..* CREDSElementDefinition "PreProcedure Total Cholesterol" "Indicate the cholesterol level mg/dL."
* procedureInformation.preprocedureLabs.totalCholesterol ^mapping[+].identity = "FHIR"
* procedureInformation.preprocedureLabs.totalCholesterol ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureLabs.totalCholesterol ^mapping[=].map = "Observation.where(code.coding.code = '2093-3' and  and effectiveDateTime >= %procedure.period.start - 30 days and effectiveDateTime < %procedure.period.start)"
* procedureInformation.preprocedureLabs.totalCholesterol ^mapping[+].identity = "Output"
* procedureInformation.preprocedureLabs.totalCholesterol ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureLabs.totalCholesterol ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab"

* procedureInformation.preprocedureLabs.highDensityLipoprotein  1..* CREDSElementDefinition "PreProcedure Total Cholesterol" "Indicate the cholesterol level mg/dL."
* procedureInformation.preprocedureLabs.highDensityLipoprotein ^mapping[+].identity = "FHIR"
* procedureInformation.preprocedureLabs.highDensityLipoprotein ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureLabs.highDensityLipoprotein ^mapping[=].map = "Observation.where(code.coding.code = '2085-9' and  and effectiveDateTime >= %procedure.period.start - 30 days and effectiveDateTime < %procedure.period.start)"
* procedureInformation.preprocedureLabs.highDensityLipoprotein ^mapping[+].identity = "Output"
* procedureInformation.preprocedureLabs.highDensityLipoprotein ^mapping[=].language = #application/fhir
* procedureInformation.preprocedureLabs.highDensityLipoprotein ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab"

* procedureInformation.postprocedureLabs 1..1 BackboneElement "Results of Postprocedure Labs"

* procedureInformation.postprocedureLabs.hemoglobin 1..* CREDSElementDefinition "Hemoglobin" "Indicate the hemoglobin (Hgb) value in g/dL."
* procedureInformation.postprocedureLabs.hemoglobin ^mapping[+].identity = "FHIR"
* procedureInformation.postprocedureLabs.hemoglobin ^mapping[=].language = #application/fhir
* procedureInformation.postprocedureLabs.hemoglobin ^mapping[=].map = "Observation.where(code.coding.code = '718-7' and effectiveDateTime >= %procedure.period.end and effectiveDateTime < %procedure.period.end + 72 hours)"
* procedureInformation.postprocedureLabs.hemoglobin ^mapping[+].identity = "Output"
* procedureInformation.postprocedureLabs.hemoglobin ^mapping[=].language = #application/fhir
* procedureInformation.postprocedureLabs.hemoglobin ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab"

* procedureInformation.postprocedureLabs.creatinine 1..* CREDSElementDefinition "Creatinine" "Indicate the creatinine (Cr) level in mg/dL."
* procedureInformation.postprocedureLabs.creatinine ^mapping[+].identity = "FHIR"
* procedureInformation.postprocedureLabs.creatinine ^mapping[=].language = #application/fhir
* procedureInformation.postprocedureLabs.creatinine ^mapping[=].map = "Observation.where(code.coding.code = '2160-0' and effectiveDateTime >= %procedure.period.end and effectiveDateTime < %procedure.period.end + 5 days)"
* procedureInformation.postprocedureLabs.creatinine ^mapping[+].identity = "Output"
* procedureInformation.postprocedureLabs.creatinine ^mapping[=].language = #application/fhir
* procedureInformation.postprocedureLabs.creatinine ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab"

* procedureInformation.postprocedureLabs.troponinI  1..* CREDSElementDefinition "PreProcedure Troponin I" "Indicate the Troponin I result in ng/mL."
* procedureInformation.postprocedureLabs.troponinI ^mapping[+].identity = "FHIR"
* procedureInformation.postprocedureLabs.troponinI ^mapping[=].language = #application/fhir
* procedureInformation.postprocedureLabs.troponinI ^mapping[=].map = "Observation.where(code.coding.code = '10839-9' and effectiveDateTime >= %procedure.period.end + 6 hours and effectiveDateTime < %procedure.period.end + 24 hours)"
* procedureInformation.postprocedureLabs.troponinI ^mapping[+].identity = "Output"
* procedureInformation.postprocedureLabs.troponinI ^mapping[=].language = #application/fhir
* procedureInformation.postprocedureLabs.troponinI ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab"

* procedureInformation.postprocedureLabs.troponinT  1..* CREDSElementDefinition "PreProcedure Troponin T" "Indicate the Troponin I result in ng/mL."
* procedureInformation.postprocedureLabs.troponinI ^mapping[+].identity = "FHIR"
* procedureInformation.postprocedureLabs.troponinI ^mapping[=].language = #application/fhir
* procedureInformation.postprocedureLabs.troponinI ^mapping[=].map = "Observation.where(code.coding.code = '6598-7' and effectiveDateTime >= %procedure.period.end + 6 hours and effectiveDateTime < %procedure.period.end + 24 hours)"
* procedureInformation.postprocedureLabs.troponinI ^mapping[+].identity = "Output"
* procedureInformation.postprocedureLabs.troponinI ^mapping[=].language = #application/fhir
* procedureInformation.postprocedureLabs.troponinI ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab"

* procedureInformation.cathLabVisit 1..1 BackboneElement "Information Regarding the Cath Lab Procedure"

* procedureInformation.cathLabVisit.indicationsForCathLabVisit 0..* CREDSElementDefinition  "Indications for Cath Lab Visit" "Indicate the patient symptoms or condition prompting the cath lab visit."

* procedureInformation.cathLabVisit.chestPainSymptomAssessment  0..* CREDSElementDefinition "Chest Pain Symptom Assessment" "Indicate the chest pain symptom assessment as diagnosed by the physician or described by the patient."
* procedureInformation.cathLabVisit.chestPainSymptomAssessment ^mapping[+].identity = "Output"
* procedureInformation.cathLabVisit.chestPainSymptomAssessment ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.chestPainSymptomAssessment ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100001274 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/ChestPainSymptomAssessment))"

* procedureInformation.cathLabVisit.cardiovascularInstabilitytype 0..* CREDSElementDefinition "Cardiovascular Instability Type" "Cardiovascular instability includes, but is not limited to, persistent ischemic symptoms (such as chest pain or ST elevation), cardiogenic shock, ventricular arrhythmias, symptoms of acute heart failure, or hemodynamic instability (not cardiogenic shock)."
* procedureInformation.cathLabVisit.cardiovascularInstabilitytype ^mapping[+].identity = "Output"
* procedureInformation.cathLabVisit.cardiovascularInstabilitytype ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.cardiovascularInstabilitytype ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014004 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/CardiacInstabilityType))"

* procedureInformation.cathLabVisit.ventricularSupport 0..* CREDSElementDefinition "Ventricular Support" "Indicate if the patient required any type of ventricular support (i.e. IV vasopressors or mechanical)."
* procedureInformation.cathLabVisit.ventricularSupport ^mapping[+].identity = "Output"
* procedureInformation.cathLabVisit.ventricularSupport ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.ventricularSupport ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100001276 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/VentricularSupport))"

* procedureInformation.cathLabVisit.pharmacologicVasopressorSupport 0..* CREDSElementDefinition "Pharmacologic Vasopressor Support" "Indicate if the patient required pharmacologic vasopressor support."
* procedureInformation.cathLabVisit.pharmacologicVasopressorSupport ^mapping[+].identity = "Output"
* procedureInformation.cathLabVisit.pharmacologicVasopressorSupport ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.pharmacologicVasopressorSupport ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100001277 and valueBoolen.exists())"

* procedureInformation.cathLabVisit.mechanicalVentricularSupportTiming 0..* CREDSElementDefinition "Mechanical Ventricular Support Timing" "Indicate when the mechanical ventricular support device was placed."
* procedureInformation.cathLabVisit.mechanicalVentricularSupportTiming ^mapping[+].identity = "Output"
* procedureInformation.cathLabVisit.mechanicalVentricularSupportTiming ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.mechanicalVentricularSupportTiming ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100001277 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/MechanicalVentricularSupportTiming))"

* procedureInformation.cathLabVisit.evaluationForSurgeryType 0..* CREDSElementDefinition "Evaluation for Surgery Type" "Indicate the type of surgery for which the diagnostic coronary angiography is being performed."
* procedureInformation.cathLabVisit.evaluationForSurgeryType ^mapping[+].identity = "Output"
* procedureInformation.cathLabVisit.evaluationForSurgeryType ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.evaluationForSurgeryType ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014009 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/MechanicalVentricularSupportTiming))"

* procedureInformation.cathLabVisit.functionalCapacity 1..* CREDSElementDefinition "Functional Capacity" "Indicate the functional capacity of the patient as documented by the physician in the medical record."
* procedureInformation.cathLabVisit.functionalCapacity ^mapping[+].identity = "Output"
* procedureInformation.cathLabVisit.functionalCapacity ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.functionalCapacity ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142418 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/FunctionalCapacity))"

* procedureInformation.cathLabVisit.surgicalRisk 0..* CREDSElementDefinition "Surgical Risk" "Indicate the surgical risk category as documented by the physician in the medical record."
* procedureInformation.cathLabVisit.surgicalRisk ^mapping[+].identity = "Output"
* procedureInformation.cathLabVisit.surgicalRisk ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.surgicalRisk ^mapping[=].map = "Observation.where( code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142420 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/SurgicalRisk))"

* procedureInformation.cathLabVisit.solidOrganTransplantdonor  0..* CREDSElementDefinition "Instance and Type of Organ Donor"
* procedureInformation.cathLabVisit.solidOrganTransplantdonor ^mapping[+].identity = "FHIR"
* procedureInformation.cathLabVisit.solidOrganTransplantdonor ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.solidOrganTransplantdonor ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/OrganDonor) or code.coding.code = '51032003')"
* procedureInformation.cathLabVisit.solidOrganTransplantdonor ^mapping[+].identity = "Output"
* procedureInformation.cathLabVisit.solidOrganTransplantdonor ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.solidOrganTransplantdonor ^mapping[=].map = "Observation"

* procedureInformation.cathLabVisit.valvularDiseaseStenosis   0..* CREDSElementDefinition "Valvular Disease Stenosis" "Indicate the severity and cardiac valve(s) with stenosis as diagnosed by the physician."
* procedureInformation.cathLabVisit.valvularDiseaseStenosis ^mapping[+].identity = "FHIR"
* procedureInformation.cathLabVisit.valvularDiseaseStenosis ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.valvularDiseaseStenosis ^mapping[=].map = "Condition.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/ValvularStenosis))"
* procedureInformation.cathLabVisit.valvularDiseaseStenosis ^mapping[+].identity = "FHIR"
* procedureInformation.cathLabVisit.valvularDiseaseStenosis ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.valvularDiseaseStenosis ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/ValvularStenosis))"
* procedureInformation.cathLabVisit.valvularDiseaseStenosis ^mapping[+].identity = "Output"
* procedureInformation.cathLabVisit.valvularDiseaseStenosis ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.valvularDiseaseStenosis ^mapping[=].map = "Observation.where(Observation.valueCodeableConcept.exists() or Observation.valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/ValvularDiseaseStenosisSeverity)"


* procedureInformation.cathLabVisit.valvularDiseaseRegurgitation 0..* CREDSElementDefinition "Valvular Disease Stenosis"
* procedureInformation.cathLabVisit.valvularDiseaseRegurgitation ^mapping[+].identity = "FHIR"
* procedureInformation.cathLabVisit.valvularDiseaseRegurgitation ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.valvularDiseaseRegurgitation ^mapping[=].map = "Condition.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/ValvularStenosis))"
* procedureInformation.cathLabVisit.valvularDiseaseRegurgitation ^mapping[+].identity = "FHIR"
* procedureInformation.cathLabVisit.valvularDiseaseRegurgitation ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.valvularDiseaseRegurgitation ^mapping[=].map = "Observation.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/ValvularStenosis))"
* procedureInformation.cathLabVisit.valvularDiseaseRegurgitation ^mapping[+].identity = "Output"
* procedureInformation.cathLabVisit.valvularDiseaseRegurgitation ^mapping[=].language = #application/fhir
* procedureInformation.cathLabVisit.valvularDiseaseRegurgitation ^mapping[=].map = "Observation.where(Observation.valueCodeableConcept.exists() or Observation.valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/ValvularDiseaseRegurgitationSeverity)"

* procedureInformation.coronaryAnatomy 1..1 BackboneElement "Coronary Anatomy"

* procedureInformation.coronaryAnatomy.nativeVessel 1..1 BackboneElement "Native Vessel"

* procedureInformation.coronaryAnatomy.nativeVessel.lesionSegmentNumber 0..* CREDSElementDefinition "Native Lesion Segment Number"
* procedureInformation.coronaryAnatomy.nativeVessel.lesionSegmentNumber ^mapping[+].identity = "Output"
* procedureInformation.coronaryAnatomy.nativeVessel.lesionSegmentNumber ^mapping[=].language = #application/fhir
* procedureInformation.coronaryAnatomy.nativeVessel.lesionSegmentNumber ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012984 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/LesionSegmentNumber)"

* procedureInformation.coronaryAnatomy.nativeVessel.coronaryVesselStenosis 0..* CREDSElementDefinition "Coronary Vessel Stenosis" "Indicate the best estimate of the most severe percent stenosis in the segment of the native coronary vessel identified."
* procedureInformation.coronaryAnatomy.nativeVessel.coronaryVesselStenosis ^mapping[+].identity = "Output"
* procedureInformation.coronaryAnatomy.nativeVessel.coronaryVesselStenosis ^mapping[=].language = #application/fhir
* procedureInformation.coronaryAnatomy.nativeVessel.coronaryVesselStenosis ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012981 and valueQuantity.exists())"

* procedureInformation.coronaryAnatomy.nativeVessel.adjunctiveMeasurementsObtained 0..* CREDSElementDefinition "Adjunctive Measurements Obtained" "Indicate if an invasive diagnostic measurement was obtained of the native vessel segment."
* procedureInformation.coronaryAnatomy.nativeVessel.adjunctiveMeasurementsObtained ^mapping[+].identity = "Output"
* procedureInformation.coronaryAnatomy.nativeVessel.adjunctiveMeasurementsObtained ^mapping[=].language = #application/fhir
* procedureInformation.coronaryAnatomy.nativeVessel.adjunctiveMeasurementsObtained ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012979 and valueBoolean.exists()"

* procedureInformation.coronaryAnatomy.nativeVessel.instantaneousWaveFreeRatio 0..* CREDSElementDefinition "Instantaneous Wave-Free Ratio" "Indicate the instantaneous wave-free ratio (iFR ratio) of the native vessel segment."
* procedureInformation.coronaryAnatomy.nativeVessel.instantaneousWaveFreeRatio ^mapping[+].identity = "Output"
* procedureInformation.coronaryAnatomy.nativeVessel.instantaneousWaveFreeRatio ^mapping[=].language = #application/fhir
* procedureInformation.coronaryAnatomy.nativeVessel.instantaneousWaveFreeRatio ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012980 and valueBoolean.exists())"

* procedureInformation.coronaryAnatomy.graftVessel 1..1 BackboneElement "Graft Vessel"

* procedureInformation.coronaryAnatomy.graftVessel.lesionSegmentNumber  0..* CREDSElementDefinition "Graft Lesion Segment Number"
* procedureInformation.coronaryAnatomy.graftVessel.lesionSegmentNumber ^mapping[+].identity = "Output"
* procedureInformation.coronaryAnatomy.graftVessel.lesionSegmentNumber ^mapping[=].language = #application/fhir
* procedureInformation.coronaryAnatomy.graftVessel.lesionSegmentNumber ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012984 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/LesionSegmentNumber))"

* procedureInformation.coronaryAnatomy.graftVessel.coronaryVesselStenosis 0..* CREDSElementDefinition "Coronary Vessel Stenosis" "Indicate the best estimate of the most severe percent stenosis in the segment of the graft coronary vessel identified."
* procedureInformation.coronaryAnatomy.graftVessel.coronaryVesselStenosis ^mapping[+].identity = "Output"
* procedureInformation.coronaryAnatomy.graftVessel.coronaryVesselStenosis ^mapping[=].language = #application/fhir
* procedureInformation.coronaryAnatomy.graftVessel.coronaryVesselStenosis ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012982 and valueQuantity.exists())"

* procedureInformation.coronaryAnatomy.graftVessel.cabg 0..1 CREDSElementDefinition "Indicate the vessel that was used for the coronary artery bypass graft."
* procedureInformation.coronaryAnatomy.graftVessel.cabg ^mapping[+].identity = "Output"
* procedureInformation.coronaryAnatomy.graftVessel.cabg ^mapping[=].language = #application/fhir
* procedureInformation.coronaryAnatomy.graftVessel.cabg ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012983 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/GraftVesselCABGVessel))"

* procedureInformation.coronaryAnatomy.graftVessel.adjunctiveMeasurementsObtained 0..1 CREDSElementDefinition "Indicate if an invasive diagnostic measurement was obtained of the graft vessel intra-procedure."
* procedureInformation.coronaryAnatomy.graftVessel.adjunctiveMeasurementsObtained ^mapping[+].identity = "Output"
* procedureInformation.coronaryAnatomy.graftVessel.adjunctiveMeasurementsObtained ^mapping[=].language = #application/fhir
* procedureInformation.coronaryAnatomy.graftVessel.adjunctiveMeasurementsObtained ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012982 and valueBoolean.exists())"

* procedureInformation.coronaryAnatomy.graftVessel.instantaneousWaveFreeRatio  0..* CREDSElementDefinition "Instantaneous Wave-Free Ratio" "Indicate the instantaneous wave-free ratio (iFR ratio) of the graft vessel segment."
* procedureInformation.coronaryAnatomy.nativeVessel.instantaneousWaveFreeRatio ^mapping[+].identity = "Output"
* procedureInformation.coronaryAnatomy.nativeVessel.instantaneousWaveFreeRatio ^mapping[=].language = #application/fhir
* procedureInformation.coronaryAnatomy.nativeVessel.instantaneousWaveFreeRatio ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012980 and valueBoolean.exists())"

* procedureInformation.pciProcedure 1..1 BackboneElement "information regarding the PCI Procedure"

* procedureInformation.pciProcedure.pciStatus 0..* CREDSElementDefinition "Indicate the status of the PCI. The status is determined at the time the operator decides to perform a PCI."
* procedureInformation.pciProcedure.pciStatus ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.pciStatus ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.pciStatus ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012986 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PCIStatus))"

* procedureInformation.pciProcedure.hypothermiaInduced 0..* CREDSElementDefinition "Indicate when hypothermia was initiated."
* procedureInformation.pciProcedure.hypothermiaInduced ^mapping[+].identity = "FHIR"
* procedureInformation.pciProcedure.hypothermiaInduced ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.hypothermiaInduced ^mapping[=].map = "Procedure.where(code.coding.code.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/HypothermiaInduced))"
* procedureInformation.pciProcedure.hypothermiaInduced ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.hypothermiaInduced ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.hypothermiaInduced ^mapping[=].map = "Procedure.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100013039 and valueDateTime.exists())"

* procedureInformation.pciProcedure.decisionForPciWithSurgicalConsult 1..* CREDSElementDefinition "Indicate if a cardiac surgical consult was obtained prior to engaging in PCI."
* procedureInformation.pciProcedure.decisionForPciWithSurgicalConsult ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.decisionForPciWithSurgicalConsult ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.decisionForPciWithSurgicalConsult ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142366 and valueBoolean.exists())"

* procedureInformation.pciProcedure.cardiovascularTreatmentDecision 1..* CREDSElementDefinition "Indicate the cardiovascular surgery recommendation and/or patient/family decision."
* procedureInformation.pciProcedure.cardiovascularTreatmentDecision ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.cardiovascularTreatmentDecision ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.cardiovascularTreatmentDecision ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142367 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/CardiovascularTreatmentDecision))"


* procedureInformation.pciProcedure.pciForMultivesselDisease  1..* CREDSElementDefinition "Indicate if the PCI procedure was performed in the presence of multi-vessel disease."
* procedureInformation.pciProcedure.pciForMultivesselDisease ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.pciForMultivesselDisease ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.pciForMultivesselDisease ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100013007 and valueBoolean.exists())"


* procedureInformation.pciProcedure.multiVesselProcedureType  0..* CREDSElementDefinition "Indicate the type of multi-vessel PCI procedure that was performed during this lab visit."
* procedureInformation.pciProcedure.multiVesselProcedureType ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.multiVesselProcedureType ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.multiVesselProcedureType ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100013008 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/MultivesselProcedureType))"

* procedureInformation.pciProcedure.percutaneousCoronaryInterventionIndication 1..* CREDSElementDefinition "Indicate the reason the percutaneous coronary intervention PCI is being performed."
* procedureInformation.pciProcedure.percutaneousCoronaryInterventionIndication ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.percutaneousCoronaryInterventionIndication ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.percutaneousCoronaryInterventionIndication ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100000880 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PCIIndications))"

* procedureInformation.pciProcedure.acuteCoronarySyndromeSymptom 1..* CREDSElementDefinition "Acute Coronary Syndrome Symptom"
* procedureInformation.pciProcedure.acuteCoronarySyndromeSymptom ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.acuteCoronarySyndromeSymptom ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.acuteCoronarySyndromeSymptom ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100013003 and valueDateTime.exists())"

* procedureInformation.pciProcedure.syntaxScore 1..1 CREDSElementDefinition "Indicate the Syntax Score for the PCI procedure."
* procedureInformation.pciProcedure.syntaxScore ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.syntaxScore ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.syntaxScore ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=10001424796 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/SyntaxScore))"

* procedureInformation.pciProcedure.stemiOrStemiEquivalentFirstNoted  0..1 CREDSElementDefinition  "Indicate if a STEMI or STEMI equivalent was noted on either the first ECG or a subsequent ECG."
* procedureInformation.pciProcedure.syntaxScore ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.syntaxScore ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.syntaxScore ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100000180 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/STEMIFirstNoted))"

* procedureInformation.pciProcedure.subsequentEcgWithStemiOrStemiEquivalent  0..1 CREDSElementDefinition "Indicate the Subsequent ECG date and time."
* procedureInformation.pciProcedure.subsequentEcgWithStemiOrStemiEquivalent ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.subsequentEcgWithStemiOrStemiEquivalent ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.subsequentEcgWithStemiOrStemiEquivalent ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012995 and valueDateTime.exists())"

* procedureInformation.pciProcedure.subsequentEcgObtainedInEmergencyDepartment 0..1 CREDSElementDefinition "Indicate if the subsequent ECG was obtained in the Emergency Department at this facility."
* procedureInformation.pciProcedure.subsequentEcgObtainedInEmergencyDepartment ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.subsequentEcgObtainedInEmergencyDepartment ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.subsequentEcgObtainedInEmergencyDepartment ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012995 and valueBoolean.exists())"

* procedureInformation.pciProcedure.patientTransferredInForImmediatePciForStemi 0..1 CREDSElementDefinition "Indicate if the patient was transferred from another facility to have a primary PCI for STEMI at this facility."
* procedureInformation.pciProcedure.patientTransferredInForImmediatePciForStemi ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.patientTransferredInForImmediatePciForStemi ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.patientTransferredInForImmediatePciForStemi ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014084 and valueBoolean.exists())"

* procedureInformation.pciProcedure.emergencyDepartmentPresentationAtReferringFacility 0..1 CREDSElementDefinition "Code the date and time of arrival to the original, transferring facility as documented in the medical record."
* procedureInformation.pciProcedure.emergencyDepartmentPresentationAtReferringFacility ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.emergencyDepartmentPresentationAtReferringFacility ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.emergencyDepartmentPresentationAtReferringFacility ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012999 and valueDateTime.exists())"

* procedureInformation.pciProcedure.firstDeviceActivation 0..1 CREDSElementDefinition "Indicate the date and time the first device was activated regardless of type of device used."
* procedureInformation.pciProcedure.firstDeviceActivation ^comment = """
Use the earliest time from the following:
1. Time of the first balloon inflation.
2. Time of the first stent deployment.
3. Time of the first treatment of lesion (AngjoJet or other thrombectomy/aspiration device, laser, rotational atherectomy).
4. If the lesion cannot be crossed with a guidewire or device (and thus none of the above apply), use the time of guidewire introduction.
This is a process measure about the timeliness of treatment. It is NOT a clinical outcomes measure based on TIMI flow or clinical reperfusion. It does not matter whether the baseline angiogram showed TIMI 3 flow or if the final post-PCI angiogram showed TIMI 0 flow. What is being measured is the time of the first mechanical treatment of the culprit lesion, not the time when TIMI 3 flow was (or was not) restored.
""" 
* procedureInformation.pciProcedure.firstDeviceActivation ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.firstDeviceActivation ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.firstDeviceActivation ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012993 and valueDateTime.exists())"

* procedureInformation.pciProcedure.patientCenteredReasonForDelayInPci 0..1 CREDSElementDefinition "Indicate the patient-centered reason for delay in performing the percutaneous coronary intervention (PCI), if needed."
* procedureInformation.pciProcedure.patientCenteredReasonForDelayInPci ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.patientCenteredReasonForDelayInPci ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.patientCenteredReasonForDelayInPci ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012993 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PatientCenteredReasonforDelay))"

* procedureInformation.pciProcedure.pciOperator 1..1 CREDSElementDefinition "The operator who is performing the PCI procedure"
* procedureInformation.pciProcedure.pciOperator ^mapping[+].identity = "FHIR"
* procedureInformation.pciProcedure.pciOperator ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.pciOperator ^mapping[=].map = "%Procedure.participant.where( function.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/PCIOperator) ).actor.resolve()"
* procedureInformation.pciProcedure.pciOperator ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.pciOperator ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.pciOperator ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner"

* procedureInformation.pciProcedure.arterialAccessSite 1..1 CREDSElementDefinition "Indicate the location of percutaneous entry for the procedure."
* procedureInformation.pciProcedure.arterialAccessSite ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.arterialAccessSite ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.arterialAccessSite ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014079 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/ArterialAccessSite))"

* procedureInformation.pciProcedure.mechanicalVentilatorSupport 1..1 CREDSElementDefinition "Indicate if the patient required mechanical ventricular support."
* procedureInformation.pciProcedure.mechanicalVentilatorSupport ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.mechanicalVentilatorSupport ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.mechanicalVentilatorSupport ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014009 and valueBoolean.exists())"

* procedureInformation.pciProcedure.mechanicalVentilatorSupportDevice 0..* CREDSElementDefinition "Indicate the mechanical ventricular support device used."
* procedureInformation.pciProcedure.mechanicalVentilatorSupportDevice ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.mechanicalVentilatorSupportDevice ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.mechanicalVentilatorSupportDevice ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100001278 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/VentricularSupportDeviceType))"

* procedureInformation.pciProcedure.pciProcedureMedicationCode 0..* CREDSElementDefinition "Medications administred intra-procedure"
* procedureInformation.pciProcedure.pciProcedureMedicationCode ^mapping[+].identity = "FHIR"
* procedureInformation.pciProcedure.pciProcedureMedicationCode ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.pciProcedureMedicationCode ^mapping[=].map = "MedicationStatement.where(effectiveDateTime >= %procedure.period.start and effectiveDateTime <= %procedure.period.end)"
* procedureInformation.pciProcedure.pciProcedureMedicationCode ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.pciProcedureMedicationCode ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.pciProcedureMedicationCode ^mapping[=].map = "MedicationStatement"

* procedureInformation.pciProcedure.lesionsAndDevices 1..1 BackboneElement "Information on the Lesions treated and Devices Used"

* procedureInformation.pciProcedure.lesionsAndDevices.lesionCounter 0..* CREDSElementDefinition "The lesion counter is used to distinguish between multiple lesions on which a PCI is attempted or performed."
* procedureInformation.pciProcedure.lesionsAndDevices.lesionCounter ^comment = """When specifying intracoronary devices, list all treated lesions in which the device was utilized.
The software-assigned lesion counter should start at one and be incremented by one for each lesion. The lesion counter is reset back to one for each new PCI lab visit.
At least one lesion must be specified for each PCI procedure.""" 
* procedureInformation.pciProcedure.lesionsAndDevices.lesionCounter ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.lesionCounter ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.lesionCounter ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142441 and valueQuantity.exists())"

//Note: This is a possible multi-code, Observation only holds one value.  Would need to put answers in .component
* procedureInformation.pciProcedure.lesionsAndDevices.nativeLesionSegmentNumber 0..* CREDSElementDefinition "Indicate the segment that the current lesion spans." 
* procedureInformation.pciProcedure.lesionsAndDevices.nativeLesionSegmentNumber ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.nativeLesionSegmentNumber ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.nativeLesionSegmentNumber ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100012984 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/LesionSegmentNumber))"

* procedureInformation.pciProcedure.lesionsAndDevices.culpritStenosis 1..1 CREDSElementDefinition "Indicate if the stenosis is considered to be responsible for the acute coronary syndrome."
* procedureInformation.pciProcedure.mechanicalVentilatorSupport ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.mechanicalVentilatorSupport ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.mechanicalVentilatorSupport ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=371895000 and valueBoolean.exists())"

* procedureInformation.pciProcedure.lesionsAndDevices.stenosisImmediatelyPriorToTreatment 0..* CREDSElementDefinition  "Indicate the percent diameter stenosis immediately prior to the treatment of this lesion."
* procedureInformation.pciProcedure.lesionsAndDevices.lesionCounter ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.lesionCounter ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.lesionCounter ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142442 and valueQuantity.exists())"

* procedureInformation.pciProcedure.lesionsAndDevices.chronicTotalOcclusion 1..1 CREDSElementDefinition "Indicate if the segment with 100% pre-procedure stenosis was presumed to be 100% occluded for at least 3 months previous to this procedure AND not related to a clinical event prompting (or leading to) this procedure."
* procedureInformation.pciProcedure.mechanicalVentilatorSupport ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.mechanicalVentilatorSupport ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.mechanicalVentilatorSupport ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100000290 and valueBoolean.exists())"

* procedureInformation.pciProcedure.lesionsAndDevices.timiFlowPreIntervention 0..* CREDSElementDefinition  "Indicate the pre-intervention TIMI flow."
* procedureInformation.pciProcedure.lesionsAndDevices.timiFlowPreIntervention ^comment = "If a lesion spans multiple segments with different TIMI flow, code the lowest TIMI flow within the entire lesion."
* procedureInformation.pciProcedure.lesionsAndDevices.timiFlowPreIntervention ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.timiFlowPreIntervention ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.timiFlowPreIntervention ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=112000000348 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/TIMIFlow))"

* procedureInformation.pciProcedure.lesionsAndDevices.previouslyTreatedLesion 0..1 CREDSElementDefinition "Indicate the date the lesion has been treated in a prior episode of care."
* procedureInformation.pciProcedure.lesionsAndDevices.previouslyTreatedLesion ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.previouslyTreatedLesion ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.previouslyTreatedLesion ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100013015 and valueDateTime.exists())"

* procedureInformation.pciProcedure.lesionsAndDevices.inStentThrombosis 0..1 CREDSElementDefinition "Indicate if the previously treated and stented lesion is being treated because of the presence of a thrombus in the stent."
* procedureInformation.pciProcedure.lesionsAndDevices.inStentThrombosis ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.inStentThrombosis ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.inStentThrombosis ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100013014 and valueBoolean.exists())"


* procedureInformation.pciProcedure.lesionsAndDevices.stentType  0..1 CREDSElementDefinition "Indicate the type of stent used in the previously treated lesion."
* procedureInformation.pciProcedure.lesionsAndDevices.stentType ^comment = """
 If a patient has multiple stents in the lesion code 'bioabsorbable' over either of the other two options when it is present.  
If a DES and BMS are present in the lesion, code 'DES'."""
* procedureInformation.pciProcedure.lesionsAndDevices.stentType ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.stentType ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.stentType ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100000856 and valueCodableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/StentType))"

* procedureInformation.pciProcedure.lesionsAndDevices.lesionInGraft 0..1 CREDSElementDefinition  "Indicated if the lesion is in a coronary artery bypass graft."
* procedureInformation.pciProcedure.lesionsAndDevices.lesionInGraft ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.lesionInGraft ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.lesionInGraft ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142443 and valueBoolean.exists())"

* procedureInformation.pciProcedure.lesionsAndDevices.typeOfCabgGraft  0..1 CREDSElementDefinition "Indicate in which type of bypass graft the lesion is located."
* procedureInformation.pciProcedure.lesionsAndDevices.typeOfCabgGraft ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.typeOfCabgGraft ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.typeOfCabgGraft ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100013028 and valueCodableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/CABGType))"
 
* procedureInformation.pciProcedure.lesionsAndDevices.locationInGraft 0..1 CREDSElementDefinition "Indicate the location of the most severe stenosis, if the lesion is in the graft."
* procedureInformation.pciProcedure.lesionsAndDevices.typeOfCabgGraft ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.typeOfCabgGraft ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.typeOfCabgGraft ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100013028 and valueCodableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/LocationInGraft))"

* procedureInformation.pciProcedure.lesionsAndDevices.navigateThroughGraftToNativeLesion 0..1 CREDSElementDefinition  "Indicate if treatment of the native artery lesion required navigating through a graft (to reach the lesion)."
* procedureInformation.pciProcedure.lesionsAndDevices.navigateThroughGraftToNativeLesion ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.navigateThroughGraftToNativeLesion ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.navigateThroughGraftToNativeLesion ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142348 and valueBoolean.exists())"

* procedureInformation.pciProcedure.lesionsAndDevices.lesionComplexity  0..1 CREDSElementDefinition  "Indicate the complexity of the lesion"
* procedureInformation.pciProcedure.lesionsAndDevices.lesionComplexity ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.lesionComplexity ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.lesionComplexity ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100000866 and valueCodableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/LesionComplexity))"


* procedureInformation.pciProcedure.lesionsAndDevices.lesionLength  0..1 CREDSElementDefinition  "Indicate the length of the treated lesion in millimeters."
* procedureInformation.pciProcedure.lesionsAndDevices.lesionLength ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.lesionLength ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.lesionLength ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100013030 and valueQuantity.exists())"

* procedureInformation.pciProcedure.lesionsAndDevices.severeCalcification  0..1 CREDSElementDefinition  "Indicate if there was severe calcification of the lesion."
* procedureInformation.pciProcedure.lesionsAndDevices.severeCalcification ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.severeCalcification ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.severeCalcification ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142350 and valueBoolean.exists())"

* procedureInformation.pciProcedure.lesionsAndDevices.guidewireAcrossLesion   0..1 CREDSElementDefinition "Indicate if a guidewire successfully crossed the lesion."
* procedureInformation.pciProcedure.lesionsAndDevices.guidewireAcrossLesion ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.guidewireAcrossLesion ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.guidewireAcrossLesion ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100000851 and valueBoolean.exists())"


* procedureInformation.pciProcedure.lesionsAndDevices.deviceDeployed  0..1 CREDSElementDefinition "Indicate if a device was deployed during the procedure."
* procedureInformation.pciProcedure.lesionsAndDevices.deviceDeployed ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.deviceDeployed ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.deviceDeployed ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142349 and valueBoolean.exists())"

* procedureInformation.pciProcedure.lesionsAndDevices.postInterventionStenosis  0..1 CREDSElementDefinition "Indicate the post-intervention percent stenosis for the treated lesion."
* procedureInformation.pciProcedure.lesionsAndDevices.postInterventionStenosis ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.postInterventionStenosis ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.postInterventionStenosis ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142461 and valueQuantity.exists())"

* procedureInformation.pciProcedure.lesionsAndDevices.postInterventionTimiFlow  0..1 CREDSElementDefinition "Indicate the post-intervention TIMI flow."
* procedureInformation.pciProcedure.lesionsAndDevices.postInterventionTimiFlow ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.lesionsAndDevices.postInterventionTimiFlow ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.lesionsAndDevices.postInterventionTimiFlow ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100013016 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/TIMIFlow))"

* procedureInformation.pciProcedure.intracoronaryDevices 1..1 BackboneElement "Devices used during the PCI procedure"

* procedureInformation.pciProcedure.intracoronaryDevices.device 0..1 CREDSElementDefinition "Indicate the devices utilized during the current procedure."
* procedureInformation.pciProcedure.intracoronaryDevices.device ^mapping[+].identity = "FHIR"
* procedureInformation.pciProcedure.intracoronaryDevices.device ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.intracoronaryDevices.device ^mapping[=].map = "Procedure.focalDevice.manipulated.resolve().memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/CardiacCatheter)"
* procedureInformation.pciProcedure.intracoronaryDevices.device ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.intracoronaryDevices.device ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.intracoronaryDevices.device ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-implantable-device"


//* procedureInformation.pciProcedure.intracoronaryDevices.associatedLesion  How to indicate multiple components?

* procedureInformation.pciProcedure.intraAndPostProcedureEvents 1..1 BackboneElement "Events occuring Intra and post-procedure"

* procedureInformation.pciProcedure.intraAndPostProcedureEvents.event 0..1 CREDSElementDefinition "Indicate the event that occurred between the procedure and the next procedure or discharge."
* procedureInformation.pciProcedure.intraAndPostProcedureEvents.event ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.intraAndPostProcedureEvents.event ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.intraAndPostProcedureEvents.event ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=1000142478 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/IntraAndPostEvents) and effectiveDateTime.exists())"

* procedureInformation.pciProcedure.intraAndPostProcedureEvents.significantCoronaryArteryDissection  0..1 CREDSElementDefinition "Indicate the post-intervention TIMI flow."
* procedureInformation.pciProcedure.intraAndPostProcedureEvents.significantCoronaryArteryDissection ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.intraAndPostProcedureEvents.significantCoronaryArteryDissection ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.intraAndPostProcedureEvents.significantCoronaryArteryDissection ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100000883 and valueBoolean.exists())"

* procedureInformation.pciProcedure.intraAndPostProcedureEvents.numberOfUnitsOfPrbcsTransfused 0..1 CREDSElementDefinition "Indicate the number of transfusion(s) of packed red blood cells."
* procedureInformation.pciProcedure.intraAndPostProcedureEvents.numberOfUnitsOfPrbcsTransfused ^mapping[+].identity = "Output"
* procedureInformation.pciProcedure.intraAndPostProcedureEvents.numberOfUnitsOfPrbcsTransfused ^mapping[=].language = #application/fhir
* procedureInformation.pciProcedure.intraAndPostProcedureEvents.numberOfUnitsOfPrbcsTransfused ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014031 and valueQuantity.exists()) and effectiveDateTime.exists()"

* discharge 1..1 BackboneElement "Discharge Information"

* discharge.interventionsThisHospitalization 0..1 CREDSElementDefinition "Indicate other interventions (percutaneous or surgical) that occurred during this hospitalization."
* discharge.interventionsThisHospitalization ^mapping[+].identity = "Output"
* discharge.interventionsThisHospitalization ^mapping[=].language = #application/fhir
* discharge.interventionsThisHospitalization ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100001284 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/InterventionTypes)"

* discharge.cabgStatus 0..1 CREDSElementDefinition "Indicate the status of the coronary artery bypass graft (CABG) surgery."
* discharge.cabgStatus ^mapping[+].identity = "Output"
* discharge.cabgStatus ^mapping[=].language = #application/fhir
* discharge.cabgStatus ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014080 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/CABGStatus)"

* discharge.cabgIndication 0..1 CREDSElementDefinition "Indicate the reason coronary artery bypass graft (CABG) surgery is being performed."
* discharge.cabgStatus ^mapping[+].identity = "Output"
* discharge.cabgStatus ^mapping[=].language = #application/fhir
* discharge.cabgStatus ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100001289 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/CABGIndication)"

* discharge.dischargeProvider 1..1 CREDSElementDefinition "Provider that discharged the patient"
* discharge.dischargeProvider ^mapping[+].identity = "FHIR"
* discharge.dischargeProvider ^mapping[=].language = #application/fhir
* discharge.dischargeProvider ^mapping[=].map = "Encounter.where(type.code.coding.code=58000006).participant.individual.resolve()"
* discharge.dischargeProvider ^mapping[+].identity = "Output"
* discharge.dischargeProvider ^mapping[=].language = #application/fhir
* discharge.dischargeProvider ^mapping[=].map = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner"
 
* discharge.transferredForCabg 0..1 CREDSElementDefinition "Indicate if the patient was transferred for the purpose of performing a coronary artery bypass graft."
* discharge.transferredForCabg ^mapping[+].identity = "Output"
* discharge.transferredForCabg ^mapping[=].language = #application/fhir
* discharge.transferredForCabg ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100001296 and valueBoolean.exists())"

* discharge.cabgPlannedAfterDischarge 0..1 CREDSElementDefinition "Indicate if the patient has a CABG planned after discharge."
* discharge.cabgPlannedAfterDischarge ^mapping[+].identity = "Output"
* discharge.cabgPlannedAfterDischarge ^mapping[=].language = #application/fhir
* discharge.cabgPlannedAfterDischarge ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=10001424792 and valueBoolean.exists())"

* discharge.cardiacRehabilitationReferral 0..1 CREDSElementDefinition "Indicate if there was written documentation of a referral for the patient (by the physician, nurse, or other personnel) to an outpatient cardiac rehabilitation program, or a documented medical or patient-centered reason why such a referral was not made."
* discharge.cardiacRehabilitationReferral ^mapping[+].identity = "Output"
* discharge.cardiacRehabilitationReferral ^mapping[=].language = #application/fhir
* discharge.cardiacRehabilitationReferral ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014067 and valueCodeableConcept.memberOf(http://hl7.org/fhir/us/fhir-registry-protocols-ig/ValueSet/CardiacRehabilitationReferral))"

* discharge.deathDuringTheProcedure 0..1 CREDSElementDefinition "Indicate if the patient expired during the procedure."
* discharge.deathDuringTheProcedure ^comment = """Make sure to only capture 'Death during the procedure' in the procedure appropriate registry. 
For example, if the patient had a CathPCI procedure and a TVT procedure in the same episode of care (hospitalization) but different cath lab visits and the death occurred during the TVT procedure.
Code 'Yes' only in the TVT Registry and not the CathPCI Registry.  If the CathPCI procedure and TVT procedure occurred during the same cath lab visit then code 'Yes' in both registries."""
* discharge.deathDuringTheProcedure ^mapping[+].identity = "Output"
* discharge.deathDuringTheProcedure ^mapping[=].language = #application/fhir
* discharge.deathDuringTheProcedure ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100014067 and valueBoolean.exists())"

* discharge.dischargeMedicationReconciliationCompleted 0..1 CREDSElementDefinition "Indicate if the medication reconciliation was completed as recommended by the Joint Commission's National Patient Safety Goals."
* discharge.dischargeMedicationReconciliationCompleted ^mapping[+].identity = "Output"
* discharge.dischargeMedicationReconciliationCompleted ^mapping[=].language = #application/fhir
* discharge.dischargeMedicationReconciliationCompleted ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100013084 and valueBoolean.exists())"

* discharge.dischargeMedicationsReconciled 0..* CREDSElementDefinition "Indicate the specific medication classes that were reconciled."
* discharge.dischargeMedicationsReconciled ^mapping[+].identity = "Output"
* discharge.dischargeMedicationsReconciled ^mapping[=].language = #application/fhir
* discharge.dischargeMedicationsReconciled ^mapping[=].map = "Observation.where(code.coding.system='http://hl7.org/fhir/us/fhir-registry-protocols-ig/CodeSystem/NCDRQuestionCodesCS' and code.coding.code=100013085 and valueBoolean.exists())"

