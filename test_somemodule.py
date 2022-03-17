from unittest import mock


def _test_db(func):
    def inner():
        print("Use Test DB")
        # ここにテストDBの接続コードなどがある
        return func()

    return inner


mock.patch("db.use_db", _test_db).start()
from somemodule import gopher  # noqa


def test_gopher():
    assert gopher() == 0
