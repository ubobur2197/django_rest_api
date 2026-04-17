import os
import django
import random
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from main.models import Ustoz, Guruh, Talaba


def run():
    # Eski ma'lumotlarni tozalash (xohlasangiz olib tashlang)
    Talaba.objects.all().delete()
    Guruh.objects.all().delete()
    Ustoz.objects.all().delete()

    # ===== USTOZLAR =====
    ustozlar_data = [
        {"firstname": "Ali", "lastname": "Valiyev", "subject": "Matematika"},
        {"firstname": "Sardor", "lastname": "Karimov", "subject": "Fizika"},
        {"firstname": "Dilnoza", "lastname": "Rasulova", "subject": "Informatika"},
    ]

    ustozlar = []
    for data in ustozlar_data:
        ustoz = Ustoz.objects.create(**data)
        ustozlar.append(ustoz)

    print("✅ 3 ta ustoz yaratildi")

    # ===== GURUHLAR =====
    guruhlar = []
    for i in range(1, 7):
        guruh = Guruh.objects.create(
            name=f"Guruh {i}",
            ustoz=random.choice(ustozlar)
        )
        guruhlar.append(guruh)

    print("✅ 6 ta guruh yaratildi")

    # ===== TALABALAR =====
    firstnames = ["Aziz", "Jasur", "Bekzod", "Diyor", "Umid", "Shahzod", "Zafar", "Akmal", "Sardor", "Islom"]
    lastnames = ["Aliyev", "Valiyev", "Karimov", "Toshmatov", "Rasulov", "Sodiqov", "Qodirov", "Ergashev", "Nazarov", "Yusupov"]
    grades = ["A", "B", "C", "A+", "B+"]

    for i in range(60):
        firstname = random.choice(firstnames)
        lastname = random.choice(lastnames)
        birth_date = date.today() - timedelta(days=random.randint(18*365, 25*365))
        grade = random.choice(grades)
        group = random.choice(guruhlar)

        Talaba.objects.create(
            firstname=firstname,
            lastname=lastname,
            birth_date=birth_date,
            grade=grade,
            group=group
        )

    print("✅ 60 ta talaba yaratildi")


if __name__ == "__main__":
    run()