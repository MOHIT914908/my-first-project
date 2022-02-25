from django.urls import path

from main import views

urlpatterns = [
    path('',views.index , name='home'),
    path('login/',views.Login , name="login"),
    path('student_detials/',views.student_details , name="student-details"),
    path('contactme/',views.contact , name="contact"),
    path('book_list/',views.lend_book , name = "book_list"),
    path('lendbook/<str:bookname>',views.add_book,name="lend-book"),
    path('info/',views.info,name="info")
]