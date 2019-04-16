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