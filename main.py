from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_data


def main() -> None:
    file1 = open('data/input_text.txt', encoding='utf-8', mode='r')
    while True:
        # считываем строку
        line = file1.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break

        items = mask_account_card(line)

        first_element = items[0]
        second_element = items[1]
        third_element = items[2]

        if third_element is True:
            card_number = first_element
            get_card = get_mask_card_number(card_number)
            pref_1 = second_element
            print("card: " + pref_1 + ' ' + get_card)

        else:
            user_account = first_element
            get_account = get_mask_account(user_account)
            pref_2 = second_element
            print("account: " + pref_2 + ' ' + get_account)
    # закрываем фай
    file1.close()


print(get_data())


if __name__ == "__main__":
    main()
