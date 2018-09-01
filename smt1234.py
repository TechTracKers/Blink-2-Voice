import smtplib
def gmail(message):

    if message:
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('from','Password')
        s.sendmail("from","to",message)
        s.quit()

    else:
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('from','password')
        s.sendmail("from","to","Hello")
        s.quit()
        print("Wrong")



#gmail("Hello")
