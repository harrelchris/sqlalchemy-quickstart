from app.database import Base


def test_base_attributes():
    assert Base.__tablename__ == 'base'
    assert hasattr(Base, 'metadata')
    assert hasattr(Base, 'session')
    assert hasattr(Base, 'id')
    assert hasattr(Base, 'created')
    assert hasattr(Base, 'modified')


def test_base_methods():
    assert hasattr(Base, 'all')
    assert hasattr(Base, 'delete')
    assert hasattr(Base, 'first')
    assert hasattr(Base, 'save')
    assert hasattr(Base, 'to_dict')
    assert hasattr(Base, 'update')


def test_instance_attributes(model):
    assert model.__tablename__ == 'thing'
    assert hasattr(model, 'metadata')
    assert hasattr(model, 'session')
    assert hasattr(model, 'id')
    assert hasattr(model, 'created')
    assert hasattr(model, 'modified')


def test_instance_methods(model):
    assert hasattr(model, 'all')
    assert hasattr(model, 'delete')
    assert hasattr(model, 'first')
    assert hasattr(model, 'save')
    assert hasattr(model, 'to_dict')
    assert hasattr(model, 'update')
