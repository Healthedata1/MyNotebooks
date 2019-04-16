
### Summary of the Mandatory Requirements



1.  A  Reference  in `CareTeam.subject`


1. One or more BackboneElements  in `CareTeam.participant`

    - which must have a  CodeableConcept value  in `CareTeam.participant.role`with a [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)\+ [MaxValueSet](general-guidance.html#max-binding)
 binding to [CareTeam Provider Roles](http://hl7.org/fhir/us/core/ValueSet/us-core-careteam-provider-roles)
    - which must have a  Reference value  in `CareTeam.participant.member`





1.  A  code  in `CareTeam.status`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [CareTeamStatus](http://hl7.org/fhir/ValueSet/care-team-status)