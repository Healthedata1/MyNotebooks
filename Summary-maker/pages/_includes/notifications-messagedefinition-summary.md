**MessageDefinition**

#### Summary of the Mandatory Requirements
1.  An  uri  in `MessageDefinition.url`
1.  A  code  in `MessageDefinition.status`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [PublicationStatus](http://hl7.org/fhir/ValueSet/publication-status|4.0.1)
1.  A  dateTime  in `MessageDefinition.date`
1.  A  code  in `MessageDefinition.category`  = the fixed value  "notification"
1. One or more  Focuses  in `MessageDefinition.focus`
 with the following constraints: *Max must be postive int or **
      - which must have a  code value  in `MessageDefinition.focus.code`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [ResourceType](http://hl7.org/fhir/ValueSet/resource-types|4.0.1)
      - which should have a  canonical value  in `MessageDefinition.focus.profile`
1. One or more  canonicals  in `MessageDefinition.graph`

#### Summary of the Must Support Requirements
1.  A  string  in `MessageDefinition.version`
1.  A  string  in `MessageDefinition.name`
1.  A  string  in `MessageDefinition.title`
1.  A  string  in `MessageDefinition.publisher`
1.  A  markdown  in `MessageDefinition.description`

#### Summary of the Unsupported Elements
1. `MessageDefinition.responseRequired`
1. `MessageDefinition.allowedResponse`

#### Summary of Constraints
1. Name should be usable as an identifier for the module by machine processing applications such as code generation
1. Max must be postive int or *