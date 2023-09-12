from django.urls import path, re_path
from django.contrib import admin
from orders import views as my_order
from django.contrib.auth import views as auth
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_order.index, name='home'),
    path('orders', my_order.index, name='home'),
    re_path(r'^order/(?P<order_id>\d+)/$', my_order.show, name='show'),
    path('order/new/', my_order.new, name='new'),
    re_path(r'^order/edit/(?P<order_id>\d+)/$', my_order.edit, name='edit'),
    re_path(r'^order/delete/(?P<order_id>\d+)/$', my_order.destroy, name='delete'),
    path('users/login/', auth.LoginView.as_view(template_name='login.html'), name='login'),
    path('users/logout/', auth.LogoutView.as_view(next_page='/'), name='logout'),
    path('users/change_password/', login_required(auth.PasswordChangeView.as_view(success_url='/')), name='change_password'),
]
