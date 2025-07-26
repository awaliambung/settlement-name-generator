import random
import re
from .base_generator import BaseGenerator
from data.celtic_elements import CELTIC_PREFIXES, CELTIC_ROOTS, CELTIC_SUFFIXES

class CelticGenerator(BaseGenerator):
    def __init__(self) -> None:
        super().__init__()
        # Rules to make Celtic names sound right
        self._translation_table = {
            'dd': 'd', 'll': 'l', 'nn': 'n', 'rr': 'r', 'ss': 's', 'tt': 't',
            'ff': 'f', 'gg': 'g', 'bb': 'b', 'cc': 'c', 'mm': 'm', 'pp': 'p',
            'aa': 'a', 'ee': 'e', 'ii': 'i', 'oo': 'o', 'uu': 'u',
            'wy': 'w', 'yr': 'y', 'gh': 'g', 'ch': 'k'
        }
        self._setup_phonetic_system()
        self.load_elements()
        self._compile_translation_pattern()
    
    def _compile_translation_pattern(self) -> None:
        pattern = '|'.join(re.escape(key) for key in self._translation_table.keys())
        self._translation_pattern = re.compile(pattern)
    
    def _setup_phonetic_system(self) -> None:
        # Celtic sounds including Welsh and Gaelic
        self._vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'w', 'ae', 'ai', 'au', 'aw', 'ey', 'wy']
        self._consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'ch', 'th', 'dh', 'gh', 'll', 'rh', 'ff', 'dd']
        
        # Celtic name patterns
        self._syllable_patterns = [
            'CVC',    # like "pen"
            'CVCC',   # like "gwyn"
            'CCV',    # like "gla"
            'CCVC',   # like "glan"
            'VC',     # like "ar"
            'VCC',    # like "ard"
            'CV',     # like "ca"
            'CVCV',   # like "cara"
            'CCVCV'   # like "bryna"
        ]
    
    def load_elements(self) -> None:
        self.prefixes = CELTIC_PREFIXES
        self.roots = CELTIC_ROOTS
        self.suffixes = CELTIC_SUFFIXES
    
    def generate_name(self, use_randomised_roots: bool = False) -> str:
        return self.generate_base_name(use_randomised_roots)