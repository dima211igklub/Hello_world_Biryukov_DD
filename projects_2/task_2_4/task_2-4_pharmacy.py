capsul_quantity = int(input("\n\t Введите общее количество произведенных капсул: "))
capacity = int(input("\t Введите вместимость одной упаковки: "))

package_quantity = capsul_quantity // capacity
remaining_capsul = capsul_quantity % capacity

print("\n--- Отчет фасовочного цеха ---")
print("Полных упаковок:  ", package_quantity)
print("Остаток капсул:   ", remaining_capsul)
