import requests
# устанивливаем requirements pip install -r requirements.txt
# запускаем monitoring module через терминал python monitoring_module.py

# в задании уже использовали curl, чтобы получать информацию от модуля мониторинга.
# Самое время использовать модуль requests, чтобы выполнить HTTP-запрос внутри вашего приложения.

def main():
    input_data = input() # input_data = requests.get(base_url)
    print(input_data[:100])

def main_post():
    base_url = 'http://127.0.0.1:21122/monitoring/infrastructure/using/summary/1'
    input_data = requests.get(base_url)

    print(input_data.text)

    # return response

if __name__ == "__main__":
    #main()
    main_post()


# чтобы перелвть результаты работы мониторинга, вводим во 2ом терминале
    # curl 127.0.0.1:21122/monitoring/infrastructure/using/summary/1 | python task_040601_course_work.py