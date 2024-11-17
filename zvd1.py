import pickle

a = int(input("Введіть початок інтервалу a: "))
b = int(input("Введіть кінець інтервалу b: "))

List1 = []

numbers_ending_with_6 = [x for x in List1 if x % 10 == 6]

with open("numbers.bin", "wb") as file:
    pickle.dump(numbers_ending_with_6, file)

print("Числа, що закінчуються на 6, успішно записані у файл 'numbers.bin'.")
