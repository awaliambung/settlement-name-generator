from typing import List

class MenuHandler:
    
    @staticmethod
    def get_user_choice(prompt: str, valid_choices: List[str]) -> str:
        while True:
            try:
                choice = input(prompt).strip().lower()
                if choice in [c.lower() for c in valid_choices]:
                    return choice
                print("Invalid option. Please try again.")
            except (EOFError, KeyboardInterrupt):
                raise
    
    @staticmethod
    def get_filename_input(default_name: str = "settlement_names") -> str:
        try:
            filename = input(f"Enter filename (default: {default_name}): ").strip()
            return filename if filename else default_name
        except (EOFError, KeyboardInterrupt):
            return default_name
    
    @staticmethod
    def confirm_action(prompt: str, default_yes: bool = False) -> bool:
        suffix = " (Y/n): " if default_yes else " (y/N): "
        try:
            response = input(prompt + suffix).strip().lower()
            if not response:
                return default_yes
            return response in ['y', 'yes']
        except (EOFError, KeyboardInterrupt):
            return False