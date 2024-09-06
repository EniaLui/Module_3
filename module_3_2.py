def send_email (message = '', recipient = '', *, sender = "university.help@gmail.com"):
    variants_end = (".com",".ru",".net")
    if -1 == recipient.find ('@') or -1 == sender.find('@') or not recipient.lower().endswith(variants_end) or not sender.lower().endswith(variants_end): #Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
        print ('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient, '.')
    elif recipient == sender:
        print ('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print ('Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient, '.')
    elif sender != 'university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, ' на адрес ', recipient, '.')



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')