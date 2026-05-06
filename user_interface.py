import functions

user_file_name = input("Пожалуйста, введите имя файла с расширением .txt, который содержит текст вашего письма")

try:
    functions.get_letter_by_user(user_file_name)
except Exception:
    pass
else:
    user_letter = functions.Letter(user_file_name)
    print(functions.is_spam(user_letter))
finally:
    pass