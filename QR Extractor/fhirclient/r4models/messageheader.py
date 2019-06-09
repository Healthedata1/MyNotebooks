#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/MessageHeader) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class MessageHeader(domainresource.DomainResource):
    """ A resource that describes a message that is exchanged between systems.
    
    The header for a message exchange that is either requesting or responding
    to an action.  The reference(s) that are the subject of the action as well
    as other information related to the action are typically transmitted in a
    bundle in which the MessageHeader resource instance is the first resource
    in the bundle.
    """
    
    resource_type = "MessageHeader"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        
        """ The source of the decision.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.definition = None
        
        """ Link to the definition for this message.
        Type `str`. """
        
        self._definition = None
        
        """ extension for fhir primitive  definition"""
        
        self.destination = None
        
        """ Message destination application(s).
        List of `MessageHeaderDestination` items (represented as `dict` in JSON). """
        
        self.enterer = None
        
        """ The source of the data entry.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.eventCoding = None
        
        """ Code for the event this message represents or link to event
        definition.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.eventUri = None
        
        """ Code for the event this message represents or link to event
        definition.
        Type `str`. """
        
        self._eventUri = None
        
        """ extension for fhir primitive  eventUri"""
        
        self.focus = None
        
        """ The actual content of the message.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.reason = None
        
        """ Cause of event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.response = None
        
        """ If this is a reply to prior message.
        Type `MessageHeaderResponse` (represented as `dict` in JSON). """
        
        self.responsible = None
        
        """ Final responsibility for event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sender = None
        
        """ Real world sender of the message.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.source = None
        
        """ Message source application.
        Type `MessageHeaderSource` (represented as `dict` in JSON). """
        
        super(MessageHeader, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageHeader, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("definition", "definition", str, False, None, False),
            ("_definition", "_definition",fhirprimitive.FHIRPrimitive, False, None, False),
            ("destination", "destination", MessageHeaderDestination, True, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("eventCoding", "eventCoding", coding.Coding, False, "event", True),
            ("eventUri", "eventUri", str, False, "event", True),
            ("_eventUri", "_eventUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, True, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("response", "response", MessageHeaderResponse, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("source", "source", MessageHeaderSource, False, None, True),
        ])
        return js


from . import backboneelement

class MessageHeaderDestination(backboneelement.BackboneElement):
    """ Message destination application(s).
    
    The destination application which the message is intended for.
    """
    
    resource_type = "MessageHeaderDestination"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.endpoint = None
        
        """ Actual destination address or id.
        Type `str`. """
        
        self._endpoint = None
        
        """ extension for fhir primitive  endpoint"""
        
        self.name = None
        
        """ Name of system.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.receiver = None
        
        """ Intended "real-world" recipient for the data.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.target = None
        
        """ Particular delivery destination within the destination.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MessageHeaderDestination, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageHeaderDestination, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", str, False, None, True),
            ("_endpoint", "_endpoint",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class MessageHeaderResponse(backboneelement.BackboneElement):
    """ If this is a reply to prior message.
    
    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """
    
    resource_type = "MessageHeaderResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ ok | transient-error | fatal-error.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.details = None
        
        """ Specific list of hints/warnings/errors.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Id of original message.
        Type `str`. """
        
        self._identifier = None
        
        """ extension for fhir primitive  identifier"""
        
        super(MessageHeaderResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageHeaderResponse, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("details", "details", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", str, False, None, True),
            ("_identifier", "_identifier",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class MessageHeaderSource(backboneelement.BackboneElement):
    """ Message source application.
    
    The source application from which this message originated.
    """
    
    resource_type = "MessageHeaderSource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        
        """ Human contact for problems.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.endpoint = None
        
        """ Actual message source address or id.
        Type `str`. """
        
        self._endpoint = None
        
        """ extension for fhir primitive  endpoint"""
        
        self.name = None
        
        """ Name of system.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.software = None
        
        """ Name of software running the system.
        Type `str`. """
        
        self._software = None
        
        """ extension for fhir primitive  software"""
        
        self.version = None
        
        """ Version of software running.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(MessageHeaderSource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageHeaderSource, self).elementProperties()
        js.extend([
            ("contact", "contact", contactpoint.ContactPoint, False, None, False),
            ("endpoint", "endpoint", str, False, None, True),
            ("_endpoint", "_endpoint",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("software", "software", str, False, None, False),
            ("_software", "_software",fhirprimitive.FHIRPrimitive, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirreference
from . import fhirprimitive

