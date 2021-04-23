# avito-assignment

Тестовое задание для программы стажировок в avito. Сервис для управления бронированием комнат. Проект был выполнен на FastApi, для общения с БД использовалась SQLAlchemy.

Запуск осуществляется командой `docker-compose up`

Доступные команды:
- `/rooms/create` - добавление комнаты. Описание комнаты передается в теле запроса параметрами `description` и `cost`.
   
    Пример вызова:
   ```
    curl -X POST "http://127.0.0.1:80/rooms/create" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "description=sgdfz&cost=5"
    ```
- `/rooms/list` - вывод списка комнат, выбор сортировки осуществляется параметрами запроса `sort_by` и `ascending`. `sort_by` принимает аргументы `date` и `cost`, `ascending`: `True` или `False`.

    Пример вызова:
    ```
    curl -X GET "http://127.0.0.1:80/rooms/list?sort_by=cost&ascending=true" -H  "accept: application/json"
    ```
- `/room/delete` - удаление комнаты, `id` комнаты передается в теле запроса.

    Пример вызова: 
    ```
    curl -X DELETE "http://127.0.0.1:80/room/delete" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "room_id=1"
    ```
- `/bookings/create` - создание брони. ID номера отеля, дата начала и дата окончания брони передаются в теле запроса аргументами `room_id`, `date_start` и `date_end`.

    Пример вызова:
    ```
    curl -X POST "http://127.0.0.1:80/bookings/create" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "room_id=1&date_start=2021-01-10&date_end=2021-01-15"
    ```
- `/bookings/delete` - удаление брони. В теле запроса передается ID брони.

    Пример вызова:
    ```
    curl -X DELETE "http://127.0.0.1:80/bookings/delete" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "booking_id=1"
    ```
- `/bookings/list` - вывод списка броней, ID номера передается параметром запроса `room_id`.
  
    Пример вызова:
    ```
    curl -X GET "http://127.0.0.1:80/bookings/list?room_id=1" -H  "accept: application/json"
    ```
