# -*- coding: utf-8 -*-
"""
    Acolyte Tests
"""

import pytest
import acolyte
from bs4 import BeautifulSoup
from config import TestConfig, TestConfigCRSF


@pytest.yield_fixture(scope='function')
def client(request):
    app = acolyte.create_app(TestConfig)
    app.app_context().push()
    client = app.test_client()

    yield client


@pytest.yield_fixture(scope='function')
def client_with_crsf(request):
    app = acolyte.create_app(TestConfigCRSF)
    app.app_context().push()
    client = app.test_client()

    yield client


def test_missing_route(client):
    resp = client.get('/uihfihihf')
    assert resp.status_code == 404


@pytest.mark.parametrize("path", [
    ('/'),
    ('/static/css/main.css')
])
def test_url_exists(client, path):
    resp = client.get(path)

    assert resp.status_code == 200


@pytest.mark.parametrize("path", [
    ('/')
])
def test_html_boilerplate(client, path):
    resp = client.get(path)
    rsoup = BeautifulSoup(resp.data, 'html.parser')

    assert rsoup.find('html') is not None
    assert rsoup.find('html')['lang'] == "en"
    assert rsoup.find('head') is not None
    assert rsoup.find(
        lambda tag: tag.name == "meta" and
        tag.has_attr('charset') and
        tag['charset'] == "utf-8"
    ) is not None
    assert rsoup.title is not None
    assert rsoup.find('body') is not None
    assert rsoup.find('title') is not None
