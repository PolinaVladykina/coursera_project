import os.path
from pathlib import Path
import tempfile
class File:
    def __init__(self, path_to_file):
        self.path = path_to_file
        self.current = 0
        # read file to variable
        # split file contain to lines
        if not os.path.exists(path_to_file):
            with open(self.path, 'w+'):
                pass

    def read(self):
        # with open(self.path, "r") as f:
        #     s = f.read()
        return self.file_contain
        # return s

    def write(self, string):
        with open(self.path, "w") as f:
            f.write(string)

    def __add__(self, obj):
        # to remake
        result_path = os.path.join(tempfile.gettempdir(), 'final.txt')
        result = File(result_path)
        result.write(self.read() + obj.read())
        return result

    def __str__(self):
        return self.path

    def __getitem__(self, index):
        # return self.lines[index] + '\n'
        with open(self.path) as file:
            lines = [line.rstrip() for line in file]
        return lines[index]+'\n'

    def __iter__(self):
        return self

    def __next__(self):
        # with open(self.path, 'r') as f:
        #     f.seek(self.current)
        #     line = f.readline()
        #
        #     if line:
        #         self.current = f.tell()
        #         return line
        #     else:
        #         self.current = 0
        #         raise StopIteration

        # self.lines
        # if self.current == len(self.lines)
        #     raise StopIteration
        # results = self.lines[self.current] + '\n'
        # self.current += 1
        pass


def main():
    path = Path("C:/Users/flora/PycharmProjects/pythonProject/some_text_file.txt")
    path_to_file = "some_filename"
    file_obj = File(path_to_file)
    file_obj_1 = File(path_to_file + '_1')
    file_obj_2 = File(path_to_file + '_2')
    file_obj_1.write('line 1\n')
    file_obj_2.write('line 2\n')
    new_file_obj = file_obj_1 + file_obj_2
    for line in new_file_obj:
        print(ascii(line))

    #example = File(path)
    #print()

if __name__ == "__main__":
    main()