#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/EnrollmentRequest) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class EnrollmentRequest(domainresource.DomainResource):
    """ Enrol in coverage.
    
    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """
    
    resource_type = "EnrollmentRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.candidate = None
        
        """ The subject to be enrolled.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.coverage = None
        
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.created = None
        
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurer = None
        
        """ Target.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.provider = None
        
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        super(EnrollmentRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EnrollmentRequest, self).elementProperties()
        js.extend([
            ("candidate", "candidate", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import fhirdate
from . import fhirreference
from . import identifier
from . import fhirprimitive

