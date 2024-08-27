def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": int(age)
                }
                cats_info.append(cat_info)
        return cats_info
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []
    
cats_info = get_cats_info("goit-algo-hw-04\cats.txt")
print(cats_info)
    