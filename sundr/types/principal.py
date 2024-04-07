"""
In SUNDR, a principal is a unique entity that can be used to
identify a user or a group. A principal has the write access
for a given file.
"""


class Princiapl:
    """
    Base class for all principals.
    """

    @property
    def id(self) -> int:
        """
        Returns the id of the principal.
        """
        raise NotImplementedError

    def is_user(self) -> bool:
        """
        Returns True if the principal is a user.
        """
        raise NotImplementedError

    def is_group(self) -> bool:
        """
        Returns True if the principal is a group.
        """
        raise NotImplementedError


class User(Princiapl):
    """
    Represents a user principal.
    """

    def __init__(self, uid: int):
        self._uid = uid

    @property
    def id(self) -> int:
        return self._uid

    def is_user(self) -> bool:
        return True

    def is_group(self) -> bool:
        return False


class Group(Princiapl):
    """
    Represents a group principal.
    """

    def __init__(self, gid: int):
        self._gid = gid

    @property
    def id(self) -> int:
        return self._gid

    def is_user(self) -> bool:
        return False

    def is_group(self) -> bool:
        return True
