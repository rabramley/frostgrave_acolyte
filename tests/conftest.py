# -*- coding: utf-8 -*-
"""
    Acolyte Tests
"""

import pytest
from acolyte import create_app
from acolyte.database import db
from config import TestConfig, TestConfigCRSF


@pytest.yield_fixture(scope='function')
def app(request):
    app = create_app(TestConfig)
    app.app_context().push()
    db.create_all()

    yield app


@pytest.yield_fixture(scope='function')
def client(app):
    result = app.test_client()

    yield result


@pytest.yield_fixture(scope='function')
def client_with_crsf(app):
    app = create_app(TestConfigCRSF)
    app.app_context().push()
    result = app.test_client()

    yield result

