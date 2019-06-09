#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Parameters) on 2018-12-20.
#  2018, SMART Health IT.


from . import resource

class Parameters(resource.Resource):
    """ Operation Request or Response.
    
    This resource is a non-persisted resource used to pass information into and
    back from an [operation](operations.html). It has no other use, and there
    is no RESTful endpoint associated with it.
    """
    
    resource_type = "Parameters"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.parameter = None
        
        """ Operation Parameter.
        List of `ParametersParameter` items (represented as `dict` in JSON). """
        
        super(Parameters, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Parameters, self).elementProperties()
        js.extend([
            ("parameter", "parameter", ParametersParameter, True, None, False),
        ])
        return js


from . import backboneelement

class ParametersParameter(backboneelement.BackboneElement):
    """ Operation Parameter.
    
    A parameter passed to or received from the operation.
    """
    
    resource_type = "ParametersParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        
        """ Name from the definition.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.part = None
        
        """ Named part of a multi-part parameter.
        List of `ParametersParameter` items (represented as `dict` in JSON). """
        
        self.resource = None
        
        """ If parameter is a whole resource.
        Type `Resource` (represented as `dict` in JSON). """
        
        self.valueAddress = None
        
        """ If parameter is a data type.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        
        """ If parameter is a data type.
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        
        """ If parameter is a data type.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        
        """ If parameter is a data type.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        
        """ If parameter is a data type.
        Type `str`. """
        
        self._valueBase64Binary = None
        
        """ extension for fhir primitive  valueBase64Binary"""
        
        self.valueBoolean = None
        
        """ If parameter is a data type.
        Type `bool`. """
        
        self._valueBoolean = None
        
        """ extension for fhir primitive  valueBoolean"""
        
        self.valueCanonical = None
        
        """ If parameter is a data type.
        Type `str`. """
        
        self._valueCanonical = None
        
        """ extension for fhir primitive  valueCanonical"""
        
        self.valueCode = None
        
        """ If parameter is a data type.
        Type `str`. """
        
        self._valueCode = None
        
        """ extension for fhir primitive  valueCode"""
        
        self.valueCodeableConcept = None
        
        """ If parameter is a data type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        
        """ If parameter is a data type.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
        
        """ If parameter is a data type.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        
        """ If parameter is a data type.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueContributor = None
        
        """ If parameter is a data type.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueCount = None
        
        """ If parameter is a data type.
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
        
        """ If parameter is a data type.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueDate = None
        
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        
        """ If parameter is a data type.
        Type `float`. """
        
        self._valueDecimal = None
        
        """ extension for fhir primitive  valueDecimal"""
        
        self.valueDistance = None
        
        """ If parameter is a data type.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDosage = None
        
        """ If parameter is a data type.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        
        """ If parameter is a data type.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueExpression = None
        
        """ If parameter is a data type.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        
        """ If parameter is a data type.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId = None
        
        """ If parameter is a data type.
        Type `str`. """
        
        self._valueId = None
        
        """ extension for fhir primitive  valueId"""
        
        self.valueIdentifier = None
        
        """ If parameter is a data type.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        
        """ If parameter is a data type.
        Type `int`. """
        
        self._valueInteger = None
        
        """ extension for fhir primitive  valueInteger"""
        
        self.valueMarkdown = None
        
        """ If parameter is a data type.
        Type `str`. """
        
        self._valueMarkdown = None
        
        """ extension for fhir primitive  valueMarkdown"""
        
        self.valueMoney = None
        
        """ If parameter is a data type.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid = None
        
        """ If parameter is a data type.
        Type `str`. """
        
        self._valueOid = None
        
        """ extension for fhir primitive  valueOid"""
        
        self.valueParameterDefinition = None
        
        """ If parameter is a data type.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        
        """ If parameter is a data type.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt = None
        
        """ If parameter is a data type.
        Type `int`. """
        
        self._valuePositiveInt = None
        
        """ extension for fhir primitive  valuePositiveInt"""
        
        self.valueQuantity = None
        
        """ If parameter is a data type.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        
        """ If parameter is a data type.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        
        """ If parameter is a data type.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        
        """ If parameter is a data type.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
        
        """ If parameter is a data type.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        
        """ If parameter is a data type.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        
        """ If parameter is a data type.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
        
        """ If parameter is a data type.
        Type `str`. """
        
        self._valueString = None
        
        """ extension for fhir primitive  valueString"""
        
        self.valueTime = None
        
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTiming = None
        
        """ If parameter is a data type.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
        
        """ If parameter is a data type.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt = None
        
        """ If parameter is a data type.
        Type `int`. """
        
        self._valueUnsignedInt = None
        
        """ extension for fhir primitive  valueUnsignedInt"""
        
        self.valueUri = None
        
        """ If parameter is a data type.
        Type `str`. """
        
        self._valueUri = None
        
        """ extension for fhir primitive  valueUri"""
        
        self.valueUrl = None
        
        """ If parameter is a data type.
        Type `str`. """
        
        self._valueUrl = None
        
        """ extension for fhir primitive  valueUrl"""
        
        self.valueUsageContext = None
        
        """ If parameter is a data type.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueUuid = None
        
        """ If parameter is a data type.
        Type `str`. """
        
        self._valueUuid = None
        
        """ extension for fhir primitive  valueUuid"""
        
        super(ParametersParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ParametersParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("part", "part", ParametersParameter, True, None, False),
            ("resource", "resource", resource.Resource, False, None, False),
            ("valueAddress", "valueAddress", address.Address, False, "value", False),
            ("valueAge", "valueAge", age.Age, False, "value", False),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", False),
            ("_valueBase64Binary", "_valueBase64Binary",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("_valueBoolean", "_valueBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCanonical", "valueCanonical", str, False, "value", False),
            ("_valueCanonical", "_valueCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCode", "valueCode", str, False, "value", False),
            ("_valueCode", "_valueCode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", False),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", False),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", False),
            ("valueCount", "valueCount", count.Count, False, "value", False),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("_valueDecimal", "_valueDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", False),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", False),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", False),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", False),
            ("valueId", "valueId", str, False, "value", False),
            ("_valueId", "_valueId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", False),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("_valueInteger", "_valueInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueMarkdown", "valueMarkdown", str, False, "value", False),
            ("_valueMarkdown", "_valueMarkdown",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueMoney", "valueMoney", money.Money, False, "value", False),
            ("valueOid", "valueOid", str, False, "value", False),
            ("_valueOid", "_valueOid",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", False),
            ("_valuePositiveInt", "_valuePositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("_valueString", "_valueString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", False),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", False),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", False),
            ("_valueUnsignedInt", "_valueUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUri", "valueUri", str, False, "value", False),
            ("_valueUri", "_valueUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUrl", "valueUrl", str, False, "value", False),
            ("_valueUrl", "_valueUrl",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", False),
            ("valueUuid", "valueUuid", str, False, "value", False),
            ("_valueUuid", "_valueUuid",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext
from . import fhirprimitive

