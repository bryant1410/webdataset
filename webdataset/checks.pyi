from typing import Any

def checktype(value: Any, types: Any, msg: str = ...) -> None: ...
def checkmember(value: Any, values: Any, msg: str = ...) -> None: ...
def checkrange(value: Any, lo: Any, hi: Any, msg: str = ...) -> None: ...
def check(value: Any, msg: str = ...) -> None: ...
def checkcallable(value: Any, msg: str = ...) -> None: ...
def checknotnone(value: Any, msg: str = ...) -> None: ...