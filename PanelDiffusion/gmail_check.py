#Create for the Upcycle clock project using the Intel Edison -- to get unread emails in the gmail account
#Author : @CarmelitoA 05/24/2017
import imaplib,re
import time
def un_read_email():
    #for this to work you will recive an email in your inbox after the first run, and you will have turn on access to less secure apps
    gmail=imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        gmail.login('username@gmail.com','xxxxxxxxxx')
        inbox,emailCount=gmail.status('INBOX','(MESSAGES UNSEEN)')
        totalMessages=str(re.search('MESSAGES\s+(\d+)',emailCount[0]).group(1))
        unRead=str(re.search('UNSEEN\s+(\d+)',emailCount[0]).group(1))
        print ("You have %s messages, and %s are unread" %(totalMessages,unRead))
        return unRead
    except:
        print("check you credentials, and also ensure you have turned on access to less secure apps in you account settings ")
        return -1
