#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ActivityDefinition) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class ActivityDefinition(domainresource.DomainResource):
    """ The definition of a specific activity to be taken, independent of any
    particular patient or context.
    
    This resource allows for the definition of some activity to be performed,
    independent of a particular patient, practitioner, or other performance
    context.
    """
    
    resource_type = "ActivityDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        
        """ When the activity definition was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.author = None
        
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        
        """ What part of body to perform on.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        
        """ Detail type of activity.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contact = None
        
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self._copyright = None
        
        """ extension for fhir primitive  copyright"""
        
        self.date = None
        
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        
        """ Natural language description of the activity definition.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.doNotPerform = None
        
        """ True if the activity should not be performed.
        Type `bool`. """
        
        self._doNotPerform = None
        
        """ extension for fhir primitive  doNotPerform"""
        
        self.dosage = None
        
        """ Detailed dosage instructions.
        List of `Dosage` items (represented as `dict` in JSON). """
        
        self.dynamicValue = None
        
        """ Dynamic aspects of the definition.
        List of `ActivityDefinitionDynamicValue` items (represented as `dict` in JSON). """
        
        self.editor = None
        
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.effectivePeriod = None
        
        """ When the activity definition is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.endorser = None
        
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.identifier = None
        
        """ Additional identifier for the activity definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.intent = None
        
        """ proposal | plan | order.
        Type `str`. """
        
        self._intent = None
        
        """ extension for fhir primitive  intent"""
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for activity definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.kind = None
        
        """ Kind of resource.
        Type `str`. """
        
        self._kind = None
        
        """ extension for fhir primitive  kind"""
        
        self.lastReviewDate = None
        
        """ When the activity definition was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.library = None
        
        """ Logic used by the activity definition.
        List of `str` items. """
        
        self._library = None
        
        """ extension for fhir primitive  library"""
        
        self.location = None
        
        """ Where it should happen.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Name for this activity definition (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.observationRequirement = None
        
        """ What observations are required to perform this action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.observationResultRequirement = None
        
        """ What observations must be produced by this action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.participant = None
        
        """ Who should participate in the action.
        List of `ActivityDefinitionParticipant` items (represented as `dict` in JSON). """
        
        self.priority = None
        
        """ routine | urgent | asap | stat.
        Type `str`. """
        
        self._priority = None
        
        """ extension for fhir primitive  priority"""
        
        self.productCodeableConcept = None
        
        """ What's administered/supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productReference = None
        
        """ What's administered/supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.profile = None
        
        """ What profile the resource needs to conform to.
        Type `str`. """
        
        self._profile = None
        
        """ extension for fhir primitive  profile"""
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this activity definition is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.quantity = None
        
        """ How much is administered/consumed/supplied.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.relatedArtifact = None
        
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.reviewer = None
        
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.specimenRequirement = None
        
        """ What specimens are required to perform this action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subjectCodeableConcept = None
        
        """ Type of individual the activity definition is intended for.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        
        """ Type of individual the activity definition is intended for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subtitle = None
        
        """ Subordinate title of the activity definition.
        Type `str`. """
        
        self._subtitle = None
        
        """ extension for fhir primitive  subtitle"""
        
        self.timingAge = None
        
        """ When activity is to occur.
        Type `Age` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        
        """ When activity is to occur.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingDuration = None
        
        """ When activity is to occur.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.timingPeriod = None
        
        """ When activity is to occur.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingRange = None
        
        """ When activity is to occur.
        Type `Range` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        
        """ When activity is to occur.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.title = None
        
        """ Name for this activity definition (human friendly).
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.topic = None
        
        """ E.g. Education, Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.transform = None
        
        """ Transform to apply the template.
        Type `str`. """
        
        self._transform = None
        
        """ extension for fhir primitive  transform"""
        
        self.url = None
        
        """ Canonical identifier for this activity definition, represented as a
        URI (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.usage = None
        
        """ Describes the clinical usage of the activity definition.
        Type `str`. """
        
        self._usage = None
        
        """ extension for fhir primitive  usage"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the activity definition.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(ActivityDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ActivityDefinition, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright",fhirprimitive.FHIRPrimitive, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("_doNotPerform", "_doNotPerform",fhirprimitive.FHIRPrimitive, False, None, False),
            ("dosage", "dosage", dosage.Dosage, True, None, False),
            ("dynamicValue", "dynamicValue", ActivityDefinitionDynamicValue, True, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("intent", "intent", str, False, None, False),
            ("_intent", "_intent",fhirprimitive.FHIRPrimitive, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, False),
            ("_kind", "_kind",fhirprimitive.FHIRPrimitive, False, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("_library", "_library",fhirprimitive.FHIRPrimitive, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("observationRequirement", "observationRequirement", fhirreference.FHIRReference, True, None, False),
            ("observationResultRequirement", "observationResultRequirement", fhirreference.FHIRReference, True, None, False),
            ("participant", "participant", ActivityDefinitionParticipant, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority",fhirprimitive.FHIRPrimitive, False, None, False),
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False),
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False),
            ("profile", "profile", str, False, None, False),
            ("_profile", "_profile",fhirprimitive.FHIRPrimitive, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("specimenRequirement", "specimenRequirement", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("_subtitle", "_subtitle",fhirprimitive.FHIRPrimitive, False, None, False),
            ("timingAge", "timingAge", age.Age, False, "timing", False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingRange", "timingRange", range.Range, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("_title", "_title",fhirprimitive.FHIRPrimitive, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("transform", "transform", str, False, None, False),
            ("_transform", "_transform",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("_usage", "_usage",fhirprimitive.FHIRPrimitive, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class ActivityDefinitionDynamicValue(backboneelement.BackboneElement):
    """ Dynamic aspects of the definition.
    
    Dynamic values that will be evaluated to produce values for elements of the
    resulting resource. For example, if the dosage of a medication must be
    computed based on the patient's weight, a dynamic value would be used to
    specify an expression that calculated the weight, and the path on the
    request resource that would contain the result.
    """
    
    resource_type = "ActivityDefinitionDynamicValue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
        
        """ An expression that provides the dynamic value for the customization.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.path = None
        
        """ The path to the element to be set dynamically.
        Type `str`. """
        
        self._path = None
        
        """ extension for fhir primitive  path"""
        
        super(ActivityDefinitionDynamicValue, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ActivityDefinitionDynamicValue, self).elementProperties()
        js.extend([
            ("expression", "expression", expression.Expression, False, None, True),
            ("path", "path", str, False, None, True),
            ("_path", "_path",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ActivityDefinitionParticipant(backboneelement.BackboneElement):
    """ Who should participate in the action.
    
    Indicates who should participate in performing the action described.
    """
    
    resource_type = "ActivityDefinitionParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.role = None
        
        """ E.g. Nurse, Surgeon, Parent, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ patient | practitioner | related-person | device.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(ActivityDefinitionParticipant, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ActivityDefinitionParticipant, self).elementProperties()
        js.extend([
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import age
from . import codeableconcept
from . import contactdetail
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import relatedartifact
from . import timing
from . import usagecontext
from . import fhirprimitive

