from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from home.models import Contact, Order, GetJob
from django.contrib import messages
from datetime import datetime
# Create your views here.


# superuser name - recxo , email - regular, password - instagram
# user for experiment name - jay, password - jignesh6^^9

# HTML 

def index(request):
    '''this function is for rendering the landing page'''
    # return HttpResponse('this is homepage')

    # in context we'll be sending all the sentences we need to show in the landing page for experimenting
    context = {"variable": "this is me "}
    return render(request, 'home/index.html', context)

def about(request):
    '''this function is for rendering the about page'''
    return render(request, 'home/aboutus.html')

def service(request):
    '''this function is for rendering the services page'''
    return render(request, 'home/services.html')

def projects(request):
    '''this function is for rendering the projects page'''
    return render(request, 'home/projects.html')

# order related

def orders(request):
    '''this function is for rendering the order page'''

    # checking the user is authenicated or not 
    if request.user.is_authenticated:
    # sending the data
        if request.method == "POST":

            softName = request.POST.get('softwarename')
            softType = request.POST.get('type')
            timeFrame = request.POST.get('time')
            amount = request.POST.get('amount')
            softInfo = request.POST.get('describe')

            # saving the data in order 
            order = Order(soft_name=softName, soft_type=softType,
                        soft_time=timeFrame, soft_amount=amount, soft_desc=softInfo)
            # saving the object
            order.save()
            # sending the message that your order has been placed
            messages.success(request, 'Your order has been placed')

        # rendering the orders page 
        return render(request, 'home/order/orders.html')
    else:
        messages.error(request, 'Please login to order ')
        # if user isn't logined then redirecting the user to the home page
        return redirect('/')

def placeOrder(request):
    '''this is the function which we which showing all the info after placing the order '''
    return render(request, 'home/order/orderplace.html')

def orderSave(request):
    '''this function is for saving the order we'll have '''

def ord_cancel(request):
    '''this function is for canceling the order '''

    return render(request, 'home/cancelation-policy.html')

# contact related

# this function is for rendering the contact page
def contact(request):
    '''this function is for rendering the contact page'''

    # checking the user is authencticated or not
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            contact = Contact(name=name, email=email,
                            message=message, date=datetime.today())
            # saving the data 
            contact.save()
            # showing a message if the contact has been submitted successfully 
            messages.success(request, 'Success,Your message has been sent!')
        return render(request, 'home/contact.html')
    else:
        # if user is not logined the showing a message , to login to contact us
        messages.error(request, 'Please login to contact us ')
        return render(request, 'home/contact.html')


# subscription related

def subscription(request):
    '''this function is for rendering the subscription page'''
    return render(request, 'home/subscription.html')

def projects(request):
    '''this function is for rendering the projects page'''
    return render(request, 'home/projects.html')

# job related

def job(request):
    '''this function is for rendering the job page'''

    # checking the user is authenticated or not 
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('name')
            UserName = request.POST.get('username')
            phoneno = request.POST.get('phoneno')
            email = request.POST.get('email')
            education = request.POST.get('education')
            qualification = request.POST.get('qualification')
            ever_worked = request.POST.get('worked_ever')
            status = request.POST.get('status')
            address = request.POST.get('address')
            jobrole = request.POST.get('jobrole')
            skills = request.POST.get('skills')
            explain = request.POST.get('describe')

            # sending the data 
            jobrequest = GetJob(name=name, UserName=UserName, email=email, phone=phoneno, education=education, qualification=qualification,
                                address=address, your_skills=skills, ever_worked=ever_worked, jobrole=jobrole, status=status, describe=explain)
            # saving the data 
            jobrequest.save()
            # showing a message that your application has been submitted successfully 
            messages.success(request, 'Your application has been submitted')
        # showing the page 
        return render(request, 'home/job.html')
    else:
         # if user is not logined the showing a message , to login to apply for a job
        messages.error(request, 'Please login to apply for a job ')
        # redirecting the user to the home page of recxo
        return redirect('/')

def ai(request):
    '''this function is for rendering the ai page'''
    return render(request, 'ai.html')

# company info related
def term_and_cond(request):
    '''this function is for rendering the terms and condition page'''
    return render(request, 'home/term&cond.html')

def priv_policy(request):
    '''this function is for rendering the terms and condition page'''
    return render(request, 'home/privacy_policy.html')

# profile related

def profile(request):
    return render(request, 'home/loginrelated/profile.html')

# APIs
# login related

def loginUser(request):
    '''this function is for rendering the login page and authenicating the user'''

    if request.method == 'POST':
        username = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')
        print(username, password)
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        # conditions logging in a user 
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In as '+ str({request.user.username}))
            return redirect('/')
        else:
            messages.error(request, 'Login Credentials didn\'t match')
            return render(request, 'home/loginrelated/loginform2.html')
            # return render(request, '/')
    return render(request, 'home/loginrelated/loginform2.html')

def logoutUser(request):
    '''this function is logging out the user'''
    # making the user logging out 
    logout(request)
    return redirect('/')

def signup(request):
    '''this function is for rendering the signup page'''
    return render(request, 'home/loginrelated/signup.html')

def handleSignup(request):
    '''this function handles the signup of user'''
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['confirmpass']
        # username should be under 10 characters
        if len(username) > 10:
            messages.error(request, 'Username must be under 10 characters')
            return redirect('/')

        # username should be alphanumeric
        if not username.isalnum():
            messages.error(
                request, 'Username should only contain letters and numbers')
            return redirect('/')

        # passwords should match
        if password != password_confirm:
            messages.error(request, 'Passwords do not match')
            return redirect('/')

        #  checks for errorneous inputs
        # create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        # saving the use
        myuser.save()
        # showing a user that you have signed up successfully
        messages.success(
            request, 'Your recxo account has been successfully created')
        return redirect('/')
    else:
        # showing error 
        return HttpResponse('404 - Page not found')

def forpass(request):
    '''this function is for rendering the forgot pass page'''
    return render(request, 'home/forgotpass.html')
