from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.conf import settings
from django.core.mail import send_mail
import uuid
from .models import Profile,Gallery,Video,Notification,Document, Message

# Create your views here.


def index(request):
    notifications = Notification.objects.all() 
    count = Notification.objects.count()
    featured_img = Gallery.objects.filter(featured=True)
    data = {'notifications': notifications,
            'count':count,
            'images':featured_img
    }

    return render(request,'index.html', data)

def accounts(request):
     if request.method=='POST' :
        if "register" in request.POST:  
         
            username = request.POST['username']
            email = request.POST['email']
            contact = request.POST['number']
            password = request.POST['password']
            standard = request.POST['standard']
     
           
            if User.objects.filter(username=username).exists():
                messages.add_message(request,messages.ERROR, 'Username Already Taken ')
    
                return redirect('/Accounts')
            elif User.objects.filter(email = email).exists():
                 messages.add_message(request,messages.ERROR, 'Email Already Taken')
                 return redirect('/Accounts')
            else:
                 new_user = User.objects.create_user(username=username,email=email,password=password)
                 new_user.save()
                 auth_token = str(uuid.uuid4())
                 new_profile = Profile(user=new_user,auth_token = auth_token , contact=contact,standard=standard)
                 new_profile.save()
                 verify_mail(email,auth_token)
                 messages.add_message(request,messages.SUCCESS, 'Thanks! Please check your email to verify.')

        elif "login" in request.POST:

            username = request.POST['username']
            password = request.POST['password']
         
            user = auth.authenticate(username = username, password = password)
            if user is not None:
                profile_obj = Profile.objects.get(user=user)
                if profile_obj.verified:
                    if profile_obj.fee:
                        auth.login(request, user)
                        return redirect('/Videos')
                    else:
                        messages.add_message(request,messages.ERROR, 'Please Pay Your Fee to Access the Website. ')
                        return redirect('/Accounts')    
                else:
                    messages.add_message(request,messages.ERROR, 'Please verify your email to login')
                    return redirect('/Accounts')    
            else:
                messages.add_message(request,messages.ERROR, 'User Not Found')
                return redirect('/Accounts')    


     return render(request,'account.html')

def verify_mail(email, token):
    subject = 'Email Confirmation'
    message = f'Hi! Click on the link below to verify your email. https://Alpha2507.pythonanywhere.com/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def verify(request, auth_token):

        matches = Profile.objects.filter(auth_token=auth_token).first()
        if matches:
            if matches.verified:
                messages.info(request,'Your Account is Already Verified!')
                return redirect('/Accounts')
            matches.verified = True
            matches.save()
            messages.info(request,'Congratulations! Verfication Done.')
            return redirect('/Accounts')
        else:
            messages.info(request,'Verfication Failed.')
            return redirect('/Accounts')

def logout(request):
     auth.logout(request)
     return redirect('/Accounts')     

@login_required(login_url="/Accounts")
def videos(request):
    notifications = Notification.objects.all() 
    count = Notification.objects.count()
    user = Profile.objects.get(user=request.user)  
    if user.standard == '11th':
       vids = Video.objects.filter(standard='11th')

    else:
       vids = Video.objects.filter(standard='12th')

    paginator = Paginator(vids, 8)
    page = request.GET.get('page')
    vids = paginator.get_page(page)   

    data = {'notifications': notifications,
            'count':count,
            'vids' : vids
            }

    return render(request,'videos.html', data)

@login_required(login_url="/Accounts")
def gallery(request):
    notifications = Notification.objects.all() 
    count = Notification.objects.count()
    images = Gallery.objects.all()

    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    data = {'notifications': notifications, 
            'count':count,
            'images' : images
            }

    return render(request,'gallery.html', data)

@login_required(login_url="/Accounts")
def docs(request):
    notifications = Notification.objects.all() 
    count = Notification.objects.count()
    documents = Document.objects.all()

    paginator = Paginator(documents, 8)
    page = request.GET.get('page')
    documents = paginator.get_page(page)
    
    data = {'notifications': notifications,
            'count':count, 
            'documents' : documents
            }

    return render(request,'docs.html', data)


def contact(request):

    notifications = Notification.objects.all() 
    count = Notification.objects.count()
    data = {'notifications': notifications,
            'count':count}
    if request.method == 'POST':
        
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        text = request.POST['text']

        msg = Message(full_name=full_name,
        email=email,phone=phone,text=text)
        msg.save()
        return redirect('/Contact')

    return render(request,'contact.html', data)

