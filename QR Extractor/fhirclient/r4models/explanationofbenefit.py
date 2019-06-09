#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class ExplanationOfBenefit(domainresource.DomainResource):
    """ Explanation of Benefit resource.
    
    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """
    
    resource_type = "ExplanationOfBenefit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accident = None
        
        """ Details of an accident.
        Type `ExplanationOfBenefitAccident` (represented as `dict` in JSON). """
        
        self.addItem = None
        
        """ Insurer added line items.
        List of `ExplanationOfBenefitAddItem` items (represented as `dict` in JSON). """
        
        self.benefitBalance = None
        
        """ Balance by Benefit Category.
        List of `ExplanationOfBenefitBenefitBalance` items (represented as `dict` in JSON). """
        
        self.billablePeriod = None
        
        """ Period for charge submission.
        Type `Period` (represented as `dict` in JSON). """
        
        self.careTeam = None
        
        """ Care Team members.
        List of `ExplanationOfBenefitCareTeam` items (represented as `dict` in JSON). """
        
        self.claim = None
        
        """ Claim reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.claimResponse = None
        
        """ Claim response reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.created = None
        
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.diagnosis = None
        
        """ List of Diagnosis.
        List of `ExplanationOfBenefitDiagnosis` items (represented as `dict` in JSON). """
        
        self.disposition = None
        
        """ Disposition Message.
        Type `str`. """
        
        self._disposition = None
        
        """ extension for fhir primitive  disposition"""
        
        self.enterer = None
        
        """ Author.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.facility = None
        
        """ Servicing Facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.form = None
        
        """ Printed Form Identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.information = None
        
        """ Exceptions, special considerations, the condition, situation, prior
        or concurrent issues.
        List of `ExplanationOfBenefitInformation` items (represented as `dict` in JSON). """
        
        self.insurance = None
        
        """ Insurance or medical plan.
        List of `ExplanationOfBenefitInsurance` items (represented as `dict` in JSON). """
        
        self.insurer = None
        
        """ Insurer responsible for the EOB.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.item = None
        
        """ Goods and Services.
        List of `ExplanationOfBenefitItem` items (represented as `dict` in JSON). """
        
        self.originalPrescription = None
        
        """ Original prescription if superceded by fulfiller.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome = None
        
        """ queued | complete | error | partial.
        Type `str`. """
        
        self._outcome = None
        
        """ extension for fhir primitive  outcome"""
        
        self.patient = None
        
        """ The subject of the Products and Services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.payee = None
        
        """ Party to be paid any benefits payable.
        Type `ExplanationOfBenefitPayee` (represented as `dict` in JSON). """
        
        self.payment = None
        
        """ Payment Details.
        Type `ExplanationOfBenefitPayment` (represented as `dict` in JSON). """
        
        self.precedence = None
        
        """ Precedence (primary, secondary, etc.).
        Type `int`. """
        
        self._precedence = None
        
        """ extension for fhir primitive  precedence"""
        
        self.prescription = None
        
        """ Prescription authorizing services or products.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.procedure = None
        
        """ Procedures performed.
        List of `ExplanationOfBenefitProcedure` items (represented as `dict` in JSON). """
        
        self.processNote = None
        
        """ Processing notes.
        List of `ExplanationOfBenefitProcessNote` items (represented as `dict` in JSON). """
        
        self.provider = None
        
        """ Responsible provider for the claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referral = None
        
        """ Treatment Referral.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.related = None
        
        """ Related Claims which may be revelant to processing this claim.
        List of `ExplanationOfBenefitRelated` items (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subType = None
        
        """ Finer grained claim type information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.total = None
        
        """ Adjudication totals.
        List of `ExplanationOfBenefitTotal` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Type or discipline.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.use = None
        
        """ claim | preauthorization | predetermination.
        Type `str`. """
        
        self._use = None
        
        """ extension for fhir primitive  use"""
        
        super(ExplanationOfBenefit, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefit, self).elementProperties()
        js.extend([
            ("accident", "accident", ExplanationOfBenefitAccident, False, None, False),
            ("addItem", "addItem", ExplanationOfBenefitAddItem, True, None, False),
            ("benefitBalance", "benefitBalance", ExplanationOfBenefitBenefitBalance, True, None, False),
            ("billablePeriod", "billablePeriod", period.Period, False, None, False),
            ("careTeam", "careTeam", ExplanationOfBenefitCareTeam, True, None, False),
            ("claim", "claim", fhirreference.FHIRReference, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("diagnosis", "diagnosis", ExplanationOfBenefitDiagnosis, True, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("_disposition", "_disposition",fhirprimitive.FHIRPrimitive, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("information", "information", ExplanationOfBenefitInformation, True, None, False),
            ("insurance", "insurance", ExplanationOfBenefitInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("item", "item", ExplanationOfBenefitItem, True, None, False),
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("_outcome", "_outcome",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("payee", "payee", ExplanationOfBenefitPayee, False, None, False),
            ("payment", "payment", ExplanationOfBenefitPayment, False, None, False),
            ("precedence", "precedence", int, False, None, False),
            ("_precedence", "_precedence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False),
            ("procedure", "procedure", ExplanationOfBenefitProcedure, True, None, False),
            ("processNote", "processNote", ExplanationOfBenefitProcessNote, True, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("referral", "referral", fhirreference.FHIRReference, False, None, False),
            ("related", "related", ExplanationOfBenefitRelated, True, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("total", "total", ExplanationOfBenefitTotal, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("use", "use", str, False, None, False),
            ("_use", "_use",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class ExplanationOfBenefitAccident(backboneelement.BackboneElement):
    """ Details of an accident.
    
    An accident which resulted in the need for healthcare services.
    """
    
    resource_type = "ExplanationOfBenefitAccident"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        
        """ When the accident occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.locationAddress = None
        
        """ Accident Place.
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationReference = None
        
        """ Accident Place.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ The nature of the accident.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitAccident, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitAccident, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ExplanationOfBenefitAddItem(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The first-tier service adjudications for payor added services.
    """
    
    resource_type = "ExplanationOfBenefitAddItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        
        """ Added items adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.billcode = None
        
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bodySite = None
        
        """ Service Location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail = None
        
        """ Insurer added line items.
        List of `ExplanationOfBenefitAddItemDetail` items (represented as `dict` in JSON). """
        
        self.detailSequence = None
        
        """ Detail sequence number.
        List of `int` items. """
        
        self._detailSequence = None
        
        """ extension for fhir primitive  detailSequence"""
        
        self.factor = None
        
        """ Price scaling factor.
        Type `float`. """
        
        self._factor = None
        
        """ extension for fhir primitive  factor"""
        
        self.itemSequence = None
        
        """ Service instances.
        List of `int` items. """
        
        self._itemSequence = None
        
        """ extension for fhir primitive  itemSequence"""
        
        self.locationAddress = None
        
        """ Place of service.
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationCodeableConcept = None
        
        """ Place of service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.locationReference = None
        
        """ Place of service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.modifier = None
        
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber = None
        
        """ List of note numbers which apply.
        List of `int` items. """
        
        self._noteNumber = None
        
        """ extension for fhir primitive  noteNumber"""
        
        self.programCode = None
        
        """ Program specific reason for item inclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.provider = None
        
        """ Authorized providers.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.quantity = None
        
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.servicedDate = None
        
        """ Date or dates of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        
        """ Date or dates of Service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.subDetailSequence = None
        
        """ Subdetail sequence number.
        List of `int` items. """
        
        self._subDetailSequence = None
        
        """ extension for fhir primitive  subDetailSequence"""
        
        self.subSite = None
        
        """ Service Sub-location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.unitPrice = None
        
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitAddItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("billcode", "billcode", codeableconcept.CodeableConcept, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", ExplanationOfBenefitAddItemDetail, True, None, False),
            ("detailSequence", "detailSequence", int, True, None, False),
            ("_detailSequence", "_detailSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("itemSequence", "itemSequence", int, True, None, False),
            ("_itemSequence", "_itemSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("provider", "provider", fhirreference.FHIRReference, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("subDetailSequence", "subDetailSequence", int, True, None, False),
            ("_subDetailSequence", "_subDetailSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitAddItemDetail(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The second-tier service adjudications for payor added services.
    """
    
    resource_type = "ExplanationOfBenefitAddItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        
        """ Added items adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.billcode = None
        
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor = None
        
        """ Price scaling factor.
        Type `float`. """
        
        self._factor = None
        
        """ extension for fhir primitive  factor"""
        
        self.modifier = None
        
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber = None
        
        """ List of note numbers which apply.
        List of `int` items. """
        
        self._noteNumber = None
        
        """ extension for fhir primitive  noteNumber"""
        
        self.quantity = None
        
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.subDetail = None
        
        """ Insurer added line items.
        List of `ExplanationOfBenefitAddItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.unitPrice = None
        
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitAddItemDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("billcode", "billcode", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("subDetail", "subDetail", ExplanationOfBenefitAddItemDetailSubDetail, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitAddItemDetailSubDetail(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The third-tier service adjudications for payor added services.
    """
    
    resource_type = "ExplanationOfBenefitAddItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        
        """ Added items adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.billcode = None
        
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor = None
        
        """ Price scaling factor.
        Type `float`. """
        
        self._factor = None
        
        """ extension for fhir primitive  factor"""
        
        self.modifier = None
        
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber = None
        
        """ List of note numbers which apply.
        List of `int` items. """
        
        self._noteNumber = None
        
        """ extension for fhir primitive  noteNumber"""
        
        self.quantity = None
        
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitAddItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("billcode", "billcode", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitBenefitBalance(backboneelement.BackboneElement):
    """ Balance by Benefit Category.
    """
    
    resource_type = "ExplanationOfBenefitBenefitBalance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        
        """ Type of services covered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        
        """ Description of the benefit or services covered.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.excluded = None
        
        """ Excluded from the plan.
        Type `bool`. """
        
        self._excluded = None
        
        """ extension for fhir primitive  excluded"""
        
        self.financial = None
        
        """ Benefit Summary.
        List of `ExplanationOfBenefitBenefitBalanceFinancial` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Short name for the benefit.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.network = None
        
        """ In or out of network.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.term = None
        
        """ Annual or lifetime.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit = None
        
        """ Individual or family.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitBenefitBalance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalance, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("excluded", "excluded", bool, False, None, False),
            ("_excluded", "_excluded",fhirprimitive.FHIRPrimitive, False, None, False),
            ("financial", "financial", ExplanationOfBenefitBenefitBalanceFinancial, True, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("network", "network", codeableconcept.CodeableConcept, False, None, False),
            ("term", "term", codeableconcept.CodeableConcept, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ExplanationOfBenefitBenefitBalanceFinancial(backboneelement.BackboneElement):
    """ Benefit Summary.
    
    Benefits Used to date.
    """
    
    resource_type = "ExplanationOfBenefitBenefitBalanceFinancial"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allowedMoney = None
        
        """ Benefits allowed.
        Type `Money` (represented as `dict` in JSON). """
        
        self.allowedString = None
        
        """ Benefits allowed.
        Type `str`. """
        
        self._allowedString = None
        
        """ extension for fhir primitive  allowedString"""
        
        self.allowedUnsignedInt = None
        
        """ Benefits allowed.
        Type `int`. """
        
        self._allowedUnsignedInt = None
        
        """ extension for fhir primitive  allowedUnsignedInt"""
        
        self.type = None
        
        """ Deductable, visits, benefit amount.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.usedMoney = None
        
        """ Benefits used.
        Type `Money` (represented as `dict` in JSON). """
        
        self.usedUnsignedInt = None
        
        """ Benefits used.
        Type `int`. """
        
        self._usedUnsignedInt = None
        
        """ extension for fhir primitive  usedUnsignedInt"""
        
        super(ExplanationOfBenefitBenefitBalanceFinancial, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalanceFinancial, self).elementProperties()
        js.extend([
            ("allowedMoney", "allowedMoney", money.Money, False, "allowed", False),
            ("allowedString", "allowedString", str, False, "allowed", False),
            ("_allowedString", "_allowedString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("allowedUnsignedInt", "allowedUnsignedInt", int, False, "allowed", False),
            ("_allowedUnsignedInt", "_allowedUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("usedMoney", "usedMoney", money.Money, False, "used", False),
            ("usedUnsignedInt", "usedUnsignedInt", int, False, "used", False),
            ("_usedUnsignedInt", "_usedUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ExplanationOfBenefitCareTeam(backboneelement.BackboneElement):
    """ Care Team members.
    
    The members of the team who provided the overall service as well as their
    role and whether responsible and qualifications.
    """
    
    resource_type = "ExplanationOfBenefitCareTeam"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.provider = None
        
        """ Member of the Care Team.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.qualification = None
        
        """ Type, classification or Specialization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.responsible = None
        
        """ Billing practitioner.
        Type `bool`. """
        
        self._responsible = None
        
        """ extension for fhir primitive  responsible"""
        
        self.role = None
        
        """ Role on the team.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Number to convey order of careteam.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        super(ExplanationOfBenefitCareTeam, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitCareTeam, self).elementProperties()
        js.extend([
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("qualification", "qualification", codeableconcept.CodeableConcept, False, None, False),
            ("responsible", "responsible", bool, False, None, False),
            ("_responsible", "_responsible",fhirprimitive.FHIRPrimitive, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ExplanationOfBenefitDiagnosis(backboneelement.BackboneElement):
    """ List of Diagnosis.
    
    Ordered list of patient diagnosis for which care is sought.
    """
    
    resource_type = "ExplanationOfBenefitDiagnosis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.diagnosisCodeableConcept = None
        
        """ Patient's diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diagnosisReference = None
        
        """ Patient's diagnosis.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.onAdmission = None
        
        """ Present on admission.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.packageCode = None
        
        """ Package billing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Number to convey order of diagnosis.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        self.type = None
        
        """ Timing or nature of the diagnosis.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitDiagnosis, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", True),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", True),
            ("onAdmission", "onAdmission", codeableconcept.CodeableConcept, False, None, False),
            ("packageCode", "packageCode", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ExplanationOfBenefitInformation(backboneelement.BackboneElement):
    """ Exceptions, special considerations, the condition, situation, prior or
    concurrent issues.
    
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues. Often there are
    mutiple jurisdiction specific valuesets which are required.
    """
    
    resource_type = "ExplanationOfBenefitInformation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        
        """ General class of information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        
        """ Type of information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        
        """ Reason associated with the information.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Information instance identifier.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        self.timingDate = None
        
        """ When it occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        
        """ When it occurred.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        
        """ Additional Data or supporting information.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        
        """ Additional Data or supporting information.
        Type `bool`. """
        
        self._valueBoolean = None
        
        """ extension for fhir primitive  valueBoolean"""
        
        self.valueQuantity = None
        
        """ Additional Data or supporting information.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference = None
        
        """ Additional Data or supporting information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueString = None
        
        """ Additional Data or supporting information.
        Type `str`. """
        
        self._valueString = None
        
        """ extension for fhir primitive  valueString"""
        
        super(ExplanationOfBenefitInformation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitInformation, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("reason", "reason", coding.Coding, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("timingDate", "timingDate", fhirdate.FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("_valueBoolean", "_valueBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("_valueString", "_valueString",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ExplanationOfBenefitInsurance(backboneelement.BackboneElement):
    """ Insurance or medical plan.
    
    Financial instrument by which payment information for health care.
    """
    
    resource_type = "ExplanationOfBenefitInsurance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverage = None
        
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.focal = None
        
        """ Is the focal Coverage.
        Type `bool`. """
        
        self._focal = None
        
        """ extension for fhir primitive  focal"""
        
        super(ExplanationOfBenefitInsurance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitInsurance, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("_focal", "_focal",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ExplanationOfBenefitItem(backboneelement.BackboneElement):
    """ Goods and Services.
    
    First-tier of goods and services.
    """
    
    resource_type = "ExplanationOfBenefitItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        
        """ Adjudication details.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.billcode = None
        
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bodySite = None
        
        """ Service Location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.careTeamSequence = None
        
        """ Applicable careteam members.
        List of `int` items. """
        
        self._careTeamSequence = None
        
        """ extension for fhir primitive  careTeamSequence"""
        
        self.category = None
        
        """ Type of service or product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail = None
        
        """ Additional items.
        List of `ExplanationOfBenefitItemDetail` items (represented as `dict` in JSON). """
        
        self.diagnosisSequence = None
        
        """ Applicable diagnoses.
        List of `int` items. """
        
        self._diagnosisSequence = None
        
        """ extension for fhir primitive  diagnosisSequence"""
        
        self.encounter = None
        
        """ Encounters related to this billed item.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.factor = None
        
        """ Price scaling factor.
        Type `float`. """
        
        self._factor = None
        
        """ extension for fhir primitive  factor"""
        
        self.informationSequence = None
        
        """ Applicable exception and supporting information.
        List of `int` items. """
        
        self._informationSequence = None
        
        """ extension for fhir primitive  informationSequence"""
        
        self.locationAddress = None
        
        """ Place of service.
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationCodeableConcept = None
        
        """ Place of service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.locationReference = None
        
        """ Place of service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.modifier = None
        
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber = None
        
        """ List of note numbers which apply.
        List of `int` items. """
        
        self._noteNumber = None
        
        """ extension for fhir primitive  noteNumber"""
        
        self.procedureSequence = None
        
        """ Applicable procedures.
        List of `int` items. """
        
        self._procedureSequence = None
        
        """ extension for fhir primitive  procedureSequence"""
        
        self.programCode = None
        
        """ Program specific reason for item inclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity = None
        
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.revenue = None
        
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Service instance.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        self.servicedDate = None
        
        """ Date or dates of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        
        """ Date or dates of Service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.subSite = None
        
        """ Service Sub-location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.udi = None
        
        """ Unique Device Identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.unitPrice = None
        
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("billcode", "billcode", codeableconcept.CodeableConcept, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("careTeamSequence", "careTeamSequence", int, True, None, False),
            ("_careTeamSequence", "_careTeamSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", ExplanationOfBenefitItemDetail, True, None, False),
            ("diagnosisSequence", "diagnosisSequence", int, True, None, False),
            ("_diagnosisSequence", "_diagnosisSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("informationSequence", "informationSequence", int, True, None, False),
            ("_informationSequence", "_informationSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("procedureSequence", "procedureSequence", int, True, None, False),
            ("_procedureSequence", "_procedureSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.
    
    The adjudication results.
    """
    
    resource_type = "ExplanationOfBenefitItemAdjudication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        
        """ Monetary amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.category = None
        
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        
        """ Explanation of Adjudication outcome.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        
        """ Non-monitory value.
        Type `float`. """
        
        self._value = None
        
        """ extension for fhir primitive  value"""
        
        super(ExplanationOfBenefitItemAdjudication, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
            ("_value", "_value",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Second-tier of goods and services.
    """
    
    resource_type = "ExplanationOfBenefitItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        
        """ Detail level adjudication details.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.billcode = None
        
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        
        """ Type of service or product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor = None
        
        """ Price scaling factor.
        Type `float`. """
        
        self._factor = None
        
        """ extension for fhir primitive  factor"""
        
        self.modifier = None
        
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        
        """ Total additional item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber = None
        
        """ List of note numbers which apply.
        List of `int` items. """
        
        self._noteNumber = None
        
        """ extension for fhir primitive  noteNumber"""
        
        self.programCode = None
        
        """ Program specific reason for item inclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity = None
        
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.revenue = None
        
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Service instance.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        self.subDetail = None
        
        """ Additional items.
        List of `ExplanationOfBenefitItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.udi = None
        
        """ Unique Device Identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.unitPrice = None
        
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItemDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("billcode", "billcode", codeableconcept.CodeableConcept, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subDetail", "subDetail", ExplanationOfBenefitItemDetailSubDetail, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Third-tier of goods and services.
    """
    
    resource_type = "ExplanationOfBenefitItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        
        """ Language if different from the resource.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.billcode = None
        
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        
        """ Type of service or product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor = None
        
        """ Price scaling factor.
        Type `float`. """
        
        self._factor = None
        
        """ extension for fhir primitive  factor"""
        
        self.modifier = None
        
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        
        """ Net additional item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber = None
        
        """ List of note numbers which apply.
        List of `int` items. """
        
        self._noteNumber = None
        
        """ extension for fhir primitive  noteNumber"""
        
        self.programCode = None
        
        """ Program specific reason for item inclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity = None
        
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.revenue = None
        
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Service instance.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        self.udi = None
        
        """ Unique Device Identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.unitPrice = None
        
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("billcode", "billcode", codeableconcept.CodeableConcept, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitPayee(backboneelement.BackboneElement):
    """ Party to be paid any benefits payable.
    
    The party to be reimbursed for the services.
    """
    
    resource_type = "ExplanationOfBenefitPayee"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.party = None
        
        """ Party to receive the payable.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.resource = None
        
        """ organization | patient | practitioner | relatedperson.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Type of party: Subscriber, Provider, other.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitPayee, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitPayee, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, False),
            ("resource", "resource", coding.Coding, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ExplanationOfBenefitPayment(backboneelement.BackboneElement):
    """ Payment Details.
    
    Payment details for the claim if the claim has been paid.
    """
    
    resource_type = "ExplanationOfBenefitPayment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjustment = None
        
        """ Payment adjustment for non-Claim issues.
        Type `Money` (represented as `dict` in JSON). """
        
        self.adjustmentReason = None
        
        """ Explanation for the non-claim adjustment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.amount = None
        
        """ Payable amount after adjustment.
        Type `Money` (represented as `dict` in JSON). """
        
        self.date = None
        
        """ Expected date of Payment.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        
        """ Identifier of the payment instrument.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Partial or Complete.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitPayment, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitPayment, self).elementProperties()
        js.extend([
            ("adjustment", "adjustment", money.Money, False, None, False),
            ("adjustmentReason", "adjustmentReason", codeableconcept.CodeableConcept, False, None, False),
            ("amount", "amount", money.Money, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ExplanationOfBenefitProcedure(backboneelement.BackboneElement):
    """ Procedures performed.
    
    Ordered list of patient procedures performed to support the adjudication.
    """
    
    resource_type = "ExplanationOfBenefitProcedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        
        """ When the procedure was performed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.procedureCodeableConcept = None
        
        """ Patient's list of procedures performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.procedureReference = None
        
        """ Patient's list of procedures performed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Procedure sequence for reference.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        super(ExplanationOfBenefitProcedure, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitProcedure, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("procedureCodeableConcept", "procedureCodeableConcept", codeableconcept.CodeableConcept, False, "procedure", True),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, "procedure", True),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ExplanationOfBenefitProcessNote(backboneelement.BackboneElement):
    """ Processing notes.
    
    Note text.
    """
    
    resource_type = "ExplanationOfBenefitProcessNote"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        
        """ Language if different from the resource.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.number = None
        
        """ Sequence number for this note.
        Type `int`. """
        
        self._number = None
        
        """ extension for fhir primitive  number"""
        
        self.text = None
        
        """ Note explanitory text.
        Type `str`. """
        
        self._text = None
        
        """ extension for fhir primitive  text"""
        
        self.type = None
        
        """ display | print | printoper.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(ExplanationOfBenefitProcessNote, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitProcessNote, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, False),
            ("number", "number", int, False, None, False),
            ("_number", "_number",fhirprimitive.FHIRPrimitive, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ExplanationOfBenefitRelated(backboneelement.BackboneElement):
    """ Related Claims which may be revelant to processing this claim.
    
    Other claims which are related to this claim such as prior claim versions
    or for related services.
    """
    
    resource_type = "ExplanationOfBenefitRelated"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.claim = None
        
        """ Reference to the related claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reference = None
        
        """ Related file or case reference.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.relationship = None
        
        """ How the reference claim is related.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitRelated, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", fhirreference.FHIRReference, False, None, False),
            ("reference", "reference", identifier.Identifier, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ExplanationOfBenefitTotal(backboneelement.BackboneElement):
    """ Adjudication totals.
    
    Totals for amounts submitted, co-pays, benefits payable etc.
    """
    
    resource_type = "ExplanationOfBenefitTotal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        
        """ Monetary amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.category = None
        
        """ Adjudication category such as submitted, co-pay, eligible, benefit,
        etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitTotal, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitTotal, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity
from . import fhirprimitive

