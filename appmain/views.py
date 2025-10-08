import requests
from datetime import datetime
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .models import User
from .models import Opinion, ReaderOpinion, Poll, video, bookmark
from .forms import ReaderOpinionForm
from django.contrib.auth.decorators import login_required


apikey2 = "713ba33001d63d0f3870852f931765a6"
url2 = f"https://gnews.io/api/v4/top-headlines?&lang=ta&country=in&max=4&apikey={apikey2}"
response2=requests.get(url2)
data2=response2.json()
breaking=data2.get('articles',[])


current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def news_category(request, category="general"):
    # api_key = "713ba33001d63d0f3870852f931765a6"
    # url = f"https://gnews.io/api/v4/top-headlines?&category={category}&lang=us&country=in&max=4&apikey={api_key}"
    # response = requests.get(url)
    # data = response.json()
    # articles = data.get("articles", [])

    categories = ["general", "business", "entertainment", "health", "science", "sports", "technology"]

    return render(request, 'home2.html', {
        #'articles': articles,
        'category': category.capitalize(),
        'categories': categories
    })

def home1(request):
    return render(request,'home1.html')




def home(request,category='top',gcountry='in'):
    if not request.session.get('name'):
        messages.error(request,'Please login to access the homepage.')
        return redirect('login')
    api_key = "pub_3430ca6136094c4faeaee793e9ee96c7"
    url=f"https://newsdata.io/api/1/latest?apikey={api_key}&q=pizza&category={category}"
    response = requests.get(url)
    data = response.json()
    articles = data.get('results', [])

    categories = ["business","crime","domestic","education","entertainment","food","health","lifestyle","politics","science","technology","top","tourism","world","other"]
    current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    apikey = "713ba33001d63d0f3870852f931765a6"
    url1 = f"https://gnews.io/api/v4/top-headlines?&lang=us&country={gcountry}&max=4&apikey={apikey}"
    response1=requests.get(url1)
    data1=response1.json()
    featured=data1.get('articles',[])

    # api_key = "pub_3430ca6136094c4faeaee793e9ee96c7"
    # url=f"https://newsdata.io/api/1/latest?apikey={api_key}&q=pizza&category={category}&country={gcountry}&max=6"
    # response = requests.get(url)
    # data = response.json()
    # featured = data.get('results', [])


    gnews_countries={
            'us': 'United States',
            'in': 'India',
            'gb': 'United Kingdom',
            'ca': 'Canada',
            'au': 'Australia'
    }

    return render(request, 'home.html', {
        'articles': articles,
        'category': category.capitalize(),
        'categories': categories,
        'current_time':current_time,
        'featured':featured,
        'breaking':breaking,
        'gnews_countries': gnews_countries
    })
    
    


def search(request,category='top'):
    if request.method=='POST':
        category=request.POST.get('search')
        if category not in ["business","crime","domestic","education","entertainment","food","health","lifestyle","politics","science","technology","top","tourism","world","other"]:
            category = 'top'
        api_key = "pub_3430ca6136094c4faeaee793e9ee96c7"
        url=f"https://newsdata.io/api/1/latest?apikey={api_key}&q=pizza&category={category}"
        response = requests.get(url)
        data = response.json()
        articles = data.get('results', [])
        return render(request,'menus/search.html',{
            'articles':articles,
            "current_time":current_time})
    

    if category not in ["business","crime","domestic","education","entertainment","food","health","lifestyle","politics","science","technology","top","tourism","world","other"]:
            category = 'top'
    api_key = "pub_3430ca6136094c4faeaee793e9ee96c7"
    url=f"https://newsdata.io/api/1/latest?apikey={api_key}&q=pizza&category={category}"
    response = requests.get(url)
    data = response.json()
    articles = data.get('results', [])
    return render(request,'home.html',{
        'articles':articles,
        "current_time":current_time,
        "breaking":breaking
        }
        )

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= User.objects.filter(username=username, password=password).first()

        if user:
            messages.success(request,'you can login without restriction')
            request.session['name']=username
            return redirect('homepage')
        else:
            messages.error(request,'You are the registered user please register first to login to the website')
            return redirect('register')
        
        return render(request,'login.html')
    
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        interested=request.POST.get('interested')
        image=request.FILES.get('image')

        if User.objects.filter(username=username).first():
            messages.error(request,'Username already exists')
            return redirect('register')

        else:
            messages.success(request,'registration successfull')
            obj=User(username=username, password=password, email=email, phone=phone, address=address, interested_field=interested)
            obj.save()

            return redirect('login')
    

    return render(request,'register.html')


