import doctest

import marshmallow_dataclass2


def load_tests(_loader, tests, _ignore):
    # Load all the doctests defined in the module
    tests.addTests(doctest.DocTestSuite(marshmallow_dataclass2))
    return tests
