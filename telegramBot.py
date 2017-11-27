import telegram
import os, os.path, time, shutil

bot = telegram.Bot(token ='TOKEN')
print(bot.get_me())

dirImg = 'Image Dir'
dirMoved = 'Moved image dir'

def moverImagem(destFile):
	try:
		shutil.move(dirImg + destFile, dirMoved + destFile + 'moved')
		print 'Foto movida com sucesso'
	except Exception as e:
		print e
		raise e

def enviarImagem(destFile):
	bot.send_photo(chat_id = 'dest_chat_id', photo=open(dirImg + destFile, 'rb'))
	print('Foto enviada com sucesso')

while (True):
	path, dirs, files = os.walk(dirImg).next()
	file_count = len(files)
	print file_count

	print 'nao tem arquivo'

	for f in files:
		print 'Foto Encontrado'
		enviarImagem(f)
		moverImagem(f)

	time.sleep(10)

