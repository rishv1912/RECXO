from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [

    path("", views.index, name="home"),
    path("About/", views.about, name="about"),
    # all realted to services
    path("Services/", views.service, name="services"),
    path("Services/Projects", views.projects, name="Projects"),
    path("Services/Job", views.job, name="GetJob"),
    path("Services/AI", views.ai, name="ai"),

    # login related
    path("Login/", views.loginUser, name="Login"),
    path("Logout/", views.logoutUser, name="Logout"),
    path("Signup/", views.signup, name="Sign Up"),
    path("CreateUser/", views.handleSignup, name="CreateUser"),
    path("Login/ForgotPass", views.forpass, name="forgotpass"),


    # contact related
    path("Contact/", views.contact, name="Contact"),
    path('savecontact/', views.contact, name='savecontact'),

    # order related
    path("Orders/", views.orders, name="orders"),
    path("orderPlace/", views.placeOrder, name="placed order"),

    # profile related
    path("Profile/", views.profile, name="profile"),




    # company related
    path("Term_Condition/", views.term_and_cond, name="Terms and Condition"),
    path("Privacy_Policy/", views.priv_policy, name="Privacy Policy"),
    path("Cancelation_Policy/", views.ord_cancel, name="cancelation-policy"),
    path("Subscriptions/", views.subscription, name="cancelation-policy"),
]
