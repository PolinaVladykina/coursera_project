from solution_6 import FileReader
from pathlib import Path

def main():
    path = Path("C:/Users/flora/PycharmProjects/pythonProject/some_textes_file.txt")
    example = FileReader(path)
    print(example.read())

if __name__ == "__main__":
    main()