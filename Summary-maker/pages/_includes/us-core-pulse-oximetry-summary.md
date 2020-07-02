**Observation**

#### Summary of the Mandatory Requirements
1.  A  CodeableConcept  in `Observation.code`
with an [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [Vital Signs](http://hl7.org/fhir/ValueSet/observation-vitalsignresult)
      - which should have one or more  Coding values  in `Observation.code.coding`
      - which must have at least  a  Coding value  in `Observation.code.coding`
         - which must have `Observation.code.coding.system` = the fixed value  "http://loinc.org"
         - which must have  `Observation.code.coding.code` = the fixed value  "59408-5"

#### Summary of the Must Support Requirements
1. One or more  Components  in `Observation.component`
 with the following constraints: *If there is no a value a data absent reason must be present*
1.  A  Component  in `Observation.component`
 with the following constraints: *If there is no a value a data absent reason must be present*
   - which must have  `Observation.component.code` =the pattern "{"coding": [{"code": "3151-8", "system": "http://loinc.org"}]}"
   - which should have a  Quantity value  in `Observation.component.valueQuantity`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [Vital Signs Units](http://hl7.org/fhir/ValueSet/ucum-vitals-common|4.0.1)
   - which should have a  decimal value  in `Observation.component.valueQuantity.value`
   - which should have a  string value  in `Observation.component.valueQuantity.unit`
   - which must have `Observation.component.valueQuantity.system` = the fixed value  "http://unitsofmeasure.org"
   - which must have  `Observation.component.valueQuantity.code` = the fixed value  "l/min"
1.  A  Component  in `Observation.component`
 with the following constraints: *If there is no a value a data absent reason must be present*
   - which must have  `Observation.component.code` =the pattern "{"coding": [{"code": "3150-0", "system": "http://loinc.org"}]}"
   - which should have a  Quantity value  in `Observation.component.valueQuantity`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [Vital Signs Units](http://hl7.org/fhir/ValueSet/ucum-vitals-common|4.0.1)
   - which should have a  decimal value  in `Observation.component.valueQuantity.value`
   - which should have a  string value  in `Observation.component.valueQuantity.unit`
   - which must have `Observation.component.valueQuantity.system` = the fixed value  "http://unitsofmeasure.org"
   - which must have  `Observation.component.valueQuantity.code` = the fixed value  "%"

#### Summary of Constraints
1. dataAbsentReason SHALL only be present if Observation.value[x] is not present
1. If Observation.code is the same as an Observation.component.code then the value element associated with the code SHALL NOT be present
1. If there is no component or hasMember element then either a value[x] or a data absent reason must be present.
1. If there is no a value a data absent reason must be present