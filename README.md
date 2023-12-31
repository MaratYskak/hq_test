# Документация по API

Это документация описывает, как взаимодействовать с нашим RESTful API для управления уроками и продуктами.
Каждый запрос в систему сопровождается заголовками и набором параметров.

Обязательными заголовками являются следующие:</br>
• Content-Type – тип тела запроса, соответствующий стандарту MIME. Данный заголовок должен соответствовать зарегистрированному значению application/vnd.api+json</br>
• X-Auth-Token – токен авторизации. Уникальный идентификатор, позволяющий получить доступ к программному интерфейсу. Сгенерировать токен авторизации можно самостоятельно через:</br>
POST   /api/token/</br>
POST   /api/token/refresh/

### Пример запроса
```json
{
  "username": "string",
  "password": "string"
}
```

### Пример ответа
```json
{
  "refresh": "yourtoken",
  "access": "yourtoken"
}
```


## Получение списка уроков

GET  /api/lesson-status/


### Пример ответа

```json
[
  {
    "viewed": true,
    "viewed_time_seconds": 81,
    "user": 1,
    "lesson": 1,
    "last_viewed_at": "2023-09-21T09:02:02.750767Z"
  },
  {
    "viewed": false,
    "viewed_time_seconds": 50,
    "user": 1,
    "lesson": 2,
    "last_viewed_at": "2023-09-21T09:02:02.750767Z"
  },
  {
    "viewed": false,
    "viewed_time_seconds": 10,
    "user": 1,
    "lesson": 3,
    "last_viewed_at": "2023-09-21T09:02:02.750767Z"
  }
]
```

## Записать пользователя на урок или обновить данные о просмотре урока
POST /api/subscribe/

### Пример запроса
```json
{
  "viewed_time_seconds": 0,
  "user": id,
  "lesson": id
}
```
### Пример ответа

```json
{
  "viewed_time_seconds": 0,
  "user": 1,
  "lesson": 3
}
```

## для отображения статистики по продуктам
GET /api/stats/

### Пример ответа

```json
[
  {
    "id": 1,
    "name": "test_product_1",
    "total_views": 1,
    "total_view_time": 81,
    "total_students": 1,
    "purchase_percentage": 50
  },
  {
    "id": 3,
    "name": "product_of_user_2",
    "total_views": 0,
    "total_view_time": null,
    "total_students": 0,
    "purchase_percentage": 0
  }
]
```





