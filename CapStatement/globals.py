#******************** NEED TO UPDATE WHEN CHANGING IGS ************************************************

#ig_source_path = ''

#TODO add these configs in the source spreadsheets

#in_path = '/Users/ehaas/Documents/FHIR/pyfhir/test/'

#======================US Core ===================================
# ----------spreadsheet source---------------
in_path = "//ERICS-AIR-2/ehaas/Documents/FHIR/US-Core-R4/source/source_spreadsheets/"  #  PC !! Change back to US-Core
in_file ="uscore-client"
#in_file ="uscore-server"
#ig_folder = 'US-Core'  # do we use use this?
# -------------ig and package source----------------
#ig_source_path = "/Users/ehaas/Documents/FHIR/US-Core-R4/source/" # mac
ig_source_path  = '//ERICS-AIR-2/ehaas/Documents/FHIR/US-Core-R4/source/' # pc
ig_package_tar_path =  "//ERICS-AIR-2/ehaas/Documents/FHIR/US-Core-R4/output"  #  pc!! Change back to US-Core
# --------- ig specific variable -------------------
pre = "US-Core"
canon = "http://hl7.org/fhir/us/core/"  # don't forget the slash  - fix using os.join or path

publisher = 'HL7 International - US Realm Steering Committee'

publisher_endpoint = dict(
                        system = 'url',
                        value = 'http://www.hl7.org/Special/committees/usrealm/index.cfm'
                        )

#===================================================================

#======================Da Vinci===================================
#in_path = "//ERICS-AIR-2/ehaas/Documents/FHIR/Davinci-Notifications/source/resources/source-data/capstatements-spreadsheets/"
#in_file ="alert-initiator"
#in_file ="alert-receiver"
#in_file ="query-responder"
#in_file ="query-requester"
#in_path = "//ERICS-AIR-2/ehaas/Documents/FHIR/Davinci-DEQM/source/resources/source-data/"
#in_file = "DEQM_Capability_Statement_Consumer_Client"
#in_file = "DEQM_Capability_Statement_Reporter_Client"
#in_file = "DEQM_Capability_Statement_Consumer_Server"
#in_file = "DEQM_Capability_Statement_Producer_Client"
#in_file = "DEQM_Capability_Statement_Producer_Server"
#in_file = "DEQM_Capability_Statement_Receiver_Server"
#in_path="C:/Users/Administrator/Downloads/"
#in_file = 'plan-net-server'

#"\\ERICS-AIR-2\ehaas\Documents\FHIR\Davinci-Alerts\source\resources\source-data\alert-sender.xlsx"
#'//ERICS-AIR-2/ehaas/Documents/FHIR/Davinci-Alerts/source/resources/source_data/alert-sender.xlsx'
# using this as a default for the plan net
#ig_package_tar_path = 'https://build.fhir.org/ig/HL7/davinci-deqm'
#ig_package_tar_path =  "//ERICS-AIR-2/ehaas/Documents/FHIR/Davinci-Notifications/output"
#ig_package_path =  "//ERICS-AIR-2/ehaas/.fhir/packages/hl7.fhir.us.davinci-alerts#dev/package"
#ig_folder = 'Davinci-Notifications'
#ig_folder = 'Davinci-DEQM'

# --------- ig specific variable -------------------
#pre = "Da Vinci"
#canon = "http://hl7.org/fhir/us/davinci-notifications/"  # don't forget the slash  - fix using os.join or path
#canon = "http://hl7.org/fhir/us/davinci-deqm/"  # don't forget the slash  - fix using os.join or path
#canon = "http://hl7.org/fhir/us/davinci-pdex-plan-net/"  # don't forget the slash  - fix using os.join or path
#publisher = 'HL7 International - Clinical Decision Support Work Group'
#publisher = 'HL7 International - Infrastructure and Messaging Work Group'
#publisher = 'HL7 International - Financial Management Working Group'
'''publisher_endpoint = dict(
                        system = 'url',
                        value = 'http://www.hl7.org/Special/committees/cds/index.cfm'
                        )
'''
'''
publisher_endpoint = dict(
                        system = 'url',
                        value = 'http://www.hl7.org/Special/committees/inm/index.cfm'
                        )

'''
'''
publisher_endpoint = dict(
                        system = 'url',
                        value = 'http://www.hl7.org/Special/committees/fm/index.cfm'
                        )
'''

#ig_package_tar_path =  "//ERICS-AIR-2/ehaas/Documents/FHIR/Davinci-DEQM/output"
#ig_package_path =  "//ERICS-AIR-2/ehaas/.fhir/packages/hl7.fhir.us.davinci-deqm#dev"
#ig_package_path = "C:/Users/Administrator/Downloads/"
#ig_source_path = "//ERICS-AIR-2/ehaas/Documents/FHIR/Davinci-DEQM/source/"
#ig_source_path = "//ERICS-AIR-2/ehaas/Documents/FHIR/Davinci-Notifications/source/"

#==========================================================================

fhir_base_url = 'http://hl7.org/fhir/'
f_jurisdiction =  CC.CodeableConcept({
      "coding" : [
        {
          "system" : "urn:iso:std:iso:3166",
          "code" : "US"
        }
      ]
    })

conf_url = 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation'
combo_url = 'http://hl7.org/fhir/StructureDefinition/capabilitystatement-search-parameter-combination'

sp_specials = {'us-core-includeprovenance':'http://hl7.org/fhir/us/core/SearchParameter/us-core-includeprovenance'}  # dict to for SP to get right canonicals, may use spreadsheet or package file in future.

none_list = ['', ' ', 'none', 'n/a', 'N/A', 'N', 'False']

sep_list = (',', ';', ' ', ', ', '; ')

f_now = D.FHIRDate(str(date.today()))
f_now.as_json()
