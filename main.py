# -*- coding: utf-8 -*-
import bot as vk_bot
f = open('фАЛвсе.txt',encoding = 'utf-8')
data = f.read()
aye = data.split('\n')
# Чтобы получить токен, нужно перейти по ссылке https://oauth.vk.com/authorize?client_id=2685278&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1 нажать "разрешить" и скопировать в адресной строке все, что идёт после access_token= до &
bot = vk_bot.Bot("", anticaptcha_key = "")
bot.set_template_list(aye) # Список шаблонов, которыми будет отвечать бот
bot.set_attachment_list(["wall-201363337_5 {delay: 10}", "photo571843010_457254738 {sticker_ids[101, 126]"]) # Список вложений. Сюда нужно добавлять идентификаторы вложений. Чтобы получить идентификатор вложения, нужно скопировать ссылку на него (пример: https://vk.com/photo530941218_457262715) и убрать https://vk.com/
bot.set_voice_message_list(["doc635418962_583254994", "doc635418962_583255027", "doc635418962_583255043", "doc635418962_583255060", "doc635418962_583255076", "doc635418962_583255099", "doc635418962_583255145", "doc635418962_583255180", "doc635418962_583255210", "doc635418962_583255239", "doc635418962_583255271", "doc635418962_583255309", "doc635418962_583255353"]) # Список голосовых сообщений. Сюда нужно добавлять идентификатооы голосовых сообщений. О том, как их получить можно прочитать в файле README.txt (пункт 3.1)
bot.set_response_chance_in_chats(30) # Шанс ответа на сообщение в беседе
bot.set_response_chance_in_private_messages(30) # Шанс ответа на личное сообщение
bot.set_attachment_response_chance(10) # Шанс того, что в случае ответа бот отправит вложение (фотографию, аудиофайл, видеофайл)
bot.set_voice_message_response_chance(10) # Шанс того, что бот в случае ответа отправит голосовое сообщение
bot.set_sticker_sending_delay(1) # задержка перед отправкой стикера
bot.set_ignore_list([571843010, 366095793, 348728224, 560873211]) # Список id пользователей, на чьи сообщения бот отвечать не будет
bot.set_ignore_chat_list([0]) # Список id бесед, в которые бот не будет отправлять сообщения
bot.set_ignore_message_list(["vto.pe", "vkbot.ru"]) # При наличии в сообщении любого слова из этого списка бот не будет на него отвечать (сюда нужно добавить ссылки, за отправку которых можно получить бан)
bot.join_chat_by_link_in_private_messages = True # True: бот будет заходить в беседы по ссылкам, которые ему отправляют в личных сообщениях, False: бот будет игнорировать ссылки, которые ему отправляют в личных сообщениях
bot.join_chat_by_link_in_chats = True # True: бот будет заходить в беседы по ссылкам, которые ему отправляют в других беседах, False: бот будет игнорировать ссылки, которые ему отправляют в беседах
bot.messages_forwarding = True # True: в случае ответа бот будет пересылать сообщение пользователя, на которое он отвечает, False: бот не будет пересылать сообщения
bot.messages_forwarding_when_sticker_sent = False # True: в случае отправки стикера бот будет пересылать сообщение пользователя, на которое он отвечает, False: бот не будет пересылать сообщения, когда отправляет стикер
bot.attachment_with_message = False # True: в случае отправки ботом вложения оно будет добавленно к текстовому сообщению, Flase: бот отправит только вложение

if __name__ == "__main__":
	bot.run()
