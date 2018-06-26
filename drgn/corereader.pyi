from os import PathLike
from typing import Any, Union


class CoreReader:
    def __init__(self, path: Union[str, bytes, PathLike]) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CoreReader: ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
    def read(self, address: int, size: int, physical: bool = ...) -> bytes: ...
    def read_u8(self, address: int, physical: bool = ...) -> int: ...
    def read_u16(self, address: int, physical: bool = ...) -> int: ...
    def read_u32(self, address: int, physical: bool = ...) -> int: ...
    def read_u64(self, address: int, physical: bool = ...) -> int: ...
    def read_s8(self, address: int, physical: bool = ...) -> int: ...
    def read_s16(self, address: int, physical: bool = ...) -> int: ...
    def read_s32(self, address: int, physical: bool = ...) -> int: ...
    def read_s64(self, address: int, physical: bool = ...) -> int: ...
    def read_bool(self, address: int, physical: bool = ...) -> bool: ...
    def read_bool16(self, address: int, physical: bool = ...) -> bool: ...
    def read_bool32(self, address: int, physical: bool = ...) -> bool: ...
    def read_bool64(self, address: int, physical: bool = ...) -> bool: ...
    def read_float(self, address: int, physical: bool = ...) -> float: ...
    def read_double(self, address: int, physical: bool = ...) -> float: ...
    def read_long_double(self, address: int, physical: bool = ...) -> float: ...
