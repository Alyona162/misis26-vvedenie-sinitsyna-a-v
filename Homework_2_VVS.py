def level_1(text, method):
    if method == 1:
        return text.upper()
    if method == 2:
        return text.lower()
    if method == 3:
        return text.capitalize()
    return "Неверный метод"


def level_2(text, method, x="", y=""):
    if method == 1:
        return text.find(x)
    if method == 2:
        return text.replace(x, y)
    if method == 3:
        return text.count(x)
    return None


def level_3(text, method, separator=""):
    """Разделение и объединение: 1 - split, 2 - join"""
    if method == 1:
        return text.split(separator) if separator else text.split()
    if method == 2:
        return separator.join(text.split())
    return None


def level_4(text, method):
    if method == 1:
        return text.isdigit()
    if method == 2:
        return text.isalpha()
    if method == 3:
        return text.strip()
    if method == 4:
        return text.lstrip()
    if method == 5:
        return text.rstrip()
    return None


def level_5(text):
    text = text.strip().capitalize()
    for symbol in [';', '-', '+']:
        text = text.replace(symbol, ' ')
    return ' '.join(text.split())


def show_examples():
    print("\n" + "=" * 50)
    print("ПРИМЕРЫ")
    print("=" * 50)

    print("\nУровень 1:")
    s = "прИвЕт МИР"
    print(f"upper:      {level_1(s, 1)}")
    print(f"lower:      {level_1(s, 2)}")
    print(f"capitalize: {level_1(s, 3)}")

    print("\nУровень 2:")
    s = "Ботать – это круто. Очень круто!"
    print(f"find('круто'):            {level_2(s, 1, 'круто')}")
    print(f"replace('круто','класс'): {level_2(s, 2, 'круто', 'класс')}")
    print(f"count('о'):               {level_2(s, 3, 'о')}")

    print("\nУровень 3:")
    s = "1,2,3,4,5"
    print(f"split(','): {level_3(s, 1, ',')}")
    print(f"join(';'):  {level_3(s, 2, ';')}")

    print("\nУровень 4:")
    for s in ["123456", "abc", "   abc   "]:
        print(f"'{s}': isdigit={level_4(s, 1)}, isalpha={level_4(s, 2)}, strip='{level_4(s, 3)}'")

    print("\nУровень 5:")
    s = " python;IS;AWEsomE;! "
    print(f"'{s}' -> '{level_5(s)}'")


def main():
    print("ДОБРО ПОЖАЛОВАТЬ!")
    show_examples()

    while True:
        print("\n" + "=" * 50)
        print("1 - Регистр (upper, lower, capitalize)")
        print("2 - Поиск и замена (find, replace, count)")
        print("3 - Разделение и объединение (split, join)")
        print("4 - Проверка и очистка (isdigit, isalpha, strip, lstrip, rstrip)")
        print("5 - Комплексное преобразование")
        print("0 - Выход")

        choice = input("\nВыберите уровень (0-5): ").strip()

        if choice == '0':
            print("Пока пока!")
            break

        if choice not in ['1', '2', '3', '4', '5']:
            print("Неверный выбор.")
            continue

        level = int(choice)
        text = input("Введите строку: ")

        if level == 1:
            method = int(input("Метод (1-upper, 2-lower, 3-capitalize): "))
            print(f"Результат: '{level_1(text, method)}'")

        elif level == 2:
            method = int(input("Метод (1-find, 2-replace, 3-count): "))
            if method == 2:
                old = input("Что заменить: ")
                new = input("На что заменить: ")
                print(f"Результат: '{level_2(text, method, old, new)}'")
            else:
                sub = input("Подстрока: ")
                print(f"Результат: {level_2(text, method, sub)}")

        elif level == 3:
            method = int(input("Метод (1-split, 2-join): "))
            sep = input("Разделитель (Enter — пробел): ")
            print(f"Результат: {level_3(text, method, sep)}")

        elif level == 4:
            method = int(input("Метод (1-isdigit, 2-isalpha, 3-strip, 4-lstrip, 5-rstrip): "))
            print(f"Результат: {level_4(text, method)}")

        elif level == 5:
            print(f"Результат: '{level_5(text)}'")


if __name__ == "__main__":
    main()