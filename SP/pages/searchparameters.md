---
title: Operations and Search Parameters
layout: default
topofpage: true
sectionnumbering: true
---

The following operations and search parameters have been defined for the US Core Implementation Guide.  For more information on the [FHIR RESTful operations], [FHIR RESTful search api] and the standard [Search Param Registry] see the FHIR specification.

### Operations


  {% include list-simple-operationdefinitions.xhtml %}


<br />

### Search Parameters

NOTE: These search parameters **SHALL NOT** be interpreted on their own as requirements for server:
This section lists the search parameters definitions that are used within the capability statement to define the search capabilities expectations for the US Core Server.  This is not a list of search requirements for the client or server.


**Condition**
  - [category](SearchParameter-us-core-condition-category.html)
  - [clinical-status](SearchParameter-us-core-condition-clinical-status.html)
  - [patient](SearchParameter-None.html)
  - [onset-date](SearchParameter-us-core-condition-onset-date.html)
  - [code](SearchParameter-us-core-condition-code.html)

**Encounter**
  - [_id](SearchParameter-None.html)
  - [class](SearchParameter-us-core-encounter-class.html)
  - [date](SearchParameter-us-core-encounter-date.html)
  - [identifier](SearchParameter-us-core-encounter-identifier.html)
  - [patient](SearchParameter-None.html)
  - [status](SearchParameter-us-core-encounter-status.html)
  - [type](SearchParameter-us-core-encounter-type.html)

**AllergyIntolerance**
  - [clinical-status](SearchParameter-us-core-allergyintolerance-clinical-status.html)
  - [patient](SearchParameter-us-core-allergyintolerance-patient.html)

**Patient**
  - [_id](SearchParameter-None.html)
  - [birthdate](SearchParameter-us-core-patient-birthdate.html)
  - [family](SearchParameter-us-core-patient-family.html)
  - [gender](SearchParameter-us-core-patient-gender.html)
  - [given](SearchParameter-us-core-patient-given.html)
  - [identifier](SearchParameter-us-core-patient-identifier.html)
  - [name](SearchParameter-us-core-patient-name.html)

**Immunization**
  - [patient](SearchParameter-None.html)
  - [status](SearchParameter-us-core-immunization-status.html)
  - [date](SearchParameter-None.html)



Editors note : append these to Patient
  - [us-core-race]
  - [us-core-ethnicity]

{% include link-list.md %}