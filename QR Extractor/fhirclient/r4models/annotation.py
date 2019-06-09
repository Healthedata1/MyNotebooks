#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Annotation) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class Annotation(element.Element):
    """ Text node with attribution.
    
    A  text note which also  contains information about who made the statement
    and when.
    """
    
    resource_type = "Annotation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorReference = None
        
        """ Individual responsible for the annotation.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.authorString = None
        
        """ Individual responsible for the annotation.
        Type `str`. """
        
        self._authorString = None
        
        """ extension for fhir primitive  authorString"""
        
        self.text = None
        
        """ The annotation  - text content (as markdown).
        Type `str`. """
        
        self._text = None
        
        """ extension for fhir primitive  text"""
        
        self.time = None
        
        """ When the annotation was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(Annotation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Annotation, self).elementProperties()
        js.extend([
            ("authorReference", "authorReference", fhirreference.FHIRReference, False, "author", False),
            ("authorString", "authorString", str, False, "author", False),
            ("_authorString", "_authorString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("text", "text", str, False, None, True),
            ("_text", "_text",fhirprimitive.FHIRPrimitive, False, None, False),
            ("time", "time", fhirdate.FHIRDate, False, None, False),
        ])
        return js


from . import fhirdate
from . import fhirreference
from . import fhirprimitive

