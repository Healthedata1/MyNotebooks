#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/RiskAssessment) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class RiskAssessment(domainresource.DomainResource):
    """ Potential outcomes for a subject with likelihood.
    
    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """
    
    resource_type = "RiskAssessment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        
        """ Request fulfilled by this assessment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.basis = None
        
        """ Information used in assessment.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.code = None
        
        """ Type of assessment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.condition = None
        
        """ Condition assessed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.context = None
        
        """ Where was assessment performed?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Unique identifier for the assessment.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.method = None
        
        """ Evaluation mechanism.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.mitigation = None
        
        """ How to reduce risk.
        Type `str`. """
        
        self._mitigation = None
        
        """ extension for fhir primitive  mitigation"""
        
        self.note = None
        
        """ Comments on the risk assessment.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        
        """ When was assessment made?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        
        """ When was assessment made?.
        Type `Period` (represented as `dict` in JSON). """
        
        self.parent = None
        
        """ Part of this occurrence.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        
        """ Who did assessment?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.prediction = None
        
        """ Outcome predicted.
        List of `RiskAssessmentPrediction` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        
        """ Why the assessment was necessary?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        
        """ Why the assessment was necessary?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        
        """ registered | preliminary | final | amended +.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subject = None
        
        """ Who/what does assessment apply to?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(RiskAssessment, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RiskAssessment, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, False, None, False),
            ("basis", "basis", fhirreference.FHIRReference, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("condition", "condition", fhirreference.FHIRReference, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("mitigation", "mitigation", str, False, None, False),
            ("_mitigation", "_mitigation",fhirprimitive.FHIRPrimitive, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("prediction", "prediction", RiskAssessmentPrediction, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import backboneelement

class RiskAssessmentPrediction(backboneelement.BackboneElement):
    """ Outcome predicted.
    
    Describes the expected outcome for the subject.
    """
    
    resource_type = "RiskAssessmentPrediction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.outcome = None
        
        """ Possible outcome for the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.probabilityDecimal = None
        
        """ Likelihood of specified outcome.
        Type `float`. """
        
        self._probabilityDecimal = None
        
        """ extension for fhir primitive  probabilityDecimal"""
        
        self.probabilityRange = None
        
        """ Likelihood of specified outcome.
        Type `Range` (represented as `dict` in JSON). """
        
        self.qualitativeRisk = None
        
        """ Likelihood of specified outcome as a qualitative value.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.rationale = None
        
        """ Explanation of prediction.
        Type `str`. """
        
        self._rationale = None
        
        """ extension for fhir primitive  rationale"""
        
        self.relativeRisk = None
        
        """ Relative likelihood.
        Type `float`. """
        
        self._relativeRisk = None
        
        """ extension for fhir primitive  relativeRisk"""
        
        self.whenPeriod = None
        
        """ Timeframe or age range.
        Type `Period` (represented as `dict` in JSON). """
        
        self.whenRange = None
        
        """ Timeframe or age range.
        Type `Range` (represented as `dict` in JSON). """
        
        super(RiskAssessmentPrediction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RiskAssessmentPrediction, self).elementProperties()
        js.extend([
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("probabilityDecimal", "probabilityDecimal", float, False, "probability", False),
            ("_probabilityDecimal", "_probabilityDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("probabilityRange", "probabilityRange", range.Range, False, "probability", False),
            ("qualitativeRisk", "qualitativeRisk", codeableconcept.CodeableConcept, False, None, False),
            ("rationale", "rationale", str, False, None, False),
            ("_rationale", "_rationale",fhirprimitive.FHIRPrimitive, False, None, False),
            ("relativeRisk", "relativeRisk", float, False, None, False),
            ("_relativeRisk", "_relativeRisk",fhirprimitive.FHIRPrimitive, False, None, False),
            ("whenPeriod", "whenPeriod", period.Period, False, "when", False),
            ("whenRange", "whenRange", range.Range, False, "when", False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import range
from . import fhirprimitive

