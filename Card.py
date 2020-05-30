test_printing = True

# star_signs
star_circle_1 = ["V", "Me", "Su", "Mo"]
star_circle_2 = ["U", "P", "N", "Ma", "J", "Sa"]

card_types = [
    "Dragon",
    "Spellcaster",
    "Zombie",
    "Warrior",
    "Beast-Warrior",
    "Beast",
    "Winged Beast",
    "Fiend",
    "Fairy",
    "Insect",
    "Dinosaur",
    "Reptile",
    "Fish",
    "Sea Serpent",
    "Machine",
    "Thunder",
    "Aqua",
    "Pyro",
    "Rock",
    "Plant",
    "Magic",  # 20
    "Trap",
    "Ritual",
    "Equip",
]

star_names = [
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Pluto",
    "Neptune",
    "Mercury",
    "Sun",
    "Moon",
    "Venus",
]


class Card:

    def __init__(self, id_num, name, atk, defen, password, cost):

        self.id_num = id_num  # id number / int
        self.name = name  # name / string
        self.atk = atk  # attack power / int
        self.defen = defen  # defense power / int
        self.password = password  # unlock password / int
        self.cost = cost  # star chip cost / int
        self.card_type = None  # card type / string
        self.combo_card = []  # list of combo partners / list(int)
        self.results_card = []  # list of result fusions / list(int) same size of combo_card and uses match index lookup
        self.sym_attr = None  # the currently set star sign / string
        self.sym_1 = None  # star sign 1 / string
        self.sym_2 = None  # star sign 2 / string
        self.is_sym_1 = None  # whether sym 1 is set or not / bool

        self.description = None  # card description / string
        self.guardian_star_A = None  # star sign 1 / int
        self.guardian_star_B = None  # star sign 2 / int
        self.level = None  # star level / int
        self.type_attribute = None  # card type from card_type list / int
        self.equip = None  # possible cards this can be equipped to / list(int) OR None
        self.fusions = None  # possible cards this can be fused with / list(int)
        self.ritual = None  # possible cards this can be used in ritual with / list(int) OR None
        self.attribute = None  # card attribute value é int
        self.name_color = None  # name color / int
        self.desc_color = None  # description color / int

    def init_attrs(self, attrs):

        self.description = attrs[0]
        self.guardian_star_A = attrs[1]
        self.guardian_star_B = attrs[2]
        self.level = attrs[3]
        self.type_attribute = attrs[4]
        self.equip = attrs[5]
        self.fusions = attrs[6]
        self.ritual = attrs[7]
        self.attribute = attrs[8]
        self.name_color = attrs[9]
        self.desc_color = attrs[10]

    # This card can fuse with another card
    def is_fusable(self):
        return len(self.combo_card) > 0

    # This card can fuse with the given card
    def is_fusable_with(self, target):
        return target in self.combo_card

    # This card can be used to make given card
    def is_fusable_to(self, target):
        return target in self.results_card

    # Set the star_sign of this card and compute the bonus of
    # challenging the given star sign
    def star_sign(self, is_sym_1, sym_2_in=None):
        self.is_sym_1 = is_sym_1
        ss = self.sym_1 if is_sym_1 else self.sym_2
        s_ss_idx_1 = -1 if ss not in star_circle_1 else star_circle_1.index(ss)
        s_ss_idx_2 = -1 if ss not in star_circle_2 else star_circle_2.index(ss)
        n_ss_idx_1 = -1 if sym_2_in not in star_circle_1 else star_circle_1.index(sym_2_in)
        n_ss_idx_2 = -1 if sym_2_in not in star_circle_2 else star_circle_2.index(sym_2_in)
        same_circle = False
        adjacent = False
        cirle_1 = False
        cirle_2 = False
        l_1 = len(star_circle_1)
        l_2 = len(star_circle_2)
        if s_ss_idx_1 >= 0:
            if n_ss_idx_1 >= 0:
                cirle_1 = True
                same_circle = True
                if (s_ss_idx_1 + 1) % l_1 == n_ss_idx_1 or (s_ss_idx_1 - 1) % l_1 == n_ss_idx_1:
                    adjacent = True
        if s_ss_idx_2 >= 0:
            if n_ss_idx_2 >= 0:
                cirle_2 = True
                same_circle = True
                if (s_ss_idx_2 + 1) % l_2 == n_ss_idx_2 or (s_ss_idx_2 - 1) % l_2 == n_ss_idx_2:
                    adjacent = True

        bonus = 0
        if same_circle:
            if adjacent:
                if cirle_1:
                    if s_ss_idx_1 < n_ss_idx_1:
                        bonus = 500
                    elif s_ss_idx_1 > n_ss_idx_1:
                        bonus = -500
                else:
                    if s_ss_idx_2 < n_ss_idx_2:
                        bonus = 500
                    elif s_ss_idx_2 > n_ss_idx_2:
                        bonus = -500
        if test_printing:
            print(str(self) + "\n against star_sign: " + str(sym_2_in) + " has a bonus of: " + str(bonus))
        return bonus

    def get_full_print(self):
        star_sign = None
        if self.is_sym_1 is not None:
            if self.is_sym_1:
                star_sign = self.sym_1
            else:
                star_sign = self.sym_2
        return str(self.id_num) \
               + ", " \
               + str(self.name) \
               + ", " \
               + str(self.card_type) \
               + ", (" + str(self.atk) \
               + "/" \
               + str(self.defen) \
               + "), " \
               + str(self.password) \
               + ", " \
               + str(self.cost) \
               + ", SS: (" + str(self.sym_1) + "/" + str(self.sym_2) \
               + "), In: " + str(star_sign) \
               + "\n\t\t\tcombos: " \
               + str(self.combo_card) \
               + "\n\t\t\tresults: " \
               + str(self.results_card) \
               + "\n\t\t\tDescription:\n[\n" \
               + str(self.description) + "\n]\n" \

    def __repr__(self):
        # return self.get_full_print()
        return "ID: " + str(self.id_num) + ", " + str(self.name)\
               + ", A/D: (" + str(self.atk) + "/" + str(self.defen) + ")"

class CardMaker:

    def __init__(self, parser):
        self.parser = parser

    def __repr__(self):
        return "CardMaker"

    # creates a new card object initializing name,
    # atk & def points, password & starchip cost,
    # and card type.
    def new_card(self, attrs):
        id_num = attrs[0]
        name = attrs[1]
        atk = attrs[2]
        defen = attrs[3]
        password = attrs[4]
        cost = attrs[5]
        card = Card(id_num, name, atk, defen, password, cost)
        card.card_type = self.what_type(card)
        return card

    # determines the type of a given card object from the
    # parser type-section dictionary
    def what_type(self, card):
        for type_name, members in self.parser.type_section.items():
            for n in members:
                if n > card.id_num:
                    continue
                if n == card.id_num:
                    return type_name
        return None
