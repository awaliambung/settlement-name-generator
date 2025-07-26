import random
import re
from abc import ABC, abstractmethod
from typing import List

class BaseGenerator(ABC):
    def __init__(self) -> None:
        self.prefixes: List[str] = []
        self.roots: List[str] = []
        self.suffixes: List[str] = []
        self._translation_table: dict = {}
        self._translation_pattern = None
        self._vowels: List[str] = []
        self._consonants: List[str] = []
        self._syllable_patterns: List[str] = []
    
    @abstractmethod
    def load_elements(self) -> None:
        pass
    
    @abstractmethod
    def generate_name(self, use_randomised_roots: bool = False) -> str:
        pass
    
    @abstractmethod
    def _setup_phonetic_system(self) -> None:
        pass
    
    def generate_names(self, count: int = 1, use_randomised_roots: bool = False) -> List[str]:
        # Simple loop instead of list comprehension for clarity
        names = []
        for _ in range(count):
            names.append(self.generate_name(use_randomised_roots))
        return names
    
    def combine_elements(self, *elements: str) -> str:
        combined = ''.join(elements)
        
        # Clean up double letters and weird combinations
        if self._translation_pattern:
            combined = self._translation_pattern.sub(
                lambda match: self._translation_table[match.group(0)], 
                combined
            )
        
        return combined.capitalize()
    
    def generate_randomised_root(self) -> str:
        if not self._syllable_patterns:
            return ""
        
        pattern = random.choice(self._syllable_patterns)
        root = ""
        
        # Build the root letter by letter
        for char in pattern:
            if char == 'V':  # Add a vowel
                root += random.choice(self._vowels)
            elif char == 'C':  # Add a consonant
                root += random.choice(self._consonants)
            else:
                root += char
        
        # Make it sound better
        if self._translation_pattern:
            root = self._translation_pattern.sub(
                lambda match: self._translation_table[match.group(0)], 
                root
            )
        
        return root
    
    def generate_base_name(self, use_randomised_roots: bool = False) -> str:
        prefix = random.choice(self.prefixes)
        suffix = random.choice(self.suffixes)
        
        # Sometimes add a middle part
        if random.random() < 0.5:
            if use_randomised_roots:
                root = self.generate_randomised_root()
            else:
                root = random.choice(self.roots) if self.roots else ""
            
            if root:
                return self.combine_elements(prefix, root, suffix)
        
        return self.combine_elements(prefix, suffix)