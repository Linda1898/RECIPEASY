from application import db
from random import randint
from application.models.food_group import FoodGroup
from application.models.food_source import FoodSource
from application.models.nutrition import Nutrition
from application.models.gender import Gender
from application.models.user_table import UserTable
from application.models.recipe import Recipe
from application.models.food_item import FoodItem
from application.models.ingredient import Ingredient
from application.models.liked import Liked
from application.models.collection import Collection
from application.models.recipe_collection import RecipeCollection

def get_collection_object(id):
    collection = db.session.query(Collection).filter_by(collection_id=id).all()
    return collection


def get_collection_object_all():
    collection = db.session.query(Collection)
    return collection


def get_food_group_object(id):
    food_group = db.session.query(FoodGroup).filter_by(food_group_id=id).first()
    return food_group

def get_food_group_object_by_groupname(user_search):
    user_search = user_search.capitalize()
    food_group = db.session.query(FoodGroup).filter_by(group_name=user_search).first()
    return food_group


def get_foods_from_group(user_search):
    food = get_food_group_object_by_groupname(user_search)
    group_id = food.food_group_id
    foods = db.session.query(FoodItem).filter_by(food_group_id=group_id).all()
    return foods

def get_recipes_from_group(user_search):
    ingredients = get_foods_from_group(user_search)
    id = ingredients.food_id
    recipes = db.session.query(Ingredient).filter_by(food_id=id)
    return recipes


def get_food_item_object(id):
    food_item = db.session.query(FoodItem).filter_by(food_id=id).first()
    return food_item

print("aaaa", (get_food_group_object_by_groupname('Dairy')))

def get_food_source_object(id):
    food_source = db.session.query(FoodSource).filter_by(source_id=id).first()
    return food_source


def get_gender_object(id):
    gender = db.session.query(Gender).filter_by(gender_id=id).first()
    return gender


def get_ingredient_object(id):
    ingredient = db.session.query(Ingredient).filter_by(ingredient_id=id).first()
    return ingredient



def get_liked_object(id):
    liked = db.session.query(Liked).filter_by(liked=id).first()
    return liked


def get_nutrition_object(id):
    nutrition = db.session.query(Nutrition).filter_by(nutrition_id=id).first()
    return nutrition


def get_recipe_object(id):
    recipe = db.session.query(Recipe).filter_by(recipe_id=id).all()
    return recipe
print(get_recipe_object(6))
def get_collection_id(id):
    recipe = db.session.query(Recipe).filter_by(collection_id=id).first
    return recipe

def get_recipe_object_all():
    recipe = db.session.query(Recipe)
    return recipe

print(get_collection_object_all())

def get_recipe_collection_object(id):
    recipe_collection = db.session.query(RecipeCollection).filter_by(recipe_collection_id=id).all()
    return recipe_collection

def get_recipes_from_collection(id):
    recipes = db.session.query(Recipe).filter_by(collection_id=id).all()
    return recipes


def get_user_table_object(id):
    user_table = db.session.query(UserTable).filter_by(user_id=id).first()
    return user_table

def add_new_user(user):
    db.session.add(user)
    db.session.commit()

def get_recipe_dict(id):
    if id > 0:
        return Recipe.query.get(id)
    else:
        return None

def get_foods_by_foodssource(user_search):
    user_search = user_search.lower()
    foods = db.session.query(FoodSource).filter_by(source_name=user_search).first()
    id = foods.source_id
    foods = db.session.query(FoodItem).filter_by(source_id=id).all()
    return foods

# food = get_food_item_object(1)
# print(food)
# food = food.__dict__
# print(food)
def search_food_facts(user_search):
    source_name = user_search.lower()
    food = db.session.query(FoodSource).filter_by(source_name=source_name).first()
    return food


def get_nutrition_by_name(food_name):
    food_name = food_name.lower()
    food = db.session.query(FoodItem).filter_by(food_name=food_name).first()
    food_id = food.food_id
    nutritionList = db.session.query(Nutrition).filter_by(nutrition_id=food_id).first()
    return nutritionList

def get_environmental_impact(food_name):
    food_name = food_name.lower()
    environment = db.session.query(FoodItem).filter_by(food_name=food_name).first()
    return environment

