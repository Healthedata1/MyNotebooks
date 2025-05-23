'

  Note: Formal authorization is optional and typically in provider to provider transactions.

  {:.bg-info}


  ##### Step 1 - Create CommunicationRequest (on Referred-To Provider system)


  ~~~

  {% include cdex-example1-authorization.json %}

  ~~~


  ##### Step 2 - POST Task to Referring Provider endpoint


  **Request**

  ~~~

  POST [base]/Task

  ~~~


  {% include request-headers.md %}


  **Request Body**


  ~~~

  {% include cdex-task-example11.json %}

  ~~~


  **Response Headers**


  ~~~

  HTTP/1.1 200 OK

  Server: CDEX Example Server

  Location: http://example.org/FHIR/Task/cdex-task-example2/_history/1

  ...(other headers)

  ~~~


  ##### Step 3 - (Optional) Referring Provider Fetches CommunicationRequest


  **Request from Referring Provider**

  ~~~

  POST [base]CommunicationRequest/cdex-example1-authorization

  ~~~


  {% include request-headers.md %}


  {% include response-headers.md %}


  **Response Body**


  ~~~

  {% include cdex-example1-authorization.json %}

  ~~~


  ##### Step 4 - Referred-To Provider Polls Task


  **Polling Request**

  ~~~

  GET Task/cdex-task-example2

  ~~~


  {% include request-headers.md %}


  {% include response-headers.md %}


  **Response Body**


  ~~~

  {% include_relative Task-cdex-task-example12.json %}

  ~~~


  ##### Step 5 - Referred-To Provider Fetches Active Conditions


  **Request**

  ~~~

  POST [base]Condition/858

  ~~~


  {% include request-headers.md %}


  {% include response-headers.md %}


  **Response Body**


  ~~~

  {% include condition-858.json %}

  ~~~

  '
