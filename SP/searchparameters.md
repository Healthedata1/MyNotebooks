---
title: Operations and Search Parameters
layout: default
topofpage: true
sectionnumbering: true
---

The following search parameters have been defined for the {{site.data.fhir.igName}} Implementation Guide.  For more information on the [FHIR RESTful search api]and the standard [Search Param Registry] see the FHIR specification.

<!-- Operations


  { % include list-simple-operationdefinitions.xhtml % }


-->

Search Parameter


**HealthcareService**
  - [active](SearchParameter-HealthcareService-active.html)

**Patient**

**Person**

**Questionnaire**
  - [url](SearchParameter-Questionnaire-url.html)
  - [status](SearchParameter-Questionnaire-status.html)
  - [title](SearchParameter-Questionnaire-title.html)
  - [publisher](SearchParameter-Questionnaire-publisher.html)
  - [version](SearchParameter-Questionnaire-version.html)

**QuestionnaireResponse**
  - [questionnaire](SearchParameter-QuestionnaireResponse-questionnaire.html)
  - [patient](SearchParameter-QuestionnaireResponse-patient.html)
  - [context](SearchParameter-QuestionnaireResponse-context.html)
  - [status](SearchParameter-QuestionnaireResponse-status.html)
  - [author](SearchParameter-QuestionnaireResponse-author.html)
  - [source](SearchParameter-QuestionnaireResponse-source.html)

**RelatedPerson**
  - [birthdate](SearchParameter-individual-birthdate.html)

{% include link_list.md %}