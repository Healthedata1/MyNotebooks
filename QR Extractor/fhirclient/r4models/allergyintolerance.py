#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/AllergyIntolerance) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class AllergyIntolerance(domainresource.DomainResource):
    """ Allergy or Intolerance (generally: Risk of adverse reaction to a substance).
    
    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """
    
    resource_type = "AllergyIntolerance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.asserter = None
        
        """ Source of the information about the allergy.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.category = None
        
        """ food | medication | environment | biologic.
        List of `str` items. """
        
        self._category = None
        
        """ extension for fhir primitive  category"""
        
        self.clinicalStatus = None
        
        """ active | inactive | resolved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        
        """ Code that identifies the allergy or intolerance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.criticality = None
        
        """ low | high | unable-to-assess.
        Type `str`. """
        
        self._criticality = None
        
        """ extension for fhir primitive  criticality"""
        
        self.encounter = None
        
        """ Encounter when the allergy or intolerance was asserted.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ External ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lastOccurrence = None
        
        """ Date(/time) of last known occurrence of a reaction.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.note = None
        
        """ Additional text not captured in other fields.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.onsetAge = None
        
        """ When allergy or intolerance was identified.
        Type `Age` (represented as `dict` in JSON). """
        
        self.onsetDateTime = None
        
        """ When allergy or intolerance was identified.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.onsetPeriod = None
        
        """ When allergy or intolerance was identified.
        Type `Period` (represented as `dict` in JSON). """
        
        self.onsetRange = None
        
        """ When allergy or intolerance was identified.
        Type `Range` (represented as `dict` in JSON). """
        
        self.onsetString = None
        
        """ When allergy or intolerance was identified.
        Type `str`. """
        
        self._onsetString = None
        
        """ extension for fhir primitive  onsetString"""
        
        self.patient = None
        
        """ Who the sensitivity is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reaction = None
        
        """ Adverse Reaction Events linked to exposure to substance.
        List of `AllergyIntoleranceReaction` items (represented as `dict` in JSON). """
        
        self.recordedDate = None
        
        """ Date record was first recorded.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.recorder = None
        
        """ Who recorded the sensitivity.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ allergy | intolerance - Underlying mechanism (if known).
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.verificationStatus = None
        
        """ unconfirmed | confirmed | refuted | entered-in-error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(AllergyIntolerance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AllergyIntolerance, self).elementProperties()
        js.extend([
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("category", "category", str, True, None, False),
            ("_category", "_category",fhirprimitive.FHIRPrimitive, False, None, False),
            ("clinicalStatus", "clinicalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("criticality", "criticality", str, False, None, False),
            ("_criticality", "_criticality",fhirprimitive.FHIRPrimitive, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lastOccurrence", "lastOccurrence", fhirdate.FHIRDate, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onsetAge", "onsetAge", age.Age, False, "onset", False),
            ("onsetDateTime", "onsetDateTime", fhirdate.FHIRDate, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("_onsetString", "_onsetString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("reaction", "reaction", AllergyIntoleranceReaction, True, None, False),
            ("recordedDate", "recordedDate", fhirdate.FHIRDate, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
            ("verificationStatus", "verificationStatus", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class AllergyIntoleranceReaction(backboneelement.BackboneElement):
    """ Adverse Reaction Events linked to exposure to substance.
    
    Details about each adverse reaction event linked to exposure to the
    identified substance.
    """
    
    resource_type = "AllergyIntoleranceReaction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ Description of the event as a whole.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.exposureRoute = None
        
        """ How the subject was exposed to the substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manifestation = None
        
        """ Clinical symptoms/signs associated with the Event.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note = None
        
        """ Text about event not captured in other fields.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.onset = None
        
        """ Date(/time) when manifestations showed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.severity = None
        
        """ mild | moderate | severe (of event as a whole).
        Type `str`. """
        
        self._severity = None
        
        """ extension for fhir primitive  severity"""
        
        self.substance = None
        
        """ Specific substance or pharmaceutical product considered to be
        responsible for event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(AllergyIntoleranceReaction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AllergyIntoleranceReaction, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("exposureRoute", "exposureRoute", codeableconcept.CodeableConcept, False, None, False),
            ("manifestation", "manifestation", codeableconcept.CodeableConcept, True, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onset", "onset", fhirdate.FHIRDate, False, None, False),
            ("severity", "severity", str, False, None, False),
            ("_severity", "_severity",fhirprimitive.FHIRPrimitive, False, None, False),
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import age
from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import range
from . import fhirprimitive

