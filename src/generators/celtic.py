import random
from .base_generator import BaseGenerator
from data.celtic_elements import CELTIC_PREFIXES, CELTIC_MIDDLES, CELTIC_SUFFIXES

class CelticGenerator(BaseGenerator):
    
    def __init__(self):
        super().__init__()
        self._translation_table = {
            'dd': 'd', 'll': 'l', 'nn': 'n', 'rr': 'r', 'ss': 's', 'tt': 't',
            'ff': 'f', 'gg': 'g', 'bb': 'b', 'cc': 'c', 'mm': 'm', 'pp': 'p',
            'aa': 'a', 'ee': 'e', 'ii': 'i', 'oo': 'o', 'uu': 'u',
            'wy': 'w', 'yr': 'y'
        }
        self.load_elements()
    
    def load_elements(self) -> None:
        self.prefixes = CELTIC_PREFIXES
        self.middles = CELTIC_MIDDLES
        self.suffixes = CELTIC_SUFFIXES
    
    def generate_name(self) -> str:
        return self.generate_base_name()