print("\n=== Анализ последовательности ДНК ===")

nucleotid_sequence = input("\nВведите последовательность ДНК: ").upper().strip()
count_A = nucleotid_sequence.count("A")
count_T = nucleotid_sequence.count("T")
count_G = nucleotid_sequence.count("G")
count_C = nucleotid_sequence.count("C")

count = count_A + count_T + count_G + count_C    #сделал именно так, чтобы не считались другие символы

print("\nПоследовательность в верхнем регистре: ", nucleotid_sequence)
print("\nПодсчёт нуклеотидов:\n", "A:", count_A, f"({(count_A / count) * 100:.2f})%", "\n", "T:", count_T, f"({(count_T / count) * 100:.2f})%", "\n", "G:", count_G, f"({(count_G / count) * 100:.2f})%", "\n", "C:", count_C, f"({(count_C / count) * 100:.2f})%") #да да, не красиво, не культурно, зато практично
print("\nОбщая длина:", count)

