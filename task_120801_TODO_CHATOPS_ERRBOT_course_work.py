# Вы работаете в операционном отделе DevOps. Пользователи отправляют вам различные вопросы по поводу доступа к используемым системам, а также ставят задачи. Управлять этим вручную становится неудобным, требуется автоматизация.
# При помощи фреймворка errbot необходимо создать чат-бота со следующей функциональностью:
# Любой пользователь может написать боту сообщение с вопросом. Сообщение помещается в очередь
# обращений. Пользователь получает от бота сообщение о том, что его обращение принято.
#
# Сотрудник отдела DevOps может при помощи команды /next взять первое сообщение из очереди
# в работу (модель FIFO). Далее при помощи команды /done <ответ> сотрудник может дать ответ.
# Ответ отобразится пользователю в боте, как новое сообщение. Также сотрудник при помощи
# команды /newtask может создать из обращения задачу в таск трекере. В этом случае
# отправившему обращение пользователю в чат с ботом приходит оповещение, что на основе его
# обращения была создана задача со ссылкой на задачу в таск трекере.
#
# Флоу следующий:
# 1) обращение пользователя
# 2) ответ пользователю, что сообщение принято
# 3) взятие в работу при помощи команды /next
# 4)  ответ через /done <ответ> или создание новой задачи через /newtask
# 5) оповещение пользователя о том, что дан ответ или создана задача через бота
#
# Также нужно создать команду, которая позволит управлять списком сотрудников отдела DevOps
# (через ID в мессенджере, например).
# Мессенджер - slack или telegram
# Для персистентности нужно использовать redis.

