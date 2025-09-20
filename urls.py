"""
URL configuration for Warehouse_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home_page,warehouse_detail_view,item_detail_view,category_detail_view,inventory_list_view,add_quantity_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home_page,name='home'),
    path('warehouse/<int:warehouse_id>/', warehouse_detail_view, name='warehouse_detail'),
    path('warehouse/<int:warehouse_id>/category/<int:category_id>/', category_detail_view, name='category_detail'),
    path('item/<int:item_id>/', item_detail_view, name='item_detail'),
    path('inventory/', inventory_list_view, name='inventory_list'),
    path('add-quantity/<int:item_id>/', add_quantity_view, name='add_quantity'),

]
