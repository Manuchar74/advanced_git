from src.masks import get_mask_account, get_mask_card_number


def main() -> None:
    get_account = get_mask_account("73654108430135874305")
    get_card = get_mask_card_number("7000792289606361")
    print("account: " + get_account)
    print("card: " + get_card)


if __name__ == "__main__":
    main()
