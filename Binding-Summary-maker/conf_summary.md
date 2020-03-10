## List all US Core Required and Must Support Elements



|Type|Profile|Element|isRequired|isMustSupport|
|---|---|---|---|---|
|Observation|US Core Pediatric BMI for Age Observation Profile|Observation|||
|Observation|US Core Pediatric BMI for Age Observation Profile|Observation.code|X||
|Observation|US Core Pediatric Weight for Height Observation Profile|Observation|||
|Observation|US Core Pediatric Weight for Height Observation Profile|Observation.code|X||
|AllergyIntolerance|US  Core AllergyIntolerance Profile|AllergyIntolerance|||
|AllergyIntolerance|US  Core AllergyIntolerance Profile|AllergyIntolerance.clinicalStatus||X|
|AllergyIntolerance|US  Core AllergyIntolerance Profile|AllergyIntolerance.verificationStatus||X|
|AllergyIntolerance|US  Core AllergyIntolerance Profile|AllergyIntolerance.code|X|X|
|AllergyIntolerance|US  Core AllergyIntolerance Profile|AllergyIntolerance.patient|X|X|
|Extension|US Core Birth Sex Extension|Extension|||
|Extension|US Core Birth Sex Extension|Extension.url|X||
|Extension|US Core Birth Sex Extension|Extension.valueCode|||
|CarePlan|US Core CarePlan Profile|CarePlan|||
|CarePlan|US Core CarePlan Profile|CarePlan.text|X|X|
|CarePlan|US Core CarePlan Profile|CarePlan.text.status|X|X|
|CarePlan|US Core CarePlan Profile|CarePlan.status|X|X|
|CarePlan|US Core CarePlan Profile|CarePlan.intent|X|X|
|CarePlan|US Core CarePlan Profile|CarePlan.category|X|X|
|CarePlan|US Core CarePlan Profile|CarePlan.category|X|X|
|CarePlan|US Core CarePlan Profile|CarePlan.subject|X|X|
|CareTeam|US Core CareTeam Profile|CareTeam|||
|CareTeam|US Core CareTeam Profile|CareTeam.status||X|
|CareTeam|US Core CareTeam Profile|CareTeam.subject|X|X|
|CareTeam|US Core CareTeam Profile|CareTeam.participant|X|X|
|CareTeam|US Core CareTeam Profile|CareTeam.participant.role|X|X|
|CareTeam|US Core CareTeam Profile|CareTeam.participant.member|X|X|
|Condition|US Core Condition Profile|Condition|||
|Condition|US Core Condition Profile|Condition.clinicalStatus||X|
|Condition|US Core Condition Profile|Condition.verificationStatus||X|
|Condition|US Core Condition Profile|Condition.category|X|X|
|Condition|US Core Condition Profile|Condition.code|X|X|
|Condition|US Core Condition Profile|Condition.subject|X|X|
|DiagnosticReport|US Core DiagnosticReport Profile for Laboratory Results Reporting|DiagnosticReport|||
|DiagnosticReport|US Core DiagnosticReport Profile for Laboratory Results Reporting|DiagnosticReport.status|X|X|
|DiagnosticReport|US Core DiagnosticReport Profile for Laboratory Results Reporting|DiagnosticReport.category|X|X|
|DiagnosticReport|US Core DiagnosticReport Profile for Laboratory Results Reporting|DiagnosticReport.category|X|X|
|DiagnosticReport|US Core DiagnosticReport Profile for Laboratory Results Reporting|DiagnosticReport.code|X|X|
|DiagnosticReport|US Core DiagnosticReport Profile for Laboratory Results Reporting|DiagnosticReport.subject|X|X|
|DiagnosticReport|US Core DiagnosticReport Profile for Laboratory Results Reporting|DiagnosticReport.effective[x]|X|X|
|DiagnosticReport|US Core DiagnosticReport Profile for Laboratory Results Reporting|DiagnosticReport.issued|X|X|
|DiagnosticReport|US Core DiagnosticReport Profile for Laboratory Results Reporting|DiagnosticReport.performer||X|
|DiagnosticReport|US Core DiagnosticReport Profile for Laboratory Results Reporting|DiagnosticReport.result||X|
|DiagnosticReport|US Core DiagnosticReport Profile for Laboratory Results Reporting|DiagnosticReport.media||X|
|DiagnosticReport|US Core DiagnosticReport Profile for Laboratory Results Reporting|DiagnosticReport.presentedForm||X|
|DiagnosticReport|US Core DiagnosticReport Profile for Report and Note exchange|DiagnosticReport|||
|DiagnosticReport|US Core DiagnosticReport Profile for Report and Note exchange|DiagnosticReport.status|X|X|
|DiagnosticReport|US Core DiagnosticReport Profile for Report and Note exchange|DiagnosticReport.category|X|X|
|DiagnosticReport|US Core DiagnosticReport Profile for Report and Note exchange|DiagnosticReport.code|X|X|
|DiagnosticReport|US Core DiagnosticReport Profile for Report and Note exchange|DiagnosticReport.subject|X|X|
|DiagnosticReport|US Core DiagnosticReport Profile for Report and Note exchange|DiagnosticReport.encounter||X|
|DiagnosticReport|US Core DiagnosticReport Profile for Report and Note exchange|DiagnosticReport.effective[x]|X|X|
|DiagnosticReport|US Core DiagnosticReport Profile for Report and Note exchange|DiagnosticReport.issued||X|
|DiagnosticReport|US Core DiagnosticReport Profile for Report and Note exchange|DiagnosticReport.performer||X|
|DiagnosticReport|US Core DiagnosticReport Profile for Report and Note exchange|DiagnosticReport.media||X|
|DiagnosticReport|US Core DiagnosticReport Profile for Report and Note exchange|DiagnosticReport.presentedForm||X|
|Extension|US Core Direct email Extension|Extension|||
|Extension|US Core Direct email Extension|Extension.url|X||
|Extension|US Core Direct email Extension|Extension.valueBoolean|||
|DocumentReference|US Core DocumentReference Profile|DocumentReference|||
|DocumentReference|US Core DocumentReference Profile|DocumentReference.identifier||X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.status|X|X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.type|X|X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.category|X|X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.subject|X|X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.date||X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.author||X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.custodian||X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.content|X|X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.content.attachment|X|X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.content.attachment.contentType|X|X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.content.attachment.data||X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.content.attachment.url||X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.content.format||X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.context||X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.context.encounter||X|
|DocumentReference|US Core DocumentReference Profile|DocumentReference.context.period||X|
|Encounter|US Core Encounter Profile|Encounter|||
|Encounter|US Core Encounter Profile|Encounter.identifier||X|
|Encounter|US Core Encounter Profile|Encounter.identifier.system|X|X|
|Encounter|US Core Encounter Profile|Encounter.identifier.value|X|X|
|Encounter|US Core Encounter Profile|Encounter.status|X|X|
|Encounter|US Core Encounter Profile|Encounter.class|X|X|
|Encounter|US Core Encounter Profile|Encounter.type|X|X|
|Encounter|US Core Encounter Profile|Encounter.subject|X|X|
|Encounter|US Core Encounter Profile|Encounter.participant||X|
|Encounter|US Core Encounter Profile|Encounter.participant.type||X|
|Encounter|US Core Encounter Profile|Encounter.participant.period||X|
|Encounter|US Core Encounter Profile|Encounter.participant.individual||X|
|Encounter|US Core Encounter Profile|Encounter.period||X|
|Encounter|US Core Encounter Profile|Encounter.reasonCode||X|
|Encounter|US Core Encounter Profile|Encounter.hospitalization||X|
|Encounter|US Core Encounter Profile|Encounter.hospitalization.dischargeDisposition||X|
|Encounter|US Core Encounter Profile|Encounter.location||X|
|Encounter|US Core Encounter Profile|Encounter.location.location|X|X|
|Extension|US Core Ethnicity Extension|Extension|||
|Extension|US Core Ethnicity Extension|Extension.extension|||
|Extension|US Core Ethnicity Extension|Extension.extension||X|
|Extension|US Core Ethnicity Extension|Extension.extension.url|X||
|Extension|US Core Ethnicity Extension|Extension.extension.valueCoding|X||
|Extension|US Core Ethnicity Extension|Extension.extension|||
|Extension|US Core Ethnicity Extension|Extension.extension.url|X||
|Extension|US Core Ethnicity Extension|Extension.extension.valueCoding|X||
|Extension|US Core Ethnicity Extension|Extension.extension|X|X|
|Extension|US Core Ethnicity Extension|Extension.extension.url|X||
|Extension|US Core Ethnicity Extension|Extension.extension.valueString|X||
|Extension|US Core Ethnicity Extension|Extension.url|X||
|Goal|US Core Goal Profile|Goal|||
|Goal|US Core Goal Profile|Goal.lifecycleStatus|X|X|
|Goal|US Core Goal Profile|Goal.description|X|X|
|Goal|US Core Goal Profile|Goal.subject|X|X|
|Goal|US Core Goal Profile|Goal.target||X|
|Immunization|US Core Immunization Profile|Immunization|||
|Immunization|US Core Immunization Profile|Immunization.status|X|X|
|Immunization|US Core Immunization Profile|Immunization.statusReason||X|
|Immunization|US Core Immunization Profile|Immunization.vaccineCode|X|X|
|Immunization|US Core Immunization Profile|Immunization.patient|X|X|
|Immunization|US Core Immunization Profile|Immunization.occurrence[x]|X|X|
|Immunization|US Core Immunization Profile|Immunization.primarySource|X|X|
|Device|US Core Implantable Device Profile|Device|||
|Device|US Core Implantable Device Profile|Device.udiCarrier||X|
|Device|US Core Implantable Device Profile|Device.udiCarrier.deviceIdentifier|X|X|
|Device|US Core Implantable Device Profile|Device.udiCarrier.carrierAIDC||X|
|Device|US Core Implantable Device Profile|Device.udiCarrier.carrierHRF||X|
|Device|US Core Implantable Device Profile|Device.distinctIdentifier||X|
|Device|US Core Implantable Device Profile|Device.manufactureDate||X|
|Device|US Core Implantable Device Profile|Device.expirationDate||X|
|Device|US Core Implantable Device Profile|Device.lotNumber||X|
|Device|US Core Implantable Device Profile|Device.serialNumber||X|
|Device|US Core Implantable Device Profile|Device.type|X|X|
|Device|US Core Implantable Device Profile|Device.patient|X|X|
|Location|US Core Location Profile|Location|||
|Location|US Core Location Profile|Location.status||X|
|Location|US Core Location Profile|Location.name|X|X|
|Location|US Core Location Profile|Location.telecom||X|
|Location|US Core Location Profile|Location.address||X|
|Location|US Core Location Profile|Location.address.line||X|
|Location|US Core Location Profile|Location.address.city||X|
|Location|US Core Location Profile|Location.address.state||X|
|Location|US Core Location Profile|Location.address.postalCode||X|
|Location|US Core Location Profile|Location.managingOrganization||X|
|Medication|US Core Medication Profile|Medication|||
|Medication|US Core Medication Profile|Medication.code|X|X|
|MedicationRequest|US Core MedicationRequest Profile|MedicationRequest|||
|MedicationRequest|US Core MedicationRequest Profile|MedicationRequest.status|X|X|
|MedicationRequest|US Core MedicationRequest Profile|MedicationRequest.intent|X|X|
|MedicationRequest|US Core MedicationRequest Profile|MedicationRequest.reported[x]||X|
|MedicationRequest|US Core MedicationRequest Profile|MedicationRequest.medication[x]|X|X|
|MedicationRequest|US Core MedicationRequest Profile|MedicationRequest.subject|X|X|
|MedicationRequest|US Core MedicationRequest Profile|MedicationRequest.encounter||X|
|MedicationRequest|US Core MedicationRequest Profile|MedicationRequest.authoredOn|X|X|
|MedicationRequest|US Core MedicationRequest Profile|MedicationRequest.requester|X|X|
|MedicationRequest|US Core MedicationRequest Profile|MedicationRequest.dosageInstruction||X|
|MedicationRequest|US Core MedicationRequest Profile|MedicationRequest.dosageInstruction.text||X|
|Observation|US Core Laboratory Result Observation Profile|Observation|||
|Observation|US Core Laboratory Result Observation Profile|Observation.status|X|X|
|Observation|US Core Laboratory Result Observation Profile|Observation.category|X|X|
|Observation|US Core Laboratory Result Observation Profile|Observation.category|X|X|
|Observation|US Core Laboratory Result Observation Profile|Observation.code|X|X|
|Observation|US Core Laboratory Result Observation Profile|Observation.subject|X|X|
|Observation|US Core Laboratory Result Observation Profile|Observation.effective[x]||X|
|Observation|US Core Laboratory Result Observation Profile|Observation.value[x]||X|
|Observation|US Core Laboratory Result Observation Profile|Observation.dataAbsentReason||X|
|Organization|US Core Organization Profile|Organization|||
|Organization|US Core Organization Profile|Organization.identifier||X|
|Organization|US Core Organization Profile|Organization.identifier.system||X|
|Organization|US Core Organization Profile|Organization.identifier.value||X|
|Organization|US Core Organization Profile|Organization.identifier||X|
|Organization|US Core Organization Profile|Organization.identifier||X|
|Organization|US Core Organization Profile|Organization.active|X|X|
|Organization|US Core Organization Profile|Organization.name|X|X|
|Organization|US Core Organization Profile|Organization.telecom||X|
|Organization|US Core Organization Profile|Organization.address||X|
|Organization|US Core Organization Profile|Organization.address.line||X|
|Organization|US Core Organization Profile|Organization.address.city||X|
|Organization|US Core Organization Profile|Organization.address.state||X|
|Organization|US Core Organization Profile|Organization.address.postalCode||X|
|Organization|US Core Organization Profile|Organization.address.country||X|
|Organization|US Core Organization Profile|Organization.endpoint||X|
|Patient|US Core Patient Profile|Patient|||
|Patient|US Core Patient Profile|Patient.extension|||
|Patient|US Core Patient Profile|Patient.extension||X|
|Patient|US Core Patient Profile|Patient.extension||X|
|Patient|US Core Patient Profile|Patient.extension||X|
|Patient|US Core Patient Profile|Patient.identifier|X|X|
|Patient|US Core Patient Profile|Patient.identifier.system|X|X|
|Patient|US Core Patient Profile|Patient.identifier.value|X|X|
|Patient|US Core Patient Profile|Patient.name|X|X|
|Patient|US Core Patient Profile|Patient.name.family||X|
|Patient|US Core Patient Profile|Patient.name.given||X|
|Patient|US Core Patient Profile|Patient.telecom||X|
|Patient|US Core Patient Profile|Patient.telecom.system|X|X|
|Patient|US Core Patient Profile|Patient.telecom.value|X|X|
|Patient|US Core Patient Profile|Patient.telecom.use||X|
|Patient|US Core Patient Profile|Patient.gender|X|X|
|Patient|US Core Patient Profile|Patient.birthDate||X|
|Patient|US Core Patient Profile|Patient.address||X|
|Patient|US Core Patient Profile|Patient.address.line||X|
|Patient|US Core Patient Profile|Patient.address.city||X|
|Patient|US Core Patient Profile|Patient.address.state||X|
|Patient|US Core Patient Profile|Patient.address.postalCode||X|
|Patient|US Core Patient Profile|Patient.address.period||X|
|Patient|US Core Patient Profile|Patient.communication||X|
|Patient|US Core Patient Profile|Patient.communication.language|X|X|
|Practitioner|US Core Practitioner Profile|Practitioner|||
|Practitioner|US Core Practitioner Profile|Practitioner.identifier|X|X|
|Practitioner|US Core Practitioner Profile|Practitioner.identifier.system|X|X|
|Practitioner|US Core Practitioner Profile|Practitioner.identifier.value|X|X|
|Practitioner|US Core Practitioner Profile|Practitioner.identifier||X|
|Practitioner|US Core Practitioner Profile|Practitioner.name|X|X|
|Practitioner|US Core Practitioner Profile|Practitioner.name.family|X|X|
|PractitionerRole|US Core PractitionerRole Profile|PractitionerRole|||
|PractitionerRole|US Core PractitionerRole Profile|PractitionerRole.practitioner|X|X|
|PractitionerRole|US Core PractitionerRole Profile|PractitionerRole.organization|X|X|
|PractitionerRole|US Core PractitionerRole Profile|PractitionerRole.code||X|
|PractitionerRole|US Core PractitionerRole Profile|PractitionerRole.specialty||X|
|PractitionerRole|US Core PractitionerRole Profile|PractitionerRole.location||X|
|PractitionerRole|US Core PractitionerRole Profile|PractitionerRole.telecom||X|
|PractitionerRole|US Core PractitionerRole Profile|PractitionerRole.telecom.system|X|X|
|PractitionerRole|US Core PractitionerRole Profile|PractitionerRole.telecom.value|X|X|
|PractitionerRole|US Core PractitionerRole Profile|PractitionerRole.endpoint||X|
|Procedure|US Core Procedure Profile|Procedure|||
|Procedure|US Core Procedure Profile|Procedure.status|X|X|
|Procedure|US Core Procedure Profile|Procedure.code|X|X|
|Procedure|US Core Procedure Profile|Procedure.subject|X|X|
|Procedure|US Core Procedure Profile|Procedure.performed[x]|X|X|
|Provenance|US Core Provenance Profile|Provenance|||
|Provenance|US Core Provenance Profile|Provenance.target|X|X|
|Provenance|US Core Provenance Profile|Provenance.recorded|X|X|
|Provenance|US Core Provenance Profile|Provenance.agent|X|X|
|Provenance|US Core Provenance Profile|Provenance.agent.type||X|
|Provenance|US Core Provenance Profile|Provenance.agent.who|X|X|
|Provenance|US Core Provenance Profile|Provenance.agent.onBehalfOf||X|
|Provenance|US Core Provenance Profile|Provenance.agent||X|
|Provenance|US Core Provenance Profile|Provenance.agent.type|X|X|
|Provenance|US Core Provenance Profile|Provenance.agent.who|X||
|Provenance|US Core Provenance Profile|Provenance.agent.onBehalfOf|||
|Provenance|US Core Provenance Profile|Provenance.agent||X|
|Provenance|US Core Provenance Profile|Provenance.agent.type|X|X|
|Provenance|US Core Provenance Profile|Provenance.agent.who|X||
|Provenance|US Core Provenance Profile|Provenance.agent.onBehalfOf|||
|Observation|US Core Pulse Oximetry Profile|Observation|||
|Observation|US Core Pulse Oximetry Profile|Observation.code|X|X|
|Observation|US Core Pulse Oximetry Profile|Observation.code.coding||X|
|Observation|US Core Pulse Oximetry Profile|Observation.code.coding|X||
|Observation|US Core Pulse Oximetry Profile|Observation.code.coding.system|X||
|Observation|US Core Pulse Oximetry Profile|Observation.code.coding.code|X||
|Observation|US Core Pulse Oximetry Profile|Observation.code.coding|X|X|
|Observation|US Core Pulse Oximetry Profile|Observation.code.coding.system|X|X|
|Observation|US Core Pulse Oximetry Profile|Observation.code.coding.code|X|X|
|Observation|US Core Pulse Oximetry Profile|Observation.component||X|
|Observation|US Core Pulse Oximetry Profile|Observation.component.code|X|X|
|Observation|US Core Pulse Oximetry Profile|Observation.component||X|
|Observation|US Core Pulse Oximetry Profile|Observation.component.code|X|X|
|Observation|US Core Pulse Oximetry Profile|Observation.component||X|
|Observation|US Core Pulse Oximetry Profile|Observation.component.code|X|X|
|Extension|US Core Race Extension|Extension|||
|Extension|US Core Race Extension|Extension.extension|||
|Extension|US Core Race Extension|Extension.extension||X|
|Extension|US Core Race Extension|Extension.extension.url|X||
|Extension|US Core Race Extension|Extension.extension.valueCoding|X||
|Extension|US Core Race Extension|Extension.extension|||
|Extension|US Core Race Extension|Extension.extension.url|X||
|Extension|US Core Race Extension|Extension.extension.valueCoding|X||
|Extension|US Core Race Extension|Extension.extension|X|X|
|Extension|US Core Race Extension|Extension.extension.url|X||
|Extension|US Core Race Extension|Extension.extension.valueString|X||
|Extension|US Core Race Extension|Extension.url|X||
|Observation|US Core Smoking Status Observation Profile|Observation|||
|Observation|US Core Smoking Status Observation Profile|Observation.status|X|X|
|Observation|US Core Smoking Status Observation Profile|Observation.code|X|X|
|Observation|US Core Smoking Status Observation Profile|Observation.subject|X|X|
|Observation|US Core Smoking Status Observation Profile|Observation.issued|X|X|
