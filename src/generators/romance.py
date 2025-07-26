import random
from .base_generator import BaseGenerator
from data.romance_elements import ROMANCE_PREFIXES, ROMANCE_ROOTS, ROMANCE_SUFFIXES

class RomanceGenerator(BaseGenerator):
    
    def __init__(self):
        super().__init__()
        self._translation_table = {
            'ii': 'i', 'uu': 'u', 'aa': 'a', 'ee': 'e', 'oo': 'o',
            'bb': 'b', 'cc': 'c', 'dd': 'd', 'ff': 'f', 'gg': 'g',
            'll': 'l', 'mm': 'm', 'nn': 'n', 'pp': 'p', 'rr': 'r',
            'ss': 's', 'tt': 't', 'qu': 'c', 'ph': 'f', 'th': 't'
        }
        self.load_elements()
    
    def load_elements(self) -> None:
        self.prefixes = ROMANCE_PREFIXES
        self.roots = ROMANCE_ROOTS
        self.suffixes = ROMANCE_SUFFIXES
    
    def generate_name(self) -> str:
        return self.generate_base_name()