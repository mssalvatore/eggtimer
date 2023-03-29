import time
from typing import Callable

import pytest

from egg_timer import EggTimer, ThreadSafeEggTimer


@pytest.fixture
def start_time(set_current_time: Callable[[float], None]) -> float:
    start_time = 100
    set_current_time(start_time)

    return start_time


@pytest.fixture
def set_current_time(monkeypatch) -> Callable[[float], None]:
    def inner(current_time_sec: float):
        monkeypatch.setattr(time, "monotonic_ns", lambda: current_time_sec * 1e9)

    return inner


@pytest.mark.parametrize("egg_timer_factory", [EggTimer, ThreadSafeEggTimer])
@pytest.mark.parametrize(("timeout"), [5, 1.25])
def test_timer_not_expired(
    egg_timer_factory: Callable[[], EggTimer],
    start_time: float,
    set_current_time: Callable[[float], None],
    timeout: float,
):
    t = egg_timer_factory()
    t.set(timeout)

    assert not t.is_expired()

    set_current_time(start_time + (timeout - 0.001))
    assert not t.is_expired()


@pytest.mark.parametrize("egg_timer_factory", [EggTimer, ThreadSafeEggTimer])
@pytest.mark.parametrize(("timeout"), [5, 1.25])
def test_timer_expired(
    egg_timer_factory: Callable[[], EggTimer],
    start_time: float,
    set_current_time: Callable[[float], None],
    timeout: float,
):
    t = egg_timer_factory()
    t.set(timeout)

    assert not t.is_expired()

    set_current_time(start_time + timeout)
    assert t.is_expired()

    set_current_time(start_time + timeout + 0.001)
    assert t.is_expired()


@pytest.mark.parametrize("egg_timer_factory", [EggTimer, ThreadSafeEggTimer])
def test_unset_timer_expired(egg_timer_factory: Callable[[], EggTimer]):
    t = egg_timer_factory()

    assert t.is_expired()


@pytest.mark.parametrize("egg_timer_factory", [EggTimer, ThreadSafeEggTimer])
@pytest.mark.parametrize(("timeout"), [5, 1.25])
def test_timer_reset(
    egg_timer_factory: Callable[[], EggTimer],
    start_time: float,
    set_current_time: Callable[[float], None],
    timeout: float,
):
    t = egg_timer_factory()
    t.set(timeout)

    assert not t.is_expired()

    set_current_time(start_time + timeout)
    assert t.is_expired()

    t.reset()
    assert not t.is_expired()

    set_current_time(start_time + (2 * timeout))
    assert t.is_expired()


@pytest.mark.parametrize("egg_timer_factory", [EggTimer, ThreadSafeEggTimer])
def test_time_remaining(
    egg_timer_factory: Callable[[], EggTimer],
    start_time: float,
    set_current_time: Callable[[float], None],
):
    timeout = 5

    t = egg_timer_factory()
    t.set(timeout)

    assert t.time_remaining_sec == timeout

    set_current_time(start_time + 2)
    assert t.time_remaining_sec == 3


@pytest.mark.parametrize("egg_timer_factory", [EggTimer, ThreadSafeEggTimer])
def test_time_remaining_is_zero(
    egg_timer_factory: Callable[[], EggTimer],
    start_time: float,
    set_current_time: Callable[[float], None],
):
    timeout = 5

    t = egg_timer_factory()
    t.set(timeout)

    set_current_time(start_time + timeout)
    assert t.time_remaining_sec == 0

    set_current_time(start_time + (2 * timeout))
    assert t.time_remaining_sec == 0
