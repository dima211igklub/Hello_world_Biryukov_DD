solution_volume = float(input("\n\tВведите нужный объем раствора (в мл): "))
salt_mass = round(solution_volume * 0.009, 2)
water_volume = solution_volume
with open("recipe.txt", "w", encoding="utf-8") as file:
    print("\nОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:")
    print("-" * 23)
    print(f"Общий объем:  {solution_volume}(мл)")
    print(f"Масса соли:   {salt_mass}(г)")
    print(f"Объем воды:   {water_volume}(мл)")

    file.write("\nОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем:  {solution_volume}(мл)\n")
    file.write(f"Масса соли:   {salt_mass}(г)\n")
    file.write(f"Объем воды:   {water_volume}(мл)\n")



