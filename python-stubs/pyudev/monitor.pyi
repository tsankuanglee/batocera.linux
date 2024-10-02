from collections.abc import Callable, Iterator
from threading import Thread
from typing import Any, Self
from typing_extensions import deprecated

from .core import Context
from .device import Device

class Monitor:
    @classmethod
    def from_netlink(cls, context: Context, source: str = ...) -> Self: ...
    @property
    def started(self) -> bool: ...
    def fileno(self) -> int: ...
    def filter_by(self, subsystem: str, device_type: str | bytes | None = None) -> None: ...
    def filter_by_tag(self, tag: str | bytes) -> None: ...
    def remove_filter(self) -> None: ...
    @deprecated('Will be removed in 1.0. Use `start()` instead.')
    def enable_receiving(self) -> None: ...
    def start(self) -> None: ...
    def set_receive_buffer_size(self, size: int) -> None: ...
    def poll(self, timeout: float | None = None) -> Device | None: ...
    @deprecated('Will be removed in 1.0. Use `poll()` instead.')
    def receive_device(self) -> tuple[str, Device]: ...
    @deprecated('Will be removed in 1.0. Use an explicit loop over `poll()` instead, or monitor asynchronously with `MonitorObserver`')
    def __iter__(self) -> Iterator[tuple[str, Device]]: ...

class MonitorObserver(Thread):
    monitor: Monitor
    daemon: bool
    def __init__(self, monitor: Monitor, callback: Callable[[Device], Any] | None = None, *args: Any, **kwargs: Any) -> None: ...
    def start(self) -> None: ...
    def run(self) -> None: ...
    def send_stop(self) -> None: ...
    def stop(self) -> None: ...