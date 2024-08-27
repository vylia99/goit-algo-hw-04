def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                _, salary = line.split(',')
                salaries.append(int(salary))
                
            total = sum(salaries)
            average = int(total / len(salaries)) if salaries else 0
            return total, average
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return 0, 0

total, average = total_salary("goit-algo-hw-04\programmists.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
