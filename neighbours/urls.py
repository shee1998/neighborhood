from django.conf.urls import url,include
from .views import(
signup,
edit_profile,
profile,
neighborhood_details,
business,
create_profile,
add_business
)   

urlpatterns=[
    url(r'^signup/',signup,name='signup'),
    url(r'^profile/',profile,name='profile'),
    url(r'^edit_profile/',edit_profile,name='edit_profile'),
    url(r'^n_details/',neighborhood_details,name='n_details'),
    url(r'^businesses/',business,name='businesses'),
    url(r'^my_profile/',create_profile,name='my_profile'),
    url(r'^add_business/',add_business,name='add_business')
]