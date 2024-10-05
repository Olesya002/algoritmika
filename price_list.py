# Класс Price_list
class Price_list():
    def __init__(self, name):
        self.name = name
        self.prices = dict()
    def add_price(self, **kwargs):
        for key in kwargs:
            self.prices[key] = kwargs[key]
    def order(self, **kwargs):
        total_price = 0
        for key in kwargs:
            price = kwargs[key] * self.prices[key]   # мы умножаем количество услуги на ее цену
            total_price += price                     # прибавляем посчитаную цену на услугу к общей стоимости
        return total_price                           # возвращаем общую стоимость заказа

# объект класса Price_list
my_offer = Price_list('Инстаграм')
my_offer.add_price(management = 1000, content_plan = 850, style = 500, stories = 100, post = 300)

# основная программа (цикл)
answer_1 = int(input('Хотите сделать заказ? (1 - да, 0 - нет)'))
while answer_1 == 1:
    answer_2 = int(input('Хотите заказать управление аккаунтами (1) или публикации (2)?'))
    if answer_2 == 1:
        # заказ - управление аккаунтами (в него входят услуги: management, content_plan, style)
        u_1 = int(input('Сколько новых аккаунтов хотите добавить?'))
        u_2 = int(input('Для скольких из них будем делать контент-план?'))
        u_3 = int(input('Для скольких из них будем разрабатывать стиль?'))
        total_price = my_offer.order(management = u_1, content_plan = u_2, style = u_3)
        print('Стоимость услуг:', total_price, 'руб.')
    elif answer_2 == 2:
        # заказ - публикации (в него входят услуги: stories, post)
        p_1 = int(input('Сколько сториз хотите заказать?'))
        p_2 = int(input('Сколько постов хотите заказать?'))
        total_price = my_offer.order(stories = p_1, post = p_2)
        print('Стоимость услуг:', total_price, 'руб.')
    answer_1 = int(input('Хотите сделать заказ? (1 - да, 0 - нет)'))
print('Спасибо за сотрудничество! Хорошего дня!')
