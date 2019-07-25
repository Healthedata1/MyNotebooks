**Bundle**

#### Summary of the Mandatory Requirements
1.  A  code  in `Bundle.type`
with a [required](http://hl7.org/fhir/R4/terminologies.html#required)
 binding to [BundleType](http://hl7.org/fhir/ValueSet/bundle-type|4.0.0)
1. One or more  Entrys  in `Bundle.entry`
 with the following constraints: *fullUrl cannot be a version specific reference, must be a resource unless there&#39;s a request or response*
   - which must have at least  a  Entry value  in `Bundle.entry`
      - which must have a Resource Reference value  in `Bundle.entry.resource`
      - which must have a  Request value  in `Bundle.entry.request`
         - which must have a fixed `Bundle.entry.request.method` = `POST`
         - which must have an  uri value  in `Bundle.entry.request.url`

#### Summary of the Must Support Requirements
1.  A  Entry  in `Bundle.entry`
 with the following constraints: *fullUrl cannot be a version specific reference, must be a resource unless there&#39;s a request or response*
   - which must have a Resource Reference value  in `Bundle.entry.resource`
   - which must have a  Request value  in `Bundle.entry.request`
   - which must have a fixed `Bundle.entry.request.method` = `POST`
   - which must have an  uri value  in `Bundle.entry.request.url`
1.  A  Entry  in `Bundle.entry`
 with the following constraints: *fullUrl cannot be a version specific reference, must be a resource unless there&#39;s a request or response*
   - which must have a Resource Reference value  in `Bundle.entry.resource`
   - which must have a  Request value  in `Bundle.entry.request`
   - which must have a fixed `Bundle.entry.request.method` = `POST`
   - which must have an  uri value  in `Bundle.entry.request.url`

#### Summary of Constraints
1. FullUrl must be unique in a bundle, or else entries with the same fullUrl must have different meta.versionId (except in history bundles)
1. A document must have an identifier with a system and a value
1. entry.request mandatory for batch/transaction/history, otherwise prohibited
1. entry.response mandatory for batch-response/transaction-response/history, otherwise prohibited
1. A message must have a MessageHeader as the first resource
1. total only when a search or history
1. entry.search only when a search
1. A document must have a Composition as the first resource
1. A document must have a date
1. fullUrl cannot be a version specific reference
1. must be a resource unless there&#39;s a request or response