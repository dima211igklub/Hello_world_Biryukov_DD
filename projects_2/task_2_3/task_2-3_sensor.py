operator_name = input("\n\tВведите имя оператора: ")
pressure_value = int(input("\tВведите текущее значение давления (Па): "))

with open("sensor_log.txt", "w", encoding="utf-8") as log_file:
    log_file.write(f"{operator_name}\t{pressure_value}\n")

print("\nДанные успешно сохранены в sensor_log.txt")