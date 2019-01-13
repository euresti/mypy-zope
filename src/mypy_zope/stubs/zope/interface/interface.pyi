# Stubs for zope.interface.interface (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from zope.interface._zope_interface_coptimizations import InterfaceBase, SpecificationBase

CO_VARARGS: int
CO_VARKEYWORDS: int
TAGGED_DATA: str

def invariant(call: Any): ...
def taggedValue(key: Any, value: Any): ...

class Element:
    __name__: Any = ...
    __doc__: Any = ...
    def __init__(self, __name__: Any, __doc__: str = ...) -> None: ...
    def getName(self): ...
    def getDoc(self): ...
    def getTaggedValue(self, tag: Any): ...
    def queryTaggedValue(self, tag: Any, default: Optional[Any] = ...): ...
    def getTaggedValueTags(self): ...
    def setTaggedValue(self, tag: Any, value: Any) -> None: ...

class SpecificationBasePy:
    def providedBy(self, ob: Any): ...
    def implementedBy(self, cls: Any): ...
    def isOrExtends(self, interface: Any): ...
    __call__: Any = ...
SpecificationBase = SpecificationBasePy

class InterfaceBasePy:
    def __call__(self, obj: Any, alternate: Any = ...): ...
    def __adapt__(self, obj: Any): ...
InterfaceBase = InterfaceBasePy
adapter_hooks: Any

class Specification(SpecificationBase):
    isOrExtends: Any = ...
    providedBy: Any = ...
    dependents: Any = ...
    __bases__: Any = ...
    def __init__(self, bases: Any = ...) -> None: ...
    def subscribe(self, dependent: Any) -> None: ...
    def unsubscribe(self, dependent: Any) -> None: ...
    __sro__: Any = ...
    __iro__: Any = ...
    def changed(self, originally_changed: Any) -> None: ...
    def interfaces(self) -> None: ...
    def extends(self, interface: Any, strict: bool = ...): ...
    def weakref(self, callback: Optional[Any] = ...): ...
    def get(self, name: Any, default: Optional[Any] = ...): ...

class InterfaceClass(Element, InterfaceBase, Specification):
    __module__: Any = ...
    __identifier__: Any = ...
    def __init__(self, name: Any, bases: Any = ..., attrs: Optional[Any] = ..., __doc__: Optional[Any] = ..., __module__: Optional[Any] = ...) -> None: ...
    def interfaces(self) -> None: ...
    def getBases(self): ...
    def isEqualOrExtendedBy(self, other: Any): ...
    def names(self, all: bool = ...): ...
    def __iter__(self): ...
    def namesAndDescriptions(self, all: bool = ...): ...
    def getDescriptionFor(self, name: Any): ...
    __getitem__: Any = ...
    def __contains__(self, name: Any): ...
    def direct(self, name: Any): ...
    def queryDescriptionFor(self, name: Any, default: Optional[Any] = ...): ...
    def validateInvariants(self, obj: Any, errors: Optional[Any] = ...) -> None: ...
    def __reduce__(self): ...
    def __hash__(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __lt__(self, other: Any): ...
    def __le__(self, other: Any): ...
    def __gt__(self, other: Any): ...
    def __ge__(self, other: Any): ...

Interface: Any

class Attribute(Element):
    interface: Any = ...

class Method(Attribute):
    positional: Any = ...
    required: Any = ...
    varargs: Any = ...
    kwargs: Any = ...
    optional: Any = ...
    def __call__(self, *args: Any, **kw: Any) -> None: ...
    def getSignatureInfo(self): ...
    def getSignatureString(self): ...

def fromFunction(func: Any, interface: Optional[Any] = ..., imlevel: int = ..., name: Optional[Any] = ...): ...
def fromMethod(meth: Any, interface: Optional[Any] = ..., name: Optional[Any] = ...): ...
