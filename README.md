Тестовое задание для likesoft
-------------------------------
## <a id="title1">Платформа онлайн-библиотеки</a>

Для работы приложения необходимо:
__________________________________________________
Создать и заполнить файл ```.env``` по шаблону файла ```.env.sample```
Создать и заполнить файл ```.env.docker``` по шаблону файла ```.env.docker.sample```

Создать Docker контейнер командой:
```shell
docker-compose build
```
Запустить Docker контейнер командой:
```shell
docker-compose up
```
После выполнения команд произойдёт:
- создание контейнера, загрузка и собор всех необходимых образов
- запуск ```redis```
- создание базы данных и выполнение всех необходимых миграций
- запуск сервера на порту ```0.0.0.0:8000```
- запуск ```celery```
  
Для работы с админкой необходимо создать суперпользователя командой:
```shell
docker-compose exec -it <container_id> python manage.py csu
```
_____________________________________________________________
## <a id="title2">Логика работы</a>
- Для работы с API необходимо использовать сервис ```Postman```, либо аналоги.
- При регистрации пользователю на адрес электронной почты приходит сообщение с приветствием.
- Для работы с книгами реализован механизм ```CRUD```.