def get_recipe_matching_collection_id(coll_id):
    recipe_collection = db.session.query(RecipeCollection).filter_by(collection_id=coll_id).first()
    if recipe_collection == None:
        print('nothing found')
    else:
        matching_recipe = recipe_collection.recipe_id
        final_recipes = db.session.query(Recipe).filter_by(recipe_id=matching_recipe).first()
        if final_recipes == None:
            print('No')
        else:
            return final_recipes


# NOT SURE ABOUT FILES BELOW THIS POINT:

def search_recipe():
    search_results = []
    recipe_table = db.session.query(Recipe).all()
    user_search = input('search here for recipes: ')
    print(f"Here are the results that match your search: {user_search}")
    for row in recipe_table:
        if user_search in row.recipe_name or user_search in row.recipe_description:
            search_results.append(row.recipe_id)
            print(row.recipe_name)
            print(row.recipe_method)
            print(row.recipe_description)

def get_nutrition_list(food_id):
    total_nutrition = db.session.query(Nutrition).filter_by(nutrition_id=food_id).first()
    nutrition_list = [total_nutrition.energy_kcal, total_nutrition.energy_kj, total_nutrition.fat,
                      total_nutrition.saturate, total_nutrition.carbohydrate, total_nutrition.sugar,
                      total_nutrition.starch, total_nutrition.fibre, total_nutrition.protein, total_nutrition.salt]
    return nutrition_list

def get_recipe_nutrition_total():
     nutrition_list_asparagus = get_nutrition_list(1)
     nutrition_list_beefmince = get_nutrition_list(2)
     nutrition_total_list = []
     for i in range(0, 10):
         nutrition_total_list.append(float(nutrition_list_asparagus[i]) + float(nutrition_list_beefmince[i]))
     print(nutrition_total_list)


def get_recipe1_nutrition_total():
    nutrition_list_1 = get_nutrition_list(43)
    nutrition_list_2 = get_nutrition_list(2)
    nutrition_list_3 = get_nutrition_list(30)
    nutrition_list_4 = get_nutrition_list(27)
    nutrition_list_5 = get_nutrition_list(6)
    nutrition_list_6 = get_nutrition_list(72)
    nutrition_list_7 = get_nutrition_list(3)
    nutrition_list_8 = get_nutrition_list(61)
    nutrition_list_9 = get_nutrition_list(77)
    nutrition_list_10 = get_nutrition_list(24)
    nutrition_total_list = []
    for i in range(0, 10):
        nutrition_total_list.append(float(nutrition_list_1[i]) + float(nutrition_list_2[i]) + float(nutrition_list_3[i]) + float(nutrition_list_4[i]) + float(nutrition_list_5[i]) + float(nutrition_list_6[i])+ float(nutrition_list_7[i])+ float(nutrition_list_8[i])+ float(nutrition_list_9[i])+float(nutrition_list_10[i])),
    print(nutrition_total_list)
    return nutrition_total_list


def get_recipe2_nutrition_total():
    nutrition_list_1 = get_nutrition_list(69)
    nutrition_list_2 = get_nutrition_list(63)
    nutrition_list_3 = get_nutrition_list(14)
    nutrition_list_4 = get_nutrition_list(16)
    nutrition_list_5 = get_nutrition_list(39)
    nutrition_list_6 = get_nutrition_list(24)
    nutrition_list_7 = get_nutrition_list(7)
    nutrition_list_8 = get_nutrition_list(28)
    nutrition_list_9 = get_nutrition_list(1)
    nutrition_list_10 = get_nutrition_list(4)
    nutrition_list_11 = get_nutrition_list(77)
    nutrition_total_list = []
    for i in range(0, 10):
        nutrition_total_list.append(float(nutrition_list_1[i]) + float(nutrition_list_2[i]) + float(nutrition_list_3[i]) + float(nutrition_list_4[i]) + float(nutrition_list_5[i]) + float(nutrition_list_6[i])+ float(nutrition_list_7[i])+ float(nutrition_list_8[i])+ float(nutrition_list_9[i])+float(nutrition_list_10[i]) + float(nutrition_list_11[i])),
    print(nutrition_total_list)
    return nutrition_total_list

