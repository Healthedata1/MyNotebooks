#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Period) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class Period(element.Element):
    """ Time range defined by start and end date/time.
    
    A time period defined by a start and end date and optionally time.
    """
    
    resource_type = "Period"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
        
        """ End time with inclusive boundary, if not ongoing.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.start = None
        
        """ Starting time with inclusive boundary.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(Period, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Period, self).elementProperties()
        js.extend([
            ("end", "end", fhirdate.FHIRDate, False, None, False),
            ("start", "start", fhirdate.FHIRDate, False, None, False),
        ])
        return js


from . import fhirdate

