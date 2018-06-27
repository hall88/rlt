import time
import Adafruit_Trellis
import numpy.ctypeslib as ctl
import ctypes
import pygame
from array import array
from GetButtons import GetData
from FireRemove import removeData
from FirebasePut import FireSend
from SoundGet import loadSound
import json
from firebase import firebase
from firebase import jsonutil

matrix0 = Adafruit_Trellis.Adafruit_Trellis()
trellis = Adafruit_Trellis.Adafruit_TrellisSet(matrix0)
trellis.begin((0x70, 1))

#pygame.mixer.init()
pygame.mixer.pre_init(22050, -16, 2, 2048)
#(44100, -16, 1, 2048)
pygame.mixer.init()
pygame.init()

libdir = './'
libtimer = ctl.load_library('timermake.so', libdir)
libgrader = ctl.load_library('gradermake.so', libdir)
getTime = libtimer.getTime
getTime.argtypes = []

print 'Rhythmic Learning Tool - Team Alternative Facts - EE 464 Fall 2017'
print 'Press Ctrl-C to quit.'

numKeys = 16
#for i in range(numKeys):
#	for i in range(numKeys):
#		trellis.setLED(i)
#		trellis.writeDisplay()	
#	time.sleep(0.015)
	
#	for i in range(numKeys):
#		trellis.clrLED(i)
#		trellis.writeDisplay()		
#	time.sleep(0.015)
for i in range(numKeys):
	trellis.setLED(i)
	trellis.writeDisplay()	


time.sleep(1)
#my_array = array('i');
#my_array = []
num = 0
getTime = libtimer.getTime
getTime.argtypes = []
offset = getTime()

string_set = GetData()

#print 'timer test start: '
#a = getTime() - offset
#print a
#print 'timer test end: '
#b = getTime() - offset
#print b
#print 'timer test delay: '
#print b - a

def record():	
	Json = firebase.FirebaseApplication('https://rhythmic-learning-tool.firebaseio.com/',authentication=None)
	JsonDict = Json.get('lessons/', None)
	currstudent= str(JsonDict['currUser'])
	bpm = int(string_set[64])
	stop_time = 1000000 *60 * (64+1) /bpm
	offset = getTime()
	current_time = ((getTime() - offset))
	
	while current_time < stop_time:
		time.sleep(0.1)
		#o = stop_time - current_time
		#print o
		if trellis.readSwitches():
			read_time = getTime() - offset			
			for i in range(numKeys):
				if trellis.justReleased(i):
					pygame.mixer.music.stop()
					trellis.clrLED(i)
					string_set.append(str(i))
					string_set.append(str(0))
					string_set.append(str(read_time))

				if trellis.justPressed(i):
					loadSound(i)
					pygame.mixer.music.play(-1,0)
					trellis.setLED(i)
					string_set.append(str(i))
					string_set.append(str(1))
					string_set.append(str(read_time))
										
				
				trellis.writeDisplay() # tell the trellis to set the LEDs we requested
			#print '* * * * * * S T A R T * * * * * *'
			#for i in my_array:
			#	print(i)
			#print '* * * * * * E N D * * * * * *'

			#string_set = ["0","1","0","0","0","1000000"]
			#pass_pointer_array()


		
			#d = getTime() - offset
			#print 'timer loop execution time: '
			#print d - c
			
		current_time = ((getTime() - offset))
	
	string_length = len(string_set)
	select_type = (ctypes.c_char_p * string_length)
	select = select_type()
	
	for key, item in enumerate(string_set):
		select[key] = item
		
	time.sleep(2.015)
	libgrader.main.argtypes = [ctypes.c_int, select_type]
	result = libgrader.main(string_length, select)
	FireSend(currstudent,result)
	
one = str(1)

flagLocation = firebase.FirebaseApplication('https://rhythmic-learning-tool.firebaseio.com/lessons/',authentication=None)
time.sleep(1)
Json = firebase.FirebaseApplication('https://rhythmic-learning-tool.firebaseio.com/',authentication=None)
time.sleep(1)

while True:
	JsonDict = Json.get('lessons/', None)
	for i in range(1):
		for i in range(16):
			trellis.setLED(i)
			trellis.writeDisplay()	
		time.sleep(0.015)

		for i in range(16):
			trellis.clrLED(i)
			trellis.writeDisplay()		
		time.sleep(0.015)
    
	LoadFlag = str(JsonDict['Flags']['Software']['LoadLesson'])
	
	if LoadFlag == one:		
		string_set = GetData()
		flagLocation.put('Flags','Hardware',{'LessonIsLoaded':1})
		time.sleep(1)
		flagLocation.put('Flags','Software',{'LoadLesson':0})
		print 'load flag taken'
		
		Json = firebase.FirebaseApplication('https://rhythmic-learning-tool.firebaseio.com/',authentication=None)
		while True:
			JsonDict = Json.get('lessons/', None)
			for i in range(16):
				if (i%2):
					trellis.setLED(i)
					trellis.writeDisplay()	
			time.sleep(0.015)

			for i in range(16):
				if (i%2):
					trellis.clrLED(i)
					trellis.writeDisplay()		
			time.sleep(0.015)      
			
			PlayFlag = str(JsonDict['Flags']['Play']['PlayLesson'])

			if PlayFlag == one:
				print 'play flag taken'
				#pygame.mixer.pre_init(22050, -16, 2, 2048)
				#pygame.mixer.init()
				#pygame.init()
				record()
				flagLocation.put('Flags','Graded',{'GradedFlag':1})
				time.sleep(0.015)
				flagLocation.put('Flags','Play',{'PlayLesson':0})
				pygame.mixer.music.load("440Hz.wav")
				pygame.mixer.music.play()
				flagLocation = firebase.FirebaseApplication('https://rhythmic-learning-tool.firebaseio.com/lessons/',authentication=None)
				time.sleep(1)
				Json = firebase.FirebaseApplication('https://rhythmic-learning-tool.firebaseio.com/',authentication=None)
				break
