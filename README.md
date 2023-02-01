# Тестовое задание на позицию Наставника SkyPro

## *Стек технологий:*
1. Python 3.11
2. Django 4.1.5
3. Django REST Framework 3.14
4. Django environ 0.9

### Для запуска необходимо:

- Создать .env файл в корне проекта и заполнить его данными по примеру файла .env_example. Файл можно не создавать, если не хотите, тогда проект воспользуется настройками по умолчанию;
- Установить зависимости комнадой 
```
pip install -r requirements.txt
```

#### В случае запуска в режиме *DEBUG = False* выполнить следующие команды:
```
python manage.py collectstatic
python manage.py migrate
python manage.py runserver --insecure
```

#### В случае запуска в режиме *DEBUG = True* выполнить следующие команды:
```
python manage.py migrate
python manage.py runserver
```

#### В проекте доступны следующие URL адреса:
| Описание запроса                                                  |                      Пример                      | 
|-------------------------------------------------------------------|:------------------------------------------------:| 
| _Получить список резюме, принадлежащих пользователю_              |       GET - http://127.0.0.1:8000/resume/        | 
| _Получить данные конкретного резюме, принадлежащего пользователю_ |     GET - http://127.0.0.1:8000/resume/<id>/     | 
| _Внести изменения в конкретное резюме принадлежащее пользователю_ |   PATCH - http://127.0.0.1:8000/resume/<id>/     | 

####  *Для доступа ко всем URL необходимо авторизоваться. В проекте используется Basic Auth*

#### Для ручного тестирования API через средcтва DRF или Postman в существующей в проекте БД создан пользователь:
*login:* devops_user, *password:* 12345678qwerty

#### Для запуска тестов, написанных на соответсвующие url необходимо выполнить команду:
```
python manage.py test
```



