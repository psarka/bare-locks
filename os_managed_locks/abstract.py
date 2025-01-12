"""
OS managed locks faithfully and thinly (but sanely!) wraps all
the available file locking mechanisms. Currently it exposes all the possible
file locking mechanisms enabled by python standard library, and in the future
it may include features and mechanisms that are only available through C
extensions.

These mechanisms can be used on their own or can be further wrapped on top to
produce a syntactically sweeter locks.
"""

import abc

from os_managed_locks.typing.literal import Literal


class FileLockingMechanism(abc.ABC):
    """File locking Mechanism"""

    can_share = False
    """Whether the mechanism supports shared locks"""

    can_block = False
    """Whether the mechanism supports blocking until lock is acquired"""

    can_switch = False
    """Whether the mechanism can atomically switch shared vs exclusive locks"""

    available = False
    """Whether the mechanism is available on the current platform"""

    @staticmethod
    @abc.abstractmethod
    def lock(handle):
        """Acquire a lock on the file

        Acquiring a lock can fail if the handle is already locked by another
        process, or because of some unexpected issue. The former (normal)
        failure is reported by the return value, the latter by an exception.

        msvcrt mechanism does not support shared locks, and does not support
        blocking until a lock is acquired.

        Parameters
        ----------
        handle:
            File handle

        Returns
        -------
        bool
            Whether a lock was acquired
        """

    @staticmethod
    @abc.abstractmethod
    def unlock(handle):
        """Release the previously acquired lock

        Parameters
        ----------
        handle:
            File handle
        """


RelativeTo = Literal["start", "current", "end"]
