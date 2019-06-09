#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/GuidanceResponse) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class GuidanceResponse(domainresource.DomainResource):
    """ The formal response to a guidance request.
    
    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """
    
    resource_type = "GuidanceResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dataRequirement = None
        
        """ Additional required data.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.encounter = None
        
        """ Encounter during which the response was returned.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.evaluationMessage = None
        
        """ Messages resulting from the evaluation of the artifact or artifacts.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.moduleCanonical = None
        
        """ What guidance was requested.
        Type `str`. """
        
        self._moduleCanonical = None
        
        """ extension for fhir primitive  moduleCanonical"""
        
        self.moduleCodeableConcept = None
        
        """ What guidance was requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.moduleUri = None
        
        """ What guidance was requested.
        Type `str`. """
        
        self._moduleUri = None
        
        """ extension for fhir primitive  moduleUri"""
        
        self.note = None
        
        """ Additional notes about the response.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        
        """ When the guidance response was processed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.outputParameters = None
        
        """ The output parameters of the evaluation, if any.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        
        """ Device returning the guidance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        
        """ Why guidance is needed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        
        """ Why guidance is needed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requestIdentifier = None
        
        """ The identifier of the request associated with this response, if any.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.result = None
        
        """ Proposed actions, if any.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ success | data-requested | data-required | in-progress | failure |
        entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subject = None
        
        """ Patient the request was performed for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(GuidanceResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(GuidanceResponse, self).elementProperties()
        js.extend([
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("evaluationMessage", "evaluationMessage", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("moduleCanonical", "moduleCanonical", str, False, "module", True),
            ("_moduleCanonical", "_moduleCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("moduleCodeableConcept", "moduleCodeableConcept", codeableconcept.CodeableConcept, False, "module", True),
            ("moduleUri", "moduleUri", str, False, "module", True),
            ("_moduleUri", "_moduleUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, None, False),
            ("outputParameters", "outputParameters", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("requestIdentifier", "requestIdentifier", identifier.Identifier, False, None, False),
            ("result", "result", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import datarequirement
from . import fhirdate
from . import fhirreference
from . import identifier
from . import fhirprimitive

