from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import authenticate,login
from django.template.loader import render_to_string
from django.core.mail import send_mail , send_mass_mail


def Master(request):
    
    return (render(request, "master.html"))


def Home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print('form is working')
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('App/email/getsupport.html', {
                'name': name,
                'phone':phone,
                'email': email,
                'message': message
            })

            send_mail('The contact form subject', 'This is the message', email, ['snsrajat@gmail.com'],fail_silently=False, html_message=html)
            print("Messages is sending")
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'home.html', {
        'form': form
    })


def About(request):
    return (render(request, 'about.html'))


def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print('form is working')
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('App/email/getsupport.html', {
                'name': name,
                'phone':phone,
                'email': email,
                'message': message
            })

            send_mail('The contact form subject', 'This is the message', email, ['snsrajat@gmail.com'],fail_silently=False, html_message=html)
            print("Messages is sending")
            return redirect('Contact-us')
    else:
        form = ContactForm()

    return render(request, 'contact-us.html', {
        'form': form
    })


def Career(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print('form is working')
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            select = form.cleaned_data['selct']
            message = form.cleaned_data['message']

            html = render_to_string('App/email/career support.html', {
                'name': name,
                'phone':phone,
                'email': email,
                'select':select,
                'message': message
            })

            send_mail('The contact form subject', 'This is the message', email, ['snsrajat@gmail.com'],fail_silently=False, html_message=html)
            print("Messages is sending")
            return redirect('career')
    else:
        form = ContactForm()

    return render(request, 'career.html', {
        'form': form
    })

@login_required(login_url='login')
def C_compiler(request):
    return(render(request,'c_compiler.html'))
    
@login_required(login_url='login')
def Cpp_compiler(request):
    return(render(request,'cpp_compiler.html'))

@login_required(login_url='login')
def Java_compiler(request):
    return(render(request,'java_compiler.html'))

@login_required(login_url='login')
def Python_compiler(request):
    return(render(request,'python_compiler.html'))

@login_required(login_url='login')
def Javascript_compiler(request):
    return(render(request,'javascript_compiler.html'))

def Html(request):
    return (render(request, "html.html"))


def Css(request):
    return (render(request, "css.html"))


def Javascript(request):
    return (render(request, "javascript.html"))


def React(request):
    return (render(request, "react.html"))


def Angular(request):
    return (render(request, "angular.html"))


def Vue(request):
    return (render(request, "vue.html"))


def Jquery(request):
    return (render(request, "jquery.html"))


def Swift(request):
    return (render(request, "swift.html"))
# Programming


def C(request):
    return (render(request, "c.html"))


def C_plus(request):
    return (render(request, "c++.html"))


def C_sharp(request):
    return (render(request, "c-sharp.html"))


def Data_structure(request):
    return (render(request, "data_structure.html"))


def Python(request):
    return (render(request, "python.html"))


def Java(request):
    return (render(request, "java.html"))


def Sql(request):
    return (render(request, "sql.html"))


def Nosql(request):
    return (render(request, "nosql.html"))


def Competative_prog(request):
    return (render(request, "competative.html"))


def Open_source(request):
    return (render(request, "open-sf-dev.html"))


def App_dev(request):
    return (render(request, "app_dev.html"))


def Web_dev(request):
    return (render(request, "web_dev.html"))


def Ml(request):
    return (render(request, "ml.html"))


def Data_science(request):
    return (render(request, "data_science.html"))

def Programming_Lang(request):
    return render(request,'Programming_lang.html')
def Technology(request):
    return render(request,'technology.html')

def Signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request,new_user)
            return redirect('login')
    else:
        form = UserCreateForm()
    
    context = {
        'form':form,
    }
    return render(request, 'registration/signup.html',context)


def Login(request):
    if request.user.is_authenticated:
        return redirect(request, 'home')
    else:
        if request.method == 'POST':
            login_username = request.POST['usernameL']
            login_password = request.POST['passwordL']
            user = auth.authenticate(username=login_username,password=login_password)
            # print(user)
            if user is not None:
                auth.login(request, user)
                messages.info(request,'You logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid Credentials.')
                return redirect('login')
            
        else:
            return redirect('login')
        
def Logout(request):
    auth.logout(request)
    messages.info(request,'You logged out')
    return redirect('home')



def Userprofile(request):
    if request.user.is_authenticated:
        return render(request, 'userprofile.html')
    else:
        return redirect('login')

def Error(request):
    if request.user.is_authenticated:
        return render(request, 'error.html')
    else:
        return redirect('signup')
    

