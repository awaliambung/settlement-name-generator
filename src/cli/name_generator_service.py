import random
from typing import Dict, List, Optional, Tuple
from generators.germanic import GermanicGenerator
from generators.romance import RomanceGenerator
from generators.celtic import CelticGenerator

class NameGeneratorService:
    def __init__(self):
        self._generators: Optional[Dict] = None
    
    @property
    def generators(self) -> Dict:
        # Lazy-loaded generators for better startup performance
        if self._generators is None:
            self._generators = {
                'Germanic': GermanicGenerator(),
                'Romance': RomanceGenerator(),
                'Celtic': CelticGenerator()
            }
        return self._generators
    
    def generate_settlement_batch(self, active_generators: List[str], count: int = 10) -> List[Tuple[str, str]]:
        if not active_generators:
            return []
        
        generated_names = []
        for _ in range(count):
            selected_type = random.choice(active_generators)
            generator = self.generators[selected_type]
            name = generator.generate_name()
            generated_names.append((name, selected_type))
        
        return generated_names
    
    def generate_single_name(self, generator_type: str) -> str:
        if generator_type not in self.generators:
            raise ValueError(f"Unknown generator type: {generator_type}")
        
        return self.generators[generator_type].generate_name()