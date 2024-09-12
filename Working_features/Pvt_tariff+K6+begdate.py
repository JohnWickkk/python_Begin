import json

# Початкова дата
begDate = "2024-08-15"

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
    "1": "4.8",
    "2": "3.5",
    "3": "2.8",
    "4": "2.5",
    "5": "1.6",
    "6": "5",
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

# Словник значень для k6
k6_options = {
    "1": {
        "B1": "2.18",
        "B2": "2.17",
        "B3": "2.16",
        "B4": "2.11",
        "B5": "2.64",
        "F": "2.88",
        "D1": "3.08",
        "D2": "3.07",
        "C1": "1.98",
        "C2": "2.16",
        "E": "2.88",
        "A1": "3.33",
        "A2": "3.1"
    },
    # Решта словника залишається такою ж...
}

def generate_single_request(begDate, k1_key, k2_key):
    k1 = {k1_key: k1_options[k1_key]}
    k2 = {k2_key: k2_options[k2_key]}
    k6_value = k6_options.get(k2_key, {}).get(k1_key, "N/A")
    k3_value = "FL0" + k1_key
    k3 = {k3_value: "1"}
    name = f"begDate={begDate}|FL|{k2_options[k2_key]}|Kf6{k6_value}"
    description = name

    return {
        "name": name,
        "description": description,
        "begDate": begDate,
        "franchise": "0",
        "bonusMalusCl": 3,
        "riskOptions": True,
        "k1": k1,
        "k2": k2,
        "k3": k3,
        "k4": {"FL": "1.76"},
        "k5": k5_options,
        "k6": {"0": k6_value},
        "k7": {
            "05": "0.15", "1": "0.2", "2": "0.3", "3": "0.4", "4": "0.5",
            "5": "0.6", "6": "0.7", "7": "0.75", "8": "0.8", "9": "0.85",
            "10": "0.9", "11": "0.95", "12": "1"
        },
        "k8": {"DIGITAL": "1"},
        "kp": {"0": "1"},
        "k9": {}
    }

def get_user_input():
    # Використання змінної begDate
    print(f"Початкова дата: {begDate}")

    # Запит у користувача, чи формувати запити поштучно чи масово
    mode = input("Введіть '1' для формування запитів поштучно або '2' для масового формування запитів: ")

    if mode == '1':
        requests = []
        while True:
            # Запит у користувача для k1 (категорія авто)
            print("Виберіть категорію авто (k1) з наступного списку:")
            for key in k1_options.keys():
                print(f"{key}: {k1_options[key]}")

            k1_key = input("Введіть ключ для категорії авто (k1): ")
            while k1_key not in k1_options:
                print("Невірний вибір. Спробуйте ще раз.")
                k1_key = input("Введіть ключ для категорії авто (к1): ")

            # Запит у користувача для k2 (територія)
            print("Виберіть територію (k2) з наступного списку:")
            for key in k2_options.keys():
                print(f"{key}: {k2_options[key]}")

            k2_key = input("Введіть ключ для території (k2): ")
            while k2_key not in k2_options:
                print("Невірний вибір. Спробуйте ще раз.")
                k2_key = input("Введіть ключ для території (k2): ")

            # Генерація запиту
            request = generate_single_request(begDate, k1_key, k2_key)
            requests.append(request)

            # Запит у користувача, чи хоче він додати ще один запит
            more = input("Бажаєте додати ще один запит? (yes/no): ")
            if more.lower() != "yes":
                break

    elif mode == '2':
        requests = []
        for k1_key in k1_options.keys():
            for k2_key in k2_options.keys():
                request = generate_single_request(begDate, k1_key, k2_key)
                requests.append(request)

    else:
        print("Невірний режим. Будь ласка, запустіть програму знову.")
        return None

    return json.dumps(requests, ensure_ascii=False, indent=4)

# Виклик функції
json_data = get_user_input()
if json_data:
    print(json_data)
