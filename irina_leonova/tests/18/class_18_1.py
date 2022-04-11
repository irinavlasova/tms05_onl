from tests.conftest import my_methode

from irina_leonova import tests


class Test:
    def test_true(self):
        a = my_methode
        b = 3
        assert a >= b

    def test_not_true(self):
        a = my_methode
        b = 3
        assert a <= b


if __name__ == "__main__":
    tests.conftest.main()
