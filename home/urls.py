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
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("createuser/", views.handleSignup, name="createuser"),
    path("login/forgotpass", views.forpass, name="forgotpass"),


    # contact related
    path("contact/", views.contact, name="contact"),
    path('savecontact/', views.contact, name='savecontact'),

    # order related
    path("orders/", views.orders, name="orders"),
    path("orderplace/", views.placeOrder, name="orderplace"),

    # profile related
    path("profile/", views.profile, name="profile"),

    # company related
    path("term-condition/", views.term_and_cond, name="term-condition"),
    path("privacy-policy/", views.priv_policy, name="privacy-policy"),
    path("cancelation-policy/", views.ord_cancel, name="cancelation-policy"),
    path("subscriptions/", views.subscription, name="subscriptions"),
]
