import telebot
from telebot import types


bot = telebot.TeleBot('1624421016:AAGbVKnT4O60i57Mwt7qNBFlzRqTgmKe2rM')

markup_menu = types.InlineKeyboardMarkup(row_width=1)
btn_address = types.InlineKeyboardButton('🎁 Магазин', callback_data='magaz')
btn_delivery = types.InlineKeyboardButton('Сообщить о проблеме 🆘', callback_data='problem')
markup_menu.add(btn_address, btn_delivery)

markup_assort = types.InlineKeyboardMarkup(row_width=1)
btn_alfapvp1 = types.InlineKeyboardButton('💎 AlfaРVР Blue 0.5г - 1000р.', callback_data='alfapvp1')
btn_alfapvp2 = types.InlineKeyboardButton('💎 AlfaРVР Blue 1г - 1500р', callback_data='alfapvp2')
btn_mef = types.InlineKeyboardButton('🧬 Mefedrone 1г - 1000р', callback_data='mef')
btn_amf = types.InlineKeyboardButton('❄️Аmfеtamin LUX 1г - 1000р', callback_data='amf')
btn_lsd = types.InlineKeyboardButton('💊 Марка LSD-25 1шт(220 мкг) - 800р', callback_data='lsd')
btn_boshki1 = types.InlineKeyboardButton('🥦 Бошки AK-47 1г - 1000р', callback_data='boshki1')
btn_boshki2 = types.InlineKeyboardButton('🥦 Бошки AK-47 2г - 1800р', callback_data='boshki2')
btn_cannab1 = types.InlineKeyboardButton('☘️Cannabis 1 коробок(3г) - 700р', callback_data='cannab1')
btn_cannab2 = types.InlineKeyboardButton('☘️Cannabis 2 коробка(6г) - 1200р', callback_data='cannab2')
markup_assort.add(btn_alfapvp1, btn_alfapvp2, btn_mef, btn_amf, btn_lsd, btn_boshki1, btn_boshki2, btn_cannab1, btn_cannab2)


markup_raion = types.InlineKeyboardMarkup(row_width=2)
btn_sokol = types.InlineKeyboardButton('Сокол', callback_data='sokol')
btn_neft = types.InlineKeyboardButton('Нефтебаза', callback_data='neft')
btn_nlmk = types.InlineKeyboardButton('НЛМК', callback_data='nlmk')
btn_9go = types.InlineKeyboardButton('Район рынка 9го', callback_data='9go')
btn_opit = types.InlineKeyboardButton('Опытная', callback_data='opit')
btn_cr = types.InlineKeyboardButton('Район ЦР', callback_data='cr')
btn_manej = types.InlineKeyboardButton('Манеж', callback_data='manej')
btn_cum = types.InlineKeyboardButton('Район ЦУМа', callback_data='cum')
btn_kolc = types.InlineKeyboardButton('Кольцевая', callback_data='kolc')
btn_evr = types.InlineKeyboardButton('Европейский', callback_data='evr')
btn_elec = types.InlineKeyboardButton('Елецкий', callback_data='elec')
btn_rudn = types.InlineKeyboardButton('Сырский рудник', callback_data='rudn')
btn_mjk = types.InlineKeyboardButton('МЖК', callback_data='mjk')
btn_ltz = types.InlineKeyboardButton('ЛТЗ', callback_data='ltz')
markup_raion.add(btn_sokol, btn_neft, btn_nlmk, btn_9go, btn_opit, btn_cr,
                btn_manej, btn_cum, btn_kolc, btn_evr, btn_elec, btn_rudn, btn_mjk, btn_ltz)


markup_payment = types.InlineKeyboardMarkup(row_width=1)
btn_qiwicash = types.InlineKeyboardButton('Пополнение QIWI кошелька', callback_data='qiwicash')
btn_qiwipay = types.InlineKeyboardButton('Перевод на QIWI кошелёк', callback_data='qiwipay')
btn_card = types.InlineKeyboardButton('Перевод на банковскую карту', callback_data='card')
markup_payment.add(btn_qiwicash, btn_qiwipay, btn_card)

