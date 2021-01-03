from django.urls import path, re_path
from. import views


app_name = 'met_app'
urlpatterns = [
    path('', views.all_meteors, name='all_meteors'),
    path('my_meteors/', views.my_meteors, name='my_meteors'),
    path('add_meteor/', views.add_meteor, name='add_meteor'),
    path('singin/', views.singin, name='singin'),
    path('meteor/<int:id>', views.meteor, name='meteor'),
    path('edit_meteor/<int:id>', views.edit_meteor, name='edit_meteor'),
    path('del_meteor/<int:id>', views.del_meteor, name='del_meteor'),
]