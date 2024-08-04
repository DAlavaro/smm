# Команды для запуска celery и redis
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