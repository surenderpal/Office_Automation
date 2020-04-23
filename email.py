import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login('surenderpal134@gmail.com','SUR@2000')
server.sendmail('surenderpal134@gmail.com','surender.pal@groundtruth.com','send as email test from python')
server.quit()
