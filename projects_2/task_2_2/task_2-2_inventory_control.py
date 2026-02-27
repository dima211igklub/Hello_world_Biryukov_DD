reagent_name = input("\nВведите название необходимого реактива: ")
reagent_quantity = int(input("Введите необходимое колличество реактива: "))

print(f"\n\tРеактив {reagent_name} поступил на склад в количестве {reagent_quantity}.")

with open("inventory.txt", "w", encoding="utf-8") as inventory_file:
 inventory_file.write(f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity}.")

print("\nДанные сохранены в файл inventory.txt")

