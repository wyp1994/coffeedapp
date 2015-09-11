import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR2 = os.path.dirname(os.path.abspath(__file__))

print("BASE DIR: " + str(BASE_DIR))
print("MAIN_DIR: " + str(MAIN_DIR))
print("BASE_DIR2: " + str(BASE_DIR2))
