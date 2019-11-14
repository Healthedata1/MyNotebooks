**Bundle**

#### Summary of the Mandatory Requirements
1. One or more  Entrys  in `Bundle.entry`
 with the following constraints: *must be a resource unless there&#39;s a request or response, fullUrl cannot be a version specific reference*
   - which must have at least  an  Entry value  in `Bundle.entry`
      - which must have a  MessageHeader value  in `Bundle.entry.resource`
   - which must have at least  one or more  Entry values  in `Bundle.entry`
      - which must have an  Encounter value  in `Bundle.entry.resource`
   - which must have at least  an  Entry value  in `Bundle.entry`
      - which must have a  Patient value  in `Bundle.entry.resource`
   - which must have at least  one or more  Entry values  in `Bundle.entry`
      - which must have a  Location value  in `Bundle.entry.resource`

#### Summary of the Must Support Requirements
1. One or more  Entrys  in `Bundle.entry`
 with the following constraints: *must be a resource unless there&#39;s a request or response, fullUrl cannot be a version specific reference*
   - which must have a  Practitioner value  in `Bundle.entry.resource`
1. One or more  Entrys  in `Bundle.entry`
 with the following constraints: *must be a resource unless there&#39;s a request or response, fullUrl cannot be a version specific reference*
   - which must have a  Condition value  in `Bundle.entry.resource`
1. One or more  Entrys  in `Bundle.entry`
 with the following constraints: *must be a resource unless there&#39;s a request or response, fullUrl cannot be a version specific reference*
   - which must have a  Coverage value  in `Bundle.entry.resource`
1.  An  Entry  in `Bundle.entry`
 with the following constraints: *must be a resource unless there&#39;s a request or response, fullUrl cannot be a version specific reference*
   - which must have a  Practitioner value  in `Bundle.entry.resource`
1.  An  Entry  in `Bundle.entry`
 with the following constraints: *must be a resource unless there&#39;s a request or response, fullUrl cannot be a version specific reference*
   - which must have a  Practitioner value  in `Bundle.entry.resource`
1.  An  Entry  in `Bundle.entry`
 with the following constraints: *must be a resource unless there&#39;s a request or response, fullUrl cannot be a version specific reference*
   - which must have a  Practitioner value  in `Bundle.entry.resource`

#### Summary of Constraints
1. total only when a search or history
1. entry.search only when a search
1. entry.request mandatory for batch/transaction/history, otherwise prohibited
1. entry.response mandatory for batch-response/transaction-response/history, otherwise prohibited
1. FullUrl must be unique in a bundle, or else entries with the same fullUrl must have different meta.versionId (except in history bundles)
1. A document must have an identifier with a system and a value
1. A document must have a date
1. A document must have a Composition as the first resource
1. A message must have a MessageHeader as the first resource
1. must be a resource unless there&#39;s a request or response
1. fullUrl cannot be a version specific reference