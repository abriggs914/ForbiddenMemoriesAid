from Card import card_types

test_printing = True

class Deck:

    def __init__(self, cards, types_section):
        self.cards_dict = cards
        self.num_cards = len(list(cards.keys()))
        self.types_section = types_section
        # print(self.types_section)
        self.appendix = None

    def __repr__(self):
        res = ""
        for id_n, card in self.cards_dict.items():
            res += str(card) + "\n"
        return res

    def init_appendix(self):
        list_of_names = []
        list_of_types = []
        list_of_ss = []
        atk_range = [0, 0]
        def_range = [0, 0]
        n_monsters = 0
        n_magics = 0
        n_equips = 0
        n_rituals = 0
        n_traps = 0
        for id_num, card in self.cards_dict.items():
            name = card.name
            type_idx = card.type_attribute
            type_name = card_types[type_idx]
            ss1 = card.sym_1
            ss2 = card.sym_2
            atk = card.atk
            defen = card.defen

            list_of_names.append(name)

            if type_name not in list_of_types:
                list_of_types.append(type_name)

            if type_idx == card_types.index("Trap"):
                n_traps += 1
            elif type_idx == card_types.index("Magic"):
                n_magics += 1
            elif type_idx == card_types.index("Equip"):
                n_equips += 1
            elif type_idx == card_types.index("Ritual"):
                n_rituals += 1
            else:
                n_monsters += 1

                if ss1 and ss1 not in list_of_ss:
                    list_of_ss.append(ss1)

                if ss2 and ss2 not in list_of_ss:
                    list_of_ss.append(ss2)

                if atk < atk_range[0]:
                    atk_range[0] = atk

                if atk > atk_range[1]:
                    atk_range[1] = atk

                if defen < def_range[0]:
                    def_range[0] = defen

                if defen > def_range[1]:
                    def_range[1] = defen

        keys = [
            "names",
            "types",
            "star_signs",
            "atk_range",
            "def_range",
            "n_monster",
            "n_magic",
            "n_equips",
            "n_rituals",
            "n_trap"
        ]
        vals = [
            list_of_names,
            list_of_types,
            list_of_ss,
            atk_range,
            def_range,
            n_monsters,
            n_magics,
            n_equips,
            n_rituals,
            n_traps
        ]
        self.appendix = dict(zip(keys, vals))
        print(self.appendix)


    ###
    #
    # Searching
    #
    # - by type
    # - by attack
    # - by defense
    #
    ###


    # return a list of all cards with the given type
    def get_all_of_type(self, type_in):
        if type_in in self.types_section:
            return [card for id_num, card in self.cards_dict.items() if id_num in self.types_section[type_in]]

    # return a list of all cards with the specified attack points +/- the
    # window value. Can also signify if exact matches are desired or if
    # cards less-than or greater-than are included
    # Can add a list of types as indices to card_types, to exclude from search
    # ex. get_all_of_atk(1500, 100) -> all cards with 1400 -> 1600 atk
    # ex. get_all_of_atk(1500, 100, False, False, True) -> all cards with 1400 -> 1600 atk
    # ex. get_all_of_atk(1500, 0, False, True, True) -> all cards with 0 -> 1500 atk
    def get_all_of_atk(self, atk, window=0, exact=True, widen=False, upTo=True, exclude=[]):
        bottom = 0
        lower = int(max(0, atk - window))
        upper = int(atk + window)
        top = 9999
        results = [card for id_num, card in self.cards_dict.items()]

        if exclude:
            results = [card for card in results if card.type_attribute not in exclude]
        # bottom <= lower <= exact <= upper <= top
        if exact:
            # only makes use of the window
            results = [card for card in results if lower <= card.atk <= upper]
        else:
            if not widen:
                bottom = lower
                top = upper

            # bottom -> exact -> upper
            if upTo:
                results = [card for card in results if bottom <= card.atk <= upper]
            # lower -> exact -> top
            else:
                results = [card for card in results if lower <= card.atk <= top]

        return [card.id_num for card in results]

    # return a list of all cards with the specified defense points +/- the
    # window value. Can also signify if exact matches are desired or if
    # cards less-than or greater-than are included
    # ex. get_all_of_atk(1500, 100) -> all cards with 1400 -> 1600 def
    # ex. get_all_of_atk(1500, 100, False, False, True) -> all cards with 1400 -> 1600 def
    # ex. get_all_of_atk(1500, 0, False, True, True) -> all cards with 0 -> 1500 def
    def get_all_of_def(self, defen, window=0, exact=True, widen=False, upTo=True, exclude=[]):
        bottom = 0
        lower = int(max(0, defen - window))
        upper = int(defen + window)
        top = 9999
        results = [card for id_num, card in self.cards_dict.items()]

        if exclude:
            results = [card for card in results if card.type_attribute not in exclude]

        # bottom <= lower <= exact <= upper <= top
        if exact:
            # only makes use of the window
            results = [card for card in results if lower <= card.defen <= upper]
        else:
            if not widen:
                bottom = lower
                top = upper

            # bottom -> exact -> upper
            if upTo:
                results = [card for card in results if bottom <= card.defen <= upper]
            # lower -> exact -> top
            else:
                results = [card for card in results if lower <= card.defen <= top]

        return [card.id_num for card in results]

        # return [card for id_num, card in self.cards_dict.items()
        #         if exact if upTo
        #             if card.atk ==]

