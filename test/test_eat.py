import pytest
from models.eat import (
    StandardCalories, Diet, NutritionDetail, DietDetail, Dish, RecipeDetail, StepsDetail
)

def test_standard_calories_initialization():
    sc = StandardCalories(stage=1, body=2, sex=0, low_carb=1800, moderate_carb=2000, high_carb=2200)
    assert sc.stage == 1
    assert sc.body == 2
    assert sc.sex == 0
    assert sc.low_carb == 1800
    assert sc.moderate_carb == 2000
    assert sc.high_carb == 2200

def test_nutrition_detail_percentages():
    nd = NutritionDetail(calories=500, carbs=50, fat=20, protein=30)
    total = nd.get_carbs_percentage() + nd.get_fat_percentage() + nd.get_protein_percentage()
    assert round(total, 5) == 1.0

def test_diet_detail_parsing():
    diet = Diet(
        calories="2000",
        nutrition="2000;250;70;150",
        breakfast="500:10x1;12x2",
        lunch="700:13x2;15x1",
        dinner="800:14x2;16x1"
    )

    # Nutrition
    nd = diet.get_nutrition_detail()
    assert isinstance(nd, NutritionDetail)
    assert nd.calories == 2000.0
    assert nd.carbs == 250.0

    # Breakfast
    bd = diet.get_breakfast_detail()
    assert isinstance(bd, DietDetail)
    assert bd.calories == "500"
    assert bd.id1 == "10"
    assert bd.amount1 == "1"
    assert bd.id2 == "12"
    assert bd.amount2 == "2"

    # Lunch
    ld = diet.get_lunch_detail()
    assert ld.id1 == "13"
    assert ld.amount1 == "2"

    # Dinner
    dd = diet.get_dinner_detail()
    assert dd.id2 == "16"

def test_dish_detail_parsing():
    dish = Dish(
        id=101,
        name="Grilled Chicken",
        image="image.jpg",
        nutrition="500;20;25;40",
        recipe="Chicken:200g;Oil:2tbsp;Salt:1tsp",
        steps="Marinate chicken;Grill until cooked"
    )

    # Nutrition
    nd = dish.get_nutrition_detail()
    assert isinstance(nd, NutritionDetail)
    assert nd.fat == 25.0

    # Recipe
    rd = dish.get_recipe_detail()
    assert isinstance(rd, RecipeDetail)
    assert rd.ingredients["Chicken"] == "200g"

    # Steps
    sd = dish.get_steps_detail()
    assert isinstance(sd, StepsDetail)
    assert sd.steps["Step 2:"] == "Grill until cooked"