#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import typing as _typing
from thrift.py3.server import RequestContext, ServiceInterface

import module.types as _module_types



class MyRootInterface(
    ServiceInterface
):
    @_typing.overload
    async def do_root(
        self,
        ctx: RequestContext
    ) -> None: ...

    async def do_root(
        self
    ) -> None: ...



class MyNodeInterface(
    _module_services.MyRootInterface
):
    @_typing.overload
    async def do_mid(
        self,
        ctx: RequestContext
    ) -> None: ...

    async def do_mid(
        self
    ) -> None: ...



class MyLeafInterface(
    _module_services.MyNodeInterface
):
    @_typing.overload
    async def do_leaf(
        self,
        ctx: RequestContext
    ) -> None: ...

    async def do_leaf(
        self
    ) -> None: ...

