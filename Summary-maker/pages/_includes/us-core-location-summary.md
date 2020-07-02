**Location**

#### Summary of the Mandatory Requirements
1.  A  string  in `Location.name`

#### Summary of the Must Support Requirements
1.  A  code  in `Location.status`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [LocationStatus](http://hl7.org/fhir/ValueSet/location-status|4.0.1)
1. One or more  ContactPoints  in `Location.telecom`
1.  An  Address  in `Location.address`
   - which should have one or more  string values  in `Location.address.line`
   - which should have a  string value  in `Location.address.city`
   - which should have a  string value  in `Location.address.state`
with an [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [USPS Two Letter Alphabetic Codes](ValueSet-us-core-usps-state.html)
   - which should have a  string value  in `Location.address.postalCode`
1.  A Managingorganization Reference  in `Location.managingOrganization`