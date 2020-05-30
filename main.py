from ListParser import *
from Hand import HandMaker


print("\n\n\tIMPORTING\n")
import tesseract_reader
print("\n\n\tDONE IMPORTING\n")
quit()


'''
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

from flask import Flask
'''

parser = Parser()

# card_types list indices for Magic, Equip, Ritual, and Trap types
exclude_M_E_R_T = [20, 21, 22, 23]

'''
# collect card data
deck = parser.parse_passwords()

# get a list of all ritual type cards from the deck
print(deck.get_all_of_type("Ritual"))

# get a list of all cards with an attack of 1200 +/- 200
print(deck.get_all_of_atk(1200, 200))

# get a list of all cards with an attack of 1500 +/- 0, and include all cards
# with attack less-than 1500
print(deck.get_all_of_atk(100, 0, False, True, True))

# for id, val in cards.cards_dict.items():
#     print(val)
'''

'''
# Printing all cards with combos and results
for key, val in parser.deck.cards_dict.items():
    print("k: " + str(key) + ", v: " + str(val))
    print("\tcombos: " + str(val.combo_card))
    print("\tresults: " + str(val.result_card))
'''

# hand_maker = parser.hand_maker
#
# hand_01_list = [2, 3, 4]
# hand_01 = hand_maker.create_hand("Hand_01", hand_01_list)
#
# hand_02_list = [127, 3, 416, 700, 95]
# hand_02 = hand_maker.create_hand("Hand_02", hand_02_list)
#
# hand_02_list = [127, 3, 416, 77, 95]
# hand_02 = hand_maker.create_hand("Hand_02", hand_02_list)
#
# hand_03_list = [313, 531, 505, 271, 245, 484, 187, 214]
# hand_03 = hand_maker.create_hand("Hand_03", hand_03_list)
#
# all_n_list = list(range(1, len(parser.deck.cards_dict) + 1))
# all_cards_hand = hand_maker.create_hand("All Cards", all_n_list)

'''
print("\n\n")
print(hand_01)

print("\n\n")
print(hand_01.is_possible_fusion_with(7))

print("\n\n")
print(hand_01.get_possible_fusion_results(7))

print("\n\n")
print(hand_02)

print("\n\n")
print(hand_02.is_possible_fusion_with(1))

print("\n\n")
print(hand_02.get_possible_fusion_results(1))
'''

print("\n\n")
# print(hand_03)
# print("FUSIONS: ")
# fusions = hand_03.gen_all_possible_fusions(hand_03, hand_03, [])
# for el in fusions:
#     for a, v in el.items():
#         b = v[0]
#         c = v[1]
#         print("a: " + str(a)
#               + "\tb: " + str(b)
#               + "\tc: " + str(c)
#               + "\n== c( " + str(hand_maker.deck.cards_dict[c])
#               + "\na( " + str(hand_maker.deck.cards_dict[a])
#               + "\n+ b( " + str(hand_maker.deck.cards_dict[b]))
#               # + " )\nv ( " + str(hand_maker.deck.cards_dict[v]) + " )")

'''
print("\n\n")
print(all_cards_hand.get_possible_fusion_results(7))
'''

'''
card_010 = parser.deck.cards_dict[10]
print(card_010)
print(card_010.star_sign(True, "V"))
print(card_010.star_sign(True, "Me"))
print(card_010.star_sign(True, "Su"))
print(card_010.star_sign(True, "Mo"))
print(card_010.star_sign(True, "Ma"))
print(card_010.star_sign(True, "J"))
print(card_010.star_sign(True, "Sa"))
print(card_010.star_sign(True, "U"))
print(card_010.star_sign(True, "P"))
print(card_010.star_sign(True, "N"))
'''


# print("highest atk: " + str(hand_03.highest_atk()))
# print("highest def: " + str(hand_03.highest_def()))
# print("lowest atk: " + str(hand_03.lowest_atk()))
# print("lowest def: " + str(hand_03.lowest_def()))
#
# print(parser.repr_cards(parser.deck.get_all_of_atk(0, exclude=exclude_M_E_R_T)))
# print(parser.repr_cards(parser.deck.get_all_of_def(0, exclude=exclude_M_E_R_T)))
# print("highest atk: " + str(parser.repr_cards(all_cards_hand.highest_atk(exclude_M_E_R_T))))
# print("highest def: " + str(parser.repr_cards(all_cards_hand.highest_def(exclude_M_E_R_T))))
# print("lowest atk: " + str(parser.repr_cards(all_cards_hand.lowest_atk(exclude_M_E_R_T))))
# print("lowest def: " + str(parser.repr_cards(all_cards_hand.lowest_def(exclude_M_E_R_T))))

# hand_01 = parser.hand_maker.draw_hand("Hand 001", 5)
# hand_02 = parser.hand_maker.draw_hand("Hand 001", 5)

# 571  B. Dragon Jungle King
# 045  Oscillo Hero #2
# 004  Baby Dragon
# 579  Abyss Flower

# test_hand_01_lst = [45, 4, 579, 9, 567, 537]

test_hand_02_lst = [393, 101, 458, 244, 620, 488, 113]
test_02_hand = parser.hand_maker.create_hand("Test 01", test_hand_02_lst)
print(test_02_hand)
print(test_02_hand.get_card_ids())
print(test_02_hand.gen_fusions(test_02_hand))
print("\n\tHolding Equip Combo\n" + str(test_02_hand.holding_equip_combo()))

# test_hand_01_lst = [45, 302, 12]
# test_01_hand = parser.hand_maker.create_hand("Test 01", test_hand_01_lst)
# print(test_01_hand.get_card_ids())
# print(test_01_hand.gen_fusions(test_01_hand))
# print("\n\tHolding Equip Combo\n" + str(test_01_hand.holding_equip_combo()))


# all_possible_hands = parser.hand_maker.create_all_hands(test_hand_01_lst)
#
# for hand in all_possible_hands:
#     print("type: " + str(type(hand)))
#     print(hand.get_card_ids())
#     print("\n\tFINAL FUSIONS: " + str(hand.gen_all_possible_fusions(hand, [])) + "\n")
# # test_hand_01 = parser.hand_maker.create_hand("Test 001", )

# print(hand_01)

