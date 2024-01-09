from warnings import warn

from .eggtimer import EggTimer, ThreadSafeEggTimer


warn(
    "The `egg_timer` package has been deprecated and will be removed in v2.0.0. Please use"
    "`eggtimer` instead.",
    DeprecationWarning,
    stacklevel=2,
)
