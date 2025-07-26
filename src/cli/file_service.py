import os
from datetime import datetime
from typing import List
from cli.menu_handler import MenuHandler

class FileService:
    def __init__(self) -> None:
        self.menu_handler = MenuHandler()
    
    def export_names(self, names: List[str], custom_filename: str = None) -> bool:
        try:
            # Get filename
            if custom_filename:
                filename = custom_filename
            else:
                filename = self.menu_handler.get_filename_input()
            
            # Add .txt if missing
            if not filename.endswith('.txt'):
                filename = f"{filename}.txt"
            
            # Check if file exists
            if os.path.exists(filename):
                if not self.menu_handler.confirm_action(f"File '{filename}' exists. Overwrite?"):
                    print("Export cancelled.")
                    input("Press Enter to continue...")
                    return False
            
            # Write the file
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                for i, name in enumerate(names, 1):
                    file.write(f"{i:2d}. {name}\n")
            
            print(f"\nNames exported to '{filename}' successfully!")
            print(f"Total names exported: {len(names)}")
            print()
            input("Press Enter to continue...")
            return True
            
        except Exception as error:
            print(f"\nError exporting file: {error}")
            print()
            input("Press Enter to continue...")
            return False
    
    def get_export_directory(self) -> str:
        return os.getcwd()