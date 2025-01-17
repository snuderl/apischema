from dataclasses import dataclass, field

from pytest import raises

from apischema import ValidationError, deserialize
from apischema.metadata import fall_back_on_default


@dataclass
class Foo:
    bar: str = "bar"
    baz: str = field(default="baz", metadata=fall_back_on_default)


with raises(ValidationError):
    deserialize(Foo, {"bar": 0})
assert deserialize(Foo, {"bar": 0}, fall_back_on_default=True) == Foo()
assert deserialize(Foo, {"baz": 0}) == Foo()
