#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import typing as _typing
from thrift.py3.server import RequestContext, ServiceInterface

import module.types as _module_types



class MyServiceInterface(
    ServiceInterface
):
    @_typing.overload
    async def ping(
        self,
        ctx: RequestContext
    ) -> None: ...

    async def ping(
        self
    ) -> None: ...

    @_typing.overload
    async def getRandomData(
        self,
        ctx: RequestContext
    ) -> str: ...

    async def getRandomData(
        self
    ) -> str: ...

    @_typing.overload
    async def hasDataById(
        self,
        ctx: RequestContext,
        id: int
    ) -> bool: ...

    async def hasDataById(
        self,
        id: int
    ) -> bool: ...

    @_typing.overload
    async def getDataById(
        self,
        ctx: RequestContext,
        id: int
    ) -> str: ...

    async def getDataById(
        self,
        id: int
    ) -> str: ...

    @_typing.overload
    async def putDataById(
        self,
        ctx: RequestContext,
        id: int,
        data: str
    ) -> None: ...

    async def putDataById(
        self,
        id: int,
        data: str
    ) -> None: ...

    @_typing.overload
    async def lobDataById(
        self,
        ctx: RequestContext,
        id: int,
        data: str
    ) -> None: ...

    async def lobDataById(
        self,
        id: int,
        data: str
    ) -> None: ...



class MyServiceFastInterface(
    ServiceInterface
):
    @_typing.overload
    async def ping(
        self,
        ctx: RequestContext
    ) -> None: ...

    async def ping(
        self
    ) -> None: ...

    @_typing.overload
    async def getRandomData(
        self,
        ctx: RequestContext
    ) -> str: ...

    async def getRandomData(
        self
    ) -> str: ...

    @_typing.overload
    async def hasDataById(
        self,
        ctx: RequestContext,
        id: int
    ) -> bool: ...

    async def hasDataById(
        self,
        id: int
    ) -> bool: ...

    @_typing.overload
    async def getDataById(
        self,
        ctx: RequestContext,
        id: int
    ) -> str: ...

    async def getDataById(
        self,
        id: int
    ) -> str: ...

    @_typing.overload
    async def putDataById(
        self,
        ctx: RequestContext,
        id: int,
        data: str
    ) -> None: ...

    async def putDataById(
        self,
        id: int,
        data: str
    ) -> None: ...

    @_typing.overload
    async def lobDataById(
        self,
        ctx: RequestContext,
        id: int,
        data: str
    ) -> None: ...

    async def lobDataById(
        self,
        id: int,
        data: str
    ) -> None: ...



class MyServiceEmptyInterface(
    ServiceInterface
):


class MyServicePrioParentInterface(
    ServiceInterface
):
    @_typing.overload
    async def ping(
        self,
        ctx: RequestContext
    ) -> None: ...

    async def ping(
        self
    ) -> None: ...

    @_typing.overload
    async def pong(
        self,
        ctx: RequestContext
    ) -> None: ...

    async def pong(
        self
    ) -> None: ...



class MyServicePrioChildInterface(
    _module_services.MyServicePrioParentInterface
):
    @_typing.overload
    async def pang(
        self,
        ctx: RequestContext
    ) -> None: ...

    async def pang(
        self
    ) -> None: ...

