def mask_account_card(user_input: str) -> (str, bool):
    """ Функция общей маскировки карты и счета,
    принимает на вход только один аргумент — строку,
    которая состоит из требуемых частей. Это может быть строка типа
    Visa Platinum 7000 7922 8960 6361
    , или Maestro 7000 7922 8960 6361, или Счет 73654108430135874305
     Разделять строку на 2 аргумента (отдельно имя, отдельно номер) нельзя!"""
    word_and_number = list(user_input)
    new_word = ''
    new_number = ''
    flag = False

    for i in word_and_number:
        if i.isalpha():
            new_word += i
        else:
            new_number += i

    if new_word == 'Счет':
        result = new_number
    else:
        flag = True
        result = new_number
    return result, flag




