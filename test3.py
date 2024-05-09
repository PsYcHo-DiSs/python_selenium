# исходные данные        
tpl = (
    ('name: Зелёная миля', 'year: 1999', 'genre: драма, фэнтези, криминал',
     'director: Фрэнк Дарабонт', 'rating: 9.1'),
    ['name: Список Шиндлера', 'year: 1993', 'genre: драма, фэнтези, криминал',
     'director: Стивен Спилберг', 'rating: 8.8'],
    ['name - Побег из Шоушенка', 'year - 1994', 'genre - драма',
     'director - Фрэнк Дарабонт', 'rating - 9.1'],
    {'name': 'Форрест Гамп', 'year': '1994', 'genre': 'драма, комедия, мелодрама, история, военный',
     'director': 'Роберт Земекис', 'rating': '8.9'},
    ('name: Тайна Коко', 'year: 2017', 'genre: мультфильм, фэнтези, комедия, приключения, семейный',
     'director: Ли Анкрич', 'rating: 8.7'),
    ['name: Властелин колец: Возвращение короля', 'year: 2003', 'genre: фэнтези, приключения, драма, боевик',
     'director: Питер Джексон', 'rating: 8.7'],
    {'name': 'Интерстеллар', 'year': '2014', 'genre': 'фантастика, драма, приключения',
     'director': 'Кристофер Нолан', 'rating': '8.6'},
    ['name - Криминальное чтиво', 'year - 1994', 'genre - криминал, драма',
     'director - Квентин Тарантино', 'rating - 8.6'],
    ['name: Бойцовский клуб', 'director: Дэвид Финчер', 'rating: 8.7'],
    ['name - Властелин колец: Братство Кольца', 'year - 2001', 'genre - фэнтези, приключения, драма, боевик',
     'director - Питер Джексон', 'rating - 8.6'],
    ['name: Назад в будущее', 'year: 1985', 'genre: фантастика, комедия, приключения',
     'director: Роберт Земекис'],
    {'name': 'Властелин колец: Две крепости', 'year': '2002', 'genre': 'фэнтези, приключения, драма, боевик',
     'director': 'Питер Джексон', 'rating': '8.6'},
    ('name: Иван Васильевич меняет профессию', 'year: 1973', 'genre: комедия, фантастика, приключения',
     'director: Леонид Гайдай', 'rating: 8.8'),
    ['year: 1994', 'genre: мультфильм, мюзикл, драма, приключения, семейный',
     'director: Роджер Аллерс', 'rating: 8.8'],
    ['name: Черная роза', 'year: 2014', 'genre: шлак',
     'director: Александр Невский', 'rating: 1.5'],
    ['name - Судный день: Носик в сметанке', 'year - 1999', 'genre - драма, фэнтези, кулинария, катастрофа',
     'director - Альфред Стилкок', 'rating - 9.1']
)

# продолжите решение здесь
lst = list()

for data in tpl:
    match data:
        case lst_data if isinstance(lst_data, list) and len(lst_data) >= 4 and 'name' in lst_data[0] and 'rating' in lst_data[-1]:
            replaced = [x.replace(' - ', ': ') for x in lst_data]
            if float(replaced[-1].split(': ')[1]) > 8.6:
                lst.append(replaced)

        case dct_data if isinstance(dct_data, dict) and {'name', 'rating'} and len(dct_data) >= 4 and float(dct_data.get('rating', 0)) > 8.6:
            temp_lst = list()
            for k, v in dct_data.items():
                temp_lst.append(f"{k}: {v}")
            lst.append(temp_lst)


print(*lst, sep='\n')
