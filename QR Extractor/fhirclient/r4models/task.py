#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Task) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class Task(domainresource.DomainResource):
    """ A task to be performed.
    """
    
    resource_type = "Task"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authoredOn = None
        
        """ Task Creation Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        
        """ Request fulfilled by this task.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.businessStatus = None
        
        """ E.g. "Specimen collected", "IV prepped".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        
        """ Task Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        
        """ Human-readable explanation of task.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.encounter = None
        
        """ Healthcare event during which this task originated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.executionPeriod = None
        
        """ Start and end time of execution.
        Type `Period` (represented as `dict` in JSON). """
        
        self.focus = None
        
        """ What task is acting on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.for_fhir = None
        
        """ Beneficiary of the Task.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.groupIdentifier = None
        
        """ Requisition or grouper id.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Task Instance Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.input = None
        
        """ Information used to perform task.
        List of `TaskInput` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        
        """ Formal definition of task.
        Type `str`. """
        
        self._instantiatesCanonical = None
        
        """ extension for fhir primitive  instantiatesCanonical"""
        
        self.instantiatesUri = None
        
        """ Formal definition of task.
        Type `str`. """
        
        self._instantiatesUri = None
        
        """ extension for fhir primitive  instantiatesUri"""
        
        self.insurance = None
        
        """ Associated insurance coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.intent = None
        
        """ unknown | proposal | plan | order | original-order | reflex-order |
        filler-order | instance-order | option.
        Type `str`. """
        
        self._intent = None
        
        """ extension for fhir primitive  intent"""
        
        self.lastModified = None
        
        """ Task Last Modified Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.location = None
        
        """ Where task occurs.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.note = None
        
        """ Comments made about the task.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.output = None
        
        """ Information produced as part of task.
        List of `TaskOutput` items (represented as `dict` in JSON). """
        
        self.owner = None
        
        """ Responsible individual.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.partOf = None
        
        """ Composite task.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.performerType = None
        
        """ Requested performer.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.priority = None
        
        """ routine | urgent | asap | stat.
        Type `str`. """
        
        self._priority = None
        
        """ extension for fhir primitive  priority"""
        
        self.reasonCode = None
        
        """ Why task is needed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        
        """ Why task is needed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relevantHistory = None
        
        """ Key events in history of the Task.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requester = None
        
        """ Who is asking for task to be done.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.restriction = None
        
        """ Constraints on fulfillment tasks.
        Type `TaskRestriction` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ draft | requested | received | accepted | +.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.statusReason = None
        
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Task, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Task, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("businessStatus", "businessStatus", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("executionPeriod", "executionPeriod", period.Period, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, False, None, False),
            ("for_fhir", "for", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("input", "input", TaskInput, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, False, None, False),
            ("_instantiatesCanonical", "_instantiatesCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, False, None, False),
            ("_instantiatesUri", "_instantiatesUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("_intent", "_intent",fhirprimitive.FHIRPrimitive, False, None, False),
            ("lastModified", "lastModified", fhirdate.FHIRDate, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("output", "output", TaskOutput, True, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority",fhirprimitive.FHIRPrimitive, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("restriction", "restriction", TaskRestriction, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class TaskInput(backboneelement.BackboneElement):
    """ Information used to perform task.
    
    Additional information that may be needed in the execution of the task.
    """
    
    resource_type = "TaskInput"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        
        """ Label for the input.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueAddress = None
        
        """ Content to use in performing the task.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        
        """ Content to use in performing the task.
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        
        """ Content to use in performing the task.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        
        """ Content to use in performing the task.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        
        """ Content to use in performing the task.
        Type `str`. """
        
        self._valueBase64Binary = None
        
        """ extension for fhir primitive  valueBase64Binary"""
        
        self.valueBoolean = None
        
        """ Content to use in performing the task.
        Type `bool`. """
        
        self._valueBoolean = None
        
        """ extension for fhir primitive  valueBoolean"""
        
        self.valueCanonical = None
        
        """ Content to use in performing the task.
        Type `str`. """
        
        self._valueCanonical = None
        
        """ extension for fhir primitive  valueCanonical"""
        
        self.valueCode = None
        
        """ Content to use in performing the task.
        Type `str`. """
        
        self._valueCode = None
        
        """ extension for fhir primitive  valueCode"""
        
        self.valueCodeableConcept = None
        
        """ Content to use in performing the task.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        
        """ Content to use in performing the task.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
        
        """ Content to use in performing the task.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        
        """ Content to use in performing the task.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueContributor = None
        
        """ Content to use in performing the task.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueCount = None
        
        """ Content to use in performing the task.
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
        
        """ Content to use in performing the task.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueDate = None
        
        """ Content to use in performing the task.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        
        """ Content to use in performing the task.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        
        """ Content to use in performing the task.
        Type `float`. """
        
        self._valueDecimal = None
        
        """ extension for fhir primitive  valueDecimal"""
        
        self.valueDistance = None
        
        """ Content to use in performing the task.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDosage = None
        
        """ Content to use in performing the task.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        
        """ Content to use in performing the task.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueExpression = None
        
        """ Content to use in performing the task.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        
        """ Content to use in performing the task.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId = None
        
        """ Content to use in performing the task.
        Type `str`. """
        
        self._valueId = None
        
        """ extension for fhir primitive  valueId"""
        
        self.valueIdentifier = None
        
        """ Content to use in performing the task.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        
        """ Content to use in performing the task.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        
        """ Content to use in performing the task.
        Type `int`. """
        
        self._valueInteger = None
        
        """ extension for fhir primitive  valueInteger"""
        
        self.valueMarkdown = None
        
        """ Content to use in performing the task.
        Type `str`. """
        
        self._valueMarkdown = None
        
        """ extension for fhir primitive  valueMarkdown"""
        
        self.valueMoney = None
        
        """ Content to use in performing the task.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid = None
        
        """ Content to use in performing the task.
        Type `str`. """
        
        self._valueOid = None
        
        """ extension for fhir primitive  valueOid"""
        
        self.valueParameterDefinition = None
        
        """ Content to use in performing the task.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        
        """ Content to use in performing the task.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt = None
        
        """ Content to use in performing the task.
        Type `int`. """
        
        self._valuePositiveInt = None
        
        """ extension for fhir primitive  valuePositiveInt"""
        
        self.valueQuantity = None
        
        """ Content to use in performing the task.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        
        """ Content to use in performing the task.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        
        """ Content to use in performing the task.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        
        """ Content to use in performing the task.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
        
        """ Content to use in performing the task.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        
        """ Content to use in performing the task.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        
        """ Content to use in performing the task.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
        
        """ Content to use in performing the task.
        Type `str`. """
        
        self._valueString = None
        
        """ extension for fhir primitive  valueString"""
        
        self.valueTime = None
        
        """ Content to use in performing the task.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTiming = None
        
        """ Content to use in performing the task.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
        
        """ Content to use in performing the task.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt = None
        
        """ Content to use in performing the task.
        Type `int`. """
        
        self._valueUnsignedInt = None
        
        """ extension for fhir primitive  valueUnsignedInt"""
        
        self.valueUri = None
        
        """ Content to use in performing the task.
        Type `str`. """
        
        self._valueUri = None
        
        """ extension for fhir primitive  valueUri"""
        
        self.valueUrl = None
        
        """ Content to use in performing the task.
        Type `str`. """
        
        self._valueUrl = None
        
        """ extension for fhir primitive  valueUrl"""
        
        self.valueUsageContext = None
        
        """ Content to use in performing the task.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueUuid = None
        
        """ Content to use in performing the task.
        Type `str`. """
        
        self._valueUuid = None
        
        """ extension for fhir primitive  valueUuid"""
        
        super(TaskInput, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TaskInput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("_valueBase64Binary", "_valueBase64Binary",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("_valueBoolean", "_valueBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("_valueCanonical", "_valueCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCode", "valueCode", str, False, "value", True),
            ("_valueCode", "_valueCode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("_valueDecimal", "_valueDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("_valueId", "_valueId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("_valueMarkdown", "_valueMarkdown",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valueOid", "valueOid", str, False, "value", True),
            ("_valueOid", "_valueOid",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("_valuePositiveInt", "_valuePositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("_valueUnsignedInt", "_valueUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUri", "valueUri", str, False, "value", True),
            ("_valueUri", "_valueUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("_valueUrl", "_valueUrl",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True),
            ("valueUuid", "valueUuid", str, False, "value", True),
            ("_valueUuid", "_valueUuid",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class TaskOutput(backboneelement.BackboneElement):
    """ Information produced as part of task.
    
    Outputs produced by the Task.
    """
    
    resource_type = "TaskOutput"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        
        """ Label for output.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueAddress = None
        
        """ Result of output.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        
        """ Result of output.
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        
        """ Result of output.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        
        """ Result of output.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        
        """ Result of output.
        Type `str`. """
        
        self._valueBase64Binary = None
        
        """ extension for fhir primitive  valueBase64Binary"""
        
        self.valueBoolean = None
        
        """ Result of output.
        Type `bool`. """
        
        self._valueBoolean = None
        
        """ extension for fhir primitive  valueBoolean"""
        
        self.valueCanonical = None
        
        """ Result of output.
        Type `str`. """
        
        self._valueCanonical = None
        
        """ extension for fhir primitive  valueCanonical"""
        
        self.valueCode = None
        
        """ Result of output.
        Type `str`. """
        
        self._valueCode = None
        
        """ extension for fhir primitive  valueCode"""
        
        self.valueCodeableConcept = None
        
        """ Result of output.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        
        """ Result of output.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
        
        """ Result of output.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        
        """ Result of output.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueContributor = None
        
        """ Result of output.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueCount = None
        
        """ Result of output.
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
        
        """ Result of output.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueDate = None
        
        """ Result of output.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        
        """ Result of output.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        
        """ Result of output.
        Type `float`. """
        
        self._valueDecimal = None
        
        """ extension for fhir primitive  valueDecimal"""
        
        self.valueDistance = None
        
        """ Result of output.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDosage = None
        
        """ Result of output.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        
        """ Result of output.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueExpression = None
        
        """ Result of output.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        
        """ Result of output.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId = None
        
        """ Result of output.
        Type `str`. """
        
        self._valueId = None
        
        """ extension for fhir primitive  valueId"""
        
        self.valueIdentifier = None
        
        """ Result of output.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        
        """ Result of output.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        
        """ Result of output.
        Type `int`. """
        
        self._valueInteger = None
        
        """ extension for fhir primitive  valueInteger"""
        
        self.valueMarkdown = None
        
        """ Result of output.
        Type `str`. """
        
        self._valueMarkdown = None
        
        """ extension for fhir primitive  valueMarkdown"""
        
        self.valueMoney = None
        
        """ Result of output.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid = None
        
        """ Result of output.
        Type `str`. """
        
        self._valueOid = None
        
        """ extension for fhir primitive  valueOid"""
        
        self.valueParameterDefinition = None
        
        """ Result of output.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        
        """ Result of output.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt = None
        
        """ Result of output.
        Type `int`. """
        
        self._valuePositiveInt = None
        
        """ extension for fhir primitive  valuePositiveInt"""
        
        self.valueQuantity = None
        
        """ Result of output.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        
        """ Result of output.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        
        """ Result of output.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        
        """ Result of output.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
        
        """ Result of output.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        
        """ Result of output.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        
        """ Result of output.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
        
        """ Result of output.
        Type `str`. """
        
        self._valueString = None
        
        """ extension for fhir primitive  valueString"""
        
        self.valueTime = None
        
        """ Result of output.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTiming = None
        
        """ Result of output.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
        
        """ Result of output.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt = None
        
        """ Result of output.
        Type `int`. """
        
        self._valueUnsignedInt = None
        
        """ extension for fhir primitive  valueUnsignedInt"""
        
        self.valueUri = None
        
        """ Result of output.
        Type `str`. """
        
        self._valueUri = None
        
        """ extension for fhir primitive  valueUri"""
        
        self.valueUrl = None
        
        """ Result of output.
        Type `str`. """
        
        self._valueUrl = None
        
        """ extension for fhir primitive  valueUrl"""
        
        self.valueUsageContext = None
        
        """ Result of output.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueUuid = None
        
        """ Result of output.
        Type `str`. """
        
        self._valueUuid = None
        
        """ extension for fhir primitive  valueUuid"""
        
        super(TaskOutput, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TaskOutput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("_valueBase64Binary", "_valueBase64Binary",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("_valueBoolean", "_valueBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("_valueCanonical", "_valueCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCode", "valueCode", str, False, "value", True),
            ("_valueCode", "_valueCode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("_valueDecimal", "_valueDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("_valueId", "_valueId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("_valueMarkdown", "_valueMarkdown",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valueOid", "valueOid", str, False, "value", True),
            ("_valueOid", "_valueOid",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("_valuePositiveInt", "_valuePositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("_valueUnsignedInt", "_valueUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUri", "valueUri", str, False, "value", True),
            ("_valueUri", "_valueUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("_valueUrl", "_valueUrl",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True),
            ("valueUuid", "valueUuid", str, False, "value", True),
            ("_valueUuid", "_valueUuid",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class TaskRestriction(backboneelement.BackboneElement):
    """ Constraints on fulfillment tasks.
    
    If the Task.focus is a request resource and the task is seeking fulfillment
    (i.e. is asking for the request to be actioned), this element identifies
    any limitations on what parts of the referenced request should be actioned.
    """
    
    resource_type = "TaskRestriction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period = None
        
        """ When fulfillment sought.
        Type `Period` (represented as `dict` in JSON). """
        
        self.recipient = None
        
        """ For whom is fulfillment sought?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.repetitions = None
        
        """ How many times to repeat.
        Type `int`. """
        
        self._repetitions = None
        
        """ extension for fhir primitive  repetitions"""
        
        super(TaskRestriction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TaskRestriction, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("repetitions", "repetitions", int, False, None, False),
            ("_repetitions", "_repetitions",fhirprimitive.FHIRPrimitive, False, None, False),
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

