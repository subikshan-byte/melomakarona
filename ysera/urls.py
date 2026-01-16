from django.urls import path
from . import viewhome,viewsingleproduct,viewsearch,viewlogin,viewcart


urlpatterns = [
    path("",viewhome.home,name="home"),
    path("product/<slug:p>",viewsingleproduct.product_detail,name="product"),
    path('<str:s>/pageno<int:page>/search', viewsearch.search, name='search'),
    path('login',viewlogin.login_view,name="login"),
     path("logout/", viewlogin.logout_view, name="logout"),
     path('signup/', viewlogin.signup_view, name='signup'),
     path("cart",viewcart.cart,name="cart"),
     path('cart/add/<slug:product_id>/', viewcart.add_to_cart, name='add to cart'),]

