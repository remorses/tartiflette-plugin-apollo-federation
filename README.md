
For now the plugin only supports simple sharing of types with the same fields and merging of the query and mutation fileds,
In the near future there will be support for the `@key`directive and a new `@ResolveReference('TypeName')` decorator to resolve the types between servers, similar to how Apollo `__resolveReference` works.

To suggest other better api ideas on how to implement `__resolveReference` open a issue.
