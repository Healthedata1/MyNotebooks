#!/usr/bin/env python
# coding: utf-8

#   ## Script to generate the `package-list.json` file

# package-list contents:
#
# ~~~
# "package-id": "hl7.org.fhir.us.meds ",
#    "title": "US Meds Implementation Guide",
#    "canonical": "http://hl7.org/fhir/us/meds",
#    "introduction": "The US-Medication FHIR Implementation Guide promotes consistent use of the FHIR pharmacy resources in the US for providing patient and provider access to patient medications.",
#    "list": [(see below for list contents)]
# ~~~
#
# - id: The NPM package id for the IG
# - title: a human readable name for the IG
# - canonical: the URL at which this package-list.json will be published
# - introduction: an optional commonmark markdown describing the purpose and contents of the IG
# - version list 1..* Publication objects
# - The first entry SHALL be a reference to the CI build. This has current = true, no date, 'current' for the version, etc:

# ~~~
#      {
#          "version": "current",
#          "desc": "Continuous Integration Build (latest in version control)",
#          "path": "http://build.fhir.org/ig/HL7/FHIR-ONC-Meds",
#          "status": "ci-build",
#          "current": true
#       },
#        {
#          "version": "1.1.0",
#          "date": "2019-01-31",
#          "desc": "STU 2",
#          "changes": "n/a",
#          "path": "us/meds/STU2",
#          "status": "trial-use",
#          "sequence": "STU2"
#       },
#       ...
# ~~~
#
# - version: the stated version of the IG for the publication
# - date: the date at which the publication was made [yyyy-mm-dd]
# - path: where the publication is found. Usually at [canonica]/version or similar (absolute URL)
# - desc: a text description of the publication (e.g. reason for publication)
# - changes: a link within the published spec that details the changes in this version (relative URL to path)
# - status: the status of the publication - one of 'draft', 'ballot', 'trial-use', or 'normative'
# - sequence: which group to publish this as part of (typically, 'STU 1' etc). Groups all the ballot publications and the final publication for the ballot sequence
# - current: true if this version should be listed in the current versions summary at the top of the history page. True for the CI-Build, and the version currently posted to the canonical URL
# - Note: the order of publication entries matters. The list should be ordered, with the ci-build entry first, then gr

# Note: run this script in python version 3.6+

# In[41]:


from json import loads, dumps
from pprint import pprint
from pandas import *


# ## Assign the input  and output paths
#
# - you will need to change these to your local directory

# In[42]:


in_path = "/Users/ehaas/Documents/Python/testing/package_list_maker/"
in_file = "package_list.xlsx"
out_path = "/Users/ehaas/Desktop/"


# ### Package list string templates:

# In[43]:


package_list_string = '''{{
 "package-id" : "{package_id}",
 "title" : "{title}",
 "canonical" : "{canonical}",
 "introduction" : "{introduction}",
 "list" : [{{
  "version" : "current",
  "desc" : "Continuous Integration Build (latest in version control)",
  "path" : "http://build.fhir.org/ig/HL7/{ci_path}",
  "status" : "ci-build",
  "current" : true
 }},
  {version_list_string}
 ]
}}'''

version_list_string = '''{{
"version" : "{version}",
 "date" : "{date}",
 "desc" : "{desc}",
 "changes" : "{changes}",
 "path" : "{path}",
 "status" : "{status}",
 "sequence" : "{sequence}"
}}'''


# ### Read read package data as excel file from in_path:
#
# See the [example excel file](#)
#
# - first the header data for the 'package_list' sheet...
#

# In[44]:


xls = ExcelFile(f'{in_path}{in_file}')
df = read_excel(xls,'package_list',na_filter = False)
package_dict = df.squeeze().to_dict()

df # display the sheet contents


# - then the versions data from the 'versions' sheet...

# In[45]:


df = read_excel(xls,'versions',na_filter = False)
versions = df.to_dict('records')

df # display the sheet contents


# ### Using String formatting, Create package-list.json

# In[46]:


version_list = []
for v in versions:
    version_list.append(version_list_string.format(**v))

version_list_string = ', '.join(version_list)

my_pl = package_list_string.format(
version_list_string=version_list_string,
**package_dict)

print(dumps(loads(my_pl), indent=3))   # display the package-list.json


# ### Write file to out_path:

# In[47]:



with open('{out_path}package-list.json'.format(out_path=out_path),'w') as f:
    f.write((dumps(loads(my_pl), indent=3)))


# ## FIN

# In[ ]:
