

**Request**

~~~
GET http://sqlonfhir-stu3.azurewebsites.net/fhir/Questionnaire?status=active

User-Agent: python-requests/2.20.0
Accept: application/fhir+json
Content-Type: application/fhir+json
[other headers]
~~~

**Response**

~~~
Response Code: 200 (OK)
Content-Type: application/fhir+json; charset=utf-8
Content-Location: http://sqlonfhir-stu3.azurewebsites.net/fhir/Bundle/urn:uuid:6eccbe318ec64cc583ceb8d54d0fc25e
[other headers]

    
{
   "resourceType": "Bundle",
   "id": "urn:uuid:6eccbe318ec64cc583ceb8d54d0fc25e",
   "meta": {
      "lastUpdated": "2019-02-13T08:37:39.359+00:00"
   },
   "type": "searchset",
   "total": 23,
   "link": [
      {
         "relation": "self",
         "url": "http://sqlonfhir-stu3.azurewebsites.net/fhir/Questionnaire?status=active&_snapshot=636856438593592368"
      },
      {
         "relation": "first",
         "url": "http://sqlonfhir-stu3.azurewebsites.net/fhir/Questionnaire?status=active&_snapshot=636856438593592368"
      },
      {
         "relation": "next",
         "url": "http://sqlonfhir-stu3.azurewebsites.net/fhir/Questionnaire?status=active&_snapshot=636856438593592368&_page=1"
      },
      {
         "relation": "last",
        ...[snipped for brevity]....
      
~~~