print(get_recipe2_nutrition_total())
def get_recipe3_nutrition_total():
    nutrition_list_1 = get_nutrition_list(43)
    nutrition_list_2 = get_nutrition_list(30)
    nutrition_list_3 = get_nutrition_list(2)
    nutrition_list_4 = get_nutrition_list(65)
    nutrition_list_5 = get_nutrition_list(47)
    nutrition_list_6 = get_nutrition_list(53)
    nutrition_list_7 = get_nutrition_list(26)
    nutrition_list_8 = get_nutrition_list(3)
    nutrition_list_9 = get_nutrition_list(71)
    nutrition_list_10 = get_nutrition_list(77)
    nutrition_list_11 = get_nutrition_list(4)
    nutrition_list_12 = get_nutrition_list(48)
    nutrition_list_13 = get_nutrition_list(57)
    nutrition_list_14 = get_nutrition_list(28)
    nutrition_list_15 = get_nutrition_list(46)
    nutrition_total_list = []
    for i in range(0, 10):
        nutrition_total_list.append(float(nutrition_list_1[i]) + float(nutrition_list_2[i]) + float(nutrition_list_3[i]) + float(nutrition_list_4[i]) + float(nutrition_list_5[i]) + float(nutrition_list_6[i])+ float(nutrition_list_7[i])+ float(nutrition_list_8[i])+ float(nutrition_list_9[i])+float(nutrition_list_10[i]) + float(nutrition_list_11[i]) + float(nutrition_list_12[i]) + float(nutrition_list_13[i]) + float(nutrition_list_14[i]) + float(nutrition_list_15[i])),
    print(nutrition_total_list)
    return nutrition_total_list


def get_recipe4_nutrition_total():
    nutrition_list_1 = get_nutrition_list(52)
    nutrition_list_2 = get_nutrition_list(41)
    nutrition_list_3 = get_nutrition_list(62)
    nutrition_list_4 = get_nutrition_list(35)
    nutrition_list_5 = get_nutrition_list(23)
    nutrition_list_6 = get_nutrition_list(4)
    nutrition_list_7 = get_nutrition_list(25)
    nutrition_list_8 = get_nutrition_list(66)
    nutrition_total_list = []
    for i in range(0, 10):
        nutrition_total_list.append(float(nutrition_list_1[i]) + float(nutrition_list_2[i]) + float(nutrition_list_3[i]) + float(nutrition_list_4[i]) + float(nutrition_list_5[i]) + float(nutrition_list_6[i])+ float(nutrition_list_7[i])+ float(nutrition_list_8[i])),
    print(nutrition_total_list)
    return nutrition_total_list


def get_recipe5_nutrition_total():
    nutrition_list_1 = get_nutrition_list(55)
    nutrition_list_2 = get_nutrition_list(7)
    nutrition_list_3 = get_nutrition_list(34)
    nutrition_list_4 = get_nutrition_list(67)
    nutrition_list_5 = get_nutrition_list(21)
    nutrition_list_6 = get_nutrition_list(47)
    nutrition_list_7 = get_nutrition_list(22)
    nutrition_total_list = []
    for i in range(0, 10):
        nutrition_total_list.append(float(nutrition_list_1[i]) + float(nutrition_list_2[i]) + float(nutrition_list_3[i]) + float(nutrition_list_4[i]) + float(nutrition_list_5[i]) + float(nutrition_list_6[i])+ float(nutrition_list_7[i])),
    print(nutrition_total_list)
    return nutrition_total_list

def get_recipe6_nutrition_total():
    nutrition_list_1 = get_nutrition_list(66)
    nutrition_list_2 = get_nutrition_list(64)
    nutrition_list_3 = get_nutrition_list(17)
    nutrition_list_4 = get_nutrition_list(49)
    nutrition_list_5 = get_nutrition_list(52)
    nutrition_list_6 = get_nutrition_list(51)
    nutrition_list_7 = get_nutrition_list(35)
    nutrition_list_8 = get_nutrition_list(33)
    nutrition_list_9 = get_nutrition_list(32)
    nutrition_list_10 = get_nutrition_list(19)
    nutrition_list_11 = get_nutrition_list(72)
    nutrition_list_12 = get_nutrition_list(4)
    nutrition_list_13 = get_nutrition_list(77)
    nutrition_list_14 = get_nutrition_list(78)
    nutrition_list_15 = get_nutrition_list(9)
    nutrition_list_16 = get_nutrition_list(39)
    nutrition_total_list = []
    for i in range(0, 10):
        nutrition_total_list.append(float(nutrition_list_1[i]) + float(nutrition_list_2[i]) + float(nutrition_list_3[i]) + float(
        nutrition_list_4[i]) + float(nutrition_list_5[i]) + float(nutrition_list_6[i]) + float(
        nutrition_list_7[i]) + float(nutrition_list_8[i]) + float(nutrition_list_9[i]) + float(
        nutrition_list_10[i]) + float(nutrition_list_11[i]) + float(nutrition_list_12[i]) + float(
        nutrition_list_13[i]) + float(nutrition_list_14[i]) + float(nutrition_list_15[i]) + float(
        nutrition_list_16[i])),
    print(nutrition_total_list)
    return nutrition_total_list

