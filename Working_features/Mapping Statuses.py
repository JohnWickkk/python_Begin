npg_statuses = {
    "522": {
        "Parrent": 'UPS',
        "UPS status code": '1C',
        "UPS status description": "Available for Pickup",
        "Description NPG": "Ready for Pickup"
    },
    "3-1": {
        "Parrent": 'UPS',
        "status code": '01',
        "status description": "Delivered, In/At Mailbox",
        "Description NPG": "Delivered, In/At Mailbox"
    }
}
def normalize_input(value):
  """
  Нормалізує введене значення до рядкового типу.

  Args:
      value: Введене значення (може бути числом або рядком).

  Returns:
      Рядкове представлення введеного значення.
  """
  return str(value)
def find_status(search_value):
    """
    Функція для пошуку статусу за ключем або значенням поля "status code".

    Args:
        search_value: Ключ або значення поля "status code" для пошуку.

    Returns:
        Словник з інформацією про статус або None, якщо статус не знайдено.
    """
    normalized_value = normalize_input(search_value)
    # Спочатку шукаємо за ключем
    if normalized_value in npg_statuses:
        return npg_statuses[normalized_value]

    # Якщо ключа немає, шукаємо за значенням поля "status code"
    for status_id, status_data in npg_statuses.items():
        if status_data.get("status code") == normalized_value:
            return status_data

    return None

def main():
    while True:
        search_value = input("Введіть ключ або значення поля 'status code' (або 'exit' для виходу): ")
        if search_value.lower() == 'exit':
            break

        result = find_status(search_value)
        if result:
            print("Знайдено наступний статус:")
            for key, value in result.items():
                print(f"{key}: {value}")
        else:
            print("Статус не знайдено.")

if __name__ == "__main__":
    main()