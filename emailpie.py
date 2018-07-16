import smtplib

#message
msg = 'xxx'
fromaddr = 'xxx@xxx.com'
toaddr = 'xxx@xxx.com'

#into gmail smtp
mail = smtplib.SMTP('smtp.gmail.com', 587)

#identify self to server
mail.ehlo()

#start tls model, encrypted stuff after
mail.starttls()

#login
mail.login('xxx@xxx.com', 'xxx')

#send
mail.sendmail(fromaddr, toaddr, msg)

#close
mail.close()