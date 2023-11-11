
def read():
    cook_book = {}
    file = open(file="recipes.txt", encoding='utf-8', mode='r')
    while True:
        name = file.readline().strip()
        if not name:
            break
        number = int(file.readline().strip())
        ingredients = []
        for i in range(number):
            ingredient = {}
            line = file.readline().strip().split(' | ')

            ingredient["ingredient_name"] = line[0]
            ingredient["quantity"] = line[1]
            ingredient["measure"] = line[2]
            ingredients.append(ingredient)
        cook_book[name] = ingredients
        file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read()
    result = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient["ingredient_name"]
            measure = ingredient["measure"]
            quantity = int(ingredient["quantity"]) * person_count

            if ingredient_name not in result:
                result[ingredient_name] = {"measure": measure, "quantity": quantity}
            else:
                result[ingredient_name]["quantity"] += quantity
    return result

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5))