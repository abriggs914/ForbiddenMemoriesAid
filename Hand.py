import random
import itertools

test_printing = True


def gen_all_permutations(lst):
    all_permutations = []
    for L in range(3, len(lst) + 1):
        for subset in itertools.permutations(lst, L):
            all_permutations.append(list(subset))
    return all_permutations


class HandMaker:

    def __init__(self, deck_in):
        self.deck = deck_in

    # Create a hand object with the given cards
    def create_hand(self, name, hand_in):
        hand = Hand(name, self.deck)
        hand.create_hand(hand_in)
        return hand

    def create_all_hands(self, cards):
        all_possible = gen_all_permutations(cards)
        new_hands = []
        num_hands = 0
        for possible in all_possible:
            num_hands += 1
            name = "Hand:\t" + str(num_hands)
            new_hands.append(self.create_hand(name, possible))

        return new_hands

    def draw_hand(self, name, n_cards):
        new_hand = [random.randint(1, len(self.deck.cards_dict)) + 1 for i in range(n_cards)]
        return self.create_hand(name, new_hand)


class Hand:

    def __init__(self, name, deck_in):
        self.name = name
        self.deck = deck_in
        self.cards = None
        self.cards_list = None

    def __repr__(self):
        res = "\t" + str(self.name) + ": [" + str(list(self.cards.keys())) + "]\n{\n"
        if self.cards:
            for id_n, card in self.cards.items():
                res += "\t\t" + str(card) + "\n"
        res += "\t}\n"
        return res

    def get_card_ids(self):
        return [id_num for id_num, card in self.cards.items()]

    # does this hand contain the given types(s)
    def contains_type(self, types):
        if type(types) is not list:
            types = [types]

        for t in types:
            for id_num, card in self.cards.items():
                if card.type_attribute == t:
                    return True

        return False

    def highest_atk(self, exclude=[]):
        highest_atk_pts = None
        highest_atk_id = None
        for id_n, card in self.cards.items():
            if not highest_atk_pts or card.atk > highest_atk_pts:
                if exclude and card.type_attribute in exclude:
                    continue
                highest_atk_pts = card.atk
                highest_atk_id = card.id_num

        return highest_atk_id

    def highest_def(self, exclude=[]):
        highest_def_pts = None
        highest_def_id = None
        for id_n, card in self.cards.items():
            if not highest_def_pts or card.defen > highest_def_pts:
                if exclude and card.type_attribute in exclude:
                    continue
                highest_def_pts = card.defen
                highest_def_id = card.id_num

        return highest_def_id

    def lowest_atk(self, exclude=[]):
        lowest_atk_pts = None
        lowest_atk_id = None
        for id_n, card in self.cards.items():
            if not lowest_atk_pts or card.atk < lowest_atk_pts:
                if exclude and card.type_attribute in exclude:
                    continue
                lowest_atk_pts = card.atk
                lowest_atk_id = card.id_num

        return lowest_atk_id

    def lowest_def(self, exclude=[]):
        lowest_def_pts = None
        lowest_def_id = None
        for id_n, card in self.cards.items():
            if not lowest_def_pts or card.defen < lowest_def_pts:
                if exclude and card.type_attribute in exclude:
                    continue
                lowest_def_pts = card.defen
                lowest_def_id = card.id_num

        return lowest_def_id

    # does this hand contain a card that the given card can be equipped to
    def is_equippable_to(self, equip_card):
        can_equip_to = equip_card.equip
        equippable = []
        if can_equip_to:
            equippable = [id_num for id_num, card in self.cards.items() if id_num in can_equip_to]
        return equippable

    # Initalizes the list of cards for the object
    def create_hand(self, hand_in):
        cards = {}
        if hand_in:
            for card_in in hand_in:
                cards[card_in] = self.deck.cards_dict[card_in]
        self.cards = cards
        self.cards_list = list(cards)

    # Creates a hand object of every card in the hand, except the given card's index
    def hand_without(self, idx):
        i = 0
        new_hand = []
        removed = None
        for id_n, card in self.cards.items():
            if i != idx:
                new_hand.append(id_n)
            else:
                removed = card
            i += 1
        new_hand_maker = HandMaker(self.deck)
        new_hand_obj = new_hand_maker.create_hand("new_hand -" + str(removed), new_hand)
        return new_hand_obj

    # get possible results of fusing entire hand with target card
    # returns a dict with keys for each card and a list of each resulting card
    def get_possible_fusion_results(self, target):
        possible = {}
        for id_number, card in self.cards.items():
            possible[id_number] = None
            if target in card.combo_card:
                idx = card.combo_card.index(target)
                # print("idx: " + str(idx) + ", combos: " + str(card.combo_card)
                #       + ", results: " + str(card.results_card))
                possible[id_number] = card.results_card[idx]
        return possible

    def add_card(self, new_card):
        # print("ADDING (" + str(new_card) + "): " + str(self.deck.cards_dict[new_card]))
        if not self.cards:
            self.cards = {}
        self.cards[new_card] = self.deck.cards_dict[new_card]

    def get_card_at_idx(self, idx):
        i = 0
        for id_number, card in self.cards.items():
            if i == idx:
                return card
            i += 1
        return None

    def gen_fusions(self, cards):
        if type(cards) == Hand:
            cards = cards.cards

        # print("\t\tcards_in: " + str(cards))
        all_permutations = gen_all_permutations(cards)
        total_fusions = {}

        if not all_permutations and len(cards) > 1:
            if type(cards) is dict:
                cards = list(cards)
            a = cards[0]
            b = cards[1]
            # print("a: " + str(a) + ", b: " + str(b) + "\n\tfusions: " + str(self.deck.cards_dict[a].fusions))
            fusions_list = [d["_card2"] for d in self.deck.cards_dict[a].fusions]
            results_list = [d["_result"] for d in self.deck.cards_dict[a].fusions]
            if b in fusions_list:
                fusion_idx = fusions_list.index(b)
                c = results_list[fusion_idx]
                return {c : [(a, b)]}

        # print("all_permutations:\t" + str(all_permutations))
        for permutation in all_permutations:
            # print("p: " + str(permutation))
            if permutation:
                card_1 = permutation[0]
                temp_hand = HandMaker(self.deck).create_hand("temp_hand", list(cards)[1:])
                possible_fusions = temp_hand.get_possible_fusion_results(card_1)
                # print("pf: " + str(possible_fusions))
                for id_n, fusion in possible_fusions.items():
                    if fusion:
                        entry = (card_1, id_n)
                        rev_entry = (id_n, card_1)
                        # print("entry: " + str(entry) + "\ttotal_fusions: " + str(total_fusions))
                        if fusion in total_fusions:
                            if entry not in total_fusions[fusion] and rev_entry not in total_fusions[fusion]:
                                total_fusions[fusion].append(entry)
                        else :
                            total_fusions[fusion] = [entry]

        # for fusion in total_fusions:
        #     print("\t" + str(fusion))

        # final_fusions = {}
        # if fusions found, try again by removing materials
        # and adding the result
        final_fusions = dict(total_fusions)
        cards_list = list(cards)
        for a, val in total_fusions.items():
            for combo in val:
                b = combo[0]
                c = combo[1]

                idx_B = cards_list.index(b)
                idx_C = cards_list.index(c)

                new_cards = [cards_list[i] for i in range(len(cards)) if i not in [idx_B, idx_C]]
                new_cards.append(a)
                # print("new_cards: " + str(new_cards))
                final_fusions.update(self.gen_fusions(new_cards))

        # print("final_fusions: " + str(final_fusions))
        # print("\n\n\t\t__________\ntotal_fusions: " + str(total_fusions))

        if not final_fusions:
            print("\n\tNo fusions detected\n")
        return final_fusions

    def clean_fusions(self, fusions_total):
        clean_fusions = {}
        for fusion in fusions_total:
            for k, v in fusion.items():
                b = v[0]
                c = v[1]
                if c not in clean_fusions:
                    clean_fusions[c] = (k, b)
        return [clean_fusions]

    def gen_all_possible_fusions(self, hand_in, fusions_total):

        if len(hand_in.cards) == 0:
            return hand_in.clean_fusions(fusions_total)

        # print(hand_in)
        current_card = hand_in.get_card_at_idx(0)
        current_fusions = hand_in.get_possible_fusion_results(current_card.id_num)
        new_fusions = []
        for k, v in current_fusions.items():
            if current_fusions[k]:
                new_fusions.append({k: (current_card.id_num, v)})
                hand_in.add_card(v)
        return fusions_total + hand_in.gen_all_possible_fusions(
            hand_in.hand_without(0),
            new_fusions
        )




    # # recursive function to detect fusion results by
    # # removing one card at a time and passing a list
    # # of found fusions.
    # # ISSUE: does not take into account that by removing
    # #        a card, detecting a fusion on the next call,
    # #        and not going back to see if the first card
    # #        can be used again.
    # def gen_all_possible_fusions(self, hand_in, fusions_total):
    #     if len(hand_in.cards) == 0:
    #         return hand_in.clean_fusions(fusions_total)
    #
    #     # print(hand_in)
    #     current_card = hand_in.get_card_at_idx(0)
    #     current_fusions = hand_in.get_possible_fusion_results(current_card.id_num)
    #     new_fusions = []
    #     for k, v in current_fusions.items():
    #         if current_fusions[k]:
    #             new_fusions.append({k: (current_card.id_num, v)})
    #             hand_in.add_card(v)
    #     return fusions_total + hand_in.gen_all_possible_fusions(
    #         hand_in.hand_without(0),
    #         new_fusions
    #     )
    #
    # def gen_all_possible_fusions_one_round(self):
    #     i = 0
    #     all_fusions = []
    #     for id_number, card in self.cards.items():
    #         left_over = self.hand_without(i)
    #         i += 1
    #         fusions = left_over.get_possible_fusion_results(id_number)
    #         all_fusions.append(fusions)
    #
    #     for f in all_fusions:
    #         print(f)
    #     return all_fusions


    ###
    #
    # Game logic
    #
    # - detect fusions
    # - detect equips
    #
    ###


    # Returns a dict of all cards in the hand as keys and the
    # values as the result of fusing each one with the given card
    def is_possible_fusion_with(self, target):
        if test_printing:
            print("Is " + str(self.deck.cards_dict[target]) + "\na good fusion partner?")
        # checking direct descendants
        for id_number, card in self.cards.items():
            possible_combo_ids = card.combo_card
            if target in possible_combo_ids:
                if test_printing:
                    print("- yes, it is a direct partner")
                return True

        # need to check if combining any of the cards in hand
        # will get to the target

        # gen fusion results for each possible combo
        # check new fusion results with remaining hand
        for i in range(len(self.cards)):
            new_hand = self.hand_without(i)
            if test_printing:
                print(new_hand)

        if test_printing:
            print("- no match found")
        return False

    # does this hand contain a combination of equippable cards
    # returns a dict of equip card to equipee if found, else None
    def holding_equip_combo(self):
        equip_combos = {}
        for id_n in self.cards:
            card = self.deck.cards_dict[id_n]
            equip_combos[id_n] = card.equip
        return equip_combos