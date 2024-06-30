from src.masks import get_mask_account, get_mask_card_number


def main() -> None:
    get_account = get_mask_account('')
    get_card = get_mask_card_number('')
    print("account: " + get_account)
    print("card: " + get_card)


if __name__ == "__main__":
    main()
