import json

# Словник значень для k1 (категорія авто)
k1_options = {
    "B1": "1",
    "B2": "1.14",
    "B3": "1.14",
    "B4": "1.82",
    "B5": "0.9",
    "F": "0.34",
    "D1": "2.55",
    "D2": "3",
    "C1": "2",
    "C2": "2.18",
    "E": "0.5",
    "A1": "0.34",
    "A2": "0.68"
}

# Словник значень для k2 (територія)
k2_options = {
    "1": "1.2",
    "2": "1.3",
    "3": "1.4",
    "4": "1.5",
    "5": "1.6",
    "6": "1.7",
    "7": "1.8",
    "8": "1.9",
    "9": "2.0"
}

# Словник значень для k5
k5_options = {
    "12": "1",
    "11": "0.95",
    "10": "0.9",
    "9": "0.85",
    "8": "0.8",
    "7": "0.75",
    "6": "0.7"
}


def get_user_input():
    name = input("Введіть name: ")
    description = input("Введіть description: ")
    begDate = input("Введіть begDate (у форматі YYYY-MM-DD): ")
    franchise = "0"  # Значення за замовчуванням
    bonusMalusCl = 3  # Значення за замовчуванням
    riskOptions = True  # Значення за замовчуванням

    # Запит у користувача для k1 (категорія авто)
    print("Виберіть категорію авто (k1) з наступного списку:")
    for key in k1_options.keys():
        print(f"{key}: {k1_options[key]}")

    k1_key = input("Введіть ключ для категорії авто (k1): ")
    while k1_key not in k1_options:
        print("Невірний вибір. Спробуйте ще раз.")
        k1_key = input("Введіть ключ для категорії авто (k1): ")

    # Запит у користувача для k2 (територія)
    print("Виберіть територію (k2) з наступного списку:")
    for key in k2_options.keys():
        print(f"{key}: {k2_options[key]}")

    k2_key = input("Введіть ключ для території (k2): ")
    while k2_key not in k2_options:
        print("Невірний вибір. Спробуйте ще раз.")
        k2_key = input("Введіть ключ для території (k2): ")

    k1 = {k1_key: k1_options[k1_key]}
    k2 = {k2_key: k2_options[k2_key]}

    # Значення для k5 береться зі словника k5_options
    k5 = k5_options

    k3 = {"FL0F": "1"}
    k4 = {"FL": "1.76"}
    k6 = {"0": "5"}
    k7 = {
        "05": "0.15", "1": "0.2", "2": "0.3", "3": "0.4", "4": "0.5",
        "5": "0.6", "6": "0.7", "7": "0.75", "8": "0.8", "9": "0.85",
        "10": "0.9", "11": "0.95", "12": "1"
    }
    k8 = {"DIGITAL": "1"}
    kp = {"0": "1"}
    k9 = {}

    # Формування JSON об'єкта
    data = [
        {
            "name": name,
            "description": description,
            "begDate": begDate,
            "franchise": franchise,
            "bonusMalusCl": bonusMalusCl,
            "riskOptions": riskOptions,
            "k1": k1,
            "k2": k2,
            "k3": k3,
            "k4": k4,
            "k5": k5,
            "k6": k6,
            "k7": k7,
            "k8": k8,
            "kp": kp,
            "k9": k9
        }
    ]

    return json.dumps(data, ensure_ascii=False, indent=4)


# Виклик функції
json_data = get_user_input()
print(json_data)
