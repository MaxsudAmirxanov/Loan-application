class LoanApplication:
    def __init__(self, name, age, floor, income, credit_history, money):
        self.name = name
        self.age = age
        self.floor = floor
        self.income = income
        self.credit_history = credit_history
        self.money = money
    
    point = 0

    def analysis_of_responses(self, name, point=point):
        if self.age == range(21, 41):
            point += 10
        elif self.age > 40:
            point += 20

        if self.floor.lower() == 'женщина':
            point += 10

        if self.income == range(20000, 40001):
            point += 10
        elif self.income > 40000:
            point += 20
        elif self.income < 20000:
            point += 20

        if self.credit_history.lower() == "да":
            point += 20
        

        # Подсчет процентов
        precent = (self.money / 100) * 5

        # Итог

        if point >= 50:
            print('Кредит был одобрен ', name, ' выдали', self.money)
            print('Вы будете платить', (precent + self.money) / 12, ' ежимесечно, в течении года')
            print(point)
        else:
            print('К сожалению в кредите вам отказали :(')
            print(point)


print('Добро пожаловать в Тинькофф банк, чтобы получить ответе на пару вопросов.')
name = input('Ваше ФИО: \n')

loop = True
while loop:
    try:
        age = int(input('Введите ваш возраст: \n'))
    except ValueError:
        print('Введите число !')
    else:
        loop = False

floor = input('Ваш пол: \n')

loop = True
while loop:
    try:
        income = int(input('Ваш доход в месяц: \n'))
    except ValueError:
        print('Введите число !')
    else:
        loop = False

credit_history = input('Вы имеете кредитную историю ?: \n')



loop = True
while loop:
    try:
        money = int(input('Какую сумму Вы хотите получить ?: \n'))
    except ValueError:
        print('Введите число !')
    else:
        loop = False


user_1 = LoanApplication(name, age, floor, income, credit_history, money)
user_1.analysis_of_responses(name)
    
