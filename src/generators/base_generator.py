import random
import re
from abc import ABC, abstractmethod
from typing import List

class BaseGenerator(ABC):
    __slots__ = ['prefixes', 'roots', 'suffixes', '_phonetic_rules', '_translation_table', '_translation_pattern']
    
    def __init__(self):
        self.prefixes = []
        self.roots = []
        self.suffixes = []
        self._phonetic_rules = {}
    
    @abstractmethod
    def load_elements(self) -> None:
        pass
    
    @abstractmethod
    def generate_name(self) -> str:
        pass
    
    def generate_names(self, count: int = 1) -> List[str]:
        return [self.generate_name() for _ in range(count)]
    
    def combine_elements(self, *elements) -> str:
        combined = ''.join(elements)
        
        # Apply phonetic rules using compiled regex pattern
        if hasattr(self, '_translation_pattern'):
            combined = self._translation_pattern.sub(
                lambda m: self._translation_table[m.group(0)], combined
            )
        
        return combined.capitalize()
    
    def __init__(self):
        if hasattr(self, '_translation_table'):
            pattern = '|'.join(re.escape(key) for key in self._translation_table.keys())
            self._translation_pattern = re.compile(pattern)
    
    def generate_base_name(self) -> str:
        prefix = random.choice(self.prefixes)
        suffix = random.choice(self.suffixes)
        
        if random.random() < 0.5 and self.roots:
            root = random.choice(self.roots)
            return self.combine_elements(prefix, root, suffix)
        else:
            return self.combine_elements(prefix, suffix)