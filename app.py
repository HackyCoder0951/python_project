import os
# from src.scripts.multiply_two_numbers import main
from src.scripts.add_two_numbers import main


if __name__ == "__main__":
    while True:
        try:
            os.system("clear")

            main();
            exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")
            input("\n\nPress Enter to restart...")
