import telebot
import requests
import json

api = 'trnsl.1.1.20200315T093820Z.ee6bad7b49c9840f.e1ab8887d49bbc5cbedecfea656325b40f157e4a'
token = '454097555:AAEKr150Vp4LBWpvJjmNHfLwNnj9S4jLe1A'
bot = telebot.TeleBot(token)
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    usertext = message.text
    myObj = {'key': api, 'text': usertext, 'lang': 'en-kk'}

    x = requests.post(url, data=myObj)
    response = json.loads(x.text)["text"][0]
    final = response.replace("я", "ıa").replace("э", "e").replace("Э", "E").replace("Я", "Ia").replace("ю",
                                                                                                       "ıý").replace(
        "Ю", "Iý").replace("ц",
                           "ts").replace(
        "а", "a").replace("ә", "á").replace("б", "b").replace("д", "d").replace("е",
                                                                                "e").replace(
        "ф", "f").replace("г", "g").replace("ғ", "ǵ").replace("х", "h").replace("һ", "h").replace("і",
                                                                                                  "i").replace(
        "и", "ı").replace("й", "ı").replace("ж", "j").replace("к", "k").replace("л", "l").replace("м",
                                                                                                  "m").replace(
        "н", "n").replace("ң", "ń").replace("о", "o").replace("ө", "ó").replace("п", "p").replace("қ",
                                                                                                  "q").replace(
        "р", "r").replace("с", "s").replace("ш", "sh").replace("щ", "sh").replace("ч", "ch").replace("т",
                                                                                                     "t").replace(
        "ұ", "u").replace("ү", "ú").replace("в", "v").replace("ы", "y").replace("у", "ý").replace("з",
                                                                                                  "z").replace(
        "ь", "").replace("ъ", "").replace("Ъ", "").replace("Ь", "").replace("А", "A").replace("Ә", "Á").replace(
        "Б",
        "B").replace(
        "Д",
        "D").replace(
        "Е", "E").replace("Ф", "F").replace("Г", "G").replace("Ғ", "Ǵ").replace("Х", "H").replace("І",
                                                                                                  "I").replace(
        "Й", "I").replace("И", "I").replace("Ж", "J").replace("К", "K").replace("Л", "L").replace("М",
                                                                                                  "M").replace(
        "Н", "N").replace("Ң", "Ń").replace("О", "O").replace("Ө", "Ó").replace("П", "P").replace("Қ",
                                                                                                  "Q").replace(
        "Р", "R").replace("С", "S").replace("Ш", "Sh").replace("Щ", "Sh").replace("Ч", "Ch").replace("Т",
                                                                                                     "T").replace(
        "Ұ", "U").replace("Ү", "Ú").replace("В", "V").replace("Ы", "Y").replace("У", "Ý").replace("З",
                                                                                                  "Z").replace(
        "ё", "е").replace("Ё", "E")
    bot.send_message(message.chat.id, final)


if __name__ == '__main__':
    bot.polling(none_stop=True)
