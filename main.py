import os

class FileSystemIterator:
    def __init__(self, root, only_files=False, only_dirs=False, pattern=None):
        if only_files and only_dirs:
            raise Exception('Only one True')
        """
        Инициализация объекта
        :param root: корневой каталог
        :param only_files: итерироваться только по файлам
        :param only_dirs: итерироваться только по директориям
        :param pattern: итерироваться только по объектам файловой системы, содержащим в имени строку pattern
        """
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern
        self.item = None

    def __iter__(self):
        return self

    def _iterate_files(self):
        for dirpath, dirnames, filenames in os.walk(self.root):
            if self.only_dirs and not self.only_files:
                yield from self.sub_generator(dirnames, dirpath)
            elif self.only_files and not self.only_dirs:
                yield from self.sub_generator(filenames, dirpath)

    def sub_generator(self, names, path):
        for name in names:
            if self.pattern is None or self.pattern in name:
                self.item = os.path.join(path, name)
                yield self.item

    def __next__(self):
        if self.item is None:
            self._generator = self._iterate_files()
        self.item = next(self._generator)
        return self.item



for item in FileSystemIterator("C:/users", False, True, None):
  print(item)

print("################################")



print(next(FileSystemIterator("C:/users", False, True, None)))


