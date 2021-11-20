print('Добро пожаловать на завод, производящий автомобили по вашему вкусу и желанию.')

#Создаем 3 родительских класса, чтобы потом унаследовать их методы и атрибуты#

#Класс тонировки новый класс, который я добавил#
class Toning:
    def addpt(self,x):
        self.p_stekla[x-1] = 'Тонированное стекло'
    def delpt(self,x):
        self.p_stekla[x-1] = 'Обычное стекло'
    def addzt(self,x):
        self.z_stekla[x-1] = 'Тонированное стекло'
    def delzt(self,x):
        self.z_stekla[x-1] = 'Обычное стекло'


class Wheel:
    def Addk(self,x):
        self.colesa[x-1] = 'Обычное колесо'
    def Addkh(self,x):
        self.colesa[x-1] = 'Зимнее колесо'
    def Delk(self,x):
        self.colesa[x-1] = 'Нет колеса'


class Fara:
    def Onp(self,x):
        self.p_fara[x-1] = 'вкл'
    def Offp(self,x):
        self.p_fara[x-1] = 'выкл'
    def Onz(self,x):
        self.z_fara[x-1] = 'вкл'
    def Offz(self,x):
        self.z_fara[x-1] = 'выкл'
    def Onpov(self,x):
        self.povor[x-1] = 'вкл'
    def Offpov(self,x):
        self.povor[x-1] = 'выкл'


class Dveri:
    def Open(self,x):
        self.doors[x-1] = 'Открыто'
    def Close(self,x):
        self.doors[x-1] = 'Закрыто'
    
        

#Создаём дочерний класс, как выше уже говорилось этот класс унаследовал характеристики и способности 3 классов свыше#
class Car(Toning,Wheel,Fara,Dveri):

    def __init__(self, color = None, model = None, body = None, year = None):
        self.aboba = None
        self.color = color
        self.model = model
        self.body = body
        self.year = year
        self.colesa = ['Обычнок колесо']*4
        self.p_fara = ['выкл']*2
        self.z_fara = ['выкл']*2
        self.povor = ['выкл']*2
        self.doors = ['Закрыто']*4
        self.p_stekla = ['Обычное стекло']*2
        self.z_stekla = ['Обычное стекло']*2


#Это просто менюшка#    
class Interface():
    def __init__(self):
        self.UserInFace()

    def UserInFace(self):
        k=0
        while True:
            print('Выберите пункт соответсвующий вашим потребностям.')
            print('1. Хочу машину')
            print('2. Изменить параметры машины')
            print('3. Посмотреть состояние машины')
            print('4. Список уже имеющихся машин')
            print('5. Удаление машин')
            a = input()


#1 строка основная здесь ты задаёшь модель, кузов, год машины#            
            if a == '1':
                print('Введите модель автомобиля:')
                massiv.append(Car(model = input()))
                k+=1
                print('Введите желаемый цвет для авто:')
                massiv[k-1].color = input()
                print('Какого года должна быть модель?')
                massiv[k-1].year = input()
                print('Какой кузов предпочитаете?')
                massiv[k-1].body = input()

#2 строка (самая лютая) здесь ты меняешь определённые параметры машины#    
            elif a == '2':
                print('Параметры какого автомобился хотите изменить?')
                for i in range(len(massiv)):
                    print(i+1,') ',massiv[i].model, sep = '')
                i = int(input())-1
                print('Выберите, что именно вы хотите изменить в машине.')
                print('1. Поменять модель')
                print('2. Поменять цвет')
                print('3. Поменять кузов')
                print('4. Поменять год выпуска')
                print('5. Поменять/удалить колёса')
                print('6. Открыть/закрыть двери')
                print('7. Настройка фар и поворотников')
                print('8. Настройка тонировки стёкол')
                print('0. Назад')
                b = input()
#Изменение модели#
                if b == '1':
                    print('Введите модель')
                    massiv[i].model = input()
#Изменение цвета#   
                if b == '2':
                    print('Введите цвет')
                    massiv[i].color = input()
#Изменение кузова# 
                if b == '3':
                    print('Введите кузов')
                    massiv[i].body = input()
#Изменение года# 
                if b == '4':
                    print('Введите год')
                    massiv[i].year = input()
#Махинации с колесом# 
                if b == '5':
                    c = ''
                    while c != '0':
                        print(massiv[i].colesa)
                        print('1. Добавить обычное колесо\n2. Добавить зимнее колесо\n3. Удалить колесо\n0.Выход')
                        c = input()
                        if c == '1':
                            print('Введите номер колеса, которое хотите заменить')
                            massiv[i].Addk(int(input()))
                        if c == '2':
                            print('Введите номер колеса, которое хотите заменить')
                            massiv[i].Addkh(int(input()))
                        if c == '3':
                            print('Введите номер колеса, которое хотите удалить')
                            massiv[i].Delk(int(input()))
