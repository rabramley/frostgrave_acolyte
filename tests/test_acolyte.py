# -*- coding: utf-8 -*-
"""
    Acolyte Tests
"""

import os
import pytest
from bs4 import BeautifulSoup
import acolyte.importer
import acolyte.database
from acolyte.models import School, Spell


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


def test_import_spells(app):
    acolyte.importer.import_spells(app, os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'test_spells.yaml'
    ))

    assert School.query.count() == 2
    assert Spell.query.count() == 3

    chrono = School.query.filter(School.name == 'Chronomancer').first()
    assert chrono
    assert len(chrono.spells) == 2

    elem = School.query.filter(School.name == 'Elementalist').first()
    assert elem
    assert len(elem.spells) == 1

    crumble = Spell.query.filter(Spell.name == 'Crumble').first()
    assert crumble
    assert crumble.required == 10
    assert crumble.target == 'Line of Sight'
    assert crumble.description == 'This spell only works against ' \
        'man-made objects'
    assert crumble.school == chrono

    decay = Spell.query.filter(Spell.name == 'Decay').first()
    assert decay
    assert decay.required == 12
    assert decay.target == 'Line of Sight'
    assert decay.description == 'The spellcaster selects and attacks a ' \
        'target\'s weapon, causing it to decay.'
    assert decay.school == chrono

    call_storm = Spell.query.filter(Spell.name == 'Call Storm').first()
    assert call_storm
    assert call_storm.required == 12
    assert call_storm.target == 'Area Effect'
    assert call_storm.description == 'If this spell is successfully ' \
        'crossbow attacks are -1 for the rest of the ' \
        'game.'
    assert call_storm.school == elem
