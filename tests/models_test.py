from app.models import Item


def test_item_attributes():
    assert Item.__tablename__ == 'item'
    assert hasattr(Item, 'boolean')
    assert hasattr(Item, 'floating')
    assert hasattr(Item, 'integer')
    assert hasattr(Item, 'string')
