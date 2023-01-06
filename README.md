# EggTimer

There are some ubiquitous patterns that are elegant and simple. There are
others that are not.

```python
from time import time, sleep

start_time = time()
timeout_sec = 42.0
max_sleep_time_sec = 1.5

while time() - start_time < timeout_sec:
    # Do or check some stuff

    time_remaining = timeout_sec - (time() - start_time)
    if time_remaining > 0:
        sleep(min(time_remaining, max_sleep_time_sec))
    else:
        sleep(max_sleep_time_sec)
```

What is the purpose of this loop? Oh, I see, it's a timeout. Is the order of
operations correct in my loop condition? Have I correctly calculated
`time_remaining`?  Is my `if` clause correct? _Hint: It's not._ Does this code
behave properly if the system clock is updated after I set `start_time`? _Hint:
It doesn't._ How many times have I duplicated this code within my application?

We can do better. **EggTimer** can help.

```python
from egg_timer import EggTimer

timer = EggTimer()
timer.set(42.0)
max_sleep_time_sec = 1.5

while not timer.is_expired():
    # Do or check some stuff

    sleep(min(timer.time_remaining_sec, max_sleep_time_sec))
```

Ah, that's better. Clear, concise, reusable, and expressive. The risk of
defects is significantly lower, too!

## Installation
Install with `pip install -U egg-timer`

## Documentation

```pycon
Python 3.10.4 (main, Jun 29 2022, 12:14:53) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from egg_timer import EggTimer
>>> help(EggTimer)
Help on class EggTimer in module egg_timer.egg_timer:

class EggTimer(builtins.object)
 |  A class for checking whether or not a certain amount of time has elapsed.
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  is_expired(self)
 |      Check whether or not the timer has expired
 |
 |      :return: True if the elapsed time since set(TIMEOUT_SEC) was called is greater than
 |               TIMEOUT_SEC, False otherwise
 |
 |  reset(self)
 |      Reset the timer without changing the timeout
 |
 |  set(self, timeout_sec: float)
 |      Set a timer
 |
 |      :param timeout_sec: A non-negative floating point number expressing the number of
 |                          seconds to set the timeout for.
 |
 |  ----------------------------------------------------------------------
 |  Readonly properties defined here:
 |
 |  time_remaining_sec
 |      Return the amount of time remaining until the timer expires.
 |
 |      :return: The number of seconds until the timer expires. If the timer is expired, this
 |               function returns 0 (it will never return a negative number).
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

>>>
```

## Running the tests

Running the tests is as simple as `poetry install && poetry run pytest`
