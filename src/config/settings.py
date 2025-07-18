from dataclasses import dataclass
from typing import Dict, List

@dataclass
class GeneratorSettings:
    enabled_generators: Dict[str, bool]
    max_settlements: int = 10
    
    def get_active_generators(self) -> List[str]:
        return [name for name, enabled in self.enabled_generators.items() if enabled]
    
    def toggle_generator(self, generator_name: str) -> bool:
        if generator_name in self.enabled_generators:
            self.enabled_generators[generator_name] = not self.enabled_generators[generator_name]
            return self.enabled_generators[generator_name]
        return False
    
    def enable_all_generators(self):
        for key in self.enabled_generators:
            self.enabled_generators[key] = True
    
    def disable_all_generators(self):
        for key in self.enabled_generators:
            self.enabled_generators[key] = False
    
    @property
    def has_active_generators(self) -> bool:
        return any(self.enabled_generators.values())