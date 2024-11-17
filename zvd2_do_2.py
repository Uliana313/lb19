import shelve

# Відкриваємо бінарний файл для читання
with shelve.open('cars_data') as db:
    print("Дані про автомобілі:")
    for key, value in db.items():
        print(f"Номер автомобіля: {key}, Володар: {value}")
