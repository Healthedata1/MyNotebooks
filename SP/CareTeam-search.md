### Quick Start
Below is an overview of the required set of RESTful FHIR interactions - for
example, search and read operations - for this profile. See the [Conformance requirements]
for a complete list of supported RESTful interactions for this IG.

#### Supported Searches
1. **MAY** support search by the **`careteam-category`** parameter:
  `GET [base]/CareTeam?careteam-category={[system]}|[code]`
    
    - with support for these [search modifiers]: `text`
    
  *Implementation Notes:* Select CareTeams of the specified type. ([how to search by token]).
  <br />
  
1. **SHOULD** support search by the **`careteam-endpoint`** parameter:
  `GET [base]/CareTeam?careteam-endpoint=[url]`
    
    - for reference target types: `Endpoint`
    - with support for these [chained search parameters]:`careteam-endpoint:Endpoint.identifier`, `careteam-endpoint:Endpoint.connection-type`, `careteam-endpoint:Endpoint.organization`
    
  *Implementation Notes:* Select CareTeams with the specified endpoint. ([how to search by reference]).
  <br />
  
1. **SHALL** support search by the **`careteam-identifier`** parameter:
  `GET [base]/CareTeam?careteam-identifier={[system]}|[code]`
    
    - with support for these [search modifiers]: `text`, `ofType`
    
  *Implementation Notes:* Select CareTeams with the specified identifier. ([how to search by token]).
  <br />
  
1. **MAY** support search by the **`careteam-identifier-assigner`** parameter:
  `GET [base]/CareTeam?careteam-identifier-assigner=[url]`
    
    - for reference target types: `Organization`
    - with support for these [chained search parameters]:`careteam-identifier-assigner:Organization.identifier`, `careteam-identifier-assigner:Organization.name`
    
    - with support for these [search modifiers]: `below`
    
  *Implementation Notes:* Select care teams with an identifier assigned by the specified organization. ([how to search by reference]).
  <br />
  
1. **SHALL** support search by the **`careteam-location`** parameter:
  `GET [base]/CareTeam?careteam-location=[url]`
    
    - for reference target types: `Location`
    - with support for these [chained search parameters]:`careteam-location:Location.identifier`, `careteam-location:Location.type`, `careteam-location:Location.address`, `careteam-location:Location.organization`
    
    - with support for these [search modifiers]: `above`, `below`
    
  *Implementation Notes:* Select care teams operating at the specified location. ([how to search by reference]).
  <br />
  
1. **SHALL** support search by the **`careteam-member`** parameter:
  `GET [base]/CareTeam?careteam-member=[url]`
    
    - for reference target types: `PractitionerRole`, `Organization`, `CareTeam`
    - with support for these [search modifiers]: `type`
    
  *Implementation Notes:* Select care teams that include the specified member. ([how to search by reference]).
  <br />
  
1. **SHOULD** support search by the **`careteam-name`** parameter:
  `GET [base]/CareTeam?careteam-name=[string]`
    
    - with support for these [search modifiers]: `exact`, `contains`
    
  *Implementation Notes:* Select care teams with the specified name. ([how to search by string]).
  <br />
  
1. **SHALL** support search by the **`careteam-organization`** parameter:
  `GET [base]/CareTeam?careteam-organization=[url]`
    
    - for reference target types: `Organization`
    - with support for these [chained search parameters]:`careteam-organization:Organization.identifier`, `careteam-organization:Organization.name`, `careteam-organization:Organization.address`, `careteam-organization:Organization.partof`, `careteam-organization:Organization.type`
    
    - with support for these [search modifiers]: `above`, `below`
    
  *Implementation Notes:* Select care teams managed by the specified organization. ([how to search by reference]).
  <br />
  
1. **SHOULD** support search by the **`careteam-service`** parameter:
  `GET [base]/CareTeam?careteam-service=[url]`
    
    - for reference target types: `HealthcareService`
    - with support for these [chained search parameters]:`careteam-service:HealthcareService.identifier`, `careteam-service:HealthcareService.category`, `careteam-service:HealthcareService.organization`, `careteam-service:HealthcareService.location`
    
  *Implementation Notes:* Select care teams providing the specified service. ([how to search by reference]).
  <br />
  
1. **SHALL** support search by the **`careteam-status`** parameter:
  `GET [base]/CareTeam?careteam-status={[system]}|[code]`
    
  *Implementation Notes:* Select CareTeams with the specified status. ([how to search by token]).
  <br />
  
1. **MAY** support search by the **`careteam-via-intermediary`** parameter:
  `GET [base]/CareTeam?careteam-via-intermediary=[url]`
    
    - for reference target types: `PractitionerRole`, `Organization`, `OrganizationAffiliation`, `Location`
  *Implementation Notes:* Select care teams with contact information available through the specified intermediary. ([how to search by reference]).
  <br />
  

{% include link-list.md %}