**Extension**

#### Summary of the Mandatory Requirements
   - which must have at least  a *Text* Extension value  in `Extension.extension`
      - which must have `Extension.extension.url` = the fixed value  "text"
      - which must have a  string value  in `Extension.extension.valueString`
1.  A  http://hl7.org/fhirpath/System.String  in `Extension.url`  = the fixed value "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"

#### Summary of the Must Support Requirements
1. One or more *Ombcategory* Extensions  in `Extension.extension`
   - which must have `Extension.extension.url` = the fixed value  "ombCategory"
   - which must have a  Coding value  in `Extension.extension.valueCoding`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [OMB Race Categories](ValueSet-omb-race-category.html)
1. One or more *Detailed* Extensions  in `Extension.extension`
   - which must have `Extension.extension.url` = the fixed value  "detailed"
   - which must have a  Coding value  in `Extension.extension.valueCoding`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [Detailed Race](ValueSet-detailed-race.html)

#### Summary of the Unsupported Elements
1. `Extension.value[x]`