#Махинации с дверями#          
                if b == '6':
                    c = ''
                    while c != '0':
                        print(massiv[i].doors)
                        print('1. Открыть дверь')
                        print('2. Закрыть дверь')
                        print('0. Назад')
                        c = input()
                        if c == '1':
                            print('Введите номер двери')
                            massiv[i].Open(int(input()))
                        if c == '2':
                            print('Введите номер колеса')
                            massiv[i].Close(int(input()))

#Суета с фарами#
                if b == '7':
                    c = ''
                    while c != '0':
                        print('состояние передних фар:', massiv[i].p_fara)
                        print('состояние задних фар:', massiv[i].z_fara)
                        print('состояние поворотников:', massiv[i].povor)
                        print('1. Включить переднюю фару')
                        print('2. Выключить переднюю фару')
                        print('3. Включить заднюю фару')
                        print('4. Выключитьь заднюю фару')
                        print('5. Включить поворотник')
                        print('6. Выключить повортник')
                        print('0. Выход')
                        c = input()
                        if c == '1':
                            print('Выберите какую из передних фар включить')
                            massiv[i].Onp(int(input()))
                        if c == '2':
                            print('Выберите какую из передних фар выключить')
                            massiv[i].Offp(int(input()))
                        if c == '3':
                            print('Выберите какую из задних фар включить')
                            massiv[i].Onz(int(input()))
                        if c == '4':
                            print('Выберите какую из задних фар выключить')
                            massiv[i].Offz(int(input()))
                        if c == '5':
                            print('Выберите какой поворотник включить')
                            massiv[i].Onpov(int(input()))
                        if c == '6':
                            print('Выберите какой поворотник выключить')
                            massiv[i].Offpov(int(input()))

#Настройка той самой тонировки#
                if b == '8':
                    c = ''
                    while c != '0':
                        print('Стёкла спереди:', massiv[i].p_stekla)
                        print('Стёкла сзади:', massiv[i].z_stekla)
                        print('1.Добавить тонировку спереди')
                        print('2.Убрать тонировку спереди')
                        print('3.Добавить тонировку сзади')
                        print('4.Убрать тонировку сзади')
                        print('0.Выход')
                        c = input()
                        if c == '1':
                            print('Выберите какое из передних стёкол затонировать')
                            massiv[i].addpt(int(input()))
                        if c == '2':
                            print('Выберите с какого переднего стекла убрать тонировку')
                            massiv[i].delpt(int(input()))
                        if c == '3':
                            print('Выберите какое из задних стёкол затонировать')
                            massiv[i].addzt(int(input()))
                        if c == '4':
                            print('Выберите с какого заднего стекла убрать тонировку')
                            massiv[i].delzt(int(input()))
                            
                        

#3 строка здесь можно посмотреть на характеристики той или иной машины, которая у тебя уже есть#
            elif a == '3':
                if len(massiv) == 0:
                    print('Извнините, но к сожалению у вас нет ни одной машины')
                    input()
                else:
                    print('0. Выход')
                    for i in range(len(massiv)):
                        print(i+1,') ',massiv[i].model, sep = '')
                    i = int(input())-1
                    if i == -1:
                        a = Interface()
                    if massiv[i].model != None:
                        print('1)Модель-', massiv[i].model)
                    if massiv[i].color != None:
                        print('2)Цвет-', massiv[i].color)
                    if massiv[i].body != None:
                        print('3)Кузов-', massiv[i].body)
                    if massiv[i].year != None:
                        print('4)Год выпуска-', massiv[i].year)
                        print('5)Колёса-', massiv[i].colesa)
                        print('6)Двери-', massiv[i].doors)
                        print('7)Фары: \n1)Передние фары: ', massiv[i].p_fara,'\n2)Задние фары: ',massiv[i].z_fara,'\n3)Поворотники: ',massiv[i].povor)
                        print('8)Стёкла: \n1)Стёкла спереди: ', massiv[i].p_stekla, '\n2)Стёкла сзади', massiv[i].z_stekla)
                    
#4 строка просмотр своих, уже имеющихся, машин#
            elif a == '4':
                if len(massiv) == 0:
                    print('Машин нету')
                else:
                    for i in range(len(massiv)):
                        print(i+1,') ',massiv[i].model, sep = '')
                input()

#5 строка соответсвенно удаление машин из списка имеющихся#
            elif a == '5':
                if len(massiv) == 0:
                    print('Нет машин для удаления')
                else:
                    for i in range(len(massiv)):
                        print(i+1,') ',massiv[i].model, sep = '')
                    c = int(input())
                    del massiv[c-1]

#Запускаем ПО и вводим пустой маасив, в который будем загонять свои машинки#
massiv = []
a = Interface()
