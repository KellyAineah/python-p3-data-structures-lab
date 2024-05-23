spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [foods["name"] for foods in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5] 

def print_spicy_foods(spicy_foods):
     for foods in spicy_foods:
        name=foods["name"]
        cuisine = foods["cuisine"]
        heat_level =foods["heat_level"] * "🌶"
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
    
        

def get_spicy_food_by_cuisine(spicy_foods, cuisine):

    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for foods in spicy_foods:
        if foods["heat_level"] > 5:
            name=foods["name"]
            cuisine = foods["cuisine"]
            heat_level =foods["heat_level"] * "🌶"
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    sum = 0
    average = 0
    for foods in spicy_foods:
        sum = sum + foods["heat_level"]
        average = sum / len(spicy_foods)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
