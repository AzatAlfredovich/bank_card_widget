from src.masks import get_mask_card_number, get_mask_account

from src.widget import mask_account_card

print(get_mask_card_number("7000 7922 8960 6361"))
print(get_mask_account("7000792289606361"))

print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("счёт 73654108430135874305"))
print(mask_account_card("Visa Gold 5999414228426353"))