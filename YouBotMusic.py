import telebot
import random

YouBotMusic = telebot.TeleBot("922646831:AAFeKIDqO_J3BClL0Jt7GR7fm1maDWPnoNY")
@YouBotMusic.message_handler(commands=['Start', 'start'])
def send_welcome(message):
	YouBotMusic.reply_to(message, "Link start!")

@YouBotMusic.message_handler(commands=['Help', 'help'])
def help(message):
	YouBotMusic.reply_to(message, "Comands: /Start /JoJo /Eminem /Metallica")

@YouBotMusic.message_handler(commands=['JoJo', 'Jojo', 'jojo'])
def music(message):
	musicList=["https://www.youtube.com/watch?v=OchozLuSHM0", "https://www.youtube.com/watch?v=FLXIFbbA_Pg"]
	YouBotMusic.reply_to(message, random.choice(musicList))
	print(message)

@YouBotMusic.message_handler(commands=['Eminem', 'eminem'])
def music(message):
	musicList=["https://www.youtube.com/watch?v=8CdcCD5V-d8", "https://www.youtube.com/watch?v=j5-yKhDd64s"]
	YouBotMusic.reply_to(message, random.choice(musicList))
	print(message)

@YouBotMusic.message_handler(commands=['Metallica', 'metallica'])
def music(message):
	musicList=["https://www.youtube.com/watch?v=Ckom3gf57Yw", "https://www.youtube.com/watch?v=IfRY3SsozuM"]
	YouBotMusic.reply_to(message, random.choice(musicList))
	print(message)

	#id: 863816876

	#Probes:

	#class telegram.Audio(random.choice(musicList)):
	#YouBotMusic.reply_to(message, telegram.Audio)

	#Message msg = await botClient.SendVideoAsync(
  	#	chatId: e.Message.Chat,
  	#	video: random.choice(musicList),
  		#thumb: "https://raw.githubusercontent.com/TelegramBots/book/master/src/2/docs/thumb-clock.jpg",
  	#	supportsStreaming: true
	#);
#, random.choice(musicList)
#@bot.message_handler(content_types=['document', 'audio'])
#def handle_docs_audio(message):
#	pass

@YouBotMusic.message_handler(func=lambda message: True)
def echo_all(message):
	YouBotMusic.reply_to(message, message.text)

YouBotMusic.polling()
