# Вариант 75
import json
from tqdm import tqdm
import argparse
import re


class ReadFile:
    """
    Объект класса ReadFile считывает текст из файла и хранит их
    Он нужен для того, чтобы хранить в себе данные из файла
    для дальнейшего использования.
    Attributes
    ----------
    __data - хранит данные из файла
    """

    __data: object

    def __init__(self, path: str) -> None:
        """
        Иизиализирует экземпляр класса ReadFile
        Parameters
        ----------
        path : str
            Путь к файлу
        """

        self.__data = json.load(open(path, encoding='windows-1251'))

    @property
    def data(self) -> object:
        """
        Выполняет доступ к данным экземпляра
        Return
        -------
        object:
            Данные из файла
        """
        return self.__data


class validator:
    """
    Класс validator проверяет данные на валидность
    Он нужен для того, чтобы найти количество валидных и
    невалидных записей в файле
    Attributes
    ----------
    __email:str
            - адресс почты
    __height: float
            - рост в метрах
    __snils: str
            - номер снилса
    __passport_number: str
            - номер паспорта
    __university: str
            - университет
    __age: int
            - возраст (полные года)
    __political_views: str
            - политические взгляды
    __worldview: str
            - вероисповедание
    __address: str
            - адресс проживания
    """
    __email: str
    __height: float
    __snils: str
    __passport_number: str
    __university: str
    __age: int
    __political_views: str
    __worldview: str
    __address: str
    __height_invalid = ['da']
    __universiti_invalid = ['Авиационно-технический университетАвиационно-технический университет']
    __worldview_invalid = ['Культ пророка Лебеды', 'Культ богини Мелитэле', 'Культ Механикус',
                           'Светское гачимученничество', 'Храм Трибунала', 'Девять божеств', 'Культ проклятых']
    __political_views_invalid = ['поддерживает Имперский легион',
                                 'согласен с действиями Гарроша Адского Крика на посту вождя Орды',
                                 'поддерживает Братьев Бури', 'патриот независимой Темерии', ]

    def __init__(self, __email: str, __height: float,
                 __snils: str, __passport_number: str,
                 __university: str, __age: int,
                 __political_views: str, __worldview: str,
                 __address: str):
        self.__email = __email
        self.__height = __height
        self.__snils = __snils
        self.__passport_number = __passport_number
        self.__university = __university
        self.__age = __age
        self.__political_views = __political_views
        self.__worldview = __worldview
        self.__address = __address

    def check_mail(self) -> bool:
        """
        Выполняет проверку валидности адреса электронной почты
        Return
        -------
        bool:
            результат проверки (всё правильно - True, найдены несовбодения - False)
        """
        return re.match(r"^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$", self.__email) is not None

    def check_height(self) -> bool:
        """
        Выполняет проверку валидности высоты
        Return
        -------
        bool:
            результат проверки (всё правильно - True, найдены несовбодения - False)
        """

        return re.match(r"\-?\d+\.\d+", str(self.__height)) is not None and 0.70 <= float(
            self.__height) <= 2.70 and self.__height not in self.__height_invalid

    def check_snils(self) -> bool:
        """
        Выполняет проверку валидности номера  нилса
        Return
        -------
        bool:
            результат проверки (всё правильно - True, найдены несовбодения - False)
        """
        return re.match(r"[0-9]{11}", str(self.__snils)) is not None

    def check_passport_number(self) -> bool:
        """
        Выполняет проверку валидности номера  паспорта
        Return
        -------
        bool:
            результат проверки (всё правильно - True, найдены несовбодения - False)
        """
        return re.match(r"[0-9]{6}", str(self.__passport_number)) is not None

    def check_university(self) -> bool:
        """
        Выполняет проверку валидности университета
        Return
        -------
        bool:
            результат проверки (всё правильно - True, найдены несовбодения - False)
        """
        return re.match(r"^[\D]+$",
                        self.__university) is not None and self.__university not in self.__universiti_invalid

    def check_age(self) -> bool:
        """
        Выполняет проверку валидности записи лет
        Return
        -------
        bool:
            результат проверки (всё правильно - True, найдены несовбодения - False)
        """
        return re.match(r"[0-9]{1,3}", str(self.__age)) is not None and 0 <= int(self.__age) <= 108

    def check_political_views(self) -> bool:
        """
        Выполняет проверку валидности политических взглядов
        Return
        -------
        bool:
            результат проверки (всё правильно - True, найдены несовбодения - False)
        """
        return re.match(r"^[\D]+$",
                        self.__political_views) is not None and \
               self.__political_views not in self.__political_views_invalid

    def check_worldview(self) -> bool:
        """
        Выполняет проверку валидности веры
        Return
        -------
        bool:
            результат проверки (всё правильно - True, найдены несовбодения - False)
        """
        return re.match(r"^[\D]+$", self.__worldview) is not None and self.__worldview not in self.__worldview_invalid

    def check_address(self) -> bool:
        """
        Выполняет проверку валидности адреса
        Return
        -------
        bool:
            результат проверки (всё правильно - True, найдены несовбодения - False)
        """
        return re.match(r"^(ул\.)?(Аллея)?\s[\w\.\s-]+\d+$", self.__address) is not None

    def chek_all(self) -> int:
        """
        Выполняет проверку валидности всех данных для определения, какие записи невалидны
        Return
        -------
        int:
            место в котором ошибка (0 - невалидный email, 1 - невалидный рост,2 - невалидный снилс,
                                    3 - невалидная серия паспорта, 4 - невалидный университет,
                                    5 - невалидный возраст, 6 - невалидный политический взгляд,
                                    7 - невалидная вера, 8 - невалидный адресс, 9 - ошибок нет)
        """
        if not self.check_mail():
            return 0
        elif not self.check_height():
            return 1
        elif not self.check_snils():
            return 2
        elif not self.check_passport_number():
            return 3
        elif not self.check_university():
            return 4
        elif not self.check_age():
            return 5
        elif not self.check_political_views():
            return 6
        elif not self.check_worldview():
            return 7
        elif not self.check_address():
            return 8
        else:
            return 9


