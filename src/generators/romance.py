import random
import re
from .base_generator import BaseGenerator
from data.romance_elements import ROMANCE_PREFIXES, ROMANCE_ROOTS, ROMANCE_SUFFIXES

class RomanceGenerator(BaseGenerator):
    def __init__(self) -> None:
        super().__init__()
        # Latin-style cleanup rules
        self._translation_table = {
            'ii': 'i', 'uu': 'u', 'aa': 'a', 'ee': 'e', 'oo': 'o',
            'bb': 'b', 'cc': 'c', 'dd': 'd', 'ff': 'f', 'gg': 'g',
            'll': 'l', 'mm': 'm', 'nn': 'n', 'pp': 'p', 'rr': 'r',
            'ss': 's', 'tt': 't', 'qu': 'c', 'ph': 'f', 'th': 't'
        }
        self._setup_phonetic_system()
        self.load_elements()
        self._compile_translation_pattern()
    
    def _compile_translation_pattern(self) -> None:
        pattern = '|'.join(re.escape(key) for key in self._translation_table.keys())
        self._translation_pattern = re.compile(pattern)
    
    def _setup_phonetic_system(self) -> None:
        # Romance language sounds
        self._vowels = ['a', 'e', 'i', 'o', 'u', 'ae', 'au', 'eu', 'ou']
        self._consonants = ['b', 'c', 'd', 'f', 'g', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'qu', 'ch', 'sc', 'st', 'sp', 'cr', 'br', 'tr', 'pr']
        
        # Romance patterns
        self._syllable_patterns = [
            'CV',     # like "la"
            'CVC',    # like "val"
            'CVCV',   # like "villa"
            'CCV',    # like "bra"
            'CCVC',   # like "grand"
            'VC',     # like "ac"
            'VCV',    # like "ava"
            'VCVC'    # like "aqua"
        ]
    
    def load_elements(self) -> None:
        self.prefixes = ROMANCE_PREFIXES
        self.roots = ROMANCE_ROOTS
        self.suffixes = ROMANCE_SUFFIXES
    
    def generate_name(self, use_randomised_roots: bool = False) -> str:
        return self.generate_base_name(use_randomised_roots)