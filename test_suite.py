import sys

from .conftest import pytest_report_header


def _run_tests(test_suite, package_name):
    """Core function to test a test suite  using UnitTest

    :param test_suite: Unittest test suite
    """
    count = test_suite.countTestCases()
    print('########')
    print(pytest_report_header(None))
    print('{} tests has been discovered in {}'.format(count, package_name))
    print('########')
    import unittest
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(test_suite)


def test_package(package='QuickOSM', engine='unittest'):
    """Test package.
    This function is called by travis without arguments.

    :param package: The package to test.
    :type package: str

    :param engine: Either 'pytest' or 'unittest'.
    :type engine: basestring
    """
    if engine == 'pytest':
        import pytest
        pytest.main(['.'])
    else:
        import unittest
        test_loader = unittest.defaultTestLoader
        test_suite = test_loader.discover(package)
        _run_tests(test_suite, package)


if __name__ == '__main__':
    test_package()
