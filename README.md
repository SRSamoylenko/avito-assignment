# avito-assignment

1. Запуск осуществляется командой "docker-compose up"
2. Добавление комнаты осуществляется командой "/rooms/create" описание комнаты передается в теле запроса параметрами description и cost.
Пример: curl -X POST "http://localhost:8000/rooms/create" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "description=sgdfz&cost=5"
3. Вывод списка комнат осуществияется командой "/rooms/list", выбор сортировки осуществляется параметрами запроса sort_by и ascending. sort_by принимает аргументы date и cost, ascending: True или False
Пример: curl -X GET "http://localhost:8000/rooms/list?sort_by=cost&ascending=true" -H  "accept: application/json"
Удаление комнаты осуществляется командой "/room/delete", id комнаты передается в теле запроса.
Пример: curl -X DELETE "http://localhost:8000/room/delete" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "room_id=1"
4. Создание брони осуществляется командой "/bookings/create". ID номера отеля, дата начала и дата окончания брони передаются в теле запроса аргументами room_id, date_start и date_end
Пример: curl -X POST "http://localhost:8000/bookings/create" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "room_id=1&date_start=2021-01-10&date_end=2021-01-15"
5. Удаление брони осуществляется командой "/bookings/delete", в теле запроса передается ID брони
Пример: curl -X DELETE "http://localhost:8000/bookings/delete" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "booking_id=1"
6. Вывод списка броней осуществляется командой "/bookings/list", ID номера передается параметром запроса room_id
Пример: curl -X GET "http://localhost:8000/bookings/list?room_id=1" -H  "accept: application/json"

В ходе выполнения задания оказалось, что веб-сервер обращается к серверу с базой данных до того, как тот успевает развернуться, что приводит к ошибкам. Для решения этой проблемы веб-сервер отправляется в сон на 10 секунд сразу после старта программы, что гарантирует, что к моменту его первого обращения к базе данных, та уже будет работать.
