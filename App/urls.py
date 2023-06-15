from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('about', views.About, name='about'),
    path('contact-us', views.Contact, name='contact-us'),
    # path('compiler', views.Compiler, name='Compiler'),
    path('c_compiler', views.C_compiler, name='c_compiler'),
    path('cpp_compiler', views.Cpp_compiler, name='cpp_compiler'),
    path('java_compiler', views.Java_compiler, name='java_compiler'),
    path('python_compiler', views.Python_compiler, name='python_compiler'),
    path('javascript_compiler', views.Javascript_compiler, name='javascript_compiler'),

    path('career', views.Career, name='career'),

    path('signup/', views.Signup, name="signup"),
    path('/accounts/', include('django.contrib.auth.urls')),
    # path('login',views.Login, name='login'),
    path('error',views.Error,name='error'),
    path('userprofile/',views.Userprofile,name='userprofile'),

    # mail service 
    # services


    path('html', views.Html, name='html'),
    path('css', views.Css, name='css'),
    path('javascript', views.Javascript, name='javascript'),
    path('react', views.React, name='react'),
    path('angular', views.Angular, name='angular'),
    path('vue', views.Vue, name='vue'),
    path('jquery', views.Jquery, name='jquery'),
    path('swift', views.Swift, name='swift'),
    path('c', views.C, name='c'),
    path('c++', views.C_plus, name='c++'),
    path('c_sharp', views.C_sharp, name='c_sharp'),
    path('data_structure', views.Data_structure, name='data_structure'),
    path('python', views.Python, name='python'),
    path('java', views.Java, name='java'),
    path('sql', views.Sql, name='sql'),
    path('nosql', views.Nosql, name='nosql'),
    path('competative', views.Competative_prog, name='competative'),
    path('open-sf-dev', views.Open_source, name='open-sf-dev'),
    path('app_dev', views.App_dev, name='app_dev'),
    path('web_dev', views.Web_dev, name='web_dev'),
    path('ml', views.Ml, name='ml'),
    path('data_science', views.Data_science, name='data_science'),
    path('Programming_lang', views.Programming_Lang, name='Programming_lang'),
    path('Technology',views.Technology, name='technology'),

    # path('',include('App2.urls'))



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
