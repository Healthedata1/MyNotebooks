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


**MedicationRequest**
  - [status](SearchParameter-us-core-medicationrequest-status.html)
  - [intent](SearchParameter-us-core-medicationrequest-intent.html)
  - [patient](SearchParameter-us-core-medicationrequest-patient.html)
  - [encounter](SearchParameter-us-core-medicationrequest-encounter.html)
  - [authoredon](SearchParameter-us-core-medicationrequest-authoredon.html)



Editors note : append these to Patient
  - [us-core-race]
  - [us-core-ethnicity]

{% include link-list.md %}