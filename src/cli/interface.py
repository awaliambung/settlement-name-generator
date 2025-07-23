import os
from typing import Dict, List, Optional
from generators.germanic import GermanicGenerator
from generators.romance import RomanceGenerator
from generators.celtic import CelticGenerator
from cli.menu_handler import MenuHandler
from cli.name_generator_service import NameGeneratorService
from cli.file_service import FileService
from config.settings import GeneratorSettings

class SettlementCLI:
    def __init__(self):
        self.settings = GeneratorSettings(
            enabled_generators={
                'Germanic': False,
                'Romance': False,
                'Celtic': False
            }
        )
        self.name_service = NameGeneratorService()
        self.file_service = FileService()
        self.menu_handler = MenuHandler()
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        print()
        print("░█▀▀░█▀▀░▀█▀░▀█▀░█░░░█▀▀░█▄█░█▀▀░█▀█░▀█▀░░░█▀▀░█▀▀░█▀█░█▀▀░█▀▄░█▀█░▀█▀░█▀█░█▀▄")
        print("░▀▀█░█▀▀░░█░░░█░░█░░░█▀▀░█░█░█▀▀░█░█░░█░░░░█░█░█▀▀░█░█░█▀▀░█▀▄░█▀█░░█░░█░█░█▀▄")
        print("░▀▀▀░▀▀▀░░▀░░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░▀░░░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀░░▀░░▀▀▀░▀░▀")
        print()
    
    def display_main_menu(self):
        print("MAIN MENU")
        print()
        print("1. Generate Settlement Names")
        print("2. Settings")
        print("3. Exit")
        print()
    
    def display_settings_menu(self):
        print("SETTINGS")
        print()
        for i, (name, enabled) in enumerate(self.settings.enabled_generators.items(), 1):
            status = "x" if enabled else " "
            print(f"{i}. [{status}] {name}")
        print()
        print("4. Back to Main Menu")
        print()
    
    def handle_settings(self):
        while True:
            self.clear_screen()
            self.display_header()
            self.display_settings_menu()
            
            try:
                choice = self.menu_handler.get_user_choice(
                    "Select option (1-4): ", 
                    ['1', '2', '3', '4']
                )
                
                if choice in ['1', '2', '3']:
                    generator_names = list(self.settings.enabled_generators.keys())
                    selected_generator = generator_names[int(choice) - 1]
                    self.settings.enabled_generators[selected_generator] = not self.settings.enabled_generators[selected_generator]
                elif choice == '4':
                    break
            except KeyboardInterrupt:
                break
    
    def generate_settlements(self):
        active_generators = self.settings.get_active_generators()
        
        if not active_generators:
            print()
            print("No language groups selected! Please configure settings first.")
            print()
            input("Press Enter to continue...")
            return
        
        while True:
            self.clear_screen()
            self.display_header()
            
            generated_names = self.name_service.generate_settlement_batch(
                active_generators, 
                self.settings.max_settlements
            )
            
            self._display_generated_names(generated_names)
            
            if not self._handle_post_generation_menu(generated_names):
                break
    
    def _display_generated_names(self, names: List[tuple]):
        print("Generated Names:")
        print()
        
        for i, (name, generator_type) in enumerate(names, 1):
            print(f"{i:2d}. {name:<20} ({generator_type})")
        print()
    
    def _handle_post_generation_menu(self, generated_names: List[tuple]) -> bool:
        while True:
            try:
                choice = self.menu_handler.get_user_choice(
                    "Options: (G)enerate new, (E)xport, (B)ack to menu: ",
                    ['g', 'generate', 'e', 'export', 'b', 'back', '']
                )
                
                if choice.lower() in ['g', 'generate', '']:
                    return True
                elif choice.lower() in ['e', 'export']:
                    formatted_names = [f"{name} ({gen_type})" for name, gen_type in generated_names]
                    self.file_service.export_names(formatted_names)
                    return False
                elif choice.lower() in ['b', 'back']:
                    return False
            except KeyboardInterrupt:
                return False
    
    def run(self):
        while True:
            self.clear_screen()
            self.display_header()
            self.display_main_menu()
            
            try:
                choice = self.menu_handler.get_user_choice(
                    "Select option (1-3): ", 
                    ['1', '2', '3']
                )
                
                if choice == '1':
                    self.generate_settlements()
                elif choice == '2':
                    self.handle_settings()
                elif choice == '3':
                    print()
                    print("Goodbye!")
                    print()
                    break
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break