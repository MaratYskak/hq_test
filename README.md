# Документация по API

Это документация описывает, как взаимодействовать с нашим RESTful API для управления уроками и продуктами.
Каждый запрос в систему сопровождается заголовками и набором параметров.

Обязательными заголовками являются следующие:</br>
• Content-Type – тип тела запроса, соответствующий стандарту MIME. Данный заголовок должен соответствовать зарегистрированному значению application/vnd.api+json</br>
• X-Auth-Token – токен авторизации. Уникальный идентификатор, позволяющий получить доступ к программному интерфейсу. Сгенерировать токен авторизации можно самостоятельно через:</br>
POST   /api/token/
POST   /api/token/refresh/

Request body</br>
{</br>
  "username": "string",</br>
  "password": "string"</br>
}</br>

Response body</br>
{</br>
  "refresh": "eyJhbGcaCIsImV4cCI6MTY5NTM2ODMxMiwiaWF0IjoxNjk1MjgxOTEyLCJqdGkiOiI4YWJkODgwZTUxNTI0ZGU0OTcxOGFhNGFkOGExYjlmZCIsInVzZXJfaWQiOjF9.F-JusNw-YHJwhciGwxlfDQ0jqQSRXylxgOk4qMEsUnY",</br>
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlCJpYXQiOjE2OTUyODE5MTIsImp0aSI6ImFjYzI4NmZkODgxMjRmOWI4OWE0OWZjYzI4ZWViOThjIiwidXNlcl9pZCI6MX0.A-TmpmxjDeoOS3J5swmVPW0-fnXI5pbWCsXCprD_Hak"</br>
}</br>


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




