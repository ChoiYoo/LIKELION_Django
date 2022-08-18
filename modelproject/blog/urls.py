from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path("update/<int:id>", views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('new_form/', views.new_form, name='new_form'),
    path('create_form/', views.create_form, name='create_form'),
    path('<int:id>/comments/', views.create_comment, name='create_comment'),
    path('<int:id>/delete_comment/', views.delete_comment, name='delete_comment'),
]

#확인용
# 확인