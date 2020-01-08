import telebot
import random

YouBotMusic = telebot.TeleBot("922646831:AAFeKIDqO_J3BClL0Jt7GR7fm1maDWPnoNY")

@YouBotMusic.message_handler(commands=['Start', 'start'])
def send_welcome(message):
	YouBotMusic.reply_to(message, "Welcome to YouBotMusic! You can see all the actual commands availables using /help")

@YouBotMusic.message_handler(commands=['Help', 'help'])
def help(message):
	YouBotMusic.reply_to(message, "Commands: /JoJo /Eminem /Metallica /New /Createds")

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

@YouBotMusic.message_handler(commands=['New', 'new'])
def group(message):
	YouBotMusic.send_message(message.chat.id, "Creating new group...")
	newSong = open(str(message.chat.first_name) + ".txt", "a")
	YouBotMusic.send_message(message.chat.id, "Introduce the new group (groupname_new):")
	newSong.close()

@YouBotMusic.message_handler(regexp="_new")
def group(message):
	newGroup = message.text.split("_new")
	newSong = open(str(message.chat.first_name) +".txt", "a")
	newSong.write(newGroup[0] +" ")
	newSong.close()
	YouBotMusic.send_message(message.chat.id, "Introduce one song's link from that group (link from Youtube only):")

@YouBotMusic.message_handler(regexp="https://www.youtube.com/")
def group(message):
	newGroup = message.text
	newSong = open(str(message.chat.first_name) +".txt", "a")
	newSong.write(newGroup+'\n')
	newSong.close()
	YouBotMusic.send_message(message.chat.id, "created!")

@YouBotMusic.message_handler(commands=['Createds', 'createds'])
def music(message):
	newSong = open(str(message.chat.first_name) +".txt", "r")
	YouBotMusic.send_message(message.chat.id, "You want to see all lines or a specific line (/All or /One)? ")
	newSong.close()

@YouBotMusic.message_handler(regexp="All")
def group(message):
	newSong = open(str(message.chat.first_name) +".txt", "r")
	YouBotMusic.send_message(message.chat.id, newSong.read())
	newSong.close()

@YouBotMusic.message_handler(regexp="One")
def group(message):
	newSong = open(str(message.chat.first_name) +".txt", "r")
	YouBotMusic.send_message(message.chat.id, "Line (0 to ...) you want to see (line_number): ")
	newSong.close()

@YouBotMusic.message_handler(regexp="line_")
def line(message):
	specifiedLine = int(message.text.split("_")[1])
	newSong = open(str(message.chat.first_name) +".txt", "r")
	lines = newSong.readlines()
	if len(lines)-1 < specifiedLine:
		YouBotMusic.send_message(message.chat.id, "This line is empty!!!")
	else:
		YouBotMusic.send_message(message.chat.id, lines[specifiedLine])
	newSong.close()

@YouBotMusic.message_handler(func=lambda message: True)
def echo_all(message):
	YouBotMusic.reply_to(message, message.text)
YouBotMusic.polling()
