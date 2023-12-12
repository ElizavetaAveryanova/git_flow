def capitalize_str():
    """
    функция, которая принимает на вход строку и возвращает строку со всеми заглавными буквами
    """
    stroka_user = input (str())
    return stroka_user.upper()

capitalize_str()


def title_str():
    """
    функция, которая делает заглавными первые буквы каждого слова в строке, поступившей на вход функции
    """
    stroka_user = input (str())
    return ' '.join(word.capitalize() for word in stroka_user.split())

title_str()

