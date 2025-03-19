# В этом задании вам нужно создать свой простой API.
#
# В блоке "Работа с текстом в различных форматах" вы писали модуль для взаимодействия
# с системой мониторинга используемых услуг. Настала пора сделать из этого сервис.
#
# У сервиса должен быть вебхук, который обновляет информацию (парсит список используемых
# услуг и их цен).
#
# А также эндпоинты для:
#
#     расчёта и получения совокупной стоимости всего ресурса
#     расчёта и получения информации о количестве денег, которые были потрачены на
#     измерения ресурсов, которые было решено удалить (по RAM, по CPU и по NetFlow)
#     получения полного отчёта об используемых ресурсах в текстовой форме.
#
# А ещё данные хотелось бы персистировать, для этого можно использовать любое хранилище
# (локальный файл, sqlite, redis, mongo, etc.)
#
# Выглядит как большая задача. Это значит, что найден хороший повод её декомпозировать,
# тем более большинство кода вы уже написали, осталось сделать из него хендлеры.