def get_recipe7_nutrition_total():
    nutrition_list_1 = get_nutrition_list(43)
    nutrition_list_2 = get_nutrition_list(58)
    nutrition_list_3 = get_nutrition_list(51)
    nutrition_list_4 = get_nutrition_list(72)
    nutrition_list_5 = get_nutrition_list(38)
    nutrition_list_6 = get_nutrition_list(59)
    nutrition_list_7 = get_nutrition_list(53)
    nutrition_total_list = []
    for i in range(0, 10):
        nutrition_total_list.append(float(nutrition_list_1[i]) + float(nutrition_list_2[i]) + float(nutrition_list_3[i]) + float(
        nutrition_list_4[i]) + float(nutrition_list_5[i]) + float(nutrition_list_6[i]) + float(
        nutrition_list_7[i])),
    print(nutrition_total_list)
    return nutrition_total_list


def get_recipe8_nutrition_total():
    nutrition_list_1 = get_nutrition_list(43)
    nutrition_list_2 = get_nutrition_list(14)
    nutrition_list_3 = get_nutrition_list(15)
    nutrition_list_4 = get_nutrition_list(30)
    nutrition_list_5 = get_nutrition_list(27)
    nutrition_list_6 = get_nutrition_list(52)
    nutrition_list_7 = get_nutrition_list(50)
    nutrition_list_8 = get_nutrition_list(35)
    nutrition_list_9 = get_nutrition_list(59)
    nutrition_list_10 = get_nutrition_list(76)
    nutrition_list_11 = get_nutrition_list(42)
    nutrition_list_12 = get_nutrition_list(25)
    nutrition_total_list = []
    for i in range(0, 10):
        nutrition_total_list.append(float(nutrition_list_1[i]) + float(nutrition_list_2[i]) + float(nutrition_list_3[i]) + float(
        nutrition_list_4[i]) + float(nutrition_list_5[i]) + float(nutrition_list_6[i]) + float(
        nutrition_list_7[i]) + float(nutrition_list_8[i]) + float(nutrition_list_9[i]) + float(
        nutrition_list_10[i]) + float(nutrition_list_11[i]) + float(nutrition_list_12[i])),
    print(nutrition_total_list)
    return nutrition_total_list


def get_recipe9_nutrition_total():
    nutrition_list_1 = get_nutrition_list(67)
    nutrition_list_2 = get_nutrition_list(68)
    nutrition_list_3 = get_nutrition_list(23)
    nutrition_list_4 = get_nutrition_list(20)
    nutrition_list_5 = get_nutrition_list(66)
    nutrition_list_6 = get_nutrition_list(51)
    nutrition_list_7 = get_nutrition_list(10)
    nutrition_list_8 = get_nutrition_list(9)
    nutrition_list_9 = get_nutrition_list(8)
    nutrition_list_10 = get_nutrition_list(11)
    nutrition_list_11 = get_nutrition_list(29)
    nutrition_list_12 = get_nutrition_list(37)
    nutrition_list_13 = get_nutrition_list(39)
    nutrition_list_14 = get_nutrition_list(77)
    nutrition_list_15 = get_nutrition_list(4)
    nutrition_list_16 = get_nutrition_list(40)
    nutrition_list_17 = get_nutrition_list(60)
    nutrition_list_18 = get_nutrition_list(36)
    nutrition_list_19 = get_nutrition_list(54)
    nutrition_total_list = []
    for i in range(0, 10):
        nutrition_total_list.append(float(nutrition_list_1[i]) + float(nutrition_list_2[i]) + float(nutrition_list_3[i]) + float(
        nutrition_list_4[i]) + float(nutrition_list_5[i]) + float(nutrition_list_6[i]) + float(
        nutrition_list_7[i]) + float(nutrition_list_8[i]) + float(nutrition_list_9[i]) + float(
        nutrition_list_10[i]) + float(nutrition_list_11[i]) + float(nutrition_list_12[i]) + float(
        nutrition_list_13[i]) + float(nutrition_list_14[i]) + float(nutrition_list_15[i]) + float(
        nutrition_list_16[i]) + float(nutrition_list_17[i]) + float(nutrition_list_18[i]) + float(
        nutrition_list_19[i])),
    print(nutrition_total_list)
    return nutrition_total_list


