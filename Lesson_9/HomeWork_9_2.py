import csv

all_data = "C:/Users/bonda/PycharmProjects/python_Begin/Lesson_9/Files/names.csv"  # 1
email_data = "C:/Users/bonda/PycharmProjects/python_Begin/Lesson_9/Files/emails_from_names.csv"  # 2

with open(all_data, "r") as all_data, open(email_data, "w", newline="") as email_data:
  reader = csv.reader(all_data, delimiter=",")


  writer = csv.writer(email_data, delimiter=",")
  for row in reader:
    email = row[2]
    writer.writerow([email])
