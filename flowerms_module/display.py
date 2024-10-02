# flower_management/display.py

def display_flowers(flowers):
    """Display all flowers in a formatted table."""
    print('_' * 30)
    print('{:<15} {:<10} {:<20} {:<15}'.format('Flower Name', 'Quantity', 'Price', 'Status'))
    print('_' * 30)
    for flower in flowers:
        print('{:<15} {:<10} {:<20} {:<15}'.format(flower['flower_name'], flower['flower_qty'], flower['price'], flower['flower_sts']))
