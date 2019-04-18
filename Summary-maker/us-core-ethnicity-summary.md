**Extension**

#### Summary of the Mandatory Requirements
1.  A *Text* Extension  in `Extension.extension`
   - which must have a fixed `Extension.extension.url` = `text`
   - which must have a  string value  in `Extension.extension.valueString`
1.  An  uri  in `Extension.url`

#### Summary of the Must Support Requirements
1.  An *Ombcategory* Extension  in `Extension.extension`
   - which must have a fixed `Extension.extension.url` = `ombCategory`
   - which must have a  Coding value  in `Extension.extension.valueCoding`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [OMB Ethnicity Categories](ValueSet-omb-ethnicity-category.html)
1. One or more *Detailed* Extensions  in `Extension.extension`
   - which must have a fixed `Extension.extension.url` = `detailed`
   - which must have a  Coding value  in `Extension.extension.valueCoding`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [US-Core Detailed ethnicity](ValueSet-detailed-ethnicity.html)