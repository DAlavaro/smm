# Инструкция по запуску
1. Создать базу данных с именем smm
2. Выполнить команды 
```shell
python manage.py makemigrations
```
```shell
python manage.py migrate
```
3. Наполнить данными blog
```shell
python manage.py loaddata blog.json
```
4. Выдать права менеджеру и контент-менеджеру
```shell
python manage.py cmg
```
5. Создать тестовых супер-пользователя, менеджера и контент-менеджера
```shell
python manage.py csu
```
#### супер-пользователь
- Логин: admin@sky.pro
- Пароль: admin
#### менеджер
- Логин: manager@sky.pro
- Пароль: manager
#### контент-менеджер
- Логин: content_manager@sky.pro
- Пароль: content_manager
6. Команды для запуска celery и redis, всё выполнить в отдельных вкладках терминала
- Запуск Redis
```shell
redis-server
```
- Запуск celery
```shell
celery -A config worker -l info
```
- Запуск celery-beat
```shell
celery -A config beat -l INFO
```