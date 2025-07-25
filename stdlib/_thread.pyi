import signal
import sys
from _typeshed import structseq
from collections.abc import Callable
from threading import Thread
from types import TracebackType
from typing import Any, Final, NoReturn, final, overload
from typing_extensions import TypeVarTuple, Unpack

_Ts = TypeVarTuple("_Ts")

error = RuntimeError

def _count() -> int: ...
@final
class RLock:
    def acquire(self, blocking: bool = True, timeout: float = -1) -> bool: ...
    def release(self) -> None: ...
    __enter__ = acquire
    def __exit__(self, t: type[BaseException] | None, v: BaseException | None, tb: TracebackType | None) -> None: ...
    if sys.version_info >= (3, 14):
        def locked(self) -> bool: ...

if sys.version_info >= (3, 13):
    @final
    class _ThreadHandle:
        ident: int

        def join(self, timeout: float | None = None, /) -> None: ...
        def is_done(self) -> bool: ...
        def _set_done(self) -> None: ...

    def start_joinable_thread(
        function: Callable[[], object], handle: _ThreadHandle | None = None, daemon: bool = True
    ) -> _ThreadHandle: ...
    @final
    class lock:
        def acquire(self, blocking: bool = True, timeout: float = -1) -> bool: ...
        def release(self) -> None: ...
        def locked(self) -> bool: ...
        def acquire_lock(self, blocking: bool = True, timeout: float = -1) -> bool: ...
        def release_lock(self) -> None: ...
        def locked_lock(self) -> bool: ...
        def __enter__(self) -> bool: ...
        def __exit__(
            self, type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
        ) -> None: ...

    LockType = lock
else:
    @final
    class LockType:
        def acquire(self, blocking: bool = True, timeout: float = -1) -> bool: ...
        def release(self) -> None: ...
        def locked(self) -> bool: ...
        def acquire_lock(self, blocking: bool = True, timeout: float = -1) -> bool: ...
        def release_lock(self) -> None: ...
        def locked_lock(self) -> bool: ...
        def __enter__(self) -> bool: ...
        def __exit__(
            self, type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
        ) -> None: ...

@overload
def start_new_thread(function: Callable[[Unpack[_Ts]], object], args: tuple[Unpack[_Ts]], /) -> int: ...
@overload
def start_new_thread(function: Callable[..., object], args: tuple[Any, ...], kwargs: dict[str, Any], /) -> int: ...

# Obsolete synonym for start_new_thread()
@overload
def start_new(function: Callable[[Unpack[_Ts]], object], args: tuple[Unpack[_Ts]], /) -> int: ...
@overload
def start_new(function: Callable[..., object], args: tuple[Any, ...], kwargs: dict[str, Any], /) -> int: ...

if sys.version_info >= (3, 10):
    def interrupt_main(signum: signal.Signals = signal.SIGINT, /) -> None: ...

else:
    def interrupt_main() -> None: ...

def exit() -> NoReturn: ...
def exit_thread() -> NoReturn: ...  # Obsolete synonym for exit()
def allocate_lock() -> LockType: ...
def allocate() -> LockType: ...  # Obsolete synonym for allocate_lock()
def get_ident() -> int: ...
def stack_size(size: int = 0, /) -> int: ...

TIMEOUT_MAX: float

def get_native_id() -> int: ...  # only available on some platforms
@final
class _ExceptHookArgs(structseq[Any], tuple[type[BaseException], BaseException | None, TracebackType | None, Thread | None]):
    if sys.version_info >= (3, 10):
        __match_args__: Final = ("exc_type", "exc_value", "exc_traceback", "thread")

    @property
    def exc_type(self) -> type[BaseException]: ...
    @property
    def exc_value(self) -> BaseException | None: ...
    @property
    def exc_traceback(self) -> TracebackType | None: ...
    @property
    def thread(self) -> Thread | None: ...

_excepthook: Callable[[_ExceptHookArgs], Any]

if sys.version_info >= (3, 12):
    def daemon_threads_allowed() -> bool: ...

if sys.version_info >= (3, 14):
    def set_name(name: str) -> None: ...

class _local:
    def __getattribute__(self, name: str, /) -> Any: ...
    def __setattr__(self, name: str, value: Any, /) -> None: ...
    def __delattr__(self, name: str, /) -> None: ...
