import shelve

cars = {
    "AB1234CD": "Іван Кришталь",
    "BC5678EF": "Петро Гарбузов",
    "DE9012GH": "Марія Ковальчук",
    "FG3456IJ": "Оксана Степаненко",
}

#Відкриваємо бінарний файл за допомогою `shelve`
with shelve.open('cars_data') as db:
    # Записуємо дані зі словника у файл
    for key, value in cars.items():
        db[key] = value

print("Дані про автомобілі успішно записані у бінарний файл!")
