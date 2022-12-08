import re
from datetime import datetime


class Note:

    def __init__(self, name, surname, birthday, phone):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.phone = phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not value.rstrip():
            raise ValueError
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not value.rstrip():
            raise ValueError
        self.__surname = value

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not re.match('(0?[1-9]|[12][0-9]|3[0-1])\/(0?[1-9]|1[0-2])\/((19[2-9][0-9]|20[0-2][0-9]))', value):
            raise ValueError
        self.__birthday = datetime.strptime(value, '%d/%m/%Y')

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not re.match('\+[0-9]{3}\((\d{2})\)-\d{3}-\d{2}-\d{2}', value):
            raise ValueError
        self.__phone = value

    def __str__(self) -> str:
        return f'name - {self.__name}\n' \
               f'surname - {self.__surname}\n' \
               f'birthday - {self.__birthday.strftime("%d/%m/%y")}\n' \
               f'phone number - {self.__phone}'


class NoteBook:

    def __init__(self, *args):
        if args:
            self.notes = list(args)
        else:
            self.__notes = []

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value):
        if not isinstance(value, list):
            raise TypeError
        if not all(isinstance(n, Note) for n in value):
            raise TypeError
        self.__notes = value

    def __iadd__(self, other):
        if not isinstance(other, Note):
            raise TypeError
        self.__notes.append(other)
        return self

    def __isub__(self, other):
        if not isinstance(other, Note):
            raise TypeError
        if not other in self.__notes:
            return self
        self.__notes.remove(other)
        return self

    def __mul__(self, other):
        if not isinstance(other, str):
            raise TypeError
        if not re.match('(0?[1-9]|[12][0-9]|3[0-1])\/(0?[1-9]|1[0-2])\/((19[2-9][0-9]|20[0-2][0-9]))', other):
            raise ValueError
        other = datetime.strptime(other, '%d/%m/%Y')
        for note in self.__notes:
            if note.birthday == other:
                return note


if __name__ == '__main__':
    note1 = Note('Pavlik', 'Morozov', '01/03/2004', '+380(66)-523-33-92')
    note2 = Note('Petya', 'Pushkin', '02/09/2010', '+380(55)-666-77-92')
    notebook = NoteBook()
    notebook += note1
    notebook += note1
    notebook += note1
    notebook += note2
    print(notebook * '02/09/2010')
    print(notebook * '01/03/2004')
