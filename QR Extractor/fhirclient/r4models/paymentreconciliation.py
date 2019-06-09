#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class PaymentReconciliation(domainresource.DomainResource):
    """ PaymentReconciliation resource.
    
    This resource provides payment details and claim references supporting a
    bulk payment.
    """
    
    resource_type = "PaymentReconciliation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
        
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
        
        """ List of settlements.
        List of `PaymentReconciliationDetail` items (represented as `dict` in JSON). """
        
        self.disposition = None
        
        """ Disposition Message.
        Type `str`. """
        
        self._disposition = None
        
        """ extension for fhir primitive  disposition"""
        
        self.form = None
        
        """ Printed Form Identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organization = None
        
        """ Insurer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome = None
        
        """ queued | complete | error | partial.
        Type `str`. """
        
        self._outcome = None
        
        """ extension for fhir primitive  outcome"""
        
        self.period = None
        
        """ Period covered.
        Type `Period` (represented as `dict` in JSON). """
        
        self.processNote = None
        
        """ Processing comments.
        List of `PaymentReconciliationProcessNote` items (represented as `dict` in JSON). """
        
        self.request = None
        
        """ Claim reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.total = None
        
        """ Total amount of Payment.
        Type `Money` (represented as `dict` in JSON). """
        
        super(PaymentReconciliation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PaymentReconciliation, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("detail", "detail", PaymentReconciliationDetail, True, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("_disposition", "_disposition",fhirprimitive.FHIRPrimitive, False, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("_outcome", "_outcome",fhirprimitive.FHIRPrimitive, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("processNote", "processNote", PaymentReconciliationProcessNote, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("total", "total", money.Money, False, None, False),
        ])
        return js


from . import backboneelement

class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """ List of settlements.
    
    List of individual settlement amounts and the corresponding transaction.
    """
    
    resource_type = "PaymentReconciliationDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        
        """ Amount being paid.
        Type `Money` (represented as `dict` in JSON). """
        
        self.date = None
        
        """ Invoice date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.payee = None
        
        """ Organization which is receiving the payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.request = None
        
        """ Claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.response = None
        
        """ Claim Response.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.submitter = None
        
        """ Organization which submitted the claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Type code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(PaymentReconciliationDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PaymentReconciliationDetail, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("payee", "payee", fhirreference.FHIRReference, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("submitter", "submitter", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    """ Processing comments.
    
    Suite of notes.
    """
    
    resource_type = "PaymentReconciliationProcessNote"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.text = None
        
        """ Comment on the processing.
        Type `str`. """
        
        self._text = None
        
        """ extension for fhir primitive  text"""
        
        self.type = None
        
        """ display | print | printoper.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(PaymentReconciliationProcessNote, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PaymentReconciliationProcessNote, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("_text", "_text",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import fhirprimitive

