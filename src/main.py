#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cli.interface import SettlementCLI

def main():
    try:
        cli = SettlementCLI()
        cli.run()
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except ImportError as e:
        print(f"Missing required modules: {e}")
    except FileNotFoundError as e:
        print(f"Required data files not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()