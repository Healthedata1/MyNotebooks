# Grouped Changes by Change Impact

## Non-substantive

1. **Applied:** Non-substantive (Clarification) Clarify Coverage.type value set usage [FHIR-44122](https://jira.hl7.org/browse/FHIR-44122) See Changes [Here](StructureDefinition-us-core-coverage.html#profile-specific-implementation-guidance)

2. **Resolved - change required:** Non-substantive (Correction) Change binding description in US Core Coverage Profile [FHIR-44124](https://jira.hl7.org/browse/FHIR-44124) See Changes [Here](StructureDefinition-us-core-coverage.html)

3. **Resolved - change required:** Non-substantive (Correction) Fix the US Core History Page [FHIR-46749](https://jira.hl7.org/browse/FHIR-46749) See Changes [Here](https://hl7.org/fhir/us/core/history.html)

4. **Triaged:** Non-substantive (Correction) Hyperlink discrepancy [FHIR-49336](https://jira.hl7.org/browse/FHIR-49336) See Changes [Here](StructureDefinition-us-core-diagnosticreport-lab.html#terminology-bindings-differential)

5. **Triaged:** Non-substantive (Correction) Hyperlink discrepancy [FHIR-49337](https://jira.hl7.org/browse/FHIR-49337) See Changes [Here](StructureDefinition-us-core-observation-lab.html#terminology-bindings-differential)

6. **Resolved - change required:** Non-substantive (Correction) correct line 81 in terminology  [FHIR-49610](https://jira.hl7.org/browse/FHIR-49610) See Changes [Here](terminology.html)

7. **Triaged:** Non-substantive (Enhancement) Create Version History Menu Item [FHIR-50345](https://jira.hl7.org/browse/FHIR-50345) See Changes [Here](changes.html)

8. **Triaged:** Non-substantive (Enhancement) Update formatting in Quick Start to make it easier to read [FHIR-50397](https://jira.hl7.org/browse/FHIR-50397) See Changes [Here](StructureDefinition-us-core-condition-encounter-diagnosis.html#notes)

9. **Applied:** Non-substantive (Enhancement) Reformat the profile pages' Implementation Guidance Sections [FHIR-50972](https://jira.hl7.org/browse/FHIR-50972) See Change [Here](StructureDefinition-us-core-allergyintolerance.html#profile-specific-implementation-guidance)

10. **Applied:** Non-substantive (Enhancement) Relax US@ address requirements [FHIR-51159](https://jira.hl7.org/browse/FHIR-51159) See Changes [Here](StructureDefinition-us-core-patient.html)

11. **Applied:** Non-substantive (Clarification) Update client expectations for preserving resource IDs between versions [FHIR-51756](https://jira.hl7.org/browse/FHIR-51756) See Changes [Here](changes-between-versions.html#no-guarantee-that-resource-ids-are-preserved)

12. **Applied:** Non-substantive (Clarification) Update guidance on Authorization Across Versions Sections [FHIR-51757](https://jira.hl7.org/browse/FHIR-51757) See Changes [Here](changes-between-versions.html#authorization-across-versions)

13. **Applied:** Non-substantive (Clarification) Add implementer guidance for non-US addresses [FHIR-51791](https://jira.hl7.org/browse/FHIR-51791) See Changes:
- [US Core Patient](StructureDefinition-us-core-patient.html#profile-specific-implementation-guidance)
- [US Core Practitioner](StructureDefinition-us-core-practitioner.html#profile-specific-implementation-guidance)
- [US Core Organization](StructureDefinition-us-core-organization.html#profile-specific-implementation-guidance)
- [US Core RelatedPerson](StructureDefinition-us-core-relatedperson.html#profile-specific-implementation-guidance)
- [US Core Location](StructureDefinition-us-core-location.html#profile-specific-implementation-guidance)

14.  **Applied:** Non-substantive (Enhancement) Call attention and link to USCDI level 1, 2 Data elements [FHIR-52492](https://jira.hl7.org/browse/FHIR-52492) See Changes [Here](uscdi.html#anticipating-future-uscdi-versions)

15. **Applied:** Non-substantive (Clarification) Clarify $docref operation behavior [FHIR-52869](https://jira.hl7.org/browse/FHIR-52869) See Changes [Here](OperationDefinition-docref.html)

16. **Applied:** Non-substantive (Correction) Remove Externally Published code systems section and table [FHIR-52980](https://jira.hl7.org/browse/FHIR-52980) See Changes [Here](terminology.html#code-systems)

17. **Triaged:** Non-substantive (Enhancement) Compare US Core Profiles with International Patient Summary Profiles [FHIR-53130](https://jira.hl7.org/browse/FHIR-53130) See Changes [Here](relationship-with-other-igs.html#relationship-to-us-core-and-other-igs)

## Compatible, substantive

18. **Resolved - change required:** Compatible, substantive (Enhancement) Seems like observation-category CodeSystem needs to be extended to include a concept for care-experience-preference [FHIR-43541](https://jira.hl7.org/browse/FHIR-43541) See Changes [Here]()

19. **Triaged:** Compatible, substantive (Correction) Update the SOPT's terminology reference in the code-system table [FHIR-44138](https://jira.hl7.org/browse/FHIR-44138) See Changes [Here](terminology.html)

20. **Resolved - change required:** Compatible, substantive (Correction) NAIC Code Number Identifier system not registered in THO [FHIR-46185](https://jira.hl7.org/browse/FHIR-46185) See Changes [Here](StructureDefinition-us-core-organization-definitions.html#diff_Organization.identifier:NAIC)

21. **Resolved - change required:** Compatible, substantive (Clarification) How to deal with searchparameters in the package that only convey expectations [FHIR-48876](https://jira.hl7.org/browse/FHIR-48876) See Changes [Here](https://www.hl7.org/fhir/us/core/search-parameters-and-operations.html#search-parameters)

22. **Resolved - change required:** Compatible, substantive (Enhancement) Move USPS value set to THO [FHIR-50143](https://jira.hl7.org/browse/FHIR-50143) See Changes [Here](StructureDefinition-us-core-patient.html)

23. **Triaged:** Compatible, substantive (Enhancement) Consider Using additional bindings instead of grouped valuesets [FHIR-50464](https://jira.hl7.org/browse/FHIR-50464) See Changes [Here](StructureDefinition-us-core-location.html)

24. **Applied:** Compatible, substantive (Enhancement) Additional Guidance for the appropriate NDC code to use from the NDC vaccine linker [FHIR-50798](https://jira.hl7.org/browse/FHIR-50798) See Changes:
- [US Core Immunization Profile](StructureDefinition-us-core-immunization.html#profile-specific-implementation-guidance)
- [Immunization Example 1](Immunization-imm-1.html)

25. **Resolved - change required:** Compatible, substantive (Enhancement) merge US Core Provenance Type CodeSystem with FHIR Provenance Type CodeSystem [FHIR-50927](https://jira.hl7.org/browse/FHIR-50927) See Changes:[Here](CodeSystem-us-core-provenance-participant-type.html)

26. **Resolved - change required:** Compatible, substantive (Enhancement) Create and bind to Grouped set in Location.type to ease extensible binding requirements [FHIR-50937](https://jira.hl7.org/browse/FHIR-50937) See Changes [Here](StructureDefinition-us-core-location.html)

27. **Applied:** Compatible, substantive (Correction) Remove guidance from US Core Simple Observation Profile [FHIR-51493](https://jira.hl7.org/browse/FHIR-51493) See Changes [Here](StructureDefinition-us-core-simple-observation.html#mandatory-and-must-support-data-elements)

28. **Resolved - change required:** Compatible, substantive (Correction) Medication Adherence Value Set - Proposed Changes [FHIR-52822](https://jira.hl7.org/browse/FHIR-52822) See Changes [Here](StructureDefinition-us-core-medication-adherence.html)

29. **Submitted:** Compatible, substantive (Enhancement) Slice the PractitionerRole.specialty element to optionally also include SNOMED CT specialty codes [FHIR-52843](https://jira.hl7.org/browse/FHIR-52843) See Changes [Here](StructureDefinition-us-core-practitionerrole.html)

30. **Resolved - change required:** Compatible, substantive (Enhancement) Add USCDI v6 Data Elements to US Core [FHIR-52965](https://jira.hl7.org/browse/FHIR-52965) See Changes Listed in the [9.0.0-Ballot Introduction](#the-january-2026-ballot) above.

## Non-compatible

31. **Resolved - change required:** Non-compatible (Enhancement) Deprecate every version before 3.1.1 [FHIR-46065](https://jira.hl7.org/browse/FHIR-46065) See Changes [Here](changes.html)

32. **Triaged:** Non-compatible (Enhancement) Clean up examples for FHIR ADI DocumentReference Profile [FHIR-49617](https://jira.hl7.org/browse/FHIR-49617) See Changes [Here]()

33. **Applied:** Non-compatible (Correction) Correct HCPCS code system URI [FHIR-50807](https://jira.hl7.org/browse/FHIR-50807) See Changes [Here](ValueSet-us-core-procedure-code.html)

34. **Triaged:** Non-compatible (Correction) Constrain subject to only patient [FHIR-51032](https://jira.hl7.org/browse/FHIR-51032) See Changes [Here](StructureDefinition-us-core-adi-documentreference.html)

## Substantive

35. **Triaged:** Substantive (Clarification) Review FMM levels for USCDI artifacts [FHIR-52975](https://jira.hl7.org/browse/FHIR-52975) See Changes [Here](#)

36. **Applied:** Substantive (Enhancement) Update context for Sex Extension [FHIR-52994](https://jira.hl7.org/browse/FHIR-52994) See Changes [Here](StructureDefinition-us-core-sex.html)

37. **Triaged:** Substantive (Enhancement) Add ValueSet and CodeSystem version guidance [FHIR-53111](https://jira.hl7.org/browse/FHIR-53111) See Changes [Here](terminology.html)

38. **Pre-Applied:** Substantive (Enhancement) Update US Core Race and Ethnicity Extension descriptions [FHIR-53113](https://jira.hl7.org/browse/FHIR-53113) See Changes:
- [US Core Race Extension](StructureDefinition-us-core-race.html)
- [US Core Ethnicity Extension](StructureDefinition-us-core-ethnicity.html)

## Unknown

39. **Triaged:** () Update client Expectation that FHIR Data is Preserved [FHIR-51760](https://jira.hl7.org/browse/FHIR-51760) See Changes [Here](changes-between-versions.html#expectation-that-fhir-dstu2-data-is-preserved-in-fhir-r4)

