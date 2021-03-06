from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/<int:post_id>/', views.post_view, name='post'),        
    path('<str:username>/<int:post_id>/edit/',views.post_edit, name='post_edit'),
    path('<str:username>/<int:post_id>/comment', views.add_comment, name='add_comment'),
    path('<str:username>/<int:post_id>/comment/<int:id>/thread/', views.add_thread, name='add_thread'),

]