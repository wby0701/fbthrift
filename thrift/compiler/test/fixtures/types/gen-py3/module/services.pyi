#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import typing as _typing
from thrift.py3.server import RequestContext, ServiceInterface

import module.types as _module_types
cimport include.types as _include_types



class SomeServiceInterface(
    ServiceInterface
):
    @_typing.overload
    async def bounce_map(
        self,
        ctx: RequestContext,
        m: _typing.Mapping[int, str]
    ) -> _typing.Mapping[int, str]: ...

    async def bounce_map(
        self,
        m: _typing.Mapping[int, str]
    ) -> _typing.Mapping[int, str]: ...

