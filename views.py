from django.shortcuts import render,get_object_or_404, redirect
from .models import Warehouse, ItemInstance, ItemType, ItemCategory
from django.contrib import messages

def home_page(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'home.html', {'warehouses': warehouses})

def warehouse_detail_view(request, warehouse_id):
    warehouse = Warehouse.objects.get(id=warehouse_id)
    categories = ItemCategory.objects.filter(itemtype__iteminstance__warehouse=warehouse)
    return render(request, 'warehouse_detail.html', {'warehouse': warehouse, 'categories': categories})

def category_detail_view(request, warehouse_id, category_id):
    warehouse = Warehouse.objects.get(id=warehouse_id)
    category = ItemCategory.objects.get(id=category_id)
    items = ItemInstance.objects.filter(warehouse=warehouse, type__category=category)
    return render(request, 'category_detail.html', {'warehouse': warehouse, 'category': category, 'items': items})

def item_detail_view(request, item_id):
    item = ItemInstance.objects.get(id=item_id)
    return render(request, 'item_detail.html', {'item': item})
def inventory_list_view(request):
    query = request.GET.get('q')
    items = ItemInstance.objects.select_related('type', 'warehouse', 'type__category')

    if query:
        items = items.filter(type__name__icontains=query)

    return render(request, 'inventory_list.html', {'items': items, 'query': query})

def add_quantity_view(request, item_id):
    item = get_object_or_404(ItemInstance, id=item_id)

    if request.method == 'POST':
       
            add_qty = int(request.POST.get('quantity'))
            if add_qty < 0:
                messages.error(request, "Quantity cannot be negative.")
            else:
                item.quantity += add_qty
                item.save()
               
                return redirect('inventory_list')
        

    return render(request, 'add_quantity.html', {'item': item})
