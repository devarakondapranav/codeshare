import smtplib





def sendEmail(to, message, articleid):

   s = smtplib.SMTP('smtp.gmail.com', 587)

   s.starttls()
   s.login("devarakondapranav@gmail.com", "vhlmhrlnxfzvutfx")
   SUBJECT = "Update from CodeShare"
   message = 'Subject: {}\n\n{}'.format(SUBJECT, message)
   message += "\n Click on the link to see who has commented. \n http://roshna.ml/" + str(articleid)
   
   s.sendmail('devarakondapranav@gmail.com', to, message)


#sendEmail("devarakondapranav@yahoo.com", "Hey")
   s.quit()