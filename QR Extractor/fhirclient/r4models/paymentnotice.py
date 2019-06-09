#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/PaymentNotice) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class PaymentNotice(domainresource.DomainResource):
    """ PaymentNotice request.
    
    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """
    
    resource_type = "PaymentNotice"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
        
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.paymentStatus = None
        
        """ Whether payment has been sent or cleared.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provider = None
        
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.request = None
        
        """ Request reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.response = None
        
        """ Response reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.statusDate = None
        
        """ Payment or clearing date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.target = None
        
        """ Insurer or Regulatory body.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(PaymentNotice, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PaymentNotice, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("paymentStatus", "paymentStatus", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import fhirprimitive

