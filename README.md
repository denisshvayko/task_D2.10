# task_D2.10
work with server

1. Вставьте свой токен от sentry в конфиг фай config.py
2. Зарегестрируйтесь на heroku
3. Создайте новый репозиторий под проект на github
4. Cделайте commit и push данного проекта на github
5. После выполните в терминале/(командной строке) команду heroku create из директории где находится сервер
6. Введите в терминале/(командной строке) логин и пароль от heroku, после данного этапа создасться приложение на heroku
7. Далее в терминале/(командной строке) выполните команды:
    git push heroku master
    heroku ps:scale web=1
    heroku config:set APP_LOCATION=heroku
8. Если Вы все сделали правильно то сможете открыть ссылку <название-приложения>.herokuapp.com/ и убедится что все работает.
9. И проверить логи в sentry

В случае, если лень с этим разбираться и ты просто хочешь проверить работоспособность кода, ссылка для перехода на мое созданное приложение.
https://safe-mountain-57183.herokuapp.com/ (помни что нужно подождать 40 секунд перед тем как сервер включится в первйо итерации)
К сожалению доступ к sentry дать не могу, так что либо придеться все самому сделать, либо поверить что оно работает.=)