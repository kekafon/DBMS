import random
import os
import re

class PriorityQueue(list):
    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)
    def __eq__(self, other):
        return len(self) == len(other)

    def shiftdown(self, startpos, pos):
        newitem = self[pos] #Получение элемента данной позиции

        while pos > startpos: #пока данная позиция > статовой
            parentpos = (pos - 1) // 2 #Ищем индекс родителя
            parent = self[parentpos] #Ищем родителя
            if newitem < parent: #Если элемент на данной прозиции меньше родителя, то меняем их местами
                self[pos] = parent #то меняем их местами
                pos = parentpos #обновляем позицию
                continue
            break
        
        self[pos] = newitem #Возвращаем элемент на правильную позицию, если if сработал, если не сработал, то остается на месте

    def shiftup(self, pos):
        endpos = len(self) #Последняя позиция - длина массива
        startpos = pos #Стартовая позиция
        newitem = self[pos] #Получение элемента стартовой позиции
    
        leftpos = 2 * pos + 1 #Проверяем child для позиции
        while leftpos < endpos: #Пока позиция child < длины массива
            rightpos = leftpos + 1

            if rightpos < endpos and self[leftpos] > self[rightpos]: #если не конец, и левое больше правого
                leftpos = rightpos #то правый лист идет вверх
        
            self[pos] = self[leftpos] #Родитель = правому листу, если if выполнилось, и левому листу, если не выполнилось
            pos = leftpos #Позиция = правому листу, если if выполнилось, и левому листу, если не выполнилось
            leftpos = 2 * pos + 1 #Обновляем позицию и если не крайние листы цикл повторяется

        self[pos] = newitem #Возвращаем на правильную позицию место
        self.shiftdown(startpos, pos)

    def heapify(self): #Метод преобразования последовательности в кучу
        n = len(self)
        for i in reversed(range(n//2)):
            self.shiftup(i)
  
    def print(self):
        print(self)

    def check(self):
        return type(self)

    def pop_(self): #Извлечение элемента с наивысшем приоритетом
        lastelt = self.pop()
        if self:
            returnitem = self[0]
            self[0] = lastelt
            self.shiftup(0)
            return returnitem
        return lastelt

    def push(self, item): #Добавление элемента
        self.append(item)
        self.shiftdown(0, len(self)-1)

    def replace(self, item): #Замена элемента (добавлеятся данный item, удаляется элемент с наивысшем приоритетом)
        returnitem = self[0]
        self[0] = item
        self.shiftup(0)
        return returnitem

class ListComparator(list): #Сравнение по длине списка
    '''Компаратор для списков'''
    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)
    def __eq__(self, other):
        return len(self) == len(other)

class StrComparator(str): #Сравнение по длине строки
    '''Компаратор для строк'''
    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)
    def __eq__(self, other):
        return len(self) == len(other)

class DictComparator(dict): #Сравнение по длине значений словаря
    '''Компаратор для словарей'''
    def __gt__(self, other):
        for k, v in self.items():
            length_v = len(v)
        for k, v in other.items():
            length_o = len(v)
        return length_v > length_o
    def __lt__(self, other):
        for k, v in self.items():
            length_v = len(v)
        for k, v in other.items():
            length_o = len(v)
        return length_v < length_o
    def __ge__(self, other):
        for k, v in self.items():
            length_v = len(v)
        for k, v in other.items():
            length_o = len(v)
        return length_v >= length_o
    def __le__(self, other):
        for k, v in self.items():
            length_v = len(v)
        for k, v in other.items():
            length_o = len(v)
        return length_v <= length_o
    def __eq__(self, other):
        for k, v in self.items():
            length_v = len(v)
        for k, v in other.items():
            length_o = len(v)
        return length_v == length_o


