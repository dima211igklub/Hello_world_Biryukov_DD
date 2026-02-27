weight = float(input("\n\tВведите ваш вес (кг): "))
height = float(input("\tВведите ваш рост (cм): "))

bmi = weight / ((height / 100)** 2)

print("\n--- Отчет о состоянии здоровья ---")
print(f"Рост:  ", height, "см")
print(f"Вес:   ", weight, "кг")
print(f"Индекс массы тела пациента: ", f"{bmi:.2f}")