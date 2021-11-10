**Observation**

#### Summary of the Mandatory Requirements
1.  A  CodeableConcept  in `Observation.code`  = the pattern "{"coding": [{"code": "59576-9", "system": "http://loinc.org"}]}"

#### Summary of the Must Support Requirements
1.  A  Quantity  in `Observation.valueQuantity`
   - which must have a  decimal value  in `Observation.valueQuantity.value`
   - which must have a  string value  in `Observation.valueQuantity.unit`
   - which must have `Observation.valueQuantity.system` = the fixed value  "http://unitsofmeasure.org"
   - which must have  `Observation.valueQuantity.code` = the fixed value  "%"

#### Summary of Constraints
1. dataAbsentReason SHALL only be present if Observation.value[x] is not present
1. If Observation.code is the same as an Observation.component.code then the value element associated with the code SHALL NOT be present
1. If there is no component or hasMember element then either a value[x] or a data absent reason must be present.