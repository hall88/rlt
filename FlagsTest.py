def Flags():
        import json
        from firebase import firebase
        from firebase import jsonutil
#       from GetFirebase import GetData
        Json=firebase.FirebaseApplication('https://rhythmic-learning-tool.firebaseio.com/',authentication=None)
        JsonDict=Json.get('lessons/', None)
        tent=str(1)
        flagLocation=firebase.FirebaseApplication('https://rhythmic-learning-tool.firebaseio.com/lessons/',authentication=None)
        LoadFlag=str(JsonDict['Flags']['Software']['LoadLesson'])
        if LoadFlag==tent:
                from GetFirebase import GetData
                setLoaded=flagLocation.put('Flags','Hardware',{'LessonIsLoaded':1})
                clearLoad=flagLocation.put('Flags','Software',{'LoadLesson':0})
Flags()
