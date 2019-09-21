from .bake import bake
from typing import List, Union

class ApolloFederationPlugin(dict):
    def __init__(self, engine_sdl: Union[str, List[str]]):
        super().__init__({
            "name": "tartiflette_plugin_apollo_federation",
            "config": {"sdl": engine_sdl},
        })


