from dataclasses import dataclass

import pytest

from src.common import isEqual


@dataclass
class User:
    username: str = "someUser"
    email: str = "some@example.com"


@pytest.fixture(scope="function")
def users() -> tuple[User, User]:
    return User(), User()


class TestIsEqual:
    def test_same_obj(self) -> None:
        u1 = User()
        u2 = u1
        assert isEqual(u1, u2) == True

    def test_type(self, users) -> None:
        u1, u2 = users
        assert isEqual(u1, u2) == True
