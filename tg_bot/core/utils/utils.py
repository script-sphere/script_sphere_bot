import json

from aiogram.types import InlineKeyboardButton


# Загружаем данные

with open('tg_bot/data.json') as f:
    data = json.load(f)


for base in data['player_1'].values():
    print(base['spheres'])

# def generate_player1_base(data):

#     player1_base = []

#     for base in data['player1_base'].values():
#         print(base['spheres'])
#         button = InlineKeyboardButton(
#             text=base['spheres'], callback_data=base['callback_data'])
#         player1_base.append(button)

#     print(player1_base)


# generate_player1_base(data)
