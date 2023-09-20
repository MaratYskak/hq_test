# Документация по API

Это документация описывает, как взаимодействовать с нашим RESTful API для управления уроками и продуктами.

## Авторизация

/api/token

Request body
{
  "username": "string",
  "password": "string"
}


## Получение списка уроков

### URL


### Описание

Этот запрос позволяет получить список всех доступных уроков.

### Параметры

- Нет.

### Пример запроса


GET /api/lessons/
Authorization: Token ваш_токен


### Пример ответа

```json
[
    {
        "id": 1,
        "name": "Урок 1",
        "video_link": "https://www.example.com/lesson1",
        "duration_seconds": 1200,
        "products": [1, 2]
    },
    {
        "id": 2,
        "name": "Урок 2",
        "video_link": "https://www.example.com/lesson2",
        "duration_seconds": 1800,
        "products": [2, 3]
    }
]


Пометить урок как просмотренный
URL

POST /api/lessons/{lesson_id}/mark-as-viewed/


Описание
Этот запрос позволяет пометить урок как просмотренный для текущего пользователя.

Параметры
lesson_id: Идентификатор урока, который нужно пометить как просмотренный.
Пример запроса

POST /api/lessons/1/mark-as-viewed/
Authorization: Token ваш_токен


{
    "message": "Урок помечен как просмотренный."
}


