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


**AllergyIntolerance**
  - [_id](SearchParameter-None.html)

**Questionnaire**
  - [_id](SearchParameter-None.html)
  - [url](SearchParameter-us-core-questionnaire-url.html)
  - [status](SearchParameter-us-core-questionnaire-status.html)
  - [title](SearchParameter-us-core-questionnaire-title.html)
  - [publisher](SearchParameter-us-core-questionnaire-publisher.html)
  - [version](SearchParameter-us-core-questionnaire-version.html)
  - [context-type-value](SearchParameter-us-core-questionnaire-context-type-value.html)

**Patient**
  - [_id](SearchParameter-None.html)
  - [identifier](SearchParameter-us-core-patient-identifier.html)
  - [name](SearchParameter-us-core-patient-name.html)
  - [birthdate](SearchParameter-us-core-individual-birthdate.html)
  - [gender](SearchParameter-us-core-individual-gender.html)
  - [family](SearchParameter-us-core-individual-family.html)
  - [given](SearchParameter-us-core-individual-given.html)
  - [address](SearchParameter-us-core-individual-address.html)
  - [telecom](SearchParameter-us-core-individual-telecom.html)

**Encounter**
  - [_id](SearchParameter-None.html)
  - [patient](SearchParameter-us-core-clinical-patient.html)
  - [date](SearchParameter-us-core-clinical-date.html)

{% include link_list.md %}