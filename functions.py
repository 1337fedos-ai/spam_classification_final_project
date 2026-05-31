import spacy # Чтобы все норм работало, надо через терминал установить эту библиотеку
import os
import re

class Letter:
    def __init__(self, text, lang):
        self.text = text
        self.set_strange_words_num(self)
        self.set_shift_letters_num(self)
        self.set_exclam_marks_num(self)
        self._lang = lang


    # Shift letters ratio in the text
    def set_shift_letters_num(self):
        text = self.text
        upper = sum(1 for c in text if c.isupper())
        total = sum(1 for c in text if c.isalpha())
        self._shift_letters_num = upper / total if total > 0 else 0


    #Exclamation marks ratio in the text
    def set_exclam_marks_num(self):
        text = self.text
        if len (text) == 0:
            return 0
        exclam_count = text.count('!')
        self.exclam_marks_num = exclam_count/len(text)


    #Spam words ratio in the text
    def count_strange_words_num(self):
        if self._lang == 'русский':
            lemmas_list = lemmatize_russian(self.text)
        else:
            lemmas_list = lemmatize_english(self.text)
        strange_words = sum (1 for c in lemmas_list if (c + "\n") in 'strange_words.txt')
        self._strange_words_num = strange_words / len(lemmas_list)


    #Final function
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


def lemmatize_russian(text):
    nlp = spacy.load("ru_core_news_sm")
    doc = nlp(text)
    lemmas_list = []
    for token in doc:
        lemmas_list.append(token.lemma_)
    return lemmas_list


def lemmatize_english(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    lemmas_list = []
    for token in doc:
        lemmas_list.append(token.lemma_)
    return lemmas_list


def get_letter_by_user(self, user_file_name):
    # Эта функция по имени файла, которое ввел пользователь, должна либо поднять ошибку, если такого файла нет,
    # либо вернуть текст
    # Для проверки расширений мб пригодятся регулярки (библиотека re)
    # Сначала надо проверить, что расширение у имени файла, которое ввёл пользователь .txt
    # Если .txt ==> искать по папкам. Если ничего не нашлось ==> поднять ошибку.
    # Если пользователь не указал расширение/указал, но забыл какую-то часть (e.g. name.tx), то добавить недостающее
    # Затем проделать то же самое, что и для файлов .txt
    # Если же расширение уже есть, но оно не .txt ==> пока что поднимаем ошибку
    f = open(user_file_name)
    self.text = f.read()
    f.close()


