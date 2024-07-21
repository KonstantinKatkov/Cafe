# Моделирование работы сети кафе с несколькими столиками и потоком посетителей, прибывающих для заказа пищи и
# уходящих после завершения приема.
#
# Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик, употребляют еду и уходят.
# Если столик свободен, новый посетитель принимается к обслуживанию, иначе он становится в очередь на ожидание.
#
# Создайте 3 класса:
# Table - класс для столов, который будет содержать следующие атрибуты: number(int) - номер стола,
# is_busy(bool) - занят стол или нет.
#
# Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
# Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
# Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
# Метод serve_customer(self, customer) - моделирует обслуживание посетителя. Проверяет наличие свободных столов,
# в случае наличия стола - начинает обслуживание посетителя (запуск потока), в противном случае - посетитель поступает
# в очередь. Время обслуживания 5 секунд.
# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
#
# Так же должны выводиться текстовые сообщения соответствующие событиям:
# Посетитель номер <номер посетителя> прибыл.
# Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
# Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
# Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь
# Пример работы:
# # Создаем столики в кафе
# table1 = Table(1)
# table2 = Table(2)
# table3 = Table(3)
# tables = [table1, table2, table3]
#
# # Инициализируем кафе
# cafe = Cafe(tables)
#
# # Запускаем поток для прибытия посетителей
# customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
# customer_arrival_thread.start()
#
# # Ожидаем завершения работы прибытия посетителей
# customer_arrival_thread.join()
#

import time
from threading import Thread
import queue

class Table:                 # Создаем словарь столов, где ключ - номер стола, значение - занят (True) или свободен (False)
    def __init__(self, number):
        self.number = number
        self.tables = {}

    def add_dict_tables(self):
        is_busy = False
        self.tables[self.number] = is_busy
        return self.tables

class Cafe:
    def __init__(self, tables):
        self.tables = tables

    def customer_arrival(self):
        customer = 0
        for i in range(1, 21):
            customer += 1
            print(f'Посетитель номер {customer} прибыл.')
            time.sleep(1)
        return customer

    def serve_customer(self, customer):
        for key in self.tables:                                      #Получаем список номеров столов из словаря
            table_list = key

        for i in len(table_list):
            if self.tables[i] == False:
                thread = Customer(table_list[i], customer)
                self.tables[i] == True
                time.sleep(5)
                print(f'Посетитель {customer} покушал и ушел')

            else:
                queue.put(customer)
                print(f'Посетитель {customer} ожидает свободный стол')

class Customer(Thread):
    def __init__(self, table_list, customer):
        super().__init__()
        self.table_list = table_list
        self.customer = customer

    def eat_customer(self):
        print(f'Посетитель {self.customer} сел за стол номер {self.table_list}')


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
table4 = Table(4)

table_1 = table1.add_dict_tables()
table_2 = table2.add_dict_tables()
table_3 = table3.add_dict_tables()
table_4 = table4.add_dict_tables()

tables = {**table_1, **table_2, **table_3, **table_4}

print(tables)
cafe = Cafe(tables)

customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()

