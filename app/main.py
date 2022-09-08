import time

from app.models import Item

# Create
item = Item(
    boolean=True,
    floating=3.14,
    integer=42,
    string='item name',
)
item.save()

print(item.id)
print(item.created)
print(item.modified)
print(item.integer)

# Read
stored_item = Item.query.get(item.id)

# Update
time.sleep(2)
stored_item.integer = 69
stored_item.save()

print(stored_item.id)
print(stored_item.created)
print(stored_item.modified)
print(stored_item.integer)

# Delete
stored_item.delete()
