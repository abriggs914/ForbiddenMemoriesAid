import json

from Card import CardMaker,card_types
from Hand import HandMaker
from Deck import Deck

# contains all cards separated by type, cost, and card number.
passwords_file = open("passwords.txt").read()

# contains all cards including all possible combinations
combinations_file = open("combinations.txt").read()

# contains all cards in a json structure including descriptions
cards_json_file = open("cards_JSON.json").read()

test_printing = True



# class to parse the passwords.txt file, pulling all cards and
# attributes, separated by type and card number.
class Parser:

    def __init__(self):
        self.card_types = {}
        self.sections = None
        self.type_section = {}
        self.deck = None
        self.populate_dict()
        self.hand_maker = HandMaker(self.deck)

    def __repr__(self):
        return "REPR"

    # determines if a given string is a valid id number
    def valid_num(self, num_in):
        if len(str(num_in)) == 0:
            return False
        for letter in str(num_in):
            val = ord(letter)
            if not ((47 < val < 58) or val == ord(" ")):
                return False
        return True

    # given the line number and the list of cards in raw-form,
    # collects the appropriate information and returns the
    # attributes in a list: (id, name, atk, def, password, cost)
    def collect_info(self, id_num, line_lst):
        atk_def = line_lst[39: 49]
        atk_def_s = atk_def.split("/")

        name = line_lst[:37].strip()
        atk = atk_def_s[0].strip()
        defen = atk_def_s[1].strip()
        password = line_lst[51: 59].strip()
        cost = line_lst[60: 71].strip()

        if not atk:
            atk = 0
        if not defen:
            defen = 0

        return [int(id_num),
                name,
                int(atk),
                int(defen),
                int(password),
                int(cost)]

    # traverses the raw data list, line by line and determines appropriate
    # sections based on file conventions. Creates a list of sections
    # and it's associated list indices.
    def sectionify(self, lst):
        divider = "======================================================================"
        sections = []
        i = 0
        while i < len(lst):
            line = lst[i]
            if divider in line:
                header = lst[i + 1]
                i += 1
                line = lst[i]
                section = []
                i += 2
                while divider not in line and i < len(lst):
                    line = lst[i]
                    section.append(i)
                    i += 1
                sections.append([[header], section])
                i -= 2
            i += 1
        # for j in sections:
        #     print(j)
        return sections

    # used in conjunction with sectionify to populate a dictionary with
    # a key for each card type, and the following card id numbers of that type.
    def populate_types(self, lst):
        for section in self.sections:
            title = section[0][0]
            pages = section[1]
            # print("section: " + str(title))
            type_line = "type"
            separator_line = "----------------------------------------------------------------------"
            separator_token = "-"
            header_line = "no  title"
            if type_line in title.lower():
                first = pages[0]
                last = pages[-1]
                i = first
                curr_type = None
                while i != last:
                    entry = lst[i]
                    if entry and separator_line not in entry:
                        length = len(entry)
                        if length < 67 and separator_token not in entry:
                            self.type_section[entry] = []
                            curr_type = entry
                        elif header_line not in entry.lower():
                            entry_num = entry[:4].strip()
                            if self.valid_num(entry_num):
                                # print("entry("+str(len(entry_num))+"): " + entry_num)
                                self.type_section[curr_type].append(int(entry_num))
                    i += 1
        # print(self.type_section)

    # takes in the opened file object and initializes the sections list and type
    # dictionary before creating and storing card objects in a dictionary by id number.
    # returns a deck object containing all information collected
    def parse_passwords(self):
        file_lst = str(passwords_file).split("\n")
        valid_ids = {}
        self.sections = self.sectionify(file_lst)
        self.populate_types(file_lst)
        sorted_section_found = False
        for line in file_lst:
            id_num = line[:4]
            rest_line = line[4:]
            sorted_section = "Reference sorted by CARD NUMBER"
            # print(line)
            if sorted_section in rest_line or sorted_section_found:
                sorted_section_found = True
                card_maker = CardMaker(self)
                if self.valid_num(id_num):
                    if id_num not in valid_ids:
                        # print("ID: " + str(id_num) + ", rest("+str(len(rest_line))+"): " + str(rest_line))
                        attributes = self.collect_info(id_num, rest_line)
                        valid_ids[int(id_num)] = card_maker.new_card(attributes)

        self.deck = Deck(valid_ids, self.type_section)

    def parse_combinations(self):
        separator = "-------------------------------------------------------------------------------"
        entries_split = combinations_file.split(separator)
        for e in entries_split:
            entries = [line for line in e.split("\n") if line]
            if entries:
                entry = e.strip()
                master_card_id = int(entries[0][:4].strip())
                rest_entries = [val for val in entries[0].strip().split(" ") if val]
                combo_cards = []
                result_cards = []
                master_card = self.deck.cards_dict[master_card_id]
                if len(rest_entries) > 7:
                    type_1 = rest_entries[-7]
                    type_2 = rest_entries[-6]
                    star_cost = rest_entries[-5]
                    sym_1 = rest_entries[-2]
                    sym_2 = rest_entries[-1]
                    # print("type_1: " + str(type_1) + ", type_2: " + str(type_2) + ", star_cost: " + str(star_cost) + ", sym_1: " + str(sym_1) + ", sym_2: " + str(sym_2))
                    master_card.type_attr = type_1
                    master_card.sym_attr = type_2
                    master_card.star_cost = star_cost
                    master_card.sym_1 = sym_1
                    master_card.sym_2 = sym_2
                for j in range(1, len(entries), 2):
                    combo_card_id = int(entries[j][2: 5].strip())
                    result_card_id = int(entries[j + 1][2: 5].strip())
                    combo_cards.append(combo_card_id)
                    result_cards.append(result_card_id)

                self.deck.cards_dict[master_card_id].combo_card = combo_cards
                self.deck.cards_dict[master_card_id].results_card = result_cards

    def parse_json(self):
        cards_json = json.loads(cards_json_file)
        cards = [card for card in cards_json]
        card_maker = CardMaker(self)
        for card in cards:
            name = card["Name"]
            description = card["Description"]
            id_num = card["Id"]
            guardian_star_A = card["GuardianStarA"]
            guardian_star_B = card["GuardianStarB"]
            level = card["Level"]
            type_attr = card["Type"]
            attack = card["Attack"]
            defense = card["Defense"]
            stars = card["Stars"]
            card_code = card["CardCode"]
            equip = card["Equip"]
            fusions = card["Fusions"]
            ritual = card["Ritual"]
            attribute = card["Attribute"]
            name_color = card["NameColor"]
            desc_color = card["DescColor"]

            # (id, name, atk, def , password, cost)
            # attrs = [id_num, name, attack, defense, card_code, stars]
            rest_attrs = [description, guardian_star_A, guardian_star_B, level, type_attr, equip, fusions, ritual, attribute, name_color, desc_color]

            card_obj = self.deck.cards_dict[id_num]
            # card_obj = card_maker.new_card(attrs)
            card_obj.init_attrs(rest_attrs)


    def repr_cards(self, cards):
        if type(cards) != list:
            cards = [cards]

        result = ""
        for card in cards:
            result += str(self.deck.cards_dict[card]) + "\n"

        return result

    def populate_dict(self):
        self.parse_passwords()
        self.parse_combinations()
        self.parse_json()
        self.deck.init_appendix()
