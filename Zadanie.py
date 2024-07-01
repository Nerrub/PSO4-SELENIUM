# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
# листать параграфы текущей статьи;
# перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
# - перейти на одну из внутренних статей.
#
# выйти из программы.
# В поле для ответа загрузи ссылку на Git.
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

def get_hatnotes(browser):
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)
    return hatnotes
def choose_random_link(hatnotes):
    links = []
    for hatnote in hatnotes:
        links.extend(hatnote.find_elements(By.TAG_NAME, "a"))
    if not links:
        print("Нет доступных связанных страниц.")
        return None
    return random.choice(links).get_attribute("href")
search_topic = input("Введите интересующую вас тему: ")
browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title
time.sleep(2)
search_box = browser.find_element(By.ID,"searchInput")
search_box.send_keys(search_topic)
search_box.send_keys(Keys.RETURN)
time.sleep(2)
a = browser.find_element(By.PARTIAL_LINK_TEXT, search_topic)
a.click()
time.sleep(2)

paragraphs = browser.find_elements(By.TAG_NAME, 'p')

# hatnotes = []
# for element in browser.find_elements(By.TAG_NAME, "div"):
#     cl = element.get_attribute("class")
#     if cl == "hatnote navigation-not-searchable":
#         hatnotes.append(element)
# hatnote = random.choice(hatnotes)
# link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
# browser.get(link)

while True:
    print("\nВыберите действие:")
    print("1. Листать параграфы текущей статьи")
    print("2. Перейти на одну из связанных страниц")
    print("3. Выйти из программы")

    choice = input("Введите номер действия: ")

    if choice == "1":
        paragraphs = browser.find_elements(By.TAG_NAME, 'p')
        for paragraph in paragraphs:
            print(paragraph.text)
            input("Нажмите Enter для продолжения...")

    elif choice == "2":
        hatnotes = get_hatnotes(browser)
        link = choose_random_link(hatnotes)
        if link:
            browser.get(link)
            time.sleep(2)
        else:
            print("Возврат к предыдущему меню.")

    elif choice == "3":
        print("Выход из программы.")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")
