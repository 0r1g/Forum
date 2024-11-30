from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_branches, name='branches'),
    path('<int:branch_id>/', views.show_all_posts, name='posts'),
    path('posts/<int:post_id>/', views.show_post, name='post')
]

