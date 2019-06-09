#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/List) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class List(domainresource.DomainResource):
    """ A list is a curated collection of resources.
    """
    
    resource_type = "List"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ What the purpose of this list is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None
        
        """ When the list was prepared.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.emptyReason = None
        
        """ Why list is empty.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.encounter = None
        
        """ Context in which list created.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.entry = None
        
        """ Entries in the list.
        List of `ListEntry` items (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.mode = None
        
        """ working | snapshot | changes.
        Type `str`. """
        
        self._mode = None
        
        """ extension for fhir primitive  mode"""
        
        self.note = None
        
        """ Comments about the list.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.orderedBy = None
        
        """ What order the list has.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.source = None
        
        """ Who and/or what defined the list contents (aka Author).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ current | retired | entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subject = None
        
        """ If all resources have the same subject.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.title = None
        
        """ Descriptive name for the list.
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        super(List, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(List, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("entry", "entry", ListEntry, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class ListEntry(backboneelement.BackboneElement):
    """ Entries in the list.
    
    Entries in this list.
    """
    
    resource_type = "ListEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        
        """ When item added to list.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deleted = None
        
        """ If this item is actually marked as deleted.
        Type `bool`. """
        
        self._deleted = None
        
        """ extension for fhir primitive  deleted"""
        
        self.flag = None
        
        """ Status/Workflow information about this item.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.item = None
        
        """ Actual entry.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ListEntry, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ListEntry, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("deleted", "deleted", bool, False, None, False),
            ("_deleted", "_deleted",fhirprimitive.FHIRPrimitive, False, None, False),
            ("flag", "flag", codeableconcept.CodeableConcept, False, None, False),
            ("item", "item", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import fhirprimitive

