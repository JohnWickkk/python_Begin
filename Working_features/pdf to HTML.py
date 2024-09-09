import PyPDF2
from bs4 import BeautifulSoup


# Функція для парсингу PDF та отримання тексту
def extract_text_from_pdf(pdf_path):
    pdf_text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            pdf_text += page.extract_text()
    return pdf_text


# Функція для створення HTML
def generate_html(pdf_text, template_html_path, output_html_path):
    # Відкриття шаблону HTML для читання стилістики
    with open(template_html_path, "r", encoding="utf-8") as template_file:
        template_html = template_file.read()

    # Створюємо структуру HTML за допомогою BeautifulSoup
    soup = BeautifulSoup(template_html, "html.parser")

    # Знаходимо контейнер для вставки контенту
    content_block = soup.find("div", {"class": "content_block"})

    # Створюємо новий блок для вставки тексту з PDF
    new_content = soup.new_tag("div")
    new_content.string = pdf_text

    # Додаємо новий контент до блоку
    content_block.append(new_content)

    # Записуємо результат у новий HTML файл
    with open(output_html_path, "w", encoding="utf-8") as output_file:
        output_file.write(str(soup))


# Шляхи до файлів
pdf_path = "/mnt/data/IEW.cancel 2.0.pdf"  # PDF файл для парсингу
template_html_path = "/mnt/data/Nova Global Partners API Doc.html"  # Шаблон HTML
output_html_path = "output.html"  # Фінальний HTML файл

# Отримання тексту з PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Генерація HTML файлу
generate_html(pdf_text, template_html_path, output_html_path)

print("HTML файл успішно згенеровано!")
