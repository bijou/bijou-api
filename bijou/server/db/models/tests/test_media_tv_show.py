import pytest

from ... import init_db, Session
from .. import MediaTVShow

@pytest.fixture(scope='module')
def session():
    init_db('sqlite://')
    yield Session()

def test_create(session):
    show = MediaTVShow(name='TestShow', path='/path/to/show')
    assert show.id == None
    assert show.name == 'TestShow'
    assert show.path == '/path/to/show'
    session.add(show)
    db_show = session.query(MediaTVShow).filter_by(name='TestShow').first()
    assert db_show.id == 1
    assert db_show.name == show.name
    assert db_show.path == show.path

def test_update(session):
    pass

def test_delete(session):
    pass
