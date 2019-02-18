

**Request**

~~~
GET http://sqlonfhir-stu3.azurewebsites.net/fhir/Questionnaire?context-code=task&value=example

User-Agent: python-requests/2.20.0
Accept: application/fhir+json
Content-Type: application/fhir+json
[other headers]
~~~

**Response**

~~~
Response Code: 200 (OK)
Content-Type: application/fhir+json; charset=utf-8
Content-Location: http://sqlonfhir-stu3.azurewebsites.net/fhir/Bundle/urn:uuid:b42a2e0bae894f3a9479cd3f96df6713
[other headers]

    
{
   "resourceType": "Bundle",
   "id": "urn:uuid:b42a2e0bae894f3a9479cd3f96df6713",
   "meta": {
      "lastUpdated": "2019-02-13T08:37:40.296+00:00"
   },
   "type": "searchset",
   "total": 67,
   "link": [
      {
         "relation": "self",
         "url": "http://sqlonfhir-stu3.azurewebsites.net/fhir/Questionnaire?context-code=task&value=example&_snapshot=636856438602967410"
      },
      {
         "relation": "first",
         "url": "http://sqlonfhir-stu3.azurewebsites.net/fhir/Questionnaire?context-code=task&value=example&_snapshot=636856438602967410"
      },
      {
         "relation": "next",
         "url": "http://sqlonfhir-stu3.azurewebsites.net/fhir/Questionnaire?context-code=task&value=example&_snapshot=636856438602967410&_page=1"

        ...[snipped for brevity]....
      
~~~
