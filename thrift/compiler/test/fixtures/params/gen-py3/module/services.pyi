#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import typing as _typing
from thrift.py3.server import RequestContext, ServiceInterface

import module.types as _module_types



class NestedContainersInterface(
    ServiceInterface
):
    @_typing.overload
    async def mapList(
        self,
        ctx: RequestContext,
        foo: _typing.Mapping[int, _typing.Sequence[int]]
    ) -> None: ...

    async def mapList(
        self,
        foo: _typing.Mapping[int, _typing.Sequence[int]]
    ) -> None: ...

    @_typing.overload
    async def mapSet(
        self,
        ctx: RequestContext,
        foo: _typing.Mapping[int, _typing.AbstractSet[int]]
    ) -> None: ...

    async def mapSet(
        self,
        foo: _typing.Mapping[int, _typing.AbstractSet[int]]
    ) -> None: ...

    @_typing.overload
    async def listMap(
        self,
        ctx: RequestContext,
        foo: _typing.Sequence[_typing.Mapping[int, int]]
    ) -> None: ...

    async def listMap(
        self,
        foo: _typing.Sequence[_typing.Mapping[int, int]]
    ) -> None: ...

    @_typing.overload
    async def listSet(
        self,
        ctx: RequestContext,
        foo: _typing.Sequence[_typing.AbstractSet[int]]
    ) -> None: ...

    async def listSet(
        self,
        foo: _typing.Sequence[_typing.AbstractSet[int]]
    ) -> None: ...

    @_typing.overload
    async def turtles(
        self,
        ctx: RequestContext,
        foo: _typing.Sequence[_typing.Sequence[_typing.Mapping[int, _typing.Mapping[int, _typing.AbstractSet[int]]]]]
    ) -> None: ...

    async def turtles(
        self,
        foo: _typing.Sequence[_typing.Sequence[_typing.Mapping[int, _typing.Mapping[int, _typing.AbstractSet[int]]]]]
    ) -> None: ...

