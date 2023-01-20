from pathlib import Path
class FileReader:
    def __init__(self, receieved_path):
        self.path = receieved_path
    def read(self):
        try:
            with open(self.path, "r") as f:
                s = f.read()
        except FileNotFoundError:
            s = ""
        return (s)


def main():
    path = Path("C:/Users/flora/PycharmProjects/pythonProject/some_text_file.txt")
    example = FileReader(path)
    print(example.read())

if __name__ == "__main__":
    main()