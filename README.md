
See https://github.com/remorses/tartiflette-apollo-federation-example for an example
For now the plugin only supports simple sharing of types with the same fields and merging of the query and mutation fileds,
In the near future there will be support for the `@key`directive and a new `@ResolveReference('TypeName')` decorator to resolve the types between servers, similar to how Apollo `__resolveReference` works.

To suggest other better api ideas on how to implement `__resolveReference` open a issue.

## Installation
`pip install tartiflette_plugin_apollo_federation`

## Usage
```py
from tartiflette_aiohttp import register_graphql_handlers
from tartiflette_plugin_apollo_federation import ApolloFederationPlugin

def run():
    engine_sdl = "./sdl/"
    app = register_graphql_handlers(
        app=web.Application(),
        engine_sdl=engine_sdl,
        engine_modules=[
            ApolloFederationPlugin(engine_sdl=engine_sdl)
        ],
        executor_http_endpoint="/graphql",
        graphiql_enabled=True,
    )
    web.run_app(app, port=PORT)

run()
```
Then use `xmorse/apollo-federation-gateway` to glue together your services
```yml
version: '3'
services:
    service1:
        build: ./service1
    service2:
        build: ./service2
    gateway:
        image: xmorse/apollo-federation-gateway
        ports:
            - 8000:80
        environment: 
            CONFIG: |
                [
                    {
                        "name": "1",
                        "url": "http://service1:8001/graphql"
                    },
                    {
                        "name": "2",
                        "url": "http://service2:8002/graphql"
                    }
                ]
```



