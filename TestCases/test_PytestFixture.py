import pytest

#D:\Coding\PageObjectSelenium\TestCases>pytest -v -s --html=..\Report\report.html

@pytest.yield_fixture()
def setup():
    print("Once before every method")
    yield
    print("Once After every method")

def testMethod1(setup):
    print("test method1")


def testMethod2(setup):
    print("test method2")