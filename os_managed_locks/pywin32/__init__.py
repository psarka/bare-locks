"""
Exposes the minimal amount of code to use Win32 native file locking. We only
need two APIs, so this is far lighter weight than pulling in all of pywin32.
"""

from os_managed_locks.pywin32 import pywintypes
from os_managed_locks.pywin32 import win32con
from os_managed_locks.pywin32 import win32file

