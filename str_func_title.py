def title_str():
    """
    функция, которая делает заглавными первые буквы каждого слова в строке, поступившей на вход функции
    """
    stroka_user = input (str())
    return ' '.join(word.capitalize() for word in stroka_user.split())

title_str()