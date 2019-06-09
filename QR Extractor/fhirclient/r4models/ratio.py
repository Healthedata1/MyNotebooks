#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Ratio) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class Ratio(element.Element):
    """ A ratio of two Quantity values - a numerator and a denominator.
    
    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """
    
    resource_type = "Ratio"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.denominator = None
        
        """ Denominator value.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.numerator = None
        
        """ Numerator value.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(Ratio, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Ratio, self).elementProperties()
        js.extend([
            ("denominator", "denominator", quantity.Quantity, False, None, False),
            ("numerator", "numerator", quantity.Quantity, False, None, False),
        ])
        return js


from . import quantity

