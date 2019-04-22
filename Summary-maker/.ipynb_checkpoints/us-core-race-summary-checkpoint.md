## Extension

### Summary of the Mandatory Requirements
1.  A 
[Text](None) Extension  in `Extension.extension`
   - which must have a fixed `Extension.extension.url` = `text`
   - which must have a  string value  in `Extension.extension.valueString`
1.  An  uri  in `Extension.url`

### Summary of the Must Support Requirements
1. One or more 
[Ombcategory](None)Extensions  in `Extension.extension`
   - which must have a fixed `Extension.extension.url` = `ombCategory`
   - which must have a  Coding value  in `Extension.extension.valueCoding`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [OMB Race Categories](http://hl7.org/fhir/us/core/ValueSet/omb-race-category)
1. One or more 
[Detailed](None)Extensions  in `Extension.extension`
   - which must have a fixed `Extension.extension.url` = `detailed`
   - which must have a  Coding value  in `Extension.extension.valueCoding`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [US-Core Detailed Race](http://hl7.org/fhir/us/core/ValueSet/detailed-race)