class Table(PriorityQueue): #Таблица условное название (для удобства), это просто очередь с приоритетом
    '''Компаратор для таблиц'''
    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)
    def __eq__(self, other):
        return len(self) == len(other)
    
    def __init__(self, table_name): #Конструктор
        self.name = table_name
        self.queue = self.user_interface()
        
    def user_interface(self): #Интрефейс для взаимодействия с пользователем
        print('МЕНЮ Таблицы\n')
        print('1. Создать очередь с приоритетом заполненную псевдослучайными числами.')
        print('2. Создать пустую очередь.')
        print('3. Добавить новый элемент.')
        print('4. Добавить несколько элементов.')
        print('5. Удалить элемент с наивысшем приоритетом.')
        print('6. Заменить элемент (т.е внести новый элемент и удалить элемент с наивысшем приоритетом).')
        print('7. Вывести на экран очередь с приоритетом.')
        print('8. Выйти\Сохранить.')
        print('\n')
    
        queue = [] #Нужны для проверки на пустоту
        t = 'None'
    
        while True: #Бесконечный цикл для вызова функций класса
            number = enter_element_number('Введите номер пункта меню(ТАБЛИЦЫ): ',
                                          'Вы ввели не верный номер. Попробуйте еще раз')

            if number == 1:
                queue, t = self.create_queue() #Создание таблицы заполненное рандомными числами
            elif number == 2:
                queue, t = self.create_empty_queue() #Создать пустую таблицу с выбором типа данных
            elif number == 3:
                self.wrapper(queue, self.push_element, t) #Добавить 1 элемент
            elif number == 4:
                self.wrapper(queue, self.push_elements, t) #Добавить несколько элементов
            elif number == 5:
                self.wrapper(queue, self.pop_element, t) #Удалить элемент с наивысшим приоритетом
            elif number == 6:
                self.wrapper(queue, self.replace_element, t) #Заменить элемент с наивысшим приоритетом
            elif number == 7:
                self.wrapper(queue, self.print_queue, t) # Вывести таблицу(очередь)
            elif number == 8: #Сохранение
                print('До свидания!')
                return queue
                break
            else:
                print('Введенного номера нет в МЕНЮ. Попробуйте еще раз.')

    def enter_element_list(self): #Парсер ввода для элементов списка
        mass = input('Введите список объектов через запятую.' +
                    '\nЕсли хотите записать строку (пример:"ваша_строка")'+
                    '\nЕсли хотите записать число кавычки не нужны.'+
                    '\nЦелые числа пишутся через точку (пример: "a","bc",5.0): ').split(',')
    
        element = []
        for i in mass: 
            if re.findall(r'[0-9]+\.[0-9]+', i) or re.findall(r'"[0-9]+\.[0-9]+"', i): #Числа через точку
                try:
                    element.append(float(i))
                except Exception:
                    element.append(re.findall(r'"[0-9]+\.[0-9]+"', i)[0][1:-1]) #Стркоа с числом
            elif re.findall(r'"\D+"', i): #Поиск
                try:
                    element.append(re.findall(r'"\D+"', i)[0][1:-1]) #Поиск любых символов кроме цифры
                except Exception:
                    continue
            elif re.findall(r'"\w+"', i):
                try:
                    element.append(re.findall(r'"\w+"', i)[0][1:-1]) #Поиск любой буквы или части слова
                except Exception:
                    continue
            else:
                try:
                    element.append(i[1:-1]) #Если ничего не найдет, то это просто слово
                except Exception:
                    continue
        return element

    def enter_element_dict(self): #Ввод элементов словаря
        size = enter_element_number('\nВведите размер словаря, который хотите внести (целое положительно число): ')  
        while True:
            try:
                element = dict([input('Введите ключ и значение через пробел: ').split() for _ in range(int(size))])
                return element
            except Exception:
                print('Не верное значение! Попробуйте сначала')

    def wrapper(self, queue, target, t): #Оболочка для вызова функций 
        if target.__code__.co_argcount == 3: #Если 3 аргумента функции
            target(queue, t)
        else:
            target(queue) #Если не 3 аргумента у функции

    def check_type_wrapper(self, queue, t, target): #Проверка на тип данных, в зависимости от этого различный тип ввода
        if t == 'int' or t == 'float':
            element = enter_element_number('Введите число: ')
            if target == 'push':
                queue.push(element)
                print('Элемент успешно добавлен!')
            elif target == 'replace':
                queue.replace(element)
                print('Элемент успешно заменен!')
        elif t == 'string':
            element = input('Введите строку: ')
            if target == 'push':
                queue.push(StrComparator(element))
                print('Элемент успешно добавлен!')
            elif target == 'replace':
                queue.replace(StrComparator(element))
                print('Элемент успешно добавлен!')
        elif t == 'list':
            element = self.enter_element_list()
            if target == 'push':
                queue.push(ListComparator(element))
                print('Элемент успешно добавлен!')
            elif target == 'replace':
                queue.replace(ListComparator(element))
                print('Элемент успешно добавлен!')
        elif t == 'dict':
            element = self.enter_element_dict()
            if target == 'push':
                queue.push(DictComparator(element))
                print('Элемент успешно добавлен!')
            elif target == 'replace':
                queue.replace(DictComparator(element))
                print('Элемент успешно добавлен!')
    
    def create_queue(self): #Создание очереди с рандомными числами
        size = enter_element_number('\nВведите размер очереди (целое положительно число): ')
        values = get_random_values(size)
        
        queue = PriorityQueue(values)
        queue.heapify()
        print('Очередь с приоритетом имеет вид: ')
        queue.print()
    
        return queue, 'int'

    def create_empty_queue(self): #создание очереди с указанием типа
        while True:
            t = input('Введите какой тип данных хотите хранить' +
                      '\n(string:строка, int:целое число, float:число с плавающей точкой, list:список объектов, dict:словарь): ')

            if t == 'float' or t == 'int' or t == 'list' or t == 'string' or t == 'dict':
                break
            else:
                print('Вы ввели не правильный тип данных, попробуйте еще раз...')
            
        queue = PriorityQueue([])
        queue.heapify()
        print('Очередь с приоритетом имеет вид: ')
        queue.print()
        print('Тип элементов: ' + t)
    
        return queue, t
                 
    def push_element(self, queue, t): #Добавление
        self.check_type_wrapper(queue, t, 'push')
 
    def replace_element(self, queue, t): #Замена
        self.check_type_wrapper(queue, t, 'replace')

    def push_elements(self, queue, t): #Добавление нескольких элементов
        size = enter_element_number('Сколько добавляем элементов?: ')
        [self.push_element(queue, t) for _ in range(int(size))]

    def pop_element(self, queue): #Удаление элементов с наивысшим приоритетом, если очередь не пуста
        if len(queue) > 0:
            element = queue.pop_()
            print(f'\nЭлемент "{element}" успешно удален')
        else:
            print('\nПустая очередь!')

    def print_queue(self, queue): #Вывод очереди
        queue.print()


