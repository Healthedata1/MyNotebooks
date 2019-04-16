
### Summary of the Mandatory Requirements



1. One or more Identifiers  in `Organization.identifier`

    - which must have an  uri value  in `Organization.identifier.system`

1.  A  boolean  in `Organization.active`


1.  A  string  in `Organization.name`


1. One or more ContactPoints  in `Organization.telecom`


1. One or more Addresses  in `Organization.address`

    - which should have one or more string values  in `Organization.address.line`
    - which should have a  string value  in `Organization.address.city`
    - which should have a  string value  in `Organization.address.state`with a [extensible](http://hl7.org/fhir/R4/terminologies.html#extensible)
 binding to [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/ValueSet/us-core-usps-state)
    - which should have a  string value  in `Organization.address.postalCode`

### Summary of the Must Support Requirements



1. One or more References  in `Organization.endpoint`