def profile(request):
    name=request.session.get('name')
    user=User.objects.filter(username=name).first()
    return render(request,'menus/profile.html',{'data':user,'current_time':current_time,
    'breaking':breaking
    })



def update_profile(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.interested_field = request.POST.get("interested_field")
        user.phone = request.POST.get("phone")
        user.address = request.POST.get("address")

        if request.FILES.get("image"):
            user.image = request.FILES["image"]

        user.save()
        return redirect("profile")  # redirect to profile view
    return render(request, "menus/profile.html", {"data": user,'current_time':current_time,
    'breaking':breaking
    })


def opinion(request):

    opinions = Opinion.objects.all().order_by('-created_at')[:5]
    reader_opinions = ReaderOpinion.objects.all().order_by('-submitted_at')[:5]
    poll = Poll.objects.first()
    
    name=request.session.get('name')
    user=User.objects.filter(username=name).first()

     #Handle opinion submission form
    if request.method == 'POST':
        if 'vote' in request.POST:
            # ✅ Handle voting
            if poll:
                if request.POST['vote'] == 'yes':
                    poll.yes_votes += 1
                elif request.POST['vote'] == 'no':
                    poll.no_votes += 1
                poll.save()
            return redirect('opinion')  # Prevent duplicate voting on refresh

        else:
            # ✅ Handle Reader Opinion form
            form = ReaderOpinionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('opinion')
    else:
        form = ReaderOpinionForm()

    return render(request, 'menus/opinion.html', {
        'opinions': opinions,
        'reader_opinions': reader_opinions,
        'form': form,
        'poll': poll,
        'names':name,
        'current_time':current_time,
        'breaking':breaking
    })



def videos(request):
    vid=video.objects.all()
    return render(request,'menus/videos.html',{'video':vid, 'current_time':current_time,
    'breaking':breaking
    })


def trending(request):
    return render(request,'menus/trending.html',{'current_time':current_time,
    'breaking':breaking
    })


def bookmarks(request):
    articles=bookmark.objects.all().order_by('created_at')
    print(articles)
    if request.method=='POST':
        img=request.POST.get('image_url')
        arturl=request.POST.get('article_url')
        title=request.POST.get('title')
        description=request.POST.get('description')        
        obj=bookmark(image_url=img, url=arturl, title=title, description=description)
        obj.save()
        return redirect('bookmark')
    
    return render(request,'menus/bookmark.html',
    {
        'current_time':current_time,
        'articles':articles,
        'breaking':breaking
    })



def subscribe(request):
    if request.method == "POST":
        name = request.session.get('name')
        user = User.objects.filter(username=name).first()

        if user:
            sendermail = "vendhanvelusamy@gmail.com"
            receiver_mail = [user.email]
            subject = "Subscription Confirmation"
            message = "You have successfully subscribed to HEADPULSE updates."

            send_mail(subject, message, sendermail, receiver_mail)

            return JsonResponse({
                "status": "success",
                "message": "Subscribed successfully! Check your email."
            })
        else:
            return JsonResponse({
                "status": "error",
                "message": "User not found."
            })
    else:
        return JsonResponse({
            "status": "error",
            "message": "Invalid request method."
        })