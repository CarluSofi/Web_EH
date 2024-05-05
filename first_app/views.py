from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

response_text = ''
# Create your views here.
def main(request):
  return render(request,'main.html')

def contactme(request):
  return render(request,'contactme.html')

def save_message(request):
  if request.method == 'POST':
    fname = request.POST.get('fname', '')
    lname = request.POST.get('lname', '')
    phone = request.POST.get('phone', '')
    email = request.POST.get('email', '')
    message = request.POST.get('message', '')

    response_text = "First Name: {}\n".format(fname)
    response_text += "Last Name: {}\n".format(lname)
    response_text += "Phone Number: {}\n".format(phone)
    response_text += "Email Address: {}\n".format(email)
    response_text += "Message: {}\n".format(message)
    if response_text:
      send_mail(
        subject= 'Someone visited your website',
        message = response_text, 
        from_email=settings.EMAIL_HOST_USER, 
        recipient_list= ['carlusofi@gmail.com', 'sixiv3@gmail.com', 'evelynholmes0374@comcast.net']
      )
      return HttpResponse('Message sent. We will contact you soon.')
    else:
      return HttpResponse("Message failed")

