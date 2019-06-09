#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class BiologicallyDerivedProduct(domainresource.DomainResource):
    """ A material substance originating from a biological entity.
    
    A material substance originating from a biological entity intended to be
    transplanted or infused
    into another (possibly the same) biological entity.
    """
    
    resource_type = "BiologicallyDerivedProduct"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collection = None
        
        """ How this product was collected.
        Type `BiologicallyDerivedProductCollection` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ External ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.manipulation = None
        
        """ Any manipulation of product post-collection.
        Type `BiologicallyDerivedProductManipulation` (represented as `dict` in JSON). """
        
        self.parent = None
        
        """ BiologicallyDerivedProduct parent.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.processing = None
        
        """ Any processing of the product during collection.
        List of `BiologicallyDerivedProductProcessing` items (represented as `dict` in JSON). """
        
        self.productCategory = None
        
        """ organ | tissue | fluid | cells | biologicalAgent.
        Type `str`. """
        
        self._productCategory = None
        
        """ extension for fhir primitive  productCategory"""
        
        self.productCode = None
        
        """ What this biologically derived product is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        
        """ The amount of this biologically derived product.
        Type `int`. """
        
        self._quantity = None
        
        """ extension for fhir primitive  quantity"""
        
        self.request = None
        
        """ Procedure request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        
        """ available | unavailable.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.storage = None
        
        """ Product storage.
        List of `BiologicallyDerivedProductStorage` items (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProduct, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BiologicallyDerivedProduct, self).elementProperties()
        js.extend([
            ("collection", "collection", BiologicallyDerivedProductCollection, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("manipulation", "manipulation", BiologicallyDerivedProductManipulation, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, True, None, False),
            ("processing", "processing", BiologicallyDerivedProductProcessing, True, None, False),
            ("productCategory", "productCategory", str, False, None, False),
            ("_productCategory", "_productCategory",fhirprimitive.FHIRPrimitive, False, None, False),
            ("productCode", "productCode", codeableconcept.CodeableConcept, False, None, False),
            ("quantity", "quantity", int, False, None, False),
            ("_quantity", "_quantity",fhirprimitive.FHIRPrimitive, False, None, False),
            ("request", "request", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("storage", "storage", BiologicallyDerivedProductStorage, True, None, False),
        ])
        return js


from . import backboneelement

class BiologicallyDerivedProductCollection(backboneelement.BackboneElement):
    """ How this product was collected.
    """
    
    resource_type = "BiologicallyDerivedProductCollection"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collectedDateTime = None
        
        """ Time of product collection.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.collectedPeriod = None
        
        """ Time of product collection.
        Type `Period` (represented as `dict` in JSON). """
        
        self.collector = None
        
        """ Individual performing collection.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.source = None
        
        """ Who is product from.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProductCollection, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BiologicallyDerivedProductCollection, self).elementProperties()
        js.extend([
            ("collectedDateTime", "collectedDateTime", fhirdate.FHIRDate, False, "collected", False),
            ("collectedPeriod", "collectedPeriod", period.Period, False, "collected", False),
            ("collector", "collector", fhirreference.FHIRReference, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class BiologicallyDerivedProductManipulation(backboneelement.BackboneElement):
    """ Any manipulation of product post-collection.
    """
    
    resource_type = "BiologicallyDerivedProductManipulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ Description of manipulation.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.timeDateTime = None
        
        """ Time of manipulation.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timePeriod = None
        
        """ Time of manipulation.
        Type `Period` (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProductManipulation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BiologicallyDerivedProductManipulation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdate.FHIRDate, False, "time", False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
        ])
        return js


class BiologicallyDerivedProductProcessing(backboneelement.BackboneElement):
    """ Any processing of the product during collection.
    """
    
    resource_type = "BiologicallyDerivedProductProcessing"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additive = None
        
        """ Substance added during processing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.description = None
        
        """ Description of of processing.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.procedure = None
        
        """ Procesing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.timeDateTime = None
        
        """ Time of processing.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timePeriod = None
        
        """ Time of processing.
        Type `Period` (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProductProcessing, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BiologicallyDerivedProductProcessing, self).elementProperties()
        js.extend([
            ("additive", "additive", fhirreference.FHIRReference, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("procedure", "procedure", codeableconcept.CodeableConcept, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdate.FHIRDate, False, "time", False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
        ])
        return js


class BiologicallyDerivedProductStorage(backboneelement.BackboneElement):
    """ Product storage.
    """
    
    resource_type = "BiologicallyDerivedProductStorage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ Description of storage.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.duration = None
        
        """ Storage timeperiod.
        Type `Period` (represented as `dict` in JSON). """
        
        self.scale = None
        
        """ farenheit | celsius | kelvin.
        Type `str`. """
        
        self._scale = None
        
        """ extension for fhir primitive  scale"""
        
        self.temperature = None
        
        """ Storage temperature.
        Type `float`. """
        
        self._temperature = None
        
        """ extension for fhir primitive  temperature"""
        
        super(BiologicallyDerivedProductStorage, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BiologicallyDerivedProductStorage, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("duration", "duration", period.Period, False, None, False),
            ("scale", "scale", str, False, None, False),
            ("_scale", "_scale",fhirprimitive.FHIRPrimitive, False, None, False),
            ("temperature", "temperature", float, False, None, False),
            ("_temperature", "_temperature",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import fhirprimitive

