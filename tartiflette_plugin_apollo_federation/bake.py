import os.path
from tartiflette_scalars import Json, AnyScalar
from glob import glob
from tartiflette import Resolver, Scalar, Engine


async def bake(schema_name, config):
    sdl = get_sdl(config['sdl'])
    Scalar("_Any")(Json)
    Scalar("_FieldSet")(AnyScalar)
    @Resolver('Query._service')
    async def revolve_service(_, args, ctx, info):
        return {
            'sdl': sdl + BUILTINS,
        }
    return _SDL


def get_sdl(sdl):
    sdl_files_list = []
    full_sdl = ""

    if isinstance(sdl, list):
        sdl_files_list += sdl
    elif os.path.isfile(sdl):
        sdl_files_list.append(sdl)
    elif os.path.isdir(sdl):
        sdl_files_list += glob(
            os.path.join(sdl, "**/*.sdl"), recursive=True
        ) + glob(os.path.join(sdl, "**/*.graphql"), recursive=True)
    for filepath in sdl_files_list:
        with open(filepath, mode="r") as sdl_file:
            full_sdl += "\n" + sdl_file.read()
    return full_sdl

BUILTINS = '''

scalar DateTime
scalar Time
scalar Date
directive @nonIntrospectable on FIELD_DEFINITION
'''
_SDL = '''
scalar _Any
scalar _FieldSet
# a union of all types that use the @key directive
# union _Entity = User

type _Service {
  sdl: String
}

extend type Query {
  # _entities(representations: [_Any!]!): [_Entity]!
  _service: _Service!
}

# directive @external on FIELD_DEFINITION
# directive @requires(fields: _FieldSet!) on FIELD_DEFINITION
# directive @provides(fields: _FieldSet!) on FIELD_DEFINITION
# directive @key(fields: _FieldSet!) on OBJECT | INTERFACE

# # this is an optional directive discussed below
# directive @extends on OBJECT | INTERFACE
'''