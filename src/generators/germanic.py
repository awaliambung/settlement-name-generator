import random
from .base_generator import BaseGenerator
from data.germanic_elements import GERMANIC_PREFIXES, GERMANIC_MIDDLES, GERMANIC_SUFFIXES

class GermanicGenerator(BaseGenerator):
    
    def __init__(self):
        super().__init__()
        self._translation_table = {
            'aa': 'a', 'ee': 'e', 'oo': 'o', 'uu': 'u',
            'bb': 'b', 'dd': 'd', 'gg': 'g', 'kk': 'k',
            'll': 'l', 'mm': 'm', 'nn': 'n', 'pp': 'p',
            'rr': 'r', 'ss': 's', 'tt': 't',
            'ck': 'k', 'tz': 'z'
        }
        self.load_elements()
    
    def load_elements(self) -> None:
        self.prefixes = GERMANIC_PREFIXES
        self.middles = GERMANIC_MIDDLES
        self.suffixes = GERMANIC_SUFFIXES
    
    def generate_name(self) -> str:
        return self.generate_base_name()