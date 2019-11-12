**Bundle**

#### Summary of the Mandatory Requirements
1.  A  code  in `Bundle.type`  = the fixed value  "message"

#### Summary of the Unsupported Elements
1. `Bundle.total`
1. `Bundle.entry.search`
1. `Bundle.entry.request`
1. `Bundle.entry.response`

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