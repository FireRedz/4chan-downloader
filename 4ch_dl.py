import requests
import wget

r = requests.session()



def getImages(directory):


	threadLink = input('> ').split('/')
	threadBoard = threadLink[3]
	threadID = threadLink[5]

	#link = 'https://a.4cdn.org/'+threadBoard+'/thread/'+threadID+'.json'

	requestData = r.get('https://a.4cdn.org/'+threadBoard+'/thread/'+threadID+'.json')
	threadData = requestData.json()['posts']

	for x in range(len(threadData)):
		#print('http://i.4cdn.org/',threadBoard'/','.jpg')
		if 'tim' in threadData[x]:
			print('Downloading', threadData[x]['no'],str(threadData[x]['ext']) ,'| Size is ', str(int(threadData[x]['fsize']/1000)),'kb')
			#print(threadData[x]['tim'])
			wget.download('https://i.4cdn.org/'+str(threadBoard)+'/'+str(threadData[x]['tim'])+ str(threadData[x]['ext']), directory+'/'+str(threadData[x]['tim'])+str(threadData[x]['ext']))

		else:
			#print(threadData[x]['name'])
			print('Not image found. Skipping')


def setDirectory():
	print('Download to where?')
	usrDir = input('> ')
	return usrDir



usrDir = setDirectory()
getImages(usrDir)

