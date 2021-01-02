from django.urls import path, re_path
from. import views


app_name = 'met_app'
urlpatterns = [
    path('', views.all_meteors, name='all_meteors'),
    path('my_meteors/', views.my_meteors, name='my_meteors'),
    path('add_meteor/', views.add_meteor, name='add_meteor'),
    path('singin/', views.singin, name='singin'),
]