def get_recipe10_nutrition_total():
    nutrition_list_1 = get_nutrition_list(70)
    nutrition_list_2 = get_nutrition_list(44)
    nutrition_list_3 = get_nutrition_list(5)
    nutrition_list_4 = get_nutrition_list(45)
    nutrition_list_5 = get_nutrition_list(43)
    nutrition_list_6 = get_nutrition_list(25)
    nutrition_list_7 = get_nutrition_list(6)
    nutrition_list_8 = get_nutrition_list(18)
    nutrition_list_9 = get_nutrition_list(72)
    nutrition_total_list = []
    for i in range(0, 10):
        nutrition_total_list.append(float(nutrition_list_1[i]) + float(nutrition_list_2[i]) + float(nutrition_list_3[i]) + float(
        nutrition_list_4[i]) + float(nutrition_list_5[i]) + float(nutrition_list_6[i]) + float(
        nutrition_list_7[i]) + float(nutrition_list_8[i]) + float(nutrition_list_9[i])),
    print(nutrition_total_list)
    return nutrition_total_list



# print(get_recipe1_nutrition_total())
# print(get_recipe2_nutrition_total())
# print(get_recipe3_nutrition_total())
# print(get_recipe4_nutrition_total())
# print(get_recipe5_nutrition_total())
# print(get_recipe6_nutrition_total())
# print(get_recipe7_nutrition_total())
# print(get_recipe8_nutrition_total())
# print(get_recipe9_nutrition_total())
# print(get_recipe10_nutrition_total())

def get_carbonfootprint_list(food_id):

    total_cfp = db.session.query(FoodItem).filter_by(food_id=food_id).first()
    cfp_list = [total_cfp.ghg_emission, total_cfp.land_use, total_cfp.freshwater_withdraw]
    return cfp_list

def get_carbonfootprint_recipe1():
    cfp_list_1 = get_carbonfootprint_list(43)
    cfp_list_2 = get_carbonfootprint_list(2)
    cfp_list_3 = get_carbonfootprint_list(30)
    cfp_list_4 = get_carbonfootprint_list(27)
    cfp_list_5 = get_carbonfootprint_list(6)
    cfp_list_6 = get_carbonfootprint_list(72)
    cfp_list_7 = get_carbonfootprint_list(3)
    cfp_list_8 = get_carbonfootprint_list(61)
    cfp_list_9 = get_carbonfootprint_list(77)
    cfp_list_10 = get_carbonfootprint_list(24)
    cfp_total_list = []
    for i in range(0, 3):
        cfp_total_list.append(float(cfp_list_1[i]) + float(cfp_list_2[i]) + float(cfp_list_3[i]) + float(
        cfp_list_4[i]) + float(cfp_list_5[i]) + float(cfp_list_6[i]) + float(
        cfp_list_7[i]) + float(cfp_list_8[i]) + float(cfp_list_9[i]) + float(cfp_list_10[i])),
    print(cfp_total_list)
    return cfp_total_list


def get_carbonfootprint_recipe2():
    cfp_list_1 = get_carbonfootprint_list(69)
    cfp_list_2 = get_carbonfootprint_list(63)
    cfp_list_3 = get_carbonfootprint_list(14)
    cfp_list_4 = get_carbonfootprint_list(16)
    cfp_list_5 = get_carbonfootprint_list(39)
    cfp_list_6 = get_carbonfootprint_list(24)
    cfp_list_7 = get_carbonfootprint_list(7)
    cfp_list_8 = get_carbonfootprint_list(28)
    cfp_list_9 = get_carbonfootprint_list(1)
    cfp_list_10 = get_carbonfootprint_list(4)
    cfp_list_11 = get_carbonfootprint_list(77)
    cfp_total_list = []
    for i in range(0, 3):
        cfp_total_list.append(float(cfp_list_1[i]) + float(cfp_list_2[i]) + float(cfp_list_3[i]) + float(
        cfp_list_4[i]) + float(cfp_list_5[i]) + float(cfp_list_6[i]) + float(
        cfp_list_7[i]) + float(cfp_list_8[i]) + float(cfp_list_9[i]) + float(cfp_list_10[i]) + float(cfp_list_11[i])),
    print(cfp_total_list)
    return cfp_total_list


