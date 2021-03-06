import requests
import os

r = requests.session()

def getImages(directory):
	threadLink = input('> ').split('/')
	threadBoard = threadLink[3]
	threadID = threadLink[5]

	requestData = r.get('https://a.4cdn.org/'+threadBoard+'/thread/'+threadID+'.json')
	threadData = requestData.json()['posts']

	for x in range(len(threadData)):

		if not os.path.exists(directory+'/'+str(threadBoard)): # create dir for Thread
			print('Creating folder')
			os.mkdir(directory+''+str(threadBoard))

		if not os.path.exists(directory+'/'+str(threadBoard)+'/'+str(threadID)): # create folder inside threadboard
			print('Creating folder')
			os.mkdir(directory+''+str(threadBoard)+'/'+str(threadID))

		if 'tim' in threadData[x]:
			print('Downloading', threadData[x]['no'],str(threadData[x]['ext']) ,'| Size is ', str(int(threadData[x]['fsize']/1000)),'kb')
			os.system("aria2c "+'https://i.4cdn.org/'+str(threadBoard)+'/'+str(threadData[x]['tim'])+ str(threadData[x]['ext']) +" -d "+directory+'\\'+str(threadBoard)+'\\'+str(threadID)+ ' -x 10')
		else:
			print('Skipping')

getImages(os.getcwd())

