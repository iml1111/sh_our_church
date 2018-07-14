from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.create, name='create'),
    # ex: /5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /5/comment/
    path('<int:question_id>/comment/', views.comment, name='comment'),
]