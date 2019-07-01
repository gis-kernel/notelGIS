from django.urls import path
from app import views as app_view

# template_url
app_name = 'app'

# urlpatterns
urlpatterns = [
    path('register/', app_view.register, name='register'),
    path('map/', app_view.map, name='map'),
    path('', app_view.index, name='landing'),

    path('logout/', app_view.user_logout, name='logout')

]
