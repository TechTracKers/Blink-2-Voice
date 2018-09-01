import smtplib
def gmail(message):

    if message:
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('ujjwalprakash333@gmail.com','Ujjwal@96')
        s.sendmail("ujjwalprakash333@gmail.com","ujjwalprakash3@gmail.com",message)
        s.quit()

    else:
        # s=smtplib.SMTP('smtp.gmail.com',587)
        # s.starttls()
        # s.login('ujjwalprakash333@gmail.com','Ujjwal@96')
        # s.sendmail("ujjwalprakash333@gmail.com","ujjwalprakash3@gmail.com","Hello")
        # s.quit()
        print("Wrong")



#gmail("Hello")
