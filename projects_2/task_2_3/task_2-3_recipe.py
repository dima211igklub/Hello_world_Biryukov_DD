nutrient_name = input("\n\tВведите название питательной среды: ")
agar_concentration = int(input("\tВведите концентрацию агара (%): "))
sterilization_temperature = int(input("\tВведите температуру стерилизации (°C): "))

with open("recipe.txt", "w", encoding="utf-8") as nutrient:
    nutrient.write(f"{nutrient_name}\n\tКонцентрация агара: {agar_concentration}\n\tТемпература стерилизации: {sterilization_temperature}")

print("\nФайл 'recipe.txt' успешно сформирован!")