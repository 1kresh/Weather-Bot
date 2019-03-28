from dbs.db_filling_main import make_query

import requests
from bs4 import BeautifulSoup

def towns_parsing():
    
    r = requests.get('http://heaclub.ru/goroda-mira-rossii-po-alfavitu-ot-a-do-ya-spisok-i-nazvaniya-gorodov-dlya-igry-v-goroda-v-alfavitnom-poryadke')
    soup = BeautifulSoup(r.text, 'html.parser') 

    spans = list()
    for span in soup.find_all('span'):
        spans.append(span.text)

    for i in range(10):
        spans.pop(0)
    for i in range(712):
        spans.pop()

    towns = list()
    for span in spans:
        towns += span.strip().split()
    
    while 'БУКВА' in towns:
        towns.remove('БУКВА')
    
    symbols = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ь','Ы','Э','Ю','Я']

    for word in towns:
        if word in symbols: towns.remove(word)
    
    for i in range(2):
        for word in towns:
            if ')' in word or '(' in word: towns.remove(word)
    
    extra_1 = ['Александровск-', 'Сахалинский', 'Белая', 'Белая', 'Калитва', 'Холуница', 'Верхний', 'Тагил','Верхний', 
               'Уфалей','Верхняя', 'Пышма','Верхняя', 'Салда','Верхняя', 'Тура', 'Горячий', 'Ключ','Великие' ,'Луки',
               'Великий' ,'Новгород','Великий', 'Устюг', 'Большой', 'Камень', 'Вышний', 'Волочек', 'Вятские', 'Поляны',
               'Гаврилов', 'Посад', 'Дагестанские', 'Огни', 'Железногорск', 'Заречный', 'Благовещенск', 
               'Гурьевск', 'Красноармейск', 'Красный', 'Кут', 'Красный', 'Сулин', 'Красный', 'Холм', 'Никольск', 'Нижние', 
               'Серги','Нижний', 'Ломов','Нижний', 'Новгород','Нижний', 'Тагил','Нижняя', 'Салда','Нижняя', 'Тура', 
               'Павловский', 'Посад', 'Советск', 'Советск', 'Советская', 'Гавань', 'Приморск', 'Старая', 'Купавна', 'Старая',
               'Русса','Мариинский', 'Посад', 'Минеральные', 'Воды','Мирный', 'Михайловск', 'Набережные', 'Челны', 'Новый',
               'Оскол', 'Новый', 'Уренгой', 'Озерск', 'Полярные', 'Зори', 'Лодейное', 'Поле', 'Краснослободск', 'Краснознаменск',
               'Кировск', 'В', 'Сосновый', 'Бор', 'Старый', 'Крым', 'Старый', 'Оскол']
    extra_2 = ['Александровск-Сахалинский', 'Белая Калитва', 'Белая Холуница', 'Верхний Тагил','Верхний Уфалей',
               'Верхняя Пышма','Верхняя Салда','Верхняя Тура', 'Горячий Ключ','Великие Луки','Великий Новгород',
               'Великий Устюг', 'Большой Камень', 'Вышний Волочек', 'Вятские Поляны', 'Гаврилов Посад', 'Дагестанские Огни',
               'Красный Кут', 'Нижние Серги','Нижний Ломов','Нижний Новгород','Нижний Тагил', 'Нижняя Салда',
               'Нижняя Тура', 'Павловский Посад', 'Советская Гавань', 'Старая Купавна', 'Старая Русса', 'Мариинский Посад', 
               'Минеральные Воды', 'Набережные Челны', 'Новый Оскол', 'Новый Уренгой', 'Полярные Зори', 'Лодейное Поле', 
               'Красный Кут','Красный Сулин','Красный Холм','Сосновый Бор', 'Старый Крым', 'Старый Оскол']
    extra_3 = ['Курчалой', 'Кудрово', 'Кукмор', 'Сунжа']

    for word in extra_1:
        towns.remove(word)  
    for town in extra_2:
        towns.append(town)
    for town in extra_3:
        towns.append(town)

    make_query('insert into Rus_Towns (Russian) values (?)', ('|'.join(towns), ))

