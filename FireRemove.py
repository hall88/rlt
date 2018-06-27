def removeData():
        import json
        from firebase import firebase
        from firebase import jsonutil
        firebase=firebase.FirebaseApplication('https://rhythmic-learning-tool.firebaseio.com/',authentication=None)
        node=firebase.delete('Feedback/',None)
#removeData()
