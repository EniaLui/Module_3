calls = 0
def count_calls():  #Создать функцию count_calls и изменять в ней значение переменной calls.
    global calls
    calls += 1

def string_info (n=''): #Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    count_calls()
    return (len(n),n.upper(),n.lower())

def is_contains (string, list_to_search): #Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
    count_calls()
    for i in list_to_search:
        new = [j.lower() for j in list(list_to_search)]
        if str(string.lower()) in new:
            return True
        else:
            return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)