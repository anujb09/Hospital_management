from django.urls import path ,include

from app1 import views

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [

    path("home/<name>",views.homepage),

    path("class",views.Demo1.as_view()),

    path("show/<name>",views.demoHtml),

    path("cal/<no1>/<no2>",views.cal),

    path("loop",views.loop),

    path("",views.products),

    path("user",views.userinput),

    path("dashboard",views.display),

    path("edit/<uid>",views.edit),

    path("delete/<uid>",views.delete),

    path("register",views.register),

    path("login",views.user_login),

    path("logout",views.user_logout),

    path("catfilter/<cv>",views.catfilter),

    path("prange",views.range),

    path("sort/<sv>",views.sort),

    path("details/<pid>",views.details),

]


if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)