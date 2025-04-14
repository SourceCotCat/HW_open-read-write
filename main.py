def open_file(file: str) -> dict:
    """
    Открывает указанный .txt-файл и возвращает содержимое в виде словаря.
    :param file: Путь к файлу с расширением '.txt'.
    :type file_path: str
    :return: Словарь, сформированный на основе содержимого файла. 
    
    """
     
    cook_book = {}

    with open(file, 'r', encoding='utf-8') as f:
        while True:

            dish_name = f.readline().strip()
            if not dish_name:
                break

            count_ingr = int(f.readline().strip())
            ingredients = []

            for _ in range(count_ingr):
                ingredient = f.readline().strip()
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredients.append({'ingredient_name' : ingredient_name, 'quantity': int(quantity), 'measure': measure})
            
            cook_book[dish_name] = ingredients

            f.readline()

    return cook_book   

def pretty_print(cook_book: dict) -> None:
    """
    Функция для красивого форматированного вывода книги рецептов.

    :param cook_book: Словарь, содержащий рецепты блюд.
    :type cook_book: dict
    :return: Ничего не возвращает, только выводит данные на экран.
    """
    print("{")
    for dish, ingredients in cook_book.items():
        print(f"'{dish}': [")
        for ingredient in ingredients:
            print(f"    {ingredient},")
        print(" ],")
    print("}")



cook_book = open_file('recipes.txt')
pretty_print(cook_book)

