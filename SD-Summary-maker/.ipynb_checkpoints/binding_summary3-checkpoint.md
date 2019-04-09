### All Required Bindings for Coded Elements without an 'other' or 'unknown' code:
1. **[RelatedArtifact.type](https://build.fhir.org/relatedartifact-definitions.html#RelatedArtifact.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/related-artifact-type|4.0.0
    (
     depends-on, 
     justification, 
     predecessor, 
     composed-of, 
     successor, 
     derived-from, 
     documentation, 
     citation)
1. **[ParameterDefinition.type](https://build.fhir.org/parameterdefinition-definitions.html#ParameterDefinition.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/all-types|4.0.0
    (
     Any, 
     Type, 
     Identifier, 
     Expression, 
     Extension, 
     Period, 
     Quantity, 
     Timing, 
     Address, 
     integer, 
     RelatedArtifact, 
     SimpleQuantity, 
     Range, 
     Signature, 
     Meta, 
     ProdCharacteristic, 
     time, 
     base64Binary, 
     ElementDefinition, 
     instant)
1. **[DeviceUseStatement.status](https://build.fhir.org/deviceusestatement-definitions.html#DeviceUseStatement.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/device-statement-status|4.0.0
    (
     stopped, 
     completed, 
     active, 
     on-hold, 
     intended, 
     entered-in-error)
1. **[ElementDefinition.constraint.severity](https://build.fhir.org/elementdefinition-definitions.html#ElementDefinition.constraint.severity)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/constraint-severity|4.0.0
    (
     warning, 
     error)
1. **[ExampleScenario.actor.type](https://build.fhir.org/examplescenario-definitions.html#ExampleScenario.actor.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/examplescenario-actor-type|4.0.0
    (
     entity, 
     person)
1. **[ExampleScenario.instance.resourceType](https://build.fhir.org/examplescenario-definitions.html#ExampleScenario.instance.resourceType)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/resource-types|4.0.0
    (
     Basic, 
     DeviceDefinition, 
     Group, 
     SubstanceNucleicAcid, 
     PractitionerRole, 
     Resource, 
     CommunicationRequest, 
     AllergyIntolerance, 
     ClaimResponse, 
     VisionPrescription, 
     CodeSystem, 
     Binary, 
     Communication, 
     Device, 
     Linkage, 
     BiologicallyDerivedProduct, 
     SubstanceSourceMaterial, 
     InsurancePlan, 
     DomainResource, 
     Patient)
1. **[Appointment.status](https://build.fhir.org/appointment-definitions.html#Appointment.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/appointmentstatus|4.0.0
    (
     checked-in, 
     proposed, 
     cancelled, 
     arrived, 
     waitlist, 
     entered-in-error, 
     pending, 
     booked, 
     fulfilled, 
     noshow)
1. **[Appointment.participant.status](https://build.fhir.org/appointment-definitions.html#Appointment.participant.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/participationstatus|4.0.0
    (
     needs-action, 
     accepted, 
     tentative, 
     declined)
1. **[RelatedArtifact.type](https://build.fhir.org/relatedartifact-definitions.html#RelatedArtifact.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/related-artifact-type|4.0.0
    (
     depends-on, 
     justification, 
     predecessor, 
     composed-of, 
     successor, 
     derived-from, 
     documentation, 
     citation)
1. **[List.status](https://build.fhir.org/list-definitions.html#List.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/list-status|4.0.0
    (
     current, 
     retired, 
     entered-in-error)
1. **[List.mode](https://build.fhir.org/list-definitions.html#List.mode)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/list-mode|4.0.0
    (
     changes, 
     working, 
     snapshot)
1. **[VerificationResult.status](https://build.fhir.org/verificationresult-definitions.html#VerificationResult.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/verificationresult-status|4.0.0
    (
     req-revalid, 
     in-process, 
     validated, 
     reval-fail, 
     attested, 
     val-fail)
1. **[ElementDefinition.extension.value[x]](https://build.fhir.org/elementdefinition-definitions.html#ElementDefinition.extension.value[x])**
    - 1..1
    - http://hl7.org/fhir/ValueSet/ucum-units|4.0.0
1. **[ElementDefinition.slicing.discriminator.type](https://build.fhir.org/elementdefinition-definitions.html#ElementDefinition.slicing.discriminator.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/discriminator-type|4.0.0
    (
     profile, 
     pattern, 
     exists, 
     type, 
     value)
1. **[ElementDefinition.slicing.rules](https://build.fhir.org/elementdefinition-definitions.html#ElementDefinition.slicing.rules)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/resource-slicing-rules|4.0.0
    (
     openAtEnd, 
     closed, 
     open)
1. **[ElementDefinition.constraint.severity](https://build.fhir.org/elementdefinition-definitions.html#ElementDefinition.constraint.severity)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/constraint-severity|4.0.0
    (
     warning, 
     error)
1. **[ElementDefinition.binding.strength](https://build.fhir.org/elementdefinition-definitions.html#ElementDefinition.binding.strength)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/binding-strength|4.0.0
    (
     extensible, 
     preferred, 
     required, 
     example)
1. **[ElementDefinition.slicing.discriminator.type](https://build.fhir.org/elementdefinition-definitions.html#ElementDefinition.slicing.discriminator.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/discriminator-type|4.0.0
    (
     profile, 
     pattern, 
     exists, 
     type, 
     value)
1. **[PlanDefinition.action.condition.kind](https://build.fhir.org/plandefinition-definitions.html#PlanDefinition.action.condition.kind)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-condition-kind|4.0.0
    (
     start, 
     applicability, 
     stop)
1. **[PlanDefinition.action.relatedAction.relationship](https://build.fhir.org/plandefinition-definitions.html#PlanDefinition.action.relatedAction.relationship)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-relationship-type|4.0.0
    (
     concurrent-with-end, 
     after-end, 
     after-start, 
     before, 
     before-end, 
     concurrent, 
     after, 
     concurrent-with-start, 
     before-start)
1. **[PlanDefinition.action.participant.type](https://build.fhir.org/plandefinition-definitions.html#PlanDefinition.action.participant.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-participant-type|4.0.0
    (
     patient, 
     practitioner, 
     device, 
     related-person)
1. **[Composition.status](https://build.fhir.org/composition-definitions.html#Composition.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/composition-status|4.0.0
    (
     preliminary, 
     amended, 
     entered-in-error, 
     final)
1. **[Composition.attester.mode](https://build.fhir.org/composition-definitions.html#Composition.attester.mode)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/composition-attestation-mode|4.0.0
    (
     official, 
     professional, 
     personal, 
     legal)
1. **[Composition.relatesTo.code](https://build.fhir.org/composition-definitions.html#Composition.relatesTo.code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/document-relationship-type|4.0.0
    (
     transforms, 
     appends, 
     signs, 
     replaces)
1. **[Contributor.type](https://build.fhir.org/contributor-definitions.html#Contributor.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/contributor-type|4.0.0
    (
     reviewer, 
     editor, 
     author, 
     endorser)
1. **[DocumentManifest.status](https://build.fhir.org/documentmanifest-definitions.html#DocumentManifest.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/document-reference-status|4.0.0
    (
     entered-in-error, 
     superseded, 
     current)
1. **[Claim.status](https://build.fhir.org/claim-definitions.html#Claim.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[Claim.use](https://build.fhir.org/claim-definitions.html#Claim.use)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/claim-use|4.0.0
    (
     claim, 
     predetermination, 
     preauthorization)
1. **[DeviceMetric.category](https://build.fhir.org/devicemetric-definitions.html#DeviceMetric.category)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/metric-category|4.0.0
    (
     unspecified, 
     setting, 
     measurement, 
     calculation)
1. **[ElementDefinition.slicing.discriminator.type](https://build.fhir.org/elementdefinition-definitions.html#ElementDefinition.slicing.discriminator.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/discriminator-type|4.0.0
    (
     profile, 
     pattern, 
     exists, 
     type, 
     value)
1. **[ElementDefinition.slicing.rules](https://build.fhir.org/elementdefinition-definitions.html#ElementDefinition.slicing.rules)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/resource-slicing-rules|4.0.0
    (
     openAtEnd, 
     closed, 
     open)
1. **[ElementDefinition.constraint.severity](https://build.fhir.org/elementdefinition-definitions.html#ElementDefinition.constraint.severity)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/constraint-severity|4.0.0
    (
     warning, 
     error)
1. **[ElementDefinition.binding.strength](https://build.fhir.org/elementdefinition-definitions.html#ElementDefinition.binding.strength)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/binding-strength|4.0.0
    (
     extensible, 
     preferred, 
     required, 
     example)
1. **[TriggerDefinition.type](https://build.fhir.org/triggerdefinition-definitions.html#TriggerDefinition.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/trigger-type|4.0.0
    (
     data-access-ended, 
     data-changed, 
     data-accessed, 
     data-added, 
     named-event, 
     data-modified, 
     periodic, 
     data-removed)
1. **[ServiceRequest.intent](https://build.fhir.org/servicerequest-definitions.html#ServiceRequest.intent)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/request-intent|4.0.0
    (
     proposal, 
     option, 
     plan, 
     original-order, 
     order, 
     instance-order, 
     directive, 
     filler-order, 
     reflex-order)
1. **[CarePlan.intent](https://build.fhir.org/careplan-definitions.html#CarePlan.intent)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/care-plan-intent|4.0.0
    (
     proposal, 
     option, 
     plan, 
     order)
1. **[Linkage.item.type](https://build.fhir.org/linkage-definitions.html#Linkage.item.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/linkage-type|4.0.0
    (
     alternate, 
     source, 
     historical)
1. **[CoverageEligibilityResponse.status](https://build.fhir.org/coverageeligibilityresponse-definitions.html#CoverageEligibilityResponse.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[CoverageEligibilityResponse.purpose](https://build.fhir.org/coverageeligibilityresponse-definitions.html#CoverageEligibilityResponse.purpose)**
    - 1..*
    - http://hl7.org/fhir/ValueSet/eligibilityresponse-purpose|4.0.0
    (
     auth-requirements, 
     validation, 
     discovery, 
     benefits)
1. **[CoverageEligibilityResponse.outcome](https://build.fhir.org/coverageeligibilityresponse-definitions.html#CoverageEligibilityResponse.outcome)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/remittance-outcome|4.0.0
    (
     queued, 
     partial, 
     complete, 
     error)
1. **[QuestionnaireResponse.status](https://build.fhir.org/questionnaireresponse-definitions.html#QuestionnaireResponse.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/questionnaire-answers-status|4.0.0
    (
     amended, 
     entered-in-error, 
     stopped, 
     completed, 
     in-progress)
1. **[ActivityDefinition.participant.type](https://build.fhir.org/activitydefinition-definitions.html#ActivityDefinition.participant.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-participant-type|4.0.0
    (
     patient, 
     practitioner, 
     device, 
     related-person)
1. **[CodeSystem.content](https://build.fhir.org/codesystem-definitions.html#CodeSystem.content)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/codesystem-content-mode|4.0.0
    (
     complete, 
     fragment, 
     not-present, 
     example, 
     supplement)
1. **[CodeSystem.filter.operator](https://build.fhir.org/codesystem-definitions.html#CodeSystem.filter.operator)**
    - 1..*
    - http://hl7.org/fhir/ValueSet/filter-operator|4.0.0
    (
     is-a, 
     in, 
     not-in, 
     regex, 
     generalizes, 
     exists, 
     =, 
     descendent-of, 
     is-not-a)
1. **[CodeSystem.property.type](https://build.fhir.org/codesystem-definitions.html#CodeSystem.property.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/concept-property-type|4.0.0
    (
     boolean, 
     decimal, 
     dateTime, 
     Coding, 
     string, 
     integer, 
     code)
1. **[Observation.code](https://build.fhir.org/observation-definitions.html#Observation.code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/ldlcholesterol-codes|4.0.0
    (
     18262-6, 
     13457-7)
1. **[EpisodeOfCare.status](https://build.fhir.org/episodeofcare-definitions.html#EpisodeOfCare.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/episode-of-care-status|4.0.0
    (
     waitlist, 
     finished, 
     entered-in-error, 
     onhold, 
     active, 
     planned, 
     cancelled)
1. **[EpisodeOfCare.statusHistory.status](https://build.fhir.org/episodeofcare-definitions.html#EpisodeOfCare.statusHistory.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/episode-of-care-status|4.0.0
    (
     waitlist, 
     finished, 
     entered-in-error, 
     onhold, 
     active, 
     planned, 
     cancelled)
1. **[DeviceRequest.intent](https://build.fhir.org/devicerequest-definitions.html#DeviceRequest.intent)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/request-intent|4.0.0
    (
     proposal, 
     option, 
     plan, 
     original-order, 
     order, 
     instance-order, 
     directive, 
     filler-order, 
     reflex-order)
1. **[CapabilityStatement.kind](https://build.fhir.org/capabilitystatement-definitions.html#CapabilityStatement.kind)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/capability-statement-kind|4.0.0
    (
     instance, 
     requirements, 
     capability)
1. **[CapabilityStatement.fhirVersion](https://build.fhir.org/capabilitystatement-definitions.html#CapabilityStatement.fhirVersion)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/FHIR-version|4.0.0
    (
     4.0.0, 
     0.5.0, 
     0.4.0, 
     3.3.0, 
     1.8.0, 
     3.0.1, 
     3.0.0, 
     0.06, 
     0.05, 
     0.0.81, 
     1.0.2, 
     0.0.80, 
     1.0.1, 
     1.1.0, 
     1.0.0, 
     0.0.82, 
     0.01, 
     1.6.0, 
     0.11, 
     1.4.0)
1. **[CapabilityStatement.format](https://build.fhir.org/capabilitystatement-definitions.html#CapabilityStatement.format)**
    - 1..*
    - http://hl7.org/fhir/ValueSet/mimetypes|4.0.0
1. **[CapabilityStatement.rest.mode](https://build.fhir.org/capabilitystatement-definitions.html#CapabilityStatement.rest.mode)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/restful-capability-mode|4.0.0
    (
     client, 
     server)
1. **[CapabilityStatement.rest.resource.type](https://build.fhir.org/capabilitystatement-definitions.html#CapabilityStatement.rest.resource.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/resource-types|4.0.0
    (
     Basic, 
     DeviceDefinition, 
     Group, 
     SubstanceNucleicAcid, 
     PractitionerRole, 
     Resource, 
     CommunicationRequest, 
     AllergyIntolerance, 
     ClaimResponse, 
     VisionPrescription, 
     CodeSystem, 
     Binary, 
     Communication, 
     Device, 
     Linkage, 
     BiologicallyDerivedProduct, 
     SubstanceSourceMaterial, 
     InsurancePlan, 
     DomainResource, 
     Patient)
1. **[CapabilityStatement.rest.resource.interaction.code](https://build.fhir.org/capabilitystatement-definitions.html#CapabilityStatement.rest.resource.interaction.code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/type-restful-interaction|4.0.0
    (
     delete, 
     search-type, 
     update, 
     history-instance, 
     vread, 
     patch, 
     create, 
     history-type, 
     read)
1. **[CapabilityStatement.rest.resource.searchParam.type](https://build.fhir.org/capabilitystatement-definitions.html#CapabilityStatement.rest.resource.searchParam.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/search-param-type|4.0.0
    (
     reference, 
     quantity, 
     string, 
     number, 
     special, 
     composite, 
     token, 
     date, 
     uri)
1. **[CapabilityStatement.rest.interaction.code](https://build.fhir.org/capabilitystatement-definitions.html#CapabilityStatement.rest.interaction.code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/system-restful-interaction|4.0.0
    (
     transaction, 
     search-system, 
     history-system, 
     batch)
1. **[CapabilityStatement.messaging.supportedMessage.mode](https://build.fhir.org/capabilitystatement-definitions.html#CapabilityStatement.messaging.supportedMessage.mode)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/event-capability-mode|4.0.0
    (
     sender, 
     receiver)
1. **[CapabilityStatement.document.mode](https://build.fhir.org/capabilitystatement-definitions.html#CapabilityStatement.document.mode)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/document-mode|4.0.0
    (
     producer, 
     consumer)
1. **[Endpoint.status](https://build.fhir.org/endpoint-definitions.html#Endpoint.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/endpoint-status|4.0.0
    (
     error, 
     off, 
     suspended, 
     entered-in-error, 
     active, 
     test)
1. **[GuidanceResponse.status](https://build.fhir.org/guidanceresponse-definitions.html#GuidanceResponse.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/guidance-response-status|4.0.0
    (
     data-required, 
     data-requested, 
     success, 
     failure, 
     in-progress, 
     entered-in-error)
1. **[CatalogEntry.relatedEntry.relationtype](https://build.fhir.org/catalogentry-definitions.html#CatalogEntry.relatedEntry.relationtype)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/relation-type|4.0.0
    (
     is-replaced-by, 
     triggers)
1. **[Group.type](https://build.fhir.org/group-definitions.html#Group.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/group-type|4.0.0
    (
     substance, 
     animal, 
     medication, 
     device, 
     practitioner, 
     person)
1. **[Contributor.type](https://build.fhir.org/contributor-definitions.html#Contributor.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/contributor-type|4.0.0
    (
     reviewer, 
     editor, 
     author, 
     endorser)
1. **[ActivityDefinition.participant.type](https://build.fhir.org/activitydefinition-definitions.html#ActivityDefinition.participant.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-participant-type|4.0.0
    (
     patient, 
     practitioner, 
     device, 
     related-person)
1. **[ChargeItemDefinition.propertyGroup.priceComponent.type](https://build.fhir.org/chargeitemdefinition-definitions.html#ChargeItemDefinition.propertyGroup.priceComponent.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/invoice-priceComponentType|4.0.0
    (
     base, 
     deduction, 
     discount, 
     surcharge, 
     tax, 
     informational)
1. **[Questionnaire.item.type](https://build.fhir.org/questionnaire-definitions.html#Questionnaire.item.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/item-type|4.0.0
    (
     dateTime, 
     question, 
     time, 
     text, 
     choice, 
     group, 
     boolean, 
     open-choice, 
     integer, 
     date, 
     decimal, 
     url, 
     quantity, 
     display, 
     reference, 
     string, 
     attachment)
1. **[Questionnaire.item.enableWhen.operator](https://build.fhir.org/questionnaire-definitions.html#Questionnaire.item.enableWhen.operator)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/questionnaire-enable-operator|4.0.0
    (
     &gt;=, 
     =, 
     &lt;=, 
     &lt;, 
     !=, 
     exists, 
     &gt;)
1. **[Group.type](https://build.fhir.org/group-definitions.html#Group.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/group-type|4.0.0
    (
     substance, 
     animal, 
     medication, 
     device, 
     practitioner, 
     person)
1. **[ResearchStudy.status](https://build.fhir.org/researchstudy-definitions.html#ResearchStudy.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/research-study-status|4.0.0
    (
     completed, 
     closed-to-accrual, 
     temporarily-closed-to-accrual, 
     approved, 
     withdrawn, 
     active, 
     closed-to-accrual-and-intervention, 
     temporarily-closed-to-accrual-and-intervention, 
     in-review, 
     disapproved, 
     administratively-completed)
1. **[TestReport.status](https://build.fhir.org/testreport-definitions.html#TestReport.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/report-status-codes|4.0.0
    (
     in-progress, 
     waiting, 
     completed, 
     entered-in-error, 
     stopped)
1. **[TestReport.result](https://build.fhir.org/testreport-definitions.html#TestReport.result)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/report-result-codes|4.0.0
    (
     pass, 
     fail, 
     pending)
1. **[TestReport.participant.type](https://build.fhir.org/testreport-definitions.html#TestReport.participant.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/report-participant-type|4.0.0
    (
     client, 
     test-engine, 
     server)
1. **[TestReport.setup.action.operation.result](https://build.fhir.org/testreport-definitions.html#TestReport.setup.action.operation.result)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/report-action-result-codes|4.0.0
    (
     fail, 
     warning, 
     error, 
     pass, 
     skip)
1. **[TestReport.setup.action.assert.result](https://build.fhir.org/testreport-definitions.html#TestReport.setup.action.assert.result)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/report-action-result-codes|4.0.0
    (
     fail, 
     warning, 
     error, 
     pass, 
     skip)
1. **[MeasureReport.status](https://build.fhir.org/measurereport-definitions.html#MeasureReport.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/measure-report-status|4.0.0
    (
     complete, 
     error, 
     pending)
1. **[MeasureReport.type](https://build.fhir.org/measurereport-definitions.html#MeasureReport.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/measure-report-type|4.0.0
    (
     summary, 
     data-collection, 
     individual, 
     subject-list)
1. **[DataRequirement.type](https://build.fhir.org/datarequirement-definitions.html#DataRequirement.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/all-types|4.0.0
    (
     Any, 
     Type, 
     Identifier, 
     Expression, 
     Extension, 
     Period, 
     Quantity, 
     Timing, 
     Address, 
     integer, 
     RelatedArtifact, 
     SimpleQuantity, 
     Range, 
     Signature, 
     Meta, 
     ProdCharacteristic, 
     time, 
     base64Binary, 
     ElementDefinition, 
     instant)
1. **[PlanDefinition.action.condition.kind](https://build.fhir.org/plandefinition-definitions.html#PlanDefinition.action.condition.kind)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-condition-kind|4.0.0
    (
     start, 
     applicability, 
     stop)
1. **[PlanDefinition.action.relatedAction.relationship](https://build.fhir.org/plandefinition-definitions.html#PlanDefinition.action.relatedAction.relationship)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-relationship-type|4.0.0
    (
     concurrent-with-end, 
     after-end, 
     after-start, 
     before, 
     before-end, 
     concurrent, 
     after, 
     concurrent-with-start, 
     before-start)
1. **[PlanDefinition.action.participant.type](https://build.fhir.org/plandefinition-definitions.html#PlanDefinition.action.participant.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-participant-type|4.0.0
    (
     patient, 
     practitioner, 
     device, 
     related-person)
1. **[DataRequirement.type](https://build.fhir.org/datarequirement-definitions.html#DataRequirement.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/all-types|4.0.0
    (
     Any, 
     Type, 
     Identifier, 
     Expression, 
     Extension, 
     Period, 
     Quantity, 
     Timing, 
     Address, 
     integer, 
     RelatedArtifact, 
     SimpleQuantity, 
     Range, 
     Signature, 
     Meta, 
     ProdCharacteristic, 
     time, 
     base64Binary, 
     ElementDefinition, 
     instant)
1. **[DataRequirement.sort.direction](https://build.fhir.org/datarequirement-definitions.html#DataRequirement.sort.direction)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/sort-direction|4.0.0
    (
     ascending, 
     descending)
1. **[Provenance.entity.role](https://build.fhir.org/provenance-definitions.html#Provenance.entity.role)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/provenance-entity-role|4.0.0
    (
     quotation, 
     derivation, 
     source, 
     removal, 
     revision)
1. **[Binary.contentType](https://build.fhir.org/binary-definitions.html#Binary.contentType)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/mimetypes|4.0.0
1. **[NamingSystem.kind](https://build.fhir.org/namingsystem-definitions.html#NamingSystem.kind)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/namingsystem-type|4.0.0
    (
     identifier, 
     root, 
     codesystem)
1. **[VisionPrescription.status](https://build.fhir.org/visionprescription-definitions.html#VisionPrescription.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[VisionPrescription.lensSpecification.eye](https://build.fhir.org/visionprescription-definitions.html#VisionPrescription.lensSpecification.eye)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/vision-eye-codes|4.0.0
    (
     right, 
     left)
1. **[VisionPrescription.lensSpecification.prism.base](https://build.fhir.org/visionprescription-definitions.html#VisionPrescription.lensSpecification.prism.base)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/vision-base-codes|4.0.0
    (
     down, 
     out, 
     in, 
     up)
1. **[Flag.status](https://build.fhir.org/flag-definitions.html#Flag.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/flag-status|4.0.0
    (
     inactive, 
     entered-in-error, 
     active)
1. **[ParameterDefinition.use](https://build.fhir.org/parameterdefinition-definitions.html#ParameterDefinition.use)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/operation-parameter-use|4.0.0
    (
     in, 
     out)
1. **[ParameterDefinition.type](https://build.fhir.org/parameterdefinition-definitions.html#ParameterDefinition.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/all-types|4.0.0
    (
     Any, 
     Type, 
     Identifier, 
     Expression, 
     Extension, 
     Period, 
     Quantity, 
     Timing, 
     Address, 
     integer, 
     RelatedArtifact, 
     SimpleQuantity, 
     Range, 
     Signature, 
     Meta, 
     ProdCharacteristic, 
     time, 
     base64Binary, 
     ElementDefinition, 
     instant)
1. **[ExplanationOfBenefit.status](https://build.fhir.org/explanationofbenefit-definitions.html#ExplanationOfBenefit.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/explanationofbenefit-status|4.0.0
    (
     cancelled, 
     active, 
     entered-in-error, 
     draft)
1. **[ExplanationOfBenefit.use](https://build.fhir.org/explanationofbenefit-definitions.html#ExplanationOfBenefit.use)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/claim-use|4.0.0
    (
     claim, 
     predetermination, 
     preauthorization)
1. **[ExplanationOfBenefit.outcome](https://build.fhir.org/explanationofbenefit-definitions.html#ExplanationOfBenefit.outcome)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/remittance-outcome|4.0.0
    (
     queued, 
     partial, 
     complete, 
     error)
1. **[Patient.link.type](https://build.fhir.org/patient-definitions.html#Patient.link.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/link-type|4.0.0
    (
     refer, 
     replaced-by, 
     replaces, 
     seealso)
1. **[ElementDefinition.binding.strength](https://build.fhir.org/elementdefinition-definitions.html#ElementDefinition.binding.strength)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/binding-strength|4.0.0
    (
     extensible, 
     preferred, 
     required, 
     example)
1. **[PlanDefinition.action.condition.kind](https://build.fhir.org/plandefinition-definitions.html#PlanDefinition.action.condition.kind)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-condition-kind|4.0.0
    (
     start, 
     applicability, 
     stop)
1. **[PlanDefinition.action.relatedAction.relationship](https://build.fhir.org/plandefinition-definitions.html#PlanDefinition.action.relatedAction.relationship)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-relationship-type|4.0.0
    (
     concurrent-with-end, 
     after-end, 
     after-start, 
     before, 
     before-end, 
     concurrent, 
     after, 
     concurrent-with-start, 
     before-start)
1. **[PlanDefinition.action.participant.type](https://build.fhir.org/plandefinition-definitions.html#PlanDefinition.action.participant.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-participant-type|4.0.0
    (
     patient, 
     practitioner, 
     device, 
     related-person)
1. **[ServiceRequest.intent](https://build.fhir.org/servicerequest-definitions.html#ServiceRequest.intent)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/request-intent|4.0.0
    (
     proposal, 
     option, 
     plan, 
     original-order, 
     order, 
     instance-order, 
     directive, 
     filler-order, 
     reflex-order)
1. **[Composition.status](https://build.fhir.org/composition-definitions.html#Composition.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/composition-status|4.0.0
    (
     preliminary, 
     amended, 
     entered-in-error, 
     final)
1. **[Composition.attester.mode](https://build.fhir.org/composition-definitions.html#Composition.attester.mode)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/composition-attestation-mode|4.0.0
    (
     official, 
     professional, 
     personal, 
     legal)
1. **[Composition.relatesTo.code](https://build.fhir.org/composition-definitions.html#Composition.relatesTo.code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/document-relationship-type|4.0.0
    (
     transforms, 
     appends, 
     signs, 
     replaces)
1. **[DataRequirement.sort.direction](https://build.fhir.org/datarequirement-definitions.html#DataRequirement.sort.direction)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/sort-direction|4.0.0
    (
     ascending, 
     descending)
1. **[FamilyMemberHistory.status](https://build.fhir.org/familymemberhistory-definitions.html#FamilyMemberHistory.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/history-status|4.0.0
    (
     entered-in-error, 
     health-unknown, 
     completed, 
     partial)
1. **[ResearchElementDefinition.type](https://build.fhir.org/researchelementdefinition-definitions.html#ResearchElementDefinition.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/research-element-type|4.0.0
    (
     outcome, 
     population, 
     exposure)
1. **[OperationDefinition.kind](https://build.fhir.org/operationdefinition-definitions.html#OperationDefinition.kind)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/operation-kind|4.0.0
    (
     query, 
     operation)
1. **[OperationDefinition.parameter.use](https://build.fhir.org/operationdefinition-definitions.html#OperationDefinition.parameter.use)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/operation-parameter-use|4.0.0
    (
     in, 
     out)
1. **[OperationDefinition.parameter.binding.strength](https://build.fhir.org/operationdefinition-definitions.html#OperationDefinition.parameter.binding.strength)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/binding-strength|4.0.0
    (
     extensible, 
     preferred, 
     required, 
     example)
1. **[ValueSet.compose.include.filter.op](https://build.fhir.org/valueset-definitions.html#ValueSet.compose.include.filter.op)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/filter-operator|4.0.0
    (
     is-a, 
     in, 
     not-in, 
     regex, 
     generalizes, 
     exists, 
     =, 
     descendent-of, 
     is-not-a)
1. **[GraphDefinition.start](https://build.fhir.org/graphdefinition-definitions.html#GraphDefinition.start)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/resource-types|4.0.0
    (
     Basic, 
     DeviceDefinition, 
     Group, 
     SubstanceNucleicAcid, 
     PractitionerRole, 
     Resource, 
     CommunicationRequest, 
     AllergyIntolerance, 
     ClaimResponse, 
     VisionPrescription, 
     CodeSystem, 
     Binary, 
     Communication, 
     Device, 
     Linkage, 
     BiologicallyDerivedProduct, 
     SubstanceSourceMaterial, 
     InsurancePlan, 
     DomainResource, 
     Patient)
1. **[GraphDefinition.link.target.type](https://build.fhir.org/graphdefinition-definitions.html#GraphDefinition.link.target.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/resource-types|4.0.0
    (
     Basic, 
     DeviceDefinition, 
     Group, 
     SubstanceNucleicAcid, 
     PractitionerRole, 
     Resource, 
     CommunicationRequest, 
     AllergyIntolerance, 
     ClaimResponse, 
     VisionPrescription, 
     CodeSystem, 
     Binary, 
     Communication, 
     Device, 
     Linkage, 
     BiologicallyDerivedProduct, 
     SubstanceSourceMaterial, 
     InsurancePlan, 
     DomainResource, 
     Patient)
1. **[GraphDefinition.link.target.compartment.use](https://build.fhir.org/graphdefinition-definitions.html#GraphDefinition.link.target.compartment.use)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/graph-compartment-use|4.0.0
    (
     requirement, 
     condition)
1. **[GraphDefinition.link.target.compartment.code](https://build.fhir.org/graphdefinition-definitions.html#GraphDefinition.link.target.compartment.code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/compartment-type|4.0.0
    (
     RelatedPerson, 
     Patient, 
     Practitioner, 
     Encounter, 
     Device)
1. **[GraphDefinition.link.target.compartment.rule](https://build.fhir.org/graphdefinition-definitions.html#GraphDefinition.link.target.compartment.rule)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/graph-compartment-rule|4.0.0
    (
     custom, 
     different, 
     identical, 
     matching)
1. **[Observation.value[x].code](https://build.fhir.org/observation-definitions.html#Observation.value[x].code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/ucum-bodyweight|4.0.0
1. **[AppointmentResponse.participantStatus](https://build.fhir.org/appointmentresponse-definitions.html#AppointmentResponse.participantStatus)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/participationstatus|4.0.0
    (
     needs-action, 
     accepted, 
     tentative, 
     declined)
1. **[Extension.value[x]](https://build.fhir.org/extension-definitions.html#Extension.value[x])**
    - 1..1
    - http://hl7.org/fhir/ValueSet/ucum-units|4.0.0
1. **[RequestGroup.intent](https://build.fhir.org/requestgroup-definitions.html#RequestGroup.intent)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/request-intent|4.0.0
    (
     proposal, 
     option, 
     plan, 
     original-order, 
     order, 
     instance-order, 
     directive, 
     filler-order, 
     reflex-order)
1. **[RequestGroup.action.condition.kind](https://build.fhir.org/requestgroup-definitions.html#RequestGroup.action.condition.kind)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-condition-kind|4.0.0
    (
     start, 
     applicability, 
     stop)
1. **[RequestGroup.action.relatedAction.relationship](https://build.fhir.org/requestgroup-definitions.html#RequestGroup.action.relatedAction.relationship)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-relationship-type|4.0.0
    (
     concurrent-with-end, 
     after-end, 
     after-start, 
     before, 
     before-end, 
     concurrent, 
     after, 
     concurrent-with-start, 
     before-start)
1. **[MessageHeader.response.code](https://build.fhir.org/messageheader-definitions.html#MessageHeader.response.code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/response-code|4.0.0
    (
     transient-error, 
     ok, 
     fatal-error)
1. **[Observation.value[x].code](https://build.fhir.org/observation-definitions.html#Observation.value[x].code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/ucum-bodytemp|4.0.0
1. **[Goal.lifecycleStatus](https://build.fhir.org/goal-definitions.html#Goal.lifecycleStatus)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/goal-status|4.0.0
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
1. **[Immunization.status](https://build.fhir.org/immunization-definitions.html#Immunization.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/immunization-status|4.0.0
    (
     completed, 
     not-done, 
     entered-in-error)
1. **[ValueSet.compose.include.filter.op](https://build.fhir.org/valueset-definitions.html#ValueSet.compose.include.filter.op)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/filter-operator|4.0.0
    (
     is-a, 
     in, 
     not-in, 
     regex, 
     generalizes, 
     exists, 
     =, 
     descendent-of, 
     is-not-a)
1. **[ClaimResponse.status](https://build.fhir.org/claimresponse-definitions.html#ClaimResponse.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[ClaimResponse.use](https://build.fhir.org/claimresponse-definitions.html#ClaimResponse.use)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/claim-use|4.0.0
    (
     claim, 
     predetermination, 
     preauthorization)
1. **[ClaimResponse.outcome](https://build.fhir.org/claimresponse-definitions.html#ClaimResponse.outcome)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/remittance-outcome|4.0.0
    (
     queued, 
     partial, 
     complete, 
     error)
1. **[Contract.contentDefinition.publicationStatus](https://build.fhir.org/contract-definitions.html#Contract.contentDefinition.publicationStatus)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/contract-publicationstatus|4.0.0
    (
     revoked, 
     appended, 
     terminated, 
     entered-in-error, 
     rejected, 
     policy, 
     executed, 
     cancelled, 
     amended, 
     offered, 
     renewed, 
     disputed, 
     executable, 
     resolved, 
     negotiable)
1. **[TerminologyCapabilities.kind](https://build.fhir.org/terminologycapabilities-definitions.html#TerminologyCapabilities.kind)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/capability-statement-kind|4.0.0
    (
     instance, 
     requirements, 
     capability)
1. **[SpecimenDefinition.typeTested.preference](https://build.fhir.org/specimendefinition-definitions.html#SpecimenDefinition.typeTested.preference)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/specimen-contained-preference|4.0.0
    (
     alternate, 
     preferred)
1. **[ConceptMap.group.element.target.equivalence](https://build.fhir.org/conceptmap-definitions.html#ConceptMap.group.element.target.equivalence)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/concept-map-equivalence|4.0.0
    (
     subsumes, 
     disjoint, 
     unmatched, 
     equivalent, 
     inexact, 
     relatedto, 
     specializes, 
     narrower, 
     equal, 
     wider)
1. **[ConceptMap.group.unmapped.mode](https://build.fhir.org/conceptmap-definitions.html#ConceptMap.group.unmapped.mode)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/conceptmap-unmapped-mode|4.0.0
    (
     other-map, 
     provided, 
     fixed)
1. **[Invoice.status](https://build.fhir.org/invoice-definitions.html#Invoice.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/invoice-status|4.0.0
    (
     issued, 
     draft, 
     balanced, 
     cancelled, 
     entered-in-error)
1. **[Invoice.lineItem.priceComponent.type](https://build.fhir.org/invoice-definitions.html#Invoice.lineItem.priceComponent.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/invoice-priceComponentType|4.0.0
    (
     base, 
     deduction, 
     discount, 
     surcharge, 
     tax, 
     informational)
1. **[StructureDefinition.kind](https://build.fhir.org/structuredefinition-definitions.html#StructureDefinition.kind)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/structure-definition-kind|4.0.0
    (
     resource, 
     logical, 
     primitive-type, 
     complex-type)
1. **[StructureDefinition.context.type](https://build.fhir.org/structuredefinition-definitions.html#StructureDefinition.context.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/extension-context-type|4.0.0
    (
     fhirpath, 
     element, 
     extension)
1. **[PaymentNotice.status](https://build.fhir.org/paymentnotice-definitions.html#PaymentNotice.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[GuidanceResponse.status](https://build.fhir.org/guidanceresponse-definitions.html#GuidanceResponse.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/guidance-response-status|4.0.0
    (
     data-required, 
     data-requested, 
     success, 
     failure, 
     in-progress, 
     entered-in-error)
1. **[RequestGroup.intent](https://build.fhir.org/requestgroup-definitions.html#RequestGroup.intent)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/request-intent|4.0.0
    (
     proposal, 
     option, 
     plan, 
     original-order, 
     order, 
     instance-order, 
     directive, 
     filler-order, 
     reflex-order)
1. **[RequestGroup.action.condition.kind](https://build.fhir.org/requestgroup-definitions.html#RequestGroup.action.condition.kind)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-condition-kind|4.0.0
    (
     start, 
     applicability, 
     stop)
1. **[RequestGroup.action.relatedAction.relationship](https://build.fhir.org/requestgroup-definitions.html#RequestGroup.action.relatedAction.relationship)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-relationship-type|4.0.0
    (
     concurrent-with-end, 
     after-end, 
     after-start, 
     before, 
     before-end, 
     concurrent, 
     after, 
     concurrent-with-start, 
     before-start)
1. **[Group.type](https://build.fhir.org/group-definitions.html#Group.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/group-type|4.0.0
    (
     substance, 
     animal, 
     medication, 
     device, 
     practitioner, 
     person)
1. **[FamilyMemberHistory.status](https://build.fhir.org/familymemberhistory-definitions.html#FamilyMemberHistory.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/history-status|4.0.0
    (
     entered-in-error, 
     health-unknown, 
     completed, 
     partial)
1. **[Composition.status](https://build.fhir.org/composition-definitions.html#Composition.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/composition-status|4.0.0
    (
     preliminary, 
     amended, 
     entered-in-error, 
     final)
1. **[Composition.attester.mode](https://build.fhir.org/composition-definitions.html#Composition.attester.mode)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/composition-attestation-mode|4.0.0
    (
     official, 
     professional, 
     personal, 
     legal)
1. **[Composition.relatesTo.code](https://build.fhir.org/composition-definitions.html#Composition.relatesTo.code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/document-relationship-type|4.0.0
    (
     transforms, 
     appends, 
     signs, 
     replaces)
1. **[Narrative.status](https://build.fhir.org/narrative-definitions.html#Narrative.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/narrative-status|4.0.0
    (
     generated, 
     additional, 
     extensions, 
     empty)
1. **[Observation.value[x].code](https://build.fhir.org/observation-definitions.html#Observation.value[x].code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/ucum-bodylength|4.0.0
1. **[Bundle.type](https://build.fhir.org/bundle-definitions.html#Bundle.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/bundle-type|4.0.0
    (
     document, 
     message, 
     transaction, 
     batch-response, 
     searchset, 
     history, 
     batch, 
     transaction-response, 
     collection)
1. **[Bundle.entry.request.method](https://build.fhir.org/bundle-definitions.html#Bundle.entry.request.method)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/http-verb|4.0.0
    (
     PUT, 
     POST, 
     GET, 
     HEAD, 
     DELETE, 
     PATCH)
1. **[MessageDefinition.focus.code](https://build.fhir.org/messagedefinition-definitions.html#MessageDefinition.focus.code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/resource-types|4.0.0
    (
     Basic, 
     DeviceDefinition, 
     Group, 
     SubstanceNucleicAcid, 
     PractitionerRole, 
     Resource, 
     CommunicationRequest, 
     AllergyIntolerance, 
     ClaimResponse, 
     VisionPrescription, 
     CodeSystem, 
     Binary, 
     Communication, 
     Device, 
     Linkage, 
     BiologicallyDerivedProduct, 
     SubstanceSourceMaterial, 
     InsurancePlan, 
     DomainResource, 
     Patient)
1. **[ImplementationGuide.fhirVersion](https://build.fhir.org/implementationguide-definitions.html#ImplementationGuide.fhirVersion)**
    - 1..*
    - http://hl7.org/fhir/ValueSet/FHIR-version|4.0.0
    (
     4.0.0, 
     0.5.0, 
     0.4.0, 
     3.3.0, 
     1.8.0, 
     3.0.1, 
     3.0.0, 
     0.06, 
     0.05, 
     0.0.81, 
     1.0.2, 
     0.0.80, 
     1.0.1, 
     1.1.0, 
     1.0.0, 
     0.0.82, 
     0.01, 
     1.6.0, 
     0.11, 
     1.4.0)
1. **[ImplementationGuide.global.type](https://build.fhir.org/implementationguide-definitions.html#ImplementationGuide.global.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/resource-types|4.0.0
    (
     Basic, 
     DeviceDefinition, 
     Group, 
     SubstanceNucleicAcid, 
     PractitionerRole, 
     Resource, 
     CommunicationRequest, 
     AllergyIntolerance, 
     ClaimResponse, 
     VisionPrescription, 
     CodeSystem, 
     Binary, 
     Communication, 
     Device, 
     Linkage, 
     BiologicallyDerivedProduct, 
     SubstanceSourceMaterial, 
     InsurancePlan, 
     DomainResource, 
     Patient)
1. **[ImplementationGuide.definition.page.generation](https://build.fhir.org/implementationguide-definitions.html#ImplementationGuide.definition.page.generation)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/guide-page-generation|4.0.0
    (
     generated, 
     html, 
     markdown, 
     xml)
1. **[ImplementationGuide.definition.parameter.code](https://build.fhir.org/implementationguide-definitions.html#ImplementationGuide.definition.parameter.code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/guide-parameter-code|4.0.0
    (
     apply, 
     expansion-parameter, 
     generate-json, 
     generate-xml, 
     path-pages, 
     generate-turtle, 
     rule-broken-links, 
     path-resource, 
     html-template, 
     path-tx-cache)
1. **[NutritionOrder.intent](https://build.fhir.org/nutritionorder-definitions.html#NutritionOrder.intent)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/request-intent|4.0.0
    (
     proposal, 
     option, 
     plan, 
     original-order, 
     order, 
     instance-order, 
     directive, 
     filler-order, 
     reflex-order)
1. **[CoverageEligibilityRequest.status](https://build.fhir.org/coverageeligibilityrequest-definitions.html#CoverageEligibilityRequest.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[CoverageEligibilityRequest.purpose](https://build.fhir.org/coverageeligibilityrequest-definitions.html#CoverageEligibilityRequest.purpose)**
    - 1..*
    - http://hl7.org/fhir/ValueSet/eligibilityrequest-purpose|4.0.0
    (
     discovery, 
     validation, 
     auth-requirements, 
     benefits)
1. **[CodeSystem.content](https://build.fhir.org/codesystem-definitions.html#CodeSystem.content)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/codesystem-content-mode|4.0.0
    (
     complete, 
     fragment, 
     not-present, 
     example, 
     supplement)
1. **[CodeSystem.filter.operator](https://build.fhir.org/codesystem-definitions.html#CodeSystem.filter.operator)**
    - 1..*
    - http://hl7.org/fhir/ValueSet/filter-operator|4.0.0
    (
     is-a, 
     in, 
     not-in, 
     regex, 
     generalizes, 
     exists, 
     =, 
     descendent-of, 
     is-not-a)
1. **[CodeSystem.property.type](https://build.fhir.org/codesystem-definitions.html#CodeSystem.property.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/concept-property-type|4.0.0
    (
     boolean, 
     decimal, 
     dateTime, 
     Coding, 
     string, 
     integer, 
     code)
1. **[MedicationRequest.intent](https://build.fhir.org/medicationrequest-definitions.html#MedicationRequest.intent)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/medicationrequest-intent|4.0.0
    (
     filler-order, 
     original-order, 
     proposal, 
     reflex-order, 
     plan, 
     order, 
     instance-order, 
     option)
1. **[ElementDefinition.slicing.rules](https://build.fhir.org/elementdefinition-definitions.html#ElementDefinition.slicing.rules)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/resource-slicing-rules|4.0.0
    (
     openAtEnd, 
     closed, 
     open)
1. **[Provenance.entity.role](https://build.fhir.org/provenance-definitions.html#Provenance.entity.role)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/provenance-entity-role|4.0.0
    (
     quotation, 
     derivation, 
     source, 
     removal, 
     revision)
1. **[Slot.status](https://build.fhir.org/slot-definitions.html#Slot.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/slotstatus|4.0.0
    (
     free, 
     busy, 
     busy-unavailable, 
     busy-tentative, 
     entered-in-error)
1. **[CompartmentDefinition.code](https://build.fhir.org/compartmentdefinition-definitions.html#CompartmentDefinition.code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/compartment-type|4.0.0
    (
     RelatedPerson, 
     Patient, 
     Practitioner, 
     Encounter, 
     Device)
1. **[CompartmentDefinition.resource.code](https://build.fhir.org/compartmentdefinition-definitions.html#CompartmentDefinition.resource.code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/resource-types|4.0.0
    (
     Basic, 
     DeviceDefinition, 
     Group, 
     SubstanceNucleicAcid, 
     PractitionerRole, 
     Resource, 
     CommunicationRequest, 
     AllergyIntolerance, 
     ClaimResponse, 
     VisionPrescription, 
     CodeSystem, 
     Binary, 
     Communication, 
     Device, 
     Linkage, 
     BiologicallyDerivedProduct, 
     SubstanceSourceMaterial, 
     InsurancePlan, 
     DomainResource, 
     Patient)
1. **[Coverage.status](https://build.fhir.org/coverage-definitions.html#Coverage.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[PaymentReconciliation.status](https://build.fhir.org/paymentreconciliation-definitions.html#PaymentReconciliation.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[Questionnaire.item.type](https://build.fhir.org/questionnaire-definitions.html#Questionnaire.item.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/item-type|4.0.0
    (
     dateTime, 
     question, 
     time, 
     text, 
     choice, 
     group, 
     boolean, 
     open-choice, 
     integer, 
     date, 
     decimal, 
     url, 
     quantity, 
     display, 
     reference, 
     string, 
     attachment)
1. **[Questionnaire.item.enableWhen.operator](https://build.fhir.org/questionnaire-definitions.html#Questionnaire.item.enableWhen.operator)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/questionnaire-enable-operator|4.0.0
    (
     &gt;=, 
     =, 
     &lt;=, 
     &lt;, 
     !=, 
     exists, 
     &gt;)
1. **[TriggerDefinition.type](https://build.fhir.org/triggerdefinition-definitions.html#TriggerDefinition.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/trigger-type|4.0.0
    (
     data-access-ended, 
     data-changed, 
     data-accessed, 
     data-added, 
     named-event, 
     data-modified, 
     periodic, 
     data-removed)
1. **[ImmunizationEvaluation.status](https://build.fhir.org/immunizationevaluation-definitions.html#ImmunizationEvaluation.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/immunization-evaluation-status|4.0.0
    (
     completed, 
     entered-in-error)
1. **[SearchParameter.base](https://build.fhir.org/searchparameter-definitions.html#SearchParameter.base)**
    - 1..*
    - http://hl7.org/fhir/ValueSet/resource-types|4.0.0
    (
     Basic, 
     DeviceDefinition, 
     Group, 
     SubstanceNucleicAcid, 
     PractitionerRole, 
     Resource, 
     CommunicationRequest, 
     AllergyIntolerance, 
     ClaimResponse, 
     VisionPrescription, 
     CodeSystem, 
     Binary, 
     Communication, 
     Device, 
     Linkage, 
     BiologicallyDerivedProduct, 
     SubstanceSourceMaterial, 
     InsurancePlan, 
     DomainResource, 
     Patient)
1. **[SearchParameter.type](https://build.fhir.org/searchparameter-definitions.html#SearchParameter.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/search-param-type|4.0.0
    (
     reference, 
     quantity, 
     string, 
     number, 
     special, 
     composite, 
     token, 
     date, 
     uri)
1. **[Narrative.status](https://build.fhir.org/narrative-definitions.html#Narrative.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/narrative-status|4.0.0
    (
     generated, 
     additional, 
     extensions, 
     empty)
1. **[PlanDefinition.action.condition.kind](https://build.fhir.org/plandefinition-definitions.html#PlanDefinition.action.condition.kind)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-condition-kind|4.0.0
    (
     start, 
     applicability, 
     stop)
1. **[PlanDefinition.action.relatedAction.relationship](https://build.fhir.org/plandefinition-definitions.html#PlanDefinition.action.relatedAction.relationship)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-relationship-type|4.0.0
    (
     concurrent-with-end, 
     after-end, 
     after-start, 
     before, 
     before-end, 
     concurrent, 
     after, 
     concurrent-with-start, 
     before-start)
1. **[PlanDefinition.action.participant.type](https://build.fhir.org/plandefinition-definitions.html#PlanDefinition.action.participant.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/action-participant-type|4.0.0
    (
     patient, 
     practitioner, 
     device, 
     related-person)
1. **[ResearchSubject.status](https://build.fhir.org/researchsubject-definitions.html#ResearchSubject.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/research-subject-status|4.0.0
    (
     pending-on-study, 
     screening, 
     withdrawn, 
     potential-candidate, 
     eligible, 
     on-study, 
     candidate, 
     not-registered, 
     on-study-intervention, 
     ineligible, 
     on-study-observation, 
     off-study, 
     follow-up)
1. **[ClinicalImpression.status](https://build.fhir.org/clinicalimpression-definitions.html#ClinicalImpression.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/clinicalimpression-status|4.0.0
    (
     completed, 
     entered-in-error, 
     in-progress)
1. **[Subscription.status](https://build.fhir.org/subscription-definitions.html#Subscription.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/subscription-status|4.0.0
    (
     off, 
     requested, 
     error, 
     active)
1. **[Subscription.channel.type](https://build.fhir.org/subscription-definitions.html#Subscription.channel.type)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/subscription-channel-type|4.0.0
    (
     websocket, 
     sms, 
     message, 
     email, 
     rest-hook)
1. **[Provenance.entity.role](https://build.fhir.org/provenance-definitions.html#Provenance.entity.role)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/provenance-entity-role|4.0.0
    (
     quotation, 
     derivation, 
     source, 
     removal, 
     revision)
1. **[Consent.status](https://build.fhir.org/consent-definitions.html#Consent.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/consent-state-codes|4.0.0
    (
     proposed, 
     rejected, 
     inactive, 
     active, 
     draft, 
     entered-in-error)
1. **[Consent.provision.data.meaning](https://build.fhir.org/consent-definitions.html#Consent.provision.data.meaning)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/consent-data-meaning|4.0.0
    (
     dependents, 
     related, 
     instance, 
     authoredby)
1. **[ParameterDefinition.use](https://build.fhir.org/parameterdefinition-definitions.html#ParameterDefinition.use)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/operation-parameter-use|4.0.0
    (
     in, 
     out)
1. **[StructureMap.structure.mode](https://build.fhir.org/structuremap-definitions.html#StructureMap.structure.mode)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/map-model-mode|4.0.0
    (
     produced, 
     queried, 
     source, 
     target)
1. **[StructureMap.group.typeMode](https://build.fhir.org/structuremap-definitions.html#StructureMap.group.typeMode)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/map-group-type-mode|4.0.0
    (
     types, 
     none, 
     type-and-types)
1. **[StructureMap.group.input.mode](https://build.fhir.org/structuremap-definitions.html#StructureMap.group.input.mode)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/map-input-mode|4.0.0
    (
     target, 
     source)
1. **[Task.status](https://build.fhir.org/task-definitions.html#Task.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/task-status|4.0.0
    (
     draft, 
     in-progress, 
     ready, 
     requested, 
     cancelled, 
     failed, 
     completed, 
     on-hold, 
     received, 
     rejected, 
     accepted, 
     entered-in-error)
1. **[DocumentReference.status](https://build.fhir.org/documentreference-definitions.html#DocumentReference.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/document-reference-status|4.0.0
    (
     entered-in-error, 
     superseded, 
     current)
1. **[DocumentReference.relatesTo.code](https://build.fhir.org/documentreference-definitions.html#DocumentReference.relatesTo.code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/document-relationship-type|4.0.0
    (
     transforms, 
     appends, 
     signs, 
     replaces)
1. **[OperationOutcome.issue.severity](https://build.fhir.org/operationoutcome-definitions.html#OperationOutcome.issue.severity)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/issue-severity|4.0.0
    (
     error, 
     information, 
     warning, 
     fatal)
1. **[Observation.value[x].code](https://build.fhir.org/observation-definitions.html#Observation.value[x].code)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/ucum-bodylength|4.0.0
1. **[AdverseEvent.actuality](https://build.fhir.org/adverseevent-definitions.html#AdverseEvent.actuality)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/adverse-event-actuality|4.0.0
    (
     potential, 
     actual)
 
### All Required Status Bindings for Coded Elements without an 'other' or 'unknown' code:
1. **[DeviceUseStatement.status](https://build.fhir.org/deviceusestatement-definitions.html#DeviceUseStatement.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/device-statement-status|4.0.0
    (
     stopped, 
     completed, 
     active, 
     on-hold, 
     intended, 
     entered-in-error)
1. **[Appointment.status](https://build.fhir.org/appointment-definitions.html#Appointment.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/appointmentstatus|4.0.0
    (
     checked-in, 
     proposed, 
     cancelled, 
     arrived, 
     waitlist, 
     entered-in-error, 
     pending, 
     booked, 
     fulfilled, 
     noshow)
1. **[Appointment.participant.status](https://build.fhir.org/appointment-definitions.html#Appointment.participant.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/participationstatus|4.0.0
    (
     needs-action, 
     accepted, 
     tentative, 
     declined)
1. **[List.status](https://build.fhir.org/list-definitions.html#List.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/list-status|4.0.0
    (
     current, 
     retired, 
     entered-in-error)
1. **[VerificationResult.status](https://build.fhir.org/verificationresult-definitions.html#VerificationResult.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/verificationresult-status|4.0.0
    (
     req-revalid, 
     in-process, 
     validated, 
     reval-fail, 
     attested, 
     val-fail)
1. **[Composition.status](https://build.fhir.org/composition-definitions.html#Composition.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/composition-status|4.0.0
    (
     preliminary, 
     amended, 
     entered-in-error, 
     final)
1. **[DocumentManifest.status](https://build.fhir.org/documentmanifest-definitions.html#DocumentManifest.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/document-reference-status|4.0.0
    (
     entered-in-error, 
     superseded, 
     current)
1. **[Claim.status](https://build.fhir.org/claim-definitions.html#Claim.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[CoverageEligibilityResponse.status](https://build.fhir.org/coverageeligibilityresponse-definitions.html#CoverageEligibilityResponse.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[QuestionnaireResponse.status](https://build.fhir.org/questionnaireresponse-definitions.html#QuestionnaireResponse.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/questionnaire-answers-status|4.0.0
    (
     amended, 
     entered-in-error, 
     stopped, 
     completed, 
     in-progress)
1. **[EpisodeOfCare.status](https://build.fhir.org/episodeofcare-definitions.html#EpisodeOfCare.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/episode-of-care-status|4.0.0
    (
     waitlist, 
     finished, 
     entered-in-error, 
     onhold, 
     active, 
     planned, 
     cancelled)
1. **[EpisodeOfCare.statusHistory.status](https://build.fhir.org/episodeofcare-definitions.html#EpisodeOfCare.statusHistory.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/episode-of-care-status|4.0.0
    (
     waitlist, 
     finished, 
     entered-in-error, 
     onhold, 
     active, 
     planned, 
     cancelled)
1. **[Endpoint.status](https://build.fhir.org/endpoint-definitions.html#Endpoint.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/endpoint-status|4.0.0
    (
     error, 
     off, 
     suspended, 
     entered-in-error, 
     active, 
     test)
1. **[GuidanceResponse.status](https://build.fhir.org/guidanceresponse-definitions.html#GuidanceResponse.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/guidance-response-status|4.0.0
    (
     data-required, 
     data-requested, 
     success, 
     failure, 
     in-progress, 
     entered-in-error)
1. **[ResearchStudy.status](https://build.fhir.org/researchstudy-definitions.html#ResearchStudy.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/research-study-status|4.0.0
    (
     completed, 
     closed-to-accrual, 
     temporarily-closed-to-accrual, 
     approved, 
     withdrawn, 
     active, 
     closed-to-accrual-and-intervention, 
     temporarily-closed-to-accrual-and-intervention, 
     in-review, 
     disapproved, 
     administratively-completed)
1. **[TestReport.status](https://build.fhir.org/testreport-definitions.html#TestReport.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/report-status-codes|4.0.0
    (
     in-progress, 
     waiting, 
     completed, 
     entered-in-error, 
     stopped)
1. **[MeasureReport.status](https://build.fhir.org/measurereport-definitions.html#MeasureReport.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/measure-report-status|4.0.0
    (
     complete, 
     error, 
     pending)
1. **[VisionPrescription.status](https://build.fhir.org/visionprescription-definitions.html#VisionPrescription.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[Flag.status](https://build.fhir.org/flag-definitions.html#Flag.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/flag-status|4.0.0
    (
     inactive, 
     entered-in-error, 
     active)
1. **[ExplanationOfBenefit.status](https://build.fhir.org/explanationofbenefit-definitions.html#ExplanationOfBenefit.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/explanationofbenefit-status|4.0.0
    (
     cancelled, 
     active, 
     entered-in-error, 
     draft)
1. **[Composition.status](https://build.fhir.org/composition-definitions.html#Composition.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/composition-status|4.0.0
    (
     preliminary, 
     amended, 
     entered-in-error, 
     final)
1. **[FamilyMemberHistory.status](https://build.fhir.org/familymemberhistory-definitions.html#FamilyMemberHistory.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/history-status|4.0.0
    (
     entered-in-error, 
     health-unknown, 
     completed, 
     partial)
1. **[Immunization.status](https://build.fhir.org/immunization-definitions.html#Immunization.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/immunization-status|4.0.0
    (
     completed, 
     not-done, 
     entered-in-error)
1. **[ClaimResponse.status](https://build.fhir.org/claimresponse-definitions.html#ClaimResponse.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[Invoice.status](https://build.fhir.org/invoice-definitions.html#Invoice.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/invoice-status|4.0.0
    (
     issued, 
     draft, 
     balanced, 
     cancelled, 
     entered-in-error)
1. **[PaymentNotice.status](https://build.fhir.org/paymentnotice-definitions.html#PaymentNotice.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[GuidanceResponse.status](https://build.fhir.org/guidanceresponse-definitions.html#GuidanceResponse.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/guidance-response-status|4.0.0
    (
     data-required, 
     data-requested, 
     success, 
     failure, 
     in-progress, 
     entered-in-error)
1. **[FamilyMemberHistory.status](https://build.fhir.org/familymemberhistory-definitions.html#FamilyMemberHistory.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/history-status|4.0.0
    (
     entered-in-error, 
     health-unknown, 
     completed, 
     partial)
1. **[Composition.status](https://build.fhir.org/composition-definitions.html#Composition.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/composition-status|4.0.0
    (
     preliminary, 
     amended, 
     entered-in-error, 
     final)
1. **[Narrative.status](https://build.fhir.org/narrative-definitions.html#Narrative.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/narrative-status|4.0.0
    (
     generated, 
     additional, 
     extensions, 
     empty)
1. **[CoverageEligibilityRequest.status](https://build.fhir.org/coverageeligibilityrequest-definitions.html#CoverageEligibilityRequest.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[Slot.status](https://build.fhir.org/slot-definitions.html#Slot.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/slotstatus|4.0.0
    (
     free, 
     busy, 
     busy-unavailable, 
     busy-tentative, 
     entered-in-error)
1. **[Coverage.status](https://build.fhir.org/coverage-definitions.html#Coverage.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[PaymentReconciliation.status](https://build.fhir.org/paymentreconciliation-definitions.html#PaymentReconciliation.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/fm-status|4.0.0
    (
     entered-in-error, 
     cancelled, 
     active, 
     draft)
1. **[ImmunizationEvaluation.status](https://build.fhir.org/immunizationevaluation-definitions.html#ImmunizationEvaluation.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/immunization-evaluation-status|4.0.0
    (
     completed, 
     entered-in-error)
1. **[Narrative.status](https://build.fhir.org/narrative-definitions.html#Narrative.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/narrative-status|4.0.0
    (
     generated, 
     additional, 
     extensions, 
     empty)
1. **[ResearchSubject.status](https://build.fhir.org/researchsubject-definitions.html#ResearchSubject.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/research-subject-status|4.0.0
    (
     pending-on-study, 
     screening, 
     withdrawn, 
     potential-candidate, 
     eligible, 
     on-study, 
     candidate, 
     not-registered, 
     on-study-intervention, 
     ineligible, 
     on-study-observation, 
     off-study, 
     follow-up)
1. **[ClinicalImpression.status](https://build.fhir.org/clinicalimpression-definitions.html#ClinicalImpression.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/clinicalimpression-status|4.0.0
    (
     completed, 
     entered-in-error, 
     in-progress)
1. **[Subscription.status](https://build.fhir.org/subscription-definitions.html#Subscription.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/subscription-status|4.0.0
    (
     off, 
     requested, 
     error, 
     active)
1. **[Consent.status](https://build.fhir.org/consent-definitions.html#Consent.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/consent-state-codes|4.0.0
    (
     proposed, 
     rejected, 
     inactive, 
     active, 
     draft, 
     entered-in-error)
1. **[Task.status](https://build.fhir.org/task-definitions.html#Task.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/task-status|4.0.0
    (
     draft, 
     in-progress, 
     ready, 
     requested, 
     cancelled, 
     failed, 
     completed, 
     on-hold, 
     received, 
     rejected, 
     accepted, 
     entered-in-error)
1. **[DocumentReference.status](https://build.fhir.org/documentreference-definitions.html#DocumentReference.status)**
    - 1..1
    - http://hl7.org/fhir/ValueSet/document-reference-status|4.0.0
    (
     entered-in-error, 
     superseded, 
     current)