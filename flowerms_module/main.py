# main.py

from operation import add_flower, update_flower, remove_flower, search_flower, available_flowers
from display import display_flowers

def main():
    
    flowers = []
    while True:
        choice = int(input('''1. Add Flower
2. Update Flower
3. Remove Flower
4. View All Flowers
5. Search Flower
6. View Available Flowers
7. Exit
Enter your choice: '''))

        if choice == 1:
            add_flower(flowers)
        elif choice == 2:
            update_flower(flowers)
        elif choice == 3:
            remove_flower(flowers)
        elif choice == 4:
            display_flowers(flowers)
        elif choice == 5:
            flower = search_flower(flowers)
            if flower:
                display_flowers([flower])
        elif choice == 6:
            available = available_flowers(flowers)
            if available:
                display_flowers(available)
            else:
                print("No available flower")
        elif choice == 7:
            print("Exit")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
