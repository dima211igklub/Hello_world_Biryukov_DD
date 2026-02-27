spectrophotometer_name = "Спектрофотометр"
spectrophotometer_inventory = "001"
spectrophotometer_condition = "Исправен"
spectrophotometer_quantity = "3"

thermostat_name = "Термостат"
thermostat_inventory = "002"
thermostat_condition = "Неисправен"
thermostat_quantity = "1"

dispenser_name = "Автодозатор"
dispenser_inventory = "003"
dispenser_condition = "Исправен"
dispenser_quantity = "15"

amplifier_name = "Амплификатор"
amplifier_inventory = "004"
amplifier_condition = "Исправен"
amplifier_quantity = "2"

equipment = [(spectrophotometer_name, spectrophotometer_inventory, spectrophotometer_condition, spectrophotometer_quantity),
             (thermostat_name, thermostat_inventory,thermostat_condition,thermostat_quantity),
             (dispenser_name,dispenser_inventory,dispenser_condition,dispenser_quantity),
             (amplifier_name,amplifier_inventory,amplifier_condition,amplifier_quantity)]

separator = "|" + "-" * 19 + "|" + "-" * 7 + "|" + "-" * 15 + "|" + "-" * 8 + "|"

def print_equipment(data):
    '''Функция вывода таблицы'''
    print("\n", "ЛАБОРАТОРНОЕ ОБОРУДОВАНИЕ".center(54))
    print("-" * 54)
    print(f"|{'Наименование':^19}|{'№':^7}|{'Состояние':^15}|{'Кол-во':^8}|")
    print(separator)

    for i, item in enumerate(data):
        print(f"|{item[0]:^19}|{item[1]:^7}|{item[2]:^15}|{item[3]:^8}|")

        if i < len(data) -1:
            print(separator)

    print("-" * 54)

print_equipment(equipment)