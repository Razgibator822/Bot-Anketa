import telebot
from telebot import types
from data import load_user_data, save_user_data

token = "6923584798:AAEtQgtD4I2nFNIb0_axGfREEDiNeC37qvM"

bot = telebot.TeleBot(token)



data_path = "user_data.json"
user_data = load_user_data(data_path)



def first(message):
    if(message.text == "Да"):
        return "Да" in message.text

def first2(message):
    if(message.text == "Нет"):
        return "Нет" in message.text

def second(message):
    if(message.text == "Да ладно, до завтра погода может поменяться, синоптики часто ошибаются"):
       return "Да ладно, до завтра погода может поменяться, синоптики часто ошибаются" in message.text

def second2(message):
    if(message.text == "Останусь лучше дома"):
        return "Останусь лучше дома" in message.text

def height1(message):
    if(message.text == "Как я рад тебя видеть, дружище, уж думал случилось что"):
        return "Как я рад тебя видеть, дружище, уж думал случилось что" in message.text

def height2(message):
    if(message.text == "Да как он может со мной на встречу опаздывать?\U0001F621"):
        return "Да как он может со мной на встречу опаздывать?\U0001F621" in message.text

def material1(message):
    if(message.text == "О, ну ка, есть там что интересное или важное?"):
        return "О, ну ка, есть там что интересное или важное?" in message.text

def material2(message):
    if(message.text == "С опаской. Мало ли что там"):
        return "С опаской. Мало ли что там" in message.text


def pol(message):
    if(message.text == "Ой, надо друзьям написать, может еще не разошлись"):
        return "Ой, надо друзьям написать, может еще не разошлись" in message.text

def type1(message):
    if(message.text == "Синоптики как всегда косячат, почему не могут нормально свою работу выполнять?"):
        return "Синоптики как всегда косячат, почему не могут нормально свою работу выполнять?" in message.text

def type2(message):
    if(message.text == "Надо наверное в кафе сходить или еще куда, а то и правда холодно"):
        return "Надо наверное в кафе сходить или еще куда, а то и правда холодно" in message.text

def not_bad(message):
    if(message.text == "Ну и кто такой умник решил на улице гулять в такую погоду?"):
        return "Ну и кто такой умник решил на улице гулять в такую погоду?" in message.text



@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    global user_data
    user_data[message.chat.id] = {"name": message.from_user.full_name,
                                  "progress": ""}
    save_user_data(user_data, data_path)

    photo1_1 = open("msg731908148-21021.jpg", "rb")

    bot.send_photo(message.chat.id, photo1_1, f"Поздравляю {user_data[message.chat.id]['name']}! Вы только что были "
                   "зарегистрированы в анкете 'Насколько вы оптимист'! Вам предстоит ответить на несколько моих вопросов "
                   "чтобы узнать правду, вы готовы?", reply_markup=markup)


@bot.message_handler(commands=["help"])
def help(message):
    photo1_0 = open("msg731908148-21041.jpg", "rb")
    bot.send_photo(message.from_user.id, photo1_0, "/start - рестарт\n"
                                           "/help - помощь\n")


@bot.message_handler(commands=["progress"])
def progression(message):
    bot.send_message(message.chat.id, user_data[message.chat.id]['progress'])



@bot.message_handler(content_types=["text"], func=first)
def question(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cl1 = types.KeyboardButton("Да ладно, до завтра погода может поменяться, синоптики часто ошибаются")
    cl2 = types.KeyboardButton("Останусь лучше дома")
    markup.add(cl1, cl2)
    bot.send_message(message.from_user.id, "Отлично! Первый вопрос:\n"
                                            "Вы запланировали встречу с друзьями, а Вам пришло смс о том, что "
                                           "будет ужасная погода, какие будут Ваши мысли?", reply_markup=markup)


@bot.message_handler(content_types=["text"], func=first2)
def answer(message):
    bot.send_message(message.from_user.id, "На нет и суда нет. Ждем Вас в любое время!"
                                           "\U0001F648", reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(content_types=["text"], func=second)
def people_animatronics(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton("Как я рад тебя видеть, дружище, уж думал случилось что")
    bt2 = types.KeyboardButton("Да как он может со мной на встречу опаздывать?\U0001F621")
    markup.add(bt1, bt2)
    bot.send_message(message.from_user.id, 'Вы пошли с друзьями, однако один из них опаздал, Ваши мысли?'
                                           '', reply_markup=markup)


@bot.message_handler(content_types=["text"], func= second2)
def animals_animatronics(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cn1 = types.KeyboardButton("О, ну ка, есть там что интересное или важное?")
    cn2 = types.KeyboardButton("С опаской. Мало ли что там")
    markup.add(cn1, cn2)
    bot.send_message(message.from_user.id, "Вы остались дома, Вам приходят результаты Ваших "
                                           "мед анализов, какие Ваши мысли?", reply_markup=markup)


@bot.message_handler(content_types=["text"], func=height1)
def gender1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kn1 = types.KeyboardButton("Надо наверное в кафе сходить или еще куда, а то и правда холодно")
    kn2 = types.KeyboardButton("Ну и кто такой умник решил на улице гулять в такую погоду?")
    markup.add(kn1, kn2)
    bot.send_message(message.from_user.id, "Вы гуляете с друзьями, дождь все таки пошел, сильный ветер "
                                           "Ваши мысли?", reply_markup=markup)

#Человекоподобные: без щёчек: мужской (Бидибаб) или женский (Минирина)
@bot.message_handler(content_types=["text"], func=height2)
def gender(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kn1 = types.KeyboardButton("Ой, надо друзьям написать, может еще не разошлись")
    kn2 = types.KeyboardButton("Синоптики как всегда косячат, почему не могут нормально свою работу выполнять?")
    markup.add(kn1, kn2)
    bot.send_message(message.from_user.id, "Вы видите, что на улице днем уже ни облачка. Ваши мысли?"
                                           "", reply_markup=markup)




@bot.message_handler(content_types=["text"], func=type2)
def ty_pe2(message):
    photo = open("msg731908148-21146.jpg", "rb")
    bot.send_photo(message.chat.id, photo, "Вы во всем стараетесь видеть только хорошее."
                                           "Думаю, у Вас очень счастливая жизнь\U0001F601",
                   reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(content_types=["text"], func=not_bad)
def cirqus_baby(message):
    photo1 = open("Wie_wichtig_ist_ein_Feedback_im_Job.jpg", "rb")
    bot.send_photo(message.chat.id, photo1, "Вы на 70% оптимист, хороший результат"
                   , reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=type1)
def cirqus_baby(message):
    photo1 = open("1645033022_51-fikiwiki-com-p-kartinki-optimizm-57.jpg", "rb")
    bot.send_photo(message.chat.id, photo1, "Вы крайне пессимистично смотрите на жизнь\U00002639"
                   , reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=pol)
def cirqus_baby(message):
    photo1 = open("6d60d605-83ef-4144-a4ad-c5dca6e7b7d5.jpg", "rb")
    bot.send_photo(message.chat.id, photo1, "Вы крайне пессимистично смотрите на жизнь, однако и хорошие"
                                            " мысли Вам не чужда, держитесь за них и удачи)\U00002639"
                   , reply_markup=types.ReplyKeyboardRemove())

bot.polling()