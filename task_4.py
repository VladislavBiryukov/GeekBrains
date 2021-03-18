"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""
#1 O(n) - линейная
def authorization_1(users, user_name, user_password):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return "Добро пожаловать!"
            elif value['password'] == user_password and not value['activation']:
                return "Учетная запись не активна!"
            elif value['password'] != user_password:
                return "Пароль не верный"
        return "Данного пользователя не существует"
#2 O(1) - постоянная
def authorization_2(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['activation']:
            return "Добро пожаловать!"
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:
            return "Учетная запись не активна!"
        elif users['password'] != user_password:
            return "Пароль не верный"
        else:
            return "Данного пользователя не существует"
my_users = {'user1' : {'pass': '1111', 'activation' : True},
            'user2' : {'pass': '1111', 'activation' : False},
            'user3' : {'pass': '1111', 'activation' : True},
            'user4' : {'pass': '1111', 'activation' : False}
           }
print(authorization_2(my_users, 'user6', '1111'))


# Второе решение будет лучше, так как в ней отсутствует цикл.