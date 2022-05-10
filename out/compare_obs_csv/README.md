### Columns:

**Column Header : Default Value, Description**
    
- 'Profile Title': None,
- 'Based On': None,  #US Core Profile or FHIR Observation Resource
- 'Category Slice Codes': [], # URI|Code  
- 'Code Binding': None,  #list patternCodeableConcept or binding with strength
- 'Code Fixed Value': None, # list patternCodeableConcept or binding with strength
- 'Effective Time Types': [], # list MS types
- 'Value Types': [], # list MS types or slice by types
- 'ValueQuantity Code Binding': None,  #binding with strength
- 'ValueQuantity Code Fixed Value': None, # URI|fixedCode - always UCUM by value
- 'Is Data Absent Reason': False, #True if MS
- 'Is Component': False, #True if MS
- 'Component Slice Codes': [], # URI|Code 
- 'Component Slice Value Types': [], # list MS types
- 'Component Slice ValueQuantity Codes': [], # URI|fixedCode - always UCUM by - value
- 'Has Member References': [], #list if MS
- 'Derived From References': [], #list if MS    
