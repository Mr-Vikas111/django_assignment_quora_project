
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name="_home"),
    path('',views.index,name="_index"),
    path('question/create/',views.create_question,name="_create_question"),
    path('question/list/',views.all_questions_list,name="_list_question"),
    path('question/user_wise_list/',views.user_wise_questions_list,name="_user_list_question"),
    path('question/<str:question_id>/comment/', views.post_answer, name='_post_answer'),
    path('question/<str:question_id>/like/', views.like_answer, name='_like_answer'),
    
    
]
