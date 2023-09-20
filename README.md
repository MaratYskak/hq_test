# Документация по API

Это документация описывает, как взаимодействовать с нашим RESTful API для управления уроками и продуктами.

## Авторизация

GET   /api/token

Request body
{
  "username": "string",
  "password": "string"
}


## Получение списка уроков

GET  /api/lesson-status/


### Пример ответа

```json
[
  {
    "id": 1,
    "viewed": true,
    "viewed_time_seconds": 81,
    "user": 1,
    "lesson": 1
  }
]




