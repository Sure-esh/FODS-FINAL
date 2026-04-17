'''
Program to create Dish and Cookbook classes
Dish: dish_id, dish_name, ingredients, instructions
Cookbook: manage collection of dishes
'''

# Define Dish class
class Dish:
    def __init__(self, dish_id, dish_name, ingredients, instructions):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.ingredients = ingredients  # List of ingredients
        self.instructions = instructions
    
    # Method to display dish details
    def display(self):
        print(f"\nDish ID: {self.dish_id}")
        print(f"Dish Name: {self.dish_name}")
        print(f"Ingredients: {', '.join(self.ingredients)}")
        print(f"Instructions: {self.instructions}")

# Define Cookbook class
class Cookbook:
    def __init__(self):
        self.dishes = {}  # Dictionary to store dishes
    
    # Method to add dish
    def add_dish(self, dish):
        self.dishes[dish.dish_id] = dish
    
    # Method to remove dish
    def remove_dish(self, dish_id):
        if dish_id in self.dishes:
            name = self.dishes[dish_id].dish_name
            del self.dishes[dish_id]
            print(f"✓ Dish '{name}' removed successfully!")
        else:
            print(f"Error: Dish with ID {dish_id} not found!")
    
    # Method to search dish
    def search_dish(self, dish_id):
        if dish_id in self.dishes:
            return self.dishes[dish_id]
        return None
    
    # Method to display all dishes
    def display_all(self):
        if not self.dishes:
            print("Cookbook is empty!")
            return
        
        print("\n" + "="*50)
        print("COOKBOOK - ALL DISHES")
        print("="*50)
        
        for dish_id, dish in self.dishes.items():
            dish.display()
            print("-"*50)

# Main program
if __name__ == "__main__":
    # Create cookbook
    cookbook = Cookbook()
    
    # Add dishes
    dish1 = Dish(1, "Pasta", ["pasta", "tomato sauce", "cheese"], "Boil pasta, add sauce, serve with cheese")
    dish2 = Dish(2, "Pizza", ["flour", "cheese", "tomato"], "Knead dough, add toppings, bake at 200C")
    dish3 = Dish(3, "Salad", ["lettuce", "tomato", "cucumber", "dressing"], "Chop vegetables, mix, add dressing")
    
    cookbook.add_dish(dish1)
    cookbook.add_dish(dish2)
    cookbook.add_dish(dish3)
    
    # Search for a dish
    print("\n" + "="*50)
    print("SEARCH DISH")
    print("="*50)
    search_id = int(input("Enter dish ID to search: "))
    found_dish = cookbook.search_dish(search_id)
    
    if found_dish:
        print("\nDish found:")
        found_dish.display()
    else:
        print(f"Error: Dish with ID {search_id} not found!")