def get_carbonfootprint_recipe3():
    cfp_list_1 = get_carbonfootprint_list(43)
    cfp_list_2 = get_carbonfootprint_list(30)
    cfp_list_3 = get_carbonfootprint_list(2)
    cfp_list_4 = get_carbonfootprint_list(65)
    cfp_list_5 = get_carbonfootprint_list(47)
    cfp_list_6 = get_carbonfootprint_list(53)
    cfp_list_7 = get_carbonfootprint_list(26)
    cfp_list_8 = get_carbonfootprint_list(3)
    cfp_list_9 = get_carbonfootprint_list(71)
    cfp_list_10 = get_carbonfootprint_list(77)
    cfp_list_11 = get_carbonfootprint_list(4)
    cfp_list_12 = get_carbonfootprint_list(48)
    cfp_list_13 = get_carbonfootprint_list(57)
    cfp_list_14 = get_carbonfootprint_list(28)
    cfp_list_15 = get_carbonfootprint_list(46)
    cfp_total_list = []
    for i in range(0, 3):
        cfp_total_list.append(float(cfp_list_1[i]) + float(cfp_list_2[i]) + float(cfp_list_3[i]) + float(
        cfp_list_4[i]) + float(cfp_list_5[i]) + float(cfp_list_6[i]) + float(
        cfp_list_7[i]) + float(cfp_list_8[i]) + float(cfp_list_9[i]) + float(cfp_list_10[i]) + float(cfp_list_11[i]) + float(cfp_list_12[i]) + float(cfp_list_13[i]) + float(cfp_list_14[i]) + float(cfp_list_15[i])),
    print(cfp_total_list)
    return cfp_total_list

def get_carbonfootprint_recipe4():
    cfp_list_1 = get_carbonfootprint_list(52)
    cfp_list_2 = get_carbonfootprint_list(41)
    cfp_list_3 = get_carbonfootprint_list(62)
    cfp_list_4 = get_carbonfootprint_list(35)
    cfp_list_5 = get_carbonfootprint_list(23)
    cfp_list_6 = get_carbonfootprint_list(4)
    cfp_list_7 = get_carbonfootprint_list(25)
    cfp_list_8 = get_carbonfootprint_list(66)
    cfp_total_list = []
    for i in range(0, 3):
        cfp_total_list.append(float(cfp_list_1[i]) + float(cfp_list_2[i]) + float(cfp_list_3[i]) + float(
        cfp_list_4[i]) + float(cfp_list_5[i]) + float(cfp_list_6[i]) + float(
        cfp_list_7[i]) + float(cfp_list_8[i])),
    print(cfp_total_list)
    return cfp_total_list

def get_carbonfootprint_recipe5():
    cfp_list_1 = get_carbonfootprint_list(55)
    cfp_list_2 = get_carbonfootprint_list(7)
    cfp_list_3 = get_carbonfootprint_list(34)
    cfp_list_4 = get_carbonfootprint_list(67)
    cfp_list_5 = get_carbonfootprint_list(21)
    cfp_list_6 = get_carbonfootprint_list(47)
    cfp_list_7 = get_carbonfootprint_list(22)
    cfp_total_list = []
    for i in range(0, 3):
        cfp_total_list.append(float(cfp_list_1[i]) + float(cfp_list_2[i]) + float(cfp_list_3[i]) + float(
        cfp_list_4[i]) + float(cfp_list_5[i]) + float(cfp_list_6[i]) + float(
        cfp_list_7[i])),
    print(cfp_total_list)
    return cfp_total_list

def get_carbonfootprint_recipe6():
    cfp_list_1 = get_carbonfootprint_list(66)
    cfp_list_2 = get_carbonfootprint_list(64)
    cfp_list_3 = get_carbonfootprint_list(17)
    cfp_list_4 = get_carbonfootprint_list(49)
    cfp_list_5 = get_carbonfootprint_list(52)
    cfp_list_6 = get_carbonfootprint_list(51)
    cfp_list_7 = get_carbonfootprint_list(35)
    cfp_list_8 = get_carbonfootprint_list(33)
    cfp_list_9 = get_carbonfootprint_list(32)
    cfp_list_10 = get_carbonfootprint_list(19)
    cfp_list_11 = get_carbonfootprint_list(72)
    cfp_list_12 = get_carbonfootprint_list(4)
    cfp_list_13 = get_carbonfootprint_list(77)
    cfp_list_14 = get_carbonfootprint_list(78)
    cfp_list_15 = get_carbonfootprint_list(9)
    cfp_list_16 = get_carbonfootprint_list(39)
    cfp_total_list = []
    for i in range(0, 3):
        cfp_total_list.append(float(cfp_list_1[i]) + float(cfp_list_2[i]) + float(cfp_list_3[i]) + float(
        cfp_list_4[i]) + float(cfp_list_5[i]) + float(cfp_list_6[i]) + float(
        cfp_list_7[i]) + float(cfp_list_8[i]) + float(cfp_list_9[i]) + float(cfp_list_10[i]) + float(cfp_list_11[i]) + float(cfp_list_12[i]) + float(cfp_list_13[i]) + float(cfp_list_14[i]) + float(cfp_list_15[i]) + float(cfp_list_16[i])),
    print(cfp_total_list)
    return cfp_total_list


