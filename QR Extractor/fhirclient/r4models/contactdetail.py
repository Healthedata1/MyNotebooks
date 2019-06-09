#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ContactDetail) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class ContactDetail(element.Element):
    """ Contact information.
    
    Specifies contact information for a person or organization.
    """
    
    resource_type = "ContactDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        
        """ Name of an individual to contact.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.telecom = None
        
        """ Contact details for individual or organization.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ContactDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ContactDetail, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import contactpoint
from . import fhirprimitive