markup_pay = types.InlineKeyboardMarkup(row_width=1)
btn_yes = types.InlineKeyboardButton('Да, перейти к оплате 🔐', callback_data='yes')
btn_no = types.InlineKeyboardButton('Нет, начать заново ↪', callback_data='no')
markup_pay.add(btn_yes, btn_no)

markup_payed = types.InlineKeyboardMarkup(row_width=2)
btn_payed = types.InlineKeyboardButton('Оплачено ✅', callback_data='payed')
btn_back = types.InlineKeyboardButton('Отмена 🚫', callback_data='back')
markup_payed.add(btn_payed, btn_back)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    sti = open('/home/vladimir/bot/stock/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, 'Добро пожаловать в наш магазин', reply_markup=markup_menu)


@bot.message_handler(func=lambda message: True)
def send(message):
    if message.text == '':
        bot.send_message(message.chat.id, '')
    else:
        bot.send_message(message.chat.id, 'Ваше обращение зарегистрировано. '
                                          'В ближайшее время с Вами свяжется наш сотрудник и мы всё уладим 🙂\n'
                                          'Нажмите /start для возврата к начальному меню')


@bot.callback_query_handler(func=lambda call: True)
def callback_stuff(call):
    global staff
    global msg
    global price
    global payment
    global pay
    global raion
    global img
    global gif
    global mesg
    global messg
    if call.data == 'magaz':
        bot.send_message(call.message.chat.id, 'Вот, что мы можем тебе предложить', reply_markup=markup_assort)
    elif call.data == 'problem':
        bot.send_message(call.message.chat.id, 'Пожалуйста, опишите проблему с которой Вы столкнулись\n ⬇⬇⬇⬇⬇⬇', KeyboardInterrupt)
    elif call.data == 'alfapvp1':
        img = 'https://hydra-ng.org/uploads/products/187/43fe73dcf111b07875afd8f3f4f3881b.jpg'
        staff = 'AlfaРVР Blue 0.5г'
        price = '1000р'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                    'Пожалуйста, выберите наиболее подходящий район ⬇⬇⬇'),
                         reply_markup=markup_raion, parse_mode='Markdown')
    elif call.data == 'alfapvp2':
        img = 'https://hydra-ng.org/uploads/products/187/43fe73dcf111b07875afd8f3f4f3881b.jpg'
        staff = 'AlfaРVР Blue 1г'
        price = '1500р'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                    'Пожалуйста, выберите наиболее подходящий район ⬇⬇⬇'),
                         reply_markup=markup_raion, parse_mode='Markdown')
    elif call.data == 'mef':
        img = 'https://centr-zdoroviya.ru/wp-content/uploads/2018/08/cherez-skolko-proxodit-lomka-ot-mefedrona-360x240.jpg'
        staff = 'Mefedrone 1г'
        price = '1000р'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                    'Пожалуйста, выберите наиболее подходящий район ⬇⬇⬇'),
                         reply_markup=markup_raion, parse_mode='Markdown')
    elif call.data == 'amf':
        img = 'https://tvsatcom.bg/content/uploads/amfetamin.jpeg'
        staff = 'Amfetamin LUX 1г'
        price = '1000р'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                    'Пожалуйста, выберите наиболее подходящий район ⬇⬇⬇'),
                         reply_markup=markup_raion, parse_mode='Markdown')
    elif call.data == 'lsd':
        img = 'https://files.merryjane.com/uploads/generic/1571084343915_a1chanelacidwide.jpg'
        staff = 'Mаркa LSD-25 1шт(220 мкг)'
        price = '800р'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                    'Пожалуйста, выберите наиболее подходящий район ⬇⬇⬇'),
                         reply_markup=markup_raion, parse_mode='Markdown')
    elif call.data == 'boshki1':
        img = 'https://imgp.golos.io/0x0/http://localpics.ru/images/1776119_konoplya-boshki.jpg'
        staff = 'Бошки AK-47 1г'
        price = '1000р'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                    'Пожалуйста, выберите наиболее подходящий район ⬇⬇⬇'),
                         reply_markup=markup_raion, parse_mode='Markdown')
    elif call.data == 'boshki2':
        img = 'https://imgp.golos.io/0x0/http://localpics.ru/images/1776119_konoplya-boshki.jpg'
        staff = 'Бошки AK-47 2г'
        price = '1800р'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                    'Пожалуйста, выберите наиболее подходящий район ⬇⬇⬇'),
                         reply_markup=markup_raion, parse_mode='Markdown')
    elif call.data == 'cannab1':
        img = 'http://wallspaper.ru/uploads/gallery/main/16/konoplja.jpg'
        staff = 'Cannabis-1коробок(3г)'
        price = '700р'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                    'Пожалуйста, выберите наиболее подходящий район ⬇⬇⬇'),
                         reply_markup=markup_raion, parse_mode='Markdown')
    elif call.data == 'cannab2':
        img = 'http://wallspaper.ru/uploads/gallery/main/16/konoplja.jpg'
        staff = 'Cannabis-2коробка(6г)'
        price = '1200р'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                    'Пожалуйста, выберите наиболее подходящий район ⬇⬇⬇'),
                         reply_markup=markup_raion, parse_mode='Markdown')
    elif call.data == 'sokol':
        raion = 'Сокол'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                'Район закладки: *'+raion+'*\n'
                                    'Пожалуйста выберите способ оплаты  ⬇⬇⬇'),
                         reply_markup=markup_payment, parse_mode='Markdown')
    elif call.data == 'neft':
        raion = 'Нефтебаза'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                'Район закладки: *'+raion+'*\n'
                                    'Пожалуйста выберите способ оплаты  ⬇⬇⬇'),
                         reply_markup=markup_payment, parse_mode='Markdown')
    elif call.data == 'nlmk':
        raion = 'НЛМК'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                'Район закладки: *'+raion+'*\n'
                                    'Пожалуйста выберите способ оплаты  ⬇⬇⬇'),
                         reply_markup=markup_payment, parse_mode='Markdown')
    elif call.data == '9go':
        raion = 'Район рынка 9го'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                'Район закладки: *'+raion+'*\n'
                                    'Пожалуйста выберите способ оплаты  ⬇⬇⬇'),
                         reply_markup=markup_payment, parse_mode='Markdown')
    elif call.data == 'opit':
        raion = 'Опытная'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                'Район закладки: *'+raion+'*\n'
                                    'Пожалуйста выберите способ оплаты  ⬇⬇⬇'),
                         reply_markup=markup_payment, parse_mode='Markdown')
    elif call.data == 'cr':
        raion = 'Район ЦР'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                'Район закладки: *'+raion+'*\n'
                                    'Пожалуйста выберите способ оплаты  ⬇⬇⬇'),
                         reply_markup=markup_payment, parse_mode='Markdown')
    elif call.data == 'manej':
        raion = 'Манеж'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                'Район закладки: *'+raion+'*\n'
                                    'Пожалуйста выберите способ оплаты  ⬇⬇⬇'),
                         reply_markup=markup_payment, parse_mode='Markdown')
    elif call.data == 'cum':
        raion = 'Район ЦУМа'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                'Район закладки: *'+raion+'*\n'
                                    'Пожалуйста выберите способ оплаты  ⬇⬇⬇'),
                         reply_markup=markup_payment, parse_mode='Markdown')
    elif call.data == 'kolc':
        raion = 'Кольцевая'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                'Район закладки: *'+raion+'*\n'
                                    'Пожалуйста выберите способ оплаты  ⬇⬇⬇'),
                         reply_markup=markup_payment, parse_mode='Markdown')
    elif call.data == 'evr':
        raion = 'Европейский'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                'Район закладки: *'+raion+'*\n'
                                    'Пожалуйста выберите способ оплаты  ⬇⬇⬇'),
                         reply_markup=markup_payment, parse_mode='Markdown')
    elif call.data == 'elec':
        raion = 'Елецкий'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                'Район закладки: *'+raion+'*\n'
                                    'Пожалуйста выберите способ оплаты  ⬇⬇⬇'),
                         reply_markup=markup_payment, parse_mode='Markdown')
    elif call.data == 'rudn':
        raion = 'Сырский рудник'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                'Район закладки: *'+raion+'*\n'
                                    'Пожалуйста выберите способ оплаты  ⬇⬇⬇'),
                         reply_markup=markup_payment, parse_mode='Markdown')
    elif call.data == 'mjk':
        raion = 'МЖК'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                'Район закладки: *'+raion+'*\n'
                                    'Пожалуйста выберите способ оплаты  ⬇⬇⬇'),
                         reply_markup=markup_payment, parse_mode='Markdown')
    elif call.data == 'ltz':
        raion = 'ЛТЗ'
        bot.send_message(call.message.chat.id, str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\n'
                                'Район закладки: *'+raion+'*\n'
                                    'Пожалуйста выберите способ оплаты  ⬇⬇⬇'),
                         reply_markup=markup_payment, parse_mode='Markdown')
    elif call.data == 'qiwicash':
        pay = 'Пополнение QIWI кошелька через терминал'
        msg = str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\nРайон закладки: *' + raion + '*\nСпособ оплаты: *' + pay + '*')
        payment = str('Пополните QIWI кошелёк\n*№ +79042876884* в ближайшем терминале оплаты на сумму '+price+' и нажмите кнопку *"Оплачено"*')
        bot.send_photo(call.message.chat.id, img, caption=msg, reply_markup=markup_pay, parse_mode='Markdown')
    elif call.data == 'qiwipay':
        pay = 'Перевод на QIWI кошелёк'
        msg = str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\nРайон закладки: *' + raion + '*\nСпособ оплаты: *' + pay + '*')
        payment = str('Переведите на QIWI кошелёк\n*№ +79042876884* со своего кошелька '+price+' и нажмите кнопку *"Оплачено"*')
        bot.send_photo(call.message.chat.id, img, caption=msg, reply_markup=markup_pay, parse_mode='Markdown')
    elif call.data == 'card':
        pay = 'Перевод на банковскую карту'
        msg = str('Выбрано: *' + staff + '*\nЦена: *' + price + '*\nРайон закладки: *' + raion + '*\nСпособ оплаты: *' + pay + '*')
        payment = str('Переведите на банковскую карту \n№ *4890 4947 2666 9773* ' + price + ' и нажмите кнопку *"Оплачено"*')
        bot.send_photo(call.message.chat.id, img, caption=msg, reply_markup=markup_pay, parse_mode='Markdown')
    elif call.data == 'yes':
        gif = 'https://i.gifer.com/77OF.gif'
        mesg = str('*Ожидание оплаты...*(резервирование канала оплаты *2 часа*) \n\nВыбрано: *' + staff + '*\nЦена: *' + price + '*\nРайон закладки: *' + raion + '*\n\n'+payment)
        bot.send_animation(call.message.chat.id, gif, caption=mesg, reply_markup=markup_payed, parse_mode='Markdown')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id,'Что-то пошло не так? Не беда😉! Попробуем заново😊?',
                         reply_markup=markup_menu, parse_mode='Markdown')
    elif call.data == 'payed':
        gif = 'https://i.gifer.com/77OF.gif'
        messg = str('*Оплата не поступила* подождите 5 минут и повторите проверку \n\nВыбрано: *' + staff + '*\nЦена: *' + price + '*\nРайон закладки: *' + raion + '*')
        bot.send_animation(call.message.chat.id, gif, caption=messg, reply_markup=markup_payed, parse_mode='Markdown')
    elif call.data == 'back':
        bot.send_message(call.message.chat.id, 'Ваш заказ отменён. Если хотите начать заново нажмите /start ', parse_mode='Markdown')

bot.polling()