def get_carbonfootprint_recipe7():
    cfp_list_1 = get_carbonfootprint_list(43)
    cfp_list_2 = get_carbonfootprint_list(58)
    cfp_list_3 = get_carbonfootprint_list(51)
    cfp_list_4 = get_carbonfootprint_list(72)
    cfp_list_5 = get_carbonfootprint_list(38)
    cfp_list_6 = get_carbonfootprint_list(59)
    cfp_list_7 = get_carbonfootprint_list(53)
    cfp_total_list = []
    for i in range(0, 3):
        cfp_total_list.append(float(cfp_list_1[i]) + float(cfp_list_2[i]) + float(cfp_list_3[i]) + float(
        cfp_list_4[i]) + float(cfp_list_5[i]) + float(cfp_list_6[i]) + float(
        cfp_list_7[i])),
    print(cfp_total_list)
    return cfp_total_list

def get_carbonfootprint_recipe8():
    cfp_list_1 = get_carbonfootprint_list(43)
    cfp_list_2 = get_carbonfootprint_list(14)
    cfp_list_3 = get_carbonfootprint_list(15)
    cfp_list_4 = get_carbonfootprint_list(30)
    cfp_list_5 = get_carbonfootprint_list(27)
    cfp_list_6 = get_carbonfootprint_list(52)
    cfp_list_7 = get_carbonfootprint_list(50)
    cfp_list_8 = get_carbonfootprint_list(35)
    cfp_list_9 = get_carbonfootprint_list(59)
    cfp_list_10 = get_carbonfootprint_list(76)
    cfp_list_11 = get_carbonfootprint_list(42)
    cfp_list_12 = get_carbonfootprint_list(25)
    cfp_total_list = []
    for i in range(0, 3):
        cfp_total_list.append(float(cfp_list_1[i]) + float(cfp_list_2[i]) + float(cfp_list_3[i]) + float(
        cfp_list_4[i]) + float(cfp_list_5[i]) + float(cfp_list_6[i]) + float(
        cfp_list_7[i]) + float(cfp_list_8[i]) + float(cfp_list_9[i]) + float(cfp_list_10[i]) + float(cfp_list_11[i]) + float(cfp_list_12[i])),
    return cfp_total_list

def get_carbonfootprint_recipe9():
    cfp_list_1 = get_carbonfootprint_list(67)
    cfp_list_2 = get_carbonfootprint_list(68)
    cfp_list_3 = get_carbonfootprint_list(23)
    cfp_list_4 = get_carbonfootprint_list(20)
    cfp_list_5 = get_carbonfootprint_list(66)
    cfp_list_6 = get_carbonfootprint_list(51)
    cfp_list_7 = get_carbonfootprint_list(10)
    cfp_list_8 = get_carbonfootprint_list(9)
    cfp_list_9 = get_carbonfootprint_list(8)
    cfp_list_10 = get_carbonfootprint_list(11)
    cfp_list_11 = get_carbonfootprint_list(29)
    cfp_list_12 = get_carbonfootprint_list(37)
    cfp_list_13 = get_carbonfootprint_list(39)
    cfp_list_14 = get_carbonfootprint_list(77)
    cfp_list_15 = get_carbonfootprint_list(4)
    cfp_list_16 = get_carbonfootprint_list(40)
    cfp_list_17 = get_carbonfootprint_list(60)
    cfp_list_18 = get_carbonfootprint_list(36)
    cfp_list_19 = get_carbonfootprint_list(54)
    cfp_total_list = []
    for i in range(0, 3):
        cfp_total_list.append(float(cfp_list_1[i]) + float(cfp_list_2[i]) + float(cfp_list_3[i]) + float(
        cfp_list_4[i]) + float(cfp_list_5[i]) + float(cfp_list_6[i]) + float(
        cfp_list_7[i]) + float(cfp_list_8[i]) + float(cfp_list_9[i]) + float(cfp_list_10[i]) + float(cfp_list_11[i]) + float(cfp_list_12[i]) + float(cfp_list_13[i]) + float(cfp_list_14[i]) + float(cfp_list_14[i]) + float(cfp_list_16[i]) + float(cfp_list_17[i]) + float(cfp_list_18[i]) + float(cfp_list_19[i])),
    return cfp_total_list

