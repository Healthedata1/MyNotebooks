#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Location) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class Location(domainresource.DomainResource):
    """ Details and position information for a physical place.
    
    Details and position information for a physical place where services are
    provided and resources and participants may be stored, found, contained, or
    accommodated.
    """
    
    resource_type = "Location"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        
        """ Physical location.
        Type `Address` (represented as `dict` in JSON). """
        
        self.alias = None
        
        """ A list of alternate names that the location is known as or was
        known as in the past.
        List of `str` items. """
        
        self._alias = None
        
        """ extension for fhir primitive  alias"""
        
        self.availabilityExceptions = None
        
        """ Description of availability exceptions.
        Type `str`. """
        
        self._availabilityExceptions = None
        
        """ extension for fhir primitive  availabilityExceptions"""
        
        self.description = None
        
        """ Additional details about the location that could be displayed as
        further information to identify the location beyond its name.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.endpoint = None
        
        """ Technical endpoints providing access to services operated for the
        location.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.hoursOfOperation = None
        
        """ What days/times during a week is this location usually open.
        List of `LocationHoursOfOperation` items (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Unique code or number identifying the location to its users.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        
        """ Organization responsible for provisioning and upkeep.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.mode = None
        
        """ instance | kind.
        Type `str`. """
        
        self._mode = None
        
        """ extension for fhir primitive  mode"""
        
        self.name = None
        
        """ Name of the location as used by humans.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.operationalStatus = None
        
        """ The Operational status of the location (typically only for a
        bed/room).
        Type `Coding` (represented as `dict` in JSON). """
        
        self.partOf = None
        
        """ Another Location this one is physically part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.physicalType = None
        
        """ Physical form of the location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.position = None
        
        """ The absolute geographic location.
        Type `LocationPosition` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | suspended | inactive.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.telecom = None
        
        """ Contact details of the location.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Type of function performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Location, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Location, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("_alias", "_alias",fhirprimitive.FHIRPrimitive, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("_availabilityExceptions", "_availabilityExceptions",fhirprimitive.FHIRPrimitive, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("hoursOfOperation", "hoursOfOperation", LocationHoursOfOperation, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("mode", "mode", str, False, None, False),
            ("_mode", "_mode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("operationalStatus", "operationalStatus", coding.Coding, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("physicalType", "physicalType", codeableconcept.CodeableConcept, False, None, False),
            ("position", "position", LocationPosition, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class LocationHoursOfOperation(backboneelement.BackboneElement):
    """ What days/times during a week is this location usually open.
    """
    
    resource_type = "LocationHoursOfOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allDay = None
        
        """ The Location is open all day.
        Type `bool`. """
        
        self._allDay = None
        
        """ extension for fhir primitive  allDay"""
        
        self.closingTime = None
        
        """ Time that the Location closes.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.daysOfWeek = None
        
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """
        
        self._daysOfWeek = None
        
        """ extension for fhir primitive  daysOfWeek"""
        
        self.openingTime = None
        
        """ Time that the Location opens.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(LocationHoursOfOperation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(LocationHoursOfOperation, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("_allDay", "_allDay",fhirprimitive.FHIRPrimitive, False, None, False),
            ("closingTime", "closingTime", fhirdate.FHIRDate, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
            ("_daysOfWeek", "_daysOfWeek",fhirprimitive.FHIRPrimitive, False, None, False),
            ("openingTime", "openingTime", fhirdate.FHIRDate, False, None, False),
        ])
        return js


class LocationPosition(backboneelement.BackboneElement):
    """ The absolute geographic location.
    
    The absolute geographic location of the Location, expressed using the WGS84
    datum (This is the same co-ordinate system used in KML).
    """
    
    resource_type = "LocationPosition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.altitude = None
        
        """ Altitude with WGS84 datum.
        Type `float`. """
        
        self._altitude = None
        
        """ extension for fhir primitive  altitude"""
        
        self.latitude = None
        
        """ Latitude with WGS84 datum.
        Type `float`. """
        
        self._latitude = None
        
        """ extension for fhir primitive  latitude"""
        
        self.longitude = None
        
        """ Longitude with WGS84 datum.
        Type `float`. """
        
        self._longitude = None
        
        """ extension for fhir primitive  longitude"""
        
        super(LocationPosition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(LocationPosition, self).elementProperties()
        js.extend([
            ("altitude", "altitude", float, False, None, False),
            ("_altitude", "_altitude",fhirprimitive.FHIRPrimitive, False, None, False),
            ("latitude", "latitude", float, False, None, True),
            ("_latitude", "_latitude",fhirprimitive.FHIRPrimitive, False, None, False),
            ("longitude", "longitude", float, False, None, True),
            ("_longitude", "_longitude",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import address
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier
from . import fhirprimitive

