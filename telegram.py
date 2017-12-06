import telebot

token = '454097555:AAEKr150Vp4LBWpvJjmNHfLwNnj9S4jLe1A'
bot = telebot.TeleBot(token)


def is_ascii(s):
    return all(ord(c) < 128 for c in s)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    usertext = message.text
    if is_ascii(usertext):
        bot.send_message(message.chat.id, 'Ваш текст не является кириллицей')
    elif message.text == 'ь':
        bot.send_message(message.chat.id, 'Эти буквы не переводятся')
    elif message.text == 'Ь':
        bot.send_message(message.chat.id, 'Эти буквы не переводятся')
    elif message.text == 'Ъ':
        bot.send_message(message.chat.id, 'Эти буквы не переводятся')
    elif message.text == 'ъ':
        bot.send_message(message.chat.id, 'Эти буквы не переводятся')
    else:
        final = message.text.replace("я", "i'a").replace("э", "e").replace("Э", "E").replace("Я", "I'a").replace("ю",
                                                                                                                 "i'y").replace(
            "Ю", "I'y").replace("ц",
                                "ts").replace(
            "а", "a").replace("ә", "a'").replace("б", "b").replace("д", "d").replace("е",
                                                                                     "e").replace(
            "ф", "f").replace("г", "g").replace("ғ", "g'").replace("х", "h").replace("һ", "h").replace("і",
                                                                                                       "i").replace(
            "и", "i'").replace("й", "i'").replace("ж", "j").replace("к", "k").replace("л", "l").replace("м",
                                                                                                        "m").replace(
            "н", "n").replace("ң", "n'").replace("о", "o").replace("ө", "o'").replace("п", "p").replace("қ",
                                                                                                        "q").replace(
            "р", "r").replace("с", "s").replace("ш", "s'").replace("щ", "s'").replace("ч", "c'").replace("т",
                                                                                                         "t").replace(
            "ұ", "u").replace("ү", "u'").replace("в", "v").replace("ы", "y").replace("у", "y'").replace("з",
                                                                                                        "z").replace(
            "ь", "").replace("ъ", "").replace("Ъ", "").replace("Ь", "").replace("А", "A").replace("Ә", "A'").replace(
            "Б",
            "B").replace(
            "Д",
            "D").replace(
            "Е", "E").replace("Ф", "F").replace("Г", "G").replace("Ғ", "G'").replace("Х", "H").replace("І",
                                                                                                       "I").replace(
            "Й", "I'").replace("И", "I'").replace("Ж", "J").replace("К", "K").replace("Л", "L").replace("М",
                                                                                                        "M").replace(
            "Н", "N").replace("Ң", "N'").replace("О", "O").replace("Ө", "O'").replace("П", "P").replace("Қ",
                                                                                                        "Q").replace(
            "Р", "R").replace("С", "S").replace("Ш", "S'").replace("Щ", "S'").replace("Ч", "C'").replace("Т",
                                                                                                         "T").replace(
            "Ұ", "U").replace("Ү", "U'").replace("В", "V").replace("Ы", "Y").replace("У", "Y'").replace("З",
                                                                                                        "Z").replace(
            "ё", "е").replace("Ё", "E")

        bot.send_message(message.chat.id, final)



if __name__ == '__main__':
    bot.polling(none_stop=True)