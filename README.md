## **ABOUT REALISATION:**
В проекте secure_t_test есть приложение posts с описанием всех моделей 'блога', для которых реализован API

Для удобства вся логика API вынесена в отдельное приложение - 'api'

API доступен только аутентифицированным пользователям. В проекте аутентификация проходит по токену TokenAuthentication.

Аутентифицированный пользователь авторизован на изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.


## **QUICK START:**
*(для пользователей операционных систем семейства MacOs/Linux):*
  Открыть терминал или консоль и перейти в нужную Вам директорию
  Прописать команду git clone https://github.com/catsoup1337/secure_t_test.git

  Перейти в директорию secure_t_test

  Прописать следующие команды:

  python3 -m venv venv
  
  source venv/bin/activate

  pip install -r requirements.txt
  
  python manage.py makemigrations
  
  python manage.py migrate
  
  Запустить сервер - python manage.py runserver


## **API DOCUMENTATION:**

api/v1/user_create/ (POST): создание пользователя data = [username, password]

api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.

api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.

api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.

api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с  id=post_id или создаём новый, указав id поста, который хотим прокомментировать.

api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.

api/v1/posts/{post_id}/comments/{comment_id}/threads/ (GET, POST): получаем список всех тредов под комментарием с id=comment_id или создаём новый, указав id комментария, к которому хотим добавить комментарий.

api/v1/posts/{post_id}/comments/{comment_id}/threads/{thread_id} (GET, PUT, PATCH, DELETE):получаем, редактируем или удаляем комментарий по id внутри треда (ветви коментария) с id=comment_id
