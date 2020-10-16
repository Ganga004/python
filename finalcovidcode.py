import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import date
import smtplib

#from prettytable import PrettyTable 
URL = 'https://medtalks.in/live-corona-counter-india'
data = pd.read_html(URL) 
table = data[0]
print(table)

df = pd.DataFrame(table)
df.to_csv ('Covid-19_Count.csv', index=False, header=True)	
today = date.today()
d1 = today.strftime("%d/%m/%Y")
email_user = 'techtalk960@gmail.com'
email_password = 'Python@123'
email_recipient = 'ganga.tharan004@gmail.com'
subject = 'Covid-19 count on '+d1
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_recipient
msg['Subject'] = subject
body = 'Pls check the todays count'
msg.attach(MIMEText(body,'plain'))
filename='Covid-19_Count.csv'
attachment =open(filename,'rb')
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)
msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)
server.sendmail(email_user,email_recipient,text)
server.quit()
print("\n")
output= 'Mail has been sent Pls check the mail'
print("Mail Status :"+output)


# import matplotlib.pyplot as plt
# import seaborn as sns
# from pylab import rcParams

# x = df['Confirmed(IN)']
# ax = sns.distplot(x, hist=True, kde=True, rug=False, color='m', bins=25, hist_kws={'edgecolor':'black'})
# plt.show()