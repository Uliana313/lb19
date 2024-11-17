import pickle

# Читання бінарного файлу
with open("numbers.bin", "rb") as file:
    data = pickle.load(file)
print(data)

