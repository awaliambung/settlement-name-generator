import random
from typing import Dict, List, Tuple
from generators.germanic import GermanicGenerator
from generators.romance import RomanceGenerator
from generators.celtic import CelticGenerator

class NameGeneratorService:
    def __init__(self) -> None:
        # Create generators when we need them
        self._generators = None
    
    def get_generators(self) -> Dict[str, object]:
        # Only create generators when first used
        if self._generators is None:
            self._generators = {
                'Germanic': GermanicGenerator(),
                'Romance': RomanceGenerator(),
                'Celtic': CelticGenerator()
            }
        return self._generators
    
    def generate_settlement_batch(self, active_generators: List[str], count: int = 10, use_randomised_roots: bool = False) -> List[Tuple[str, str]]:
        if not active_generators:
            return []
        
        generators = self.get_generators()
        names = []
        
        # Generate names one by one
        for _ in range(count):
            generator_type = random.choice(active_generators)
            generator = generators[generator_type]
            name = generator.generate_name(use_randomised_roots)
            names.append((name, generator_type))
        
        return names
    
    def generate_single_name(self, generator_type: str, use_randomised_roots: bool = False) -> str:
        generators = self.get_generators()
        
        if generator_type not in generators:
            raise ValueError(f"Don't know how to make {generator_type} names!")
        
        return generators[generator_type].generate_name(use_randomised_roots)