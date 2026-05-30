import spacy # Чтобы все норм работало, надо через терминал установить эту библиотеку
import os
import re

class Letter:
    def __init__(self, text):
        self.text = text
        self.set_strange_words_num(self)
        self.set_shift_letters_num(self)
        self.set_exclam_marks_num(self)

    def set_shift_letters_num(self):
        #shift_letters_num = 0

        text = self.text
        upper = sum(1 for c in text if c.isupper())
        total = sum(1 for c in text if c.isalpha())
        self._shift_letters_num = upper / total if total > 0 else 0
        # Тут надо написать функцию, которая считает отношение букв верхнего регистра к общему числу букв
        #self._shift_letters_num = shift_letters

    def set_exclam_marks_num(self):
        #exclam_marks_num = 0

        text = self.text
        if len (text) == 0:
            return 0
        exclam_count = text.count('!')
        self.exclam_marks_num = exclam_count/len(text)
        # Тут надо написать функцию, которая считает отношение кол-ва "!" ко всем символам
        #self._exclam_marks_num = exclam_marks_num
        
    doc = nlp(self.text)
    lemmas_list = []
    for lemma in doc:
        lemmas_list.append(token.lemma_)

    def count_strange_words_num(self):
        strange_words_num = 0
        # Тут надо прописать функцию, которая считает отношение "спам-слов" к вообще всем словам в тексте.
        self._strange_words_num = strange_words_num

    def is_spam(self):
        fl = False
        comment = ""
        if self._shift_letters_num >= 0.05:
            fl = True
            comment += "Это письмо может быть спамом, так как в нём много слов в верхнем регистре"
        if self._exclam_marks_num >= 0.005:
            fl = True
            comment += "Это письмо может быть спамом, так как в нём много восклицательных знаков"
        if self._strange_words_num >= 0.05:
            fl = True
            comment += "Это письмо может быть спамом, так как в нём много характерных для спама слов"

        return fl, comment


        # Это итоговая функция, которая будет вовзращать ответ: спам/не спам + краткий комментарий

def get_letter_by_user(self, user_file_name):
    f = open(user_file_name)
    self.text = f.read()
    f.close()
    # Эта функция по имени файла, которое ввел пользователь, должна либо поднять ошибку, если такого файла нет,
    # либо вернуть текст
    # Для проверки расширений мб пригодятся регулярки (библиотека re)
    # Сначала надо проверить, что расширение у имени файла, которое ввёл пользователь .txt
    # Если .txt ==> искать по папкам. Если ничего не нашлось ==> поднять ошибку.
    # Если пользователь не указал расширение/указал, но забыл какую-то часть (e.g. name.tx), то добавить недостающее
    # Затем проделать то же самое, что и для файлов .txt
    # Если же расширение уже есть, но оно не .txt ==> пока что поднимаем ошибку

    # return text - как-то так должна выглядеть строка с возвратом результата

