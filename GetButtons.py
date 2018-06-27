def GetData():
    import json
    from firebase import firebase
    from firebase import jsonutil
    firebase=firebase.FirebaseApplication('https://rhythmic-learning-tool.firebaseio.com/', authentication=None)
    JsonDict=firebase.get('lessons/',None)
    
    x=str(JsonDict['lessonchosen'])
    y=str(JsonDict['rhythmicpatternchosen'])
    beats=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['bpm'])

    #Sequencer 1 Buttons
    seq1Button1=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn1']) 
    seq1Button2=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn2'])
    seq1Button3=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn3'])
    seq1Button4=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn4'])
    seq1Button5=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn5'])
    seq1Button6=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn6'])
    seq1Button7=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn7'])
    seq1Button8=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn8'])
    seq1Button9=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn9'])
    seq1Button10=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn10'])
    seq1Button11=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn11'])
    seq1Button12=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn12'])
    seq1Button13=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn13'])
    seq1Button14=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn14'])
    seq1Button15=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn15'])
    seq1Button16=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer1']['btn16'])
    
    #Sequencer 2 Buttons
    seq2Button1=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn1'])  
    seq2Button2=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn2'])
    seq2Button3=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn3'])
    seq2Button4=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn4'])
    seq2Button5=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn5'])
    seq2Button6=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn6'])
    seq2Button7=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn7'])
    seq2Button8=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn8'])
    seq2Button9=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn9'])
    seq2Button10=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn10'])
    seq2Button11=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn11'])
    seq2Button12=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn12'])
    seq2Button13=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn13'])
    seq2Button14=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn14'])
    seq2Button15=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn15'])
    seq2Button16=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer2']['btn16'])

    #Sequencer 3 Buttons
    seq3Button1=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn1'])  
    seq3Button2=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn2'])
    seq3Button3=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn3']) 
    seq3Button4=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn4'])
    seq3Button5=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn5'])  
    seq3Button6=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn6'])
    seq3Button7=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn7']) 
    seq3Button8=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn8'])
    seq3Button9=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn9']) 
    seq3Button10=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn10'])
    seq3Button11=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn11']) 
    seq3Button12=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn12'])
    seq3Button13=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn13']) 
    seq3Button14=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn14'])
    seq3Button15=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn15']) 
    seq3Button16=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer3']['btn16'])

    #Sequencer 4 Buttons
    seq4Button1=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn1']) 
    seq4Button2=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn2'])
    seq4Button3=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn3']) 
    seq4Button4=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn4'])
    seq4Button5=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn5']) 
    seq4Button6=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn6'])
    seq4Button7=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn7']) 
    seq4Button8=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn8'])
    seq4Button9=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn9']) 
    seq4Button10=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn10'])
    seq4Button11=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn11'])  
    seq4Button12=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn12'])
    seq4Button13=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn13'])
    seq4Button14=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn14'])
    seq4Button15=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn15'])   
    seq4Button16=str(JsonDict['lesson'+x]['rhythmicpattern'+y]['sequencer4']['btn16'])
    
    #Full Rhythmic Pattern Buttons
    #LessonArray=[x,y]
    ButtonPattern=[seq1Button1,seq1Button2,seq1Button3,seq1Button4,seq1Button5,seq1Button6,seq1Button7,seq1Button8,seq1Button9,seq1Button10,seq1Button11,seq1Button12,seq1Button13,seq1Button14,seq1Button15,seq1Button16,seq2Button1,seq2Button2,seq2Button3,seq2Button4,seq2Button5,seq2Button6,seq2Button7,seq2Button8,seq2Button9,seq2Button10,seq2Button11,seq2Button12,seq2Button13,seq2Button14,seq2Button15,seq2Button16,seq3Button1,seq3Button2,seq3Button3,seq3Button4,seq3Button5,seq3Button6,seq3Button7,seq3Button8,seq3Button9,seq3Button10,seq3Button11,seq3Button12,seq3Button13,seq3Button14,seq3Button15,seq3Button16,seq4Button1,seq4Button2,seq4Button3,seq4Button4,seq4Button5,seq4Button6,seq4Button7,seq4Button8,seq4Button9,seq4Button10,seq4Button11,seq4Button12,seq4Button13,seq4Button14,seq4Button15,seq4Button16,beats]
    #Original order: BPM->Lesson->RP->Buttons
    #new order:      Lesson->RP->BPM->Buttons
    return ButtonPattern #,LessonArray 
#temp=GetData()
#print temp