parser = argparse.ArgumentParser()
parser.add_argument('-in', type=str, dest="file_input", default='75.txt')
parser.add_argument('-out', type=str, dest="file_output", default='75_result.txt')
args = parser.parse_args()
input_file = ReadFile(args.file_input)
output_file = open(args.file_output, "w")
counter_valid = 0
counter_unvalid_of_records = [0, 0, 0, 0, 0, 0, 0, 0, 0]
with tqdm(input_file.data, desc='Процесс проверки записей(не выключайте проргамму)') as progressbar:
    for record in input_file.data:
        check = validator(record['email'], record['height'], record['snils'],
                          record['passport_number'], record['university'], record['age'],
                          record['political_views'], record['worldview'], record['address'])
        unvalid = check.chek_all()
        if unvalid == 9:
            output_file.write('email: ' + str(record['email']) + '\n' + 'height:' + str(record['height']) + '\n'
                              + 'snils: ' + str(record['snils']) + '\n' + 'passport_number: ' +
                              str(record['passport_number']) + '\n'
                              + 'university: ' + str(record['university']) + '\n' + 'age: ' + str(record['age']) + '\n'
                              + 'political_views: ' + str(record['political_views']) + '\n' + 'worldview: ' +
                              str(record['worldview']) + '\n' + 'address: ' + str(record['address']) + '\n')
            output_file.write("-------------------------------------------\n")
            counter_valid += 1
        else:
            counter_unvalid_of_records[unvalid] += 1
        progressbar.update(1)
all_unvalid_of_record = 0
for elem in counter_unvalid_of_records:
    all_unvalid_of_record += elem
print("Количество валидных записей:", counter_valid)
print("Количество невалидных записей:", all_unvalid_of_record)
print("Количество невалидных email:", counter_unvalid_of_records[0])
print("Количество невалидных записей роста:", counter_unvalid_of_records[1])
print("Количесвто невалидных снилсов:", counter_unvalid_of_records[2])
print("Количество неалидных номеров паспорта", counter_unvalid_of_records[3])
print("Количество невалидных названий университета", counter_unvalid_of_records[4])
print("Количество невалидных возрастов", counter_unvalid_of_records[5])
print("Количество невалидных политических взглядов", counter_unvalid_of_records[6])
print("Количество невалидных вероисповеданий", counter_unvalid_of_records[7])
print("Количество невалидных адресов", counter_unvalid_of_records[8])
output_file.close()
