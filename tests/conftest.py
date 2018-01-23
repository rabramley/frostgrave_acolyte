# -*- coding: utf-8 -*-
"""Acolyte test fixtures
"""


import pytest
from acolyte import create_app
from acolyte.database import db
from config import TestConfig, TestConfigCRSF


@pytest.yield_fixture(scope='function')
def app():
    """Pytest fixture to yield a fully initialised Acolyte
    
    Decorators:
        pytest
    
    Yields:
        obj -- Fully initialised Acolyte application
    """

    result = create_app(TestConfig)
    result.app_context().push()
    db.create_all()

    yield result


@pytest.yield_fixture(scope='function')
def client(app):
    """Pytest fixture to yield Flask test client for
    initialised Acolyte application
    
    Decorators:
        pytest
    
    Arguments:
        app {obj} -- Initialised Acolyte application
    
    Yields:
        obj -- Flask test client
    """

    result = app.test_client()

    yield result


@pytest.yield_fixture(scope='function')
def client_with_crsf():
    """Pytest fixture that yields Flask test client for
    Acolyte application initialised with CRSF testing
    
    Decorators:
        pytest
    
    Yields:
        obj -- Flask test client
    """

    crsf_app = create_app(TestConfigCRSF)
    crsf_app.app_context().push()
    result = crsf_app.test_client()

    yield result
