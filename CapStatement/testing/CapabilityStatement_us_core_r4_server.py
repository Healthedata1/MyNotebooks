from json import dumps, loads
from  pprint import pprint

cs = {'contact': [{'telecom': [{'system': 'other',
                           'value': 'http://www.hl7.org/SpecialCommittees/usrealm/index.cfm'}]}],
 'date': '2017-12-17',
 'description': 'This profile defines the expected capabilities of the US Core '
                'Server conforming to the US Core IG.',
 'fhirVersion': '3.0.1',
 'format': ['xml', 'json'],
 'id': 'us-core-r4-server',
 'jurisdiction': [{'coding': [{'code': 'US',
                               'display': 'United States of America',
                               'system': 'urn:iso:std:iso:3166'}]}],
 'kind': 'requirements',
 'name': 'UsCoreServer',
 'publisher': 'HL7 US Realm Steering Committee',
 'resourceType': 'CapabilityStatement',
 'rest': [{'documentation': '\n'
                            'The US Core Server **SHALL**:\n'
                            '\n'
                            '1.  Support the US Core Patient resource '
                            'profile.\n'
                            '1.  Support *at least* one additional resource '
                            'profile from the list of\n'
                            '    US Core Profiles.\n'
                            '1.  Implement the RESTful behavior according to '
                            'the FHIR specification.\n'
                            '1.  Make available the '
                            '[read](http://hl7.org/fhir/STU3/http.html#read) and '
                            '[search](http://hl7.org/fhir/STU3/http.html#search) interactions for '
                            'the US Core Profiles the server chooses to support.\n'
                            '1.  Return the following response classes:\n'
                            '      - (Status 200): successful operation\n'
                            '      - (Status 400): invalid parameter\n'
                            '      - (Status 401/4xx): unauthorized request\n'
                            '      - (Status 403): insufficient scope\n'
                            '      - (Status 404): unknown resource\n'
                            '      - (Status 410): deleted resource.\n'
                            '1.  Support *json* resource formats for all US '
                            'Core interactions.\n'
                            '1.  Declare a CapabilityStatement identifying the '
                            'supported profiles,\n'
                            '    operations and search parameters.\n'
                            '\n'
                            'The US Core Server **SHOULD**:\n'
                            '\n'
                            '1.  Support *xml* resource formats for all US '
                            'Core interactions.\n'
                            '1.  Identify the US Core profiles supported as '
                            'part of the FHIR\n'
                            '    `meta.profile` attribute for each instance.\n'
                            '1. Make available the '
                            '[vread](http://hl7.org/fhir/STU3/http.html#vread) and '
                            '[history-instance](http://hl7.org/fhir/STU3/http.html#history) '
                            'interactions for the US Core Profiles the server chooses to support.\n'
,
           'mode': 'server',
           'resource': [{'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'Patient '
                                                                              'Profile'}]}],
                         'extension': [{'extension': [{'url': 'required',
                                                       'valueString': 'name'},
                                                      {'url': 'required',
                                                       'valueString': 'gender'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'},
                                       {'extension': [{'url': 'required',
                                                       'valueString': 'name'},
                                                      {'url': 'required',
                                                       'valueString': 'birthdate'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'},
                                       {'extension': [{'url': 'required',
                                                       'valueString': 'family'},
                                                      {'url': 'required',
                                                       'valueString': 'gender'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'},
                                       {'extension': [{'url': 'required',
                                                       'valueString': 'given'},
                                                      {'url': 'required',
                                                       'valueString': 'gender'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core patient '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core patients by '
                                                           'id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'patient instance '
                                                           'over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core patient '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/Patient-name',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'name',
                                          'type': 'string'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Patient-family',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'family',
                                          'type': 'string'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Patient-given',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'given',
                                          'type': 'string'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Patient-identifier',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'identifier',
                                          'type': 'token'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Patient-gender',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'gender',
                                          'type': 'token'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Patient-birthdate',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'birthdate',
                                          'type': 'date'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-patient'],
                         'type': 'Patient'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'AllergyIntolerance '
                                                                              'Profile'}]}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core '
                                                           'AllergyIntolerance '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core '
                                                           'AllergyIntolerance '
                                                           'by id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'AllergyIntolerance '
                                                           'instance over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core '
                                                           'AllergyIntolerance '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/AllergyIntolerance-Patient',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'patient',
                                          'type': 'reference'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-allergyintolerance'],
                         'type': 'AllergyIntolerance'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'CarePlan '
                                                                              'Profile'}]}],
                         'extension': [{'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'category'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'},
                                       {'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'category'},
                                                      {'url': 'required',
                                                       'valueString': 'date'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'},
                                       {'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                       'valueString': 'category'},
                                                       {'url': 'required',
                                                      {'url': 'required',
                                                       'valueString': 'status'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'},
                                       {'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'category'},
                                                      {'url': 'required',
                                                       'valueString': 'status'},
                                                      {'url': 'required',
                                                       'valueString': 'date'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core careplan '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core careplan by '
                                                           'id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'careplan instance '
                                                           'over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core careplan '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/CarePlan-Patient',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'patient',
                                          'type': 'reference'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/CarePlan-Category',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'category',
                                          'type': 'token'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/CarePlan-Status',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'status',
                                          'type': 'token'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/CarePlan-Date',
                                          'documentation': 'The server SHALL '
                                                           'support the date '
                                                           'search modifiers '
                                                           "'ge','le','gt', "
                                                           "and 'lt'",
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'date',
                                          'type': 'date'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-careplan'],
                         'type': 'CarePlan'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'CareTeam '
                                                                              'Profile'}]}],
                         'extension': [{'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'status'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core careteam '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core careteam by '
                                                           'id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'careteam instance '
                                                           'over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core careteam '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/CareTeam-Patient',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'patient',
                                          'type': 'reference'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/CareTeam-Status',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'status',
                                          'type': 'token'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-careteam'],
                         'type': 'CareTeam'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'Condition '
                                                                              'Profile'}]}],
                         'extension': [{'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'clinicalstatus'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'},
                                       {'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'category'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core condition '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core condition by '
                                                           'id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'condition instance '
                                                           'over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core condition '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/Condition-Patient',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'patient',
                                          'type': 'reference'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Condition-Category',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}],
                                          'name': 'category',
                                          'type': 'token'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Condition-ClinicalStatus',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}],
                                          'name': 'clinicalstatus',
                                          'type': 'token'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-condition'],
                         'type': 'Condition'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'Device '
                                                                              'Profile'}]}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core device '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core device by id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'device instance '
                                                           'over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core device '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/Device-Patient',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'patient',
                                          'type': 'reference'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-device'],
                         'type': 'Device'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'DocumentReference '
                                                                              'Profile'}]}],
                         'extension': [{'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'date'},
                                                      {'url': 'required',
                                                       'valueString': 'type'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core '
                                                           'DocumentReference '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core '
                                                           'DocumentReference '
                                                           'by id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'DocumentReference '
                                                           'instance over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core '
                                                           'DocumentReference '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/DocumentReference-Patient',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'patient',
                                          'type': 'reference'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/DocumentReference-Date',
                                          'documentation': 'The server SHALL '
                                                           'support the date '
                                                           'search modifiers '
                                                           "'ge','le','gt', "
                                                           "and 'lt'",
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'date',
                                          'type': 'date'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/DocumentReference-Type',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'type',
                                          'type': 'token'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-documentreference'],
                         'type': 'DocumentReference'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'Encounter '
                                                                              'Profile'}]}],
                         'extension': [{'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'date'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core Encounter '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core Encounter by '
                                                           'id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'Encounter instance '
                                                           'over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core Encounter '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/Encounter-Patient',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'patient',
                                          'type': 'reference'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Encounter-Date',
                                          'documentation': 'The server SHALL '
                                                           'support the date '
                                                           'search modifiers '
                                                           "'ge','le','gt', "
                                                           "and 'lt'",
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'date',
                                          'type': 'date'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-encounter'],
                         'type': 'Encounter'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'Goal '
                                                                              'Profile'}]}],
                         'extension': [{'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'date'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core Goal '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core Goal by id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'Goal instance over '
                                                           'time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core Goal instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/Goal-Patient',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'patient',
                                          'type': 'reference'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Goal-Date',
                                          'documentation': 'The server SHALL '
                                                           'support the date '
                                                           'search modifiers '
                                                           "'ge','le','gt', "
                                                           "and 'lt'",
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'date',
                                          'type': 'date'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-goal'],
                         'type': 'Goal'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'Immunization '
                                                                              'Profile'}]}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core immunization '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core immunization '
                                                           'by id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'immunization '
                                                           'instance over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core immunization '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/Immunization-Patient',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'patient',
                                          'type': 'reference'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-immunization'],
                         'type': 'Immunization'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'DiagnosticReport '
                                                                              'Profile'}]}],
                         'extension': [{'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'category'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'},
                                       {'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'category'},
                                                      {'url': 'required',
                                                       'valueString': 'date'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'},
                                       {'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'category'},
                                                      {'url': 'required',
                                                       'valueString': 'code'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'},
                                       {'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'category'},
                                                      {'url': 'required',
                                                       'valueString': 'code'},
                                                      {'url': 'required',
                                                       'valueString': 'date'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core '
                                                           'diagnosticreport '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core '
                                                           'diagnosticreport '
                                                           'by id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'diagnosticreport '
                                                           'instance over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core '
                                                           'diagnosticreport '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/DiagnosticReport-Patient',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'patient',
                                          'type': 'reference'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/DiagnosticReport-Category',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'category',
                                          'type': 'token'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/DiagnosticReport-Code',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'code',
                                          'type': 'token'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/DiagnosticReport-Date',
                                          'documentation': 'The server SHALL '
                                                           'support the date '
                                                           'search modifiers '
                                                           "'ge','le','gt', "
                                                           "and 'lt'",
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'date',
                                          'type': 'date'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-diagnosticreport'],
                         'type': 'DiagnosticReport'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'Location '
                                                                              'Profile'}]}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core location '
                                                           'resources using '
                                                           'different search '
                                                           'criteria.',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core location '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'Medication '
                                                           'instance over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core Medication '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/Location-Name',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'name',
                                          'type': 'string'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Location-Address',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'address',
                                          'type': 'string'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-location'],
                         'type': 'Location'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'Medication '
                                                                              'Profile'}]}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'IF the Medication '
                                                           'Resource is used '
                                                           'in a '
                                                           'MedicationStatement '
                                                           'or a '
                                                           'MedicationRequest.   '
                                                           'Allows discovery '
                                                           'of existing US '
                                                           'Core Medication '
                                                           'resources using '
                                                           'different search '
                                                           'criteria.',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'read',
                                          'documentation': 'IF the Medication '
                                                           'Resource is used '
                                                           'in a '
                                                           'MedicationStatement '
                                                           'or a '
                                                           'MedicationRequest.  '
                                                           'Allows retrieval '
                                                           'of a specific US '
                                                           'Core Medication by '
                                                           'id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'Medication '
                                                           'instance over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core Medication '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-medication'],
                         'type': 'Medication'},
                        {'_searchInclude': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                            'valueCode': 'MAY'}]}],
                         '_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'MedicationStatement '
                                                                              'Profile'}]}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core '
                                                           'medicationstatement '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core '
                                                           'medicationstatement '
                                                           'by id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'medicationstatement '
                                                           'instance over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core '
                                                           'medicationstatement '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchInclude': ['MedicationStatement.medicationReference'],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/MedicationStatement-Patient',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'patient',
                                          'type': 'reference'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-medicationstatement'],
                         'type': 'MedicationStatement'},
                        {'_searchInclude': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                            'valueCode': 'MAY'}]}],
                         '_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'MedicationRequest '
                                                                              'Profile'}]}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core '
                                                           'medicationrequest '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core '
                                                           'medicationrequest '
                                                           'by id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'medicationrequest '
                                                           'instance over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core '
                                                           'medicationrequest '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchInclude': ['MedicationRequest.medicationReference'],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/MedicationRequest-Patient',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'patient',
                                          'type': 'reference'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-medicationrequest'],
                         'type': 'MedicationRequest'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'Result '
                                                                              'Observation '
                                                                              'Profile'}]},
                                               {'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'Vital '
                                                                              'Signs '
                                                                              'Profile'}]},
                                               {'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'Smoking '
                                                                              'Status '
                                                                              'Observation '
                                                                              'Profile'}]}],
                         'extension': [{'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'category'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'},
                                       {'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'category'},
                                                      {'url': 'required',
                                                       'valueString': 'date'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'},
                                       {'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'category'},
                                                      {'url': 'required',
                                                       'valueString': 'code'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'},
                                       {'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'category'},
                                                      {'url': 'required',
                                                       'valueString': 'code'},
                                                      {'url': 'required',
                                                       'valueString': 'date'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core results '
                                                           'observation, '
                                                           'smokingstatus, and '
                                                           'vitals signs '
                                                           'observation using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core results '
                                                           'observation, '
                                                           'smokingstatus, and '
                                                           'vitals signs '
                                                           'observation by id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'results '
                                                           'observation, '
                                                           'smokingstatus, and '
                                                           'vitals signs '
                                                           'observation over '
                                                           'time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core results '
                                                           'observation, '
                                                           'smokingstatus, and '
                                                           'vitals signs '
                                                           'observation '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/Observation-Patient',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'patient',
                                          'type': 'reference'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Organization-Category',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'category',
                                          'type': 'token'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Organization-Code',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'code',
                                          'type': 'token'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Organization-Date',
                                          'documentation': 'The server SHALL '
                                                           'support the date '
                                                           'search modifiers '
                                                           "'ge','le','gt', "
                                                           "and 'lt'",
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'date',
                                          'type': 'date'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-observationresults',
                                              'http://hl7.org/fhir/StructureDefinition/vitalsigns',
                                              'http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-smokingstatus'],
                         'type': 'Observation'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'Organization '
                                                                              'Profile'}]}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core organization '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core organization '
                                                           'by id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'organization '
                                                           'instance over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core organization '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/Organization-Identifier',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'identifier',
                                          'type': 'token'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Organization-Name',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'name',
                                          'type': 'string'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Organization-Address',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'address',
                                          'type': 'string'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-organization'],
                         'type': 'Organization'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'Practitioner '
                                                                              'Profile'}]}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core practitioner '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core practitioner '
                                                           'by id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'practitioner '
                                                           'instance over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core practitioner '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/Practitioner-Identifier',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'identifier',
                                          'type': 'token'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Practitioner-Name',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'name',
                                          'type': 'string'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-practitioner'],
                         'type': 'Practitioner'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'PractitionerRole '
                                                                              'Profile'}]}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core '
                                                           'PractitionerRole '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core '
                                                           'PractitionerRole '
                                                           'by id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'PractitionerRole '
                                                           'instance over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core '
                                                           'PractitionerRole '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/PractitionerRole-Identifier',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'identifier',
                                          'type': 'token'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/PractitionerRole-Name',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'name',
                                          'type': 'string'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/PractitionerRole-Specialty',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'speciality',
                                          'type': 'token'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-practitionerrole'],
                         'type': 'PractitionerRole'},
                        {'_supportedProfile': [{'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/display',
                                                               'valueString': 'US '
                                                                              'Core '
                                                                              'Procedure '
                                                                              'Profile'}]}],
                         'extension': [{'extension': [{'url': 'required',
                                                       'valueString': 'patient'},
                                                      {'url': 'required',
                                                       'valueString': 'date'}],
                                        'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'}],
                         'interaction': [{'code': 'search-type',
                                          'documentation': 'Allows discovery '
                                                           'of existing US '
                                                           'Core procedure '
                                                           'resources using '
                                                           'different search '
                                                           'criteria',
                                                           'valueCode': 'SHALL'}]},
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                         {'code': 'read',
                                          'documentation': 'Allows retrieval '
                                                           'of a specific US '
                                                           'Core procedure by '
                                                           'id',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}]},
                                         {'code': 'history-instance',
                                          'documentation': 'Allows review of '
                                                           'changes to US Core '
                                                           'procedure instance '
                                                           'over time',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]},
                                         {'code': 'vread',
                                          'documentation': 'Allows retrieval '
                                                           'of a historical '
                                                           'version of a US '
                                                           'Core procedure '
                                                           'instance',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHOULD'}]}],
                         'searchParam': [{'definition': 'http://hl7.org/fhir/SearchParameter/Procedure-Patient',
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'patient',
                                          'type': 'reference'},
                                         {'definition': 'http://hl7.org/fhir/SearchParameter/Procedure-Date',
                                          'documentation': 'The server SHALL '
                                                           'support the date '
                                                           'search modifiers '
                                                           "'ge','le','gt', "
                                                           "and 'lt'",
                                          'extension': [{'url': 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation',
                                                         'valueCode': 'SHALL'}],
                                          'name': 'date',
                                          'type': 'date'}],
                         'supportedProfile': ['http://hl7.org/fhir/us/core-r4/StructureDefinition/us-core-procedure'],
                         'type': 'Procedure'}],
           'security': {'description': 'US Core Servers **SHALL**:\n'
                                       '\n'
                                       '1.  Implement the [security '
                                       'requirements](security.html) '
                                       'documented in\n'
                                       '    the this IG.\n'
                                       '2.  A server has ensured that every '
                                       'API request includes a valid\n'
                                       '    Authorization token, supplied via: '
                                       '`Authorization: Bearer\n'
                                       '    {server-specific-token-here}`\n'
                                       '3.  A server has rejected any '
                                       'unauthorized requests by returning an\n'
                                       '    `HTTP 401` unauthorized response '
                                       'code.'}}],
 'status': 'active',
 'title': 'US Core Server',
 'url': 'http://hl7.org/fhir/us/core-r4/CapabilityStatement/us-core-r4-server',
 'version': '2.0.0'}

if __name__ == "__main__": # test dict
    # round trip
    csjs = dumps(cs, indent=3)
    print(csjs)
    pprint(loads(csjs))
