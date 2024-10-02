# flower_management/flower_operations.py

def get_flower_details():
    """Get flower details from the user."""
    name = input("Name of Flower: ")
    qty = input("Quantity of Flower: ")
    price = input("Price of Flower: ")
    payment = input("Modes of Payment: ")
    status = input("Available or Unavailable: ")
    return {'flower_name': name, 'flower_qty': qty, 'price': price, 'pay': payment, 'flower_sts': status}

def add_flower(flowers):
    """Add a new flower to the list."""
    flower = get_flower_details()
    flowers.append(flower)
    print(f"Added: {flower['flower_name']}")

def update_flower(flowers):
    """Update details of an existing flower."""
    name = input("Name of Flower to Update: ")
    for flower in flowers:
        if flower['flower_name'].lower() == name.lower():
            flower['flower_qty'] = input("New Quantity: ")
            flower['price'] = input("New Price: ")
            flower['pay'] = input("Updated Modes of Payment: ")
            flower['flower_sts'] = input("Updated Status: ")
            print(f"Updated: {flower['flower_name']}")
            return
    print("Flower not found.")

def remove_flower(flowers):
    """Remove a flower from the list."""
    name = input("Enter Flower Name to Remove: ")
    initial_count = len(flowers)
    flowers[:] = [flower for flower in flowers if flower['flower_name'].lower() != name.lower()]
    if len(flowers) < initial_count:
        print(f"Removed: {name}")
    else:
        print("Flower not found.")

def search_flower(flowers):
    """Search for a flower by name."""
    name = input("Enter Flower Name to Search: ")
    for flower in flowers:
        if flower['flower_name'].lower() == name.lower():
            return flower
    print("Flower not found.")
    return None

def available_flowers(flowers):
    """Return a list of available flowers."""
    return [flower for flower in flowers if flower['flower_sts'].lower() == 'available']
