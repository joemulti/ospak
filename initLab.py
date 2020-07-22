import initCreateRoom
import initCreateWebhook
import initCreateWebhookForAdaptiveCards
import re

regexroom = re.compile('ROOMID = ".*"')
regexwebhook = re.compile('WEBHOOKID = ".*"')
regexattwebhook = re.compile('WEBHOOKATT = ".*"')

def initLab():
    classroomid,classroomtitle=initCreateRoom.createRoom()
    classroomwebhookid,classroomwebhookname=initCreateWebhook.createWebhook(classroomid)
    classroomattwebhookid,classroomattwebhookname=initCreateWebhookForAdaptiveCards.createAttWebhook(classroomid)


    def changeenv():
        with open(".env") as fobj_in:
            environmentvariablelist=[]
            for line in fobj_in.readlines():
                line=re.sub(regexroom,'ROOMID = "'+classroomid+'"',line)
                line=re.sub(regexwebhook,'WEBHOOKID = "'+classroomwebhookid+'"',line)
                line=re.sub(regexattwebhook,'WEBHOOKATT = "'+classroomattwebhookid+'"',line)
                environmentvariablelist.append(line)

        with open('.env', 'w') as fobj_out:
            for line in environmentvariablelist:
                fobj_out.write("%s" % line)
        print ('Environment angepasst')

    changeenv()
    return ('Die Laborumgebung wurde eingerichtet')