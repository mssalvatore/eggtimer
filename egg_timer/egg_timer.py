import threading
import time


class EggTimer:
    """
    A class for checking whether or not a certain amount of time has elapsed.
    """

    def __init__(self):
        self._timeout_ns = 0
        self._start_time_ns = 0

    def set(self, timeout_sec: float):
        """
        Set a timer

        :param timeout_sec: A non-negative floating point number expressing the number of
                            seconds to set the timeout for.
        """
        self._timeout_ns = timeout_sec * 1e9
        self._start_time_ns = time.monotonic_ns()

    def is_expired(self) -> bool:
        """
        Check whether or not the timer has expired

        :return: True if the elapsed time since set(TIMEOUT_SEC) was called is greater than
                 TIMEOUT_SEC, False otherwise
        """
        return self.time_remaining_sec == 0

    @property
    def time_remaining_sec(self) -> float:
        """
        Return the amount of time remaining until the timer expires.

        :return: The number of seconds until the timer expires. If the timer is expired, this
                 function returns 0 (it will never return a negative number).
        """
        time_remaining = (self._timeout_ns - (time.monotonic_ns() - self._start_time_ns)) / 1e9
        return max(time_remaining, 0)

    def reset(self):
        """
        Reset the timer without changing the timeout
        """
        self._start_time_ns = time.monotonic_ns()


class ThreadSafeEggTimer(EggTimer):
    """
    A thread-safe implementation of EggTimer.
    """

    def __init__(self):
        self._lock = threading.Lock()
        self._egg_timer = EggTimer()

    def set(self, timeout_sec: float):
        with self._lock:
            self._egg_timer.set(timeout_sec)

    def is_expired(self) -> bool:
        with self._lock:
            return self._egg_timer.is_expired()

    @property
    def time_remaining_sec(self) -> float:
        with self._lock:
            return self._egg_timer.time_remaining_sec

    def reset(self):
        with self._lock:
            self._egg_timer.reset()
