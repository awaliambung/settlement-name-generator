import random
import re
from .base_generator import BaseGenerator
from data.germanic_elements import GERMANIC_PREFIXES, GERMANIC_ROOTS, GERMANIC_SUFFIXES

class GermanicGenerator(BaseGenerator):
    def __init__(self) -> None:
        super().__init__()
        # Simple rules to make names sound better
        self._translation_table = {
            'aa': 'a', 'ee': 'e', 'oo': 'o', 'uu': 'u',
            'bb': 'b', 'dd': 'd', 'gg': 'g', 'kk': 'k',
            'll': 'l', 'mm': 'm', 'nn': 'n', 'pp': 'p',
            'rr': 'r', 'ss': 's', 'tt': 't',
            'ck': 'k', 'tz': 'z', 'th': 't', 'sch': 'sh'
        }
        self._setup_phonetic_system()
        self.load_elements()
        self._compile_translation_pattern()
    
    def _compile_translation_pattern(self) -> None:
        # Build the pattern to fix weird letter combinations
        pattern = '|'.join(re.escape(key) for key in self._translation_table.keys())
        self._translation_pattern = re.compile(pattern)
    
    def _setup_phonetic_system(self) -> None:
        # Letters that sound good in Germanic names
        self._vowels = ['a', 'e', 'i', 'o', 'u', 'ae', 'oe', 'ue', 'ei', 'au', 'eu']
        self._consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'z', 'th', 'sch', 'st', 'sp', 'sk']
        
        # Simple patterns for making roots
        self._syllable_patterns = [
            'CVC',    # like "berg"
            'CVCC',   # like "burg"
            'CCV',    # like "stra"
            'CCVC',   # like "stein"
            'VC',     # like "ing"
            'VCC',    # like "ald"
            'CV',     # like "wa"
            'CVCV'    # like "hagen"
        ]
    
    def load_elements(self) -> None:
        self.prefixes = GERMANIC_PREFIXES
        self.roots = GERMANIC_ROOTS
        self.suffixes = GERMANIC_SUFFIXES
    
    def generate_name(self, use_randomised_roots: bool = False) -> str:
        return self.generate_base_name(use_randomised_roots)