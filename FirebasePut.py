def FireSend(student,correctness):
        import json
        from firebase import firebase
        from firebase import jsonutil
        correctness=str(correctness)
        firebaseNode=firebase.FirebaseApplication('https://rhythmic-learning-tool.firebaseio.com/',authentication=None)
        firebaseDict=firebaseNode.get('lessons/',None)
        currentLesson=str(firebaseDict['lessonchosen'])
        currentPattern=str(firebaseDict['rhythmicpatternchosen'])
        lessonPlacement=firebase.FirebaseApplication('https://rhythmic-learning-tool.firebaseio.com/Feedback/lesson'+currentLesson+'/'+'RhythmicPattern/'+currentPattern+'/',authentication=None)
        putStudent=lessonPlacement.put('Grade',student,{'Percentage':correctness})