class Database(PriorityQueue):
    '''Класс для хранения таблиц, тип: очередь с приоритетом'''
        
    def user_interface(self): #Интерфейс для вызова методов
        print('МЕНЮ Базы данных\n')
        print('1. Создать новую таблицу.')
        print('2. Вывести все таблицы базы данных.')
        print('3. Удалить таблицу с наивысшим приоритетом.')
        print('4. Заменить таблицу (заменяет таблицу с наивысшим приоритетом).')
        print('5. Выйти\Сохранить.')
        print('\n')
    
    
        while True:
            number = enter_element_number('Введите номер пункта меню(БАЗА ДАННЫХ): ',
                                          'Вы ввели не верный номер. Попробуйте еще раз')

            if number == 1:
                self.create_table() #Создание очереди с приоритетом
                break
            elif number == 2:
                self.print_table() #Вывод базы данных
            elif number == 3:
                self.pop_table() #Удаление таблицы
            elif number == 4:
                self.replace_table() #Замена таблицы
                break
            elif number == 5: #Сохранение
                print('До свидания!')
                break
            else:
                print('Введенного номера нет в МЕНЮ. Попробуйте еще раз.')

    def create_table(self):
        os.system("cls")
        print('Создание новой таблицы...')
        name_table = input('Введите имя новой таблицы: ')
        table = Table(name_table)
        self.push(DictComparator({name_table: table.queue}))
        os.system("cls")
        self.user_interface()

    def print_table(self):
        print(self)

    def pop_table(self):
        if len(self) > 0:
            element = self.pop_()
            print(f'\nЭлемент "{element}" успешно удален')
        else:
            print('\nПустая база данных!')
            
    def replace_table(self):
        self.pop_table()
        self.create_table()


def get_random_values(size, minimum = 1, maximum = 100): #Получение случайных чисел 0..100
    return [random.uniform(minimum, maximum) for _ in range(int(size)) if int(size) > 0]

def create_database(): #Осноаня функция Создания базы данных
    while True:
        print('Создание новой базы данных...')
        name_database = input('\nВведите название базы данных без пробелов: ')

        if len(name_database.split(' ')) == 1 and name_database != '':
            break
        else:
            print('Вы ввели недопустимое имя, попробуйте еще раз...')
            
    database = Database(PriorityQueue([])) #Создание пустой базы данных на основе Очереди с приоритетом    
    print('База данных ' + name_database + ' успешно создана!')
    return database

def enter_element_number(text_input,
                         text_except='Вы ввели не число. Попробуйте еще раз...'): #Функция для ввода чисел
    while True:
        try:
            element = float(input(text_input))
            return element
        except ValueError:
            print(text_except)
    

if __name__ == '__main__':
    database = create_database()
    database.user_interface()
    
    '''
    list_database = []
    
    print('Cписок БАЗ ДАННЫХ\n')
    print('1. Показать весь список баз данных.')
    print('2. Добавить новую базу данных.')
    print('3. Удалить базу данных.')
    print('4. Выйти.')
    print('\n')
    
    while True:
        number = enter_element_number('Введите номер пункта меню: ',
                                      'Вы ввели не верный номер. Попробуйте еще раз')
        if number == 1:
            print(list_database)
        elif number == 2:
            os.system("cls")
            database, name_database = create_database()
            database.user_interface()
            list_database.append(DictComparator({name_database: database}))
            os.system("cls")
        elif number == 3:
            key = input('Введите имя базы данных для удаления: ')
            for i in range(len(list_database)):
                for k, v in list_database[i].items():
                    if k == key:
                        db = list_database.pop(i)
                        print(key + ' успешно удалена!')
                        break
                    
        elif number == 4: #Сохранение
            print('До свидания!')
            break
        else:
            print('Введенного номера нет в МЕНЮ. Попробуйте еще раз.')

    '''