def get_carbonfootprint_recipe10():
    cfp_list_1 = get_carbonfootprint_list(70)
    cfp_list_2 = get_carbonfootprint_list(44)
    cfp_list_3 = get_carbonfootprint_list(5)
    cfp_list_4 = get_carbonfootprint_list(45)
    cfp_list_5 = get_carbonfootprint_list(43)
    cfp_list_6 = get_carbonfootprint_list(25)
    cfp_list_7 = get_carbonfootprint_list(6)
    cfp_list_8 = get_carbonfootprint_list(18)
    cfp_list_9 = get_carbonfootprint_list(72)
    cfp_total_list = []
    for i in range(0, 3):
        cfp_total_list.append(float(cfp_list_1[i]) + float(cfp_list_2[i]) + float(cfp_list_3[i]) + float(
        cfp_list_4[i]) + float(cfp_list_5[i]) + float(cfp_list_6[i]) + float(
        cfp_list_7[i]) + float(cfp_list_8[i]) + float(cfp_list_9[i])),
    print(cfp_total_list)
    return cfp_total_list

# Function to calculate total carbon footprint for a recipe

def get_totalcarbonfootprint_recipe(rec_id):
    ingredient = db.session.query(Ingredient).filter_by(recipe_id=rec_id).all()
    ingredientlist = []
    if ingredient == Ingredient.recipe_id :
        ingredientlist.append(Ingredient.ingredient_id)
    else:
        return None

print(get_totalcarbonfootprint_recipe(5))

def get_random_number():
    x = randint(1, 7)
    return x

def get_fact(num):
    if num == 1:
        fact = "If you want to minimise your carbon footprint without giving up meat, chicken is your best option. Chicken produces 2.33 kg of C02 per kg of meat before transport and processing. There are issues with slaughter and processing though. Slaughtering poultry is more energy intensive than slaughtering ruminant animals."
    elif num == 2:
        fact = "What foods have the biggest carbon footprint? Beef has the highest carbon footprint of any food. This is because of what is required to raise and farm cattle. Animals used for beef production require a tremendous amount of feed, which must be grown on its own"
    elif num == 3:
        fact = "How much of our total carbon footprint comes from the food we eat? Food accounts for 10-30% of a household's carbon footprint, typically a higher portion in lower-income households. Production accounts for 68% of food emissions, while transportation accounts for 5%."
    elif num == 4:
        fact = "According to figures from the United Nations Environment Programme (UNEP), it takes 3,781 liters of water to make a pair of jeans, from the production of the cotton to the delivery of the final product to the store. That equates to the emission of around 33.4 kilograms of carbon equivalent."
    elif num == 5:
        fact = "The average daily footprint in the UK is currently 35.6kg CO2e which includes travel, home heating, and so on. The average diet related carbon footprint is 5.17kg CO2e – but this needs to shrink to 4.09kg CO2e by 2030."
    elif num == 6:
        fact = "The climate and our food is a two-way street. We have identified twenty risks posed by climate change to our classic British dishes, some affecting food production overseas, while others emerging on home shores. Example impacts include lower yields for global commodities like rice and soybeans; heat stress disrupting livestock productivity; warmer, wetter conditions leading to pest invasions and proliferations; and water shortagesthreatening age-old production regions."
    return fact

# def get_recipe_matching_collection_id(coll_id):
#     recipe_collection = db.session.query(RecipeCollection).filter(collection_id=coll_id).first()
#     if recipe_collection == None:
#         print('nothing found')
#     else:
#         matching_recipe = recipe_collection.recipe_id
#         final_recipes = db.session.query(Recipe).filter_by(recipe_id=matching_recipe).first()
#         if final_recipes == None:
#             print('No')
#         else:
#             return final_recipes

