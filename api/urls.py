from django.conf.urls import url

from .views import ProductView,ProductPKView,UserView,UserPKView,CartView,CartPKView

urlpatterns = [
    url('products/$', ProductView.as_view()),
    url('products/(?P<pk>[0-9]+)/$', ProductPKView.as_view()),
    url('users/$',UserView.as_view()),
    url('users/(?P<pk>[0-9]+)/$',UserPKView.as_view()),
    url('carts/$',CartView.as_view()),
    url('carts/(?P<pk>[0-9]+)/$',CartPKView.as_view())
]