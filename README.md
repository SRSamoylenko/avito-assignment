# avito-assignment

1. Запуск осуществляется командой "docker-compose up"
2. Добавление комнаты осуществляется командой "/rooms/create" описание комнаты передается в теле запроса параметрами description и cost.
Пример: curl -X POST "http://localhost:8000/rooms/create" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "description=sgdfz&cost=5"
3. Вывод списка комнат осуществияется командой "/rooms/list", выбор сортировки осуществляется параметрами запроса sort_by и ascending. sort_by принимает аргументы date и cost, ascending: True или False
Пример: curl -X GET "http://localhost:8000/rooms/list?sort_by=cost&ascending=true" -H  "accept: application/json"
Удаление комнаты осуществляется командой "/room/delete", id комнаты передается в теле запроса.
Пример: curl -X DELETE "http://localhost:8000/room/delete" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "room_id=1"
