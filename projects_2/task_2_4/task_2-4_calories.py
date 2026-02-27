proteins_weight = int(input("\n\tВведите массу белков в продукте (г).: "))
fats_weight = int(input("\tВведите массу жиров в продукте (г).: "))
carbohydrates_weight = int(input("\tВведите массу углеводов в продукте (г).: "))

calorie = (proteins_weight * 4) + (fats_weight * 9) + (carbohydrates_weight * 4)

print(f"\nОбщая калорийность: {calorie}")
