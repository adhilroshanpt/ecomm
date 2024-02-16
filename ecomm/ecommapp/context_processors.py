from ecommapp.models import Carts

def cart_count_context(request):
    if request.user.is_authenticated:
        count=Carts.objects.filter(user_id=request.user).exclude(statud='order-plced')
        return {'count':count}
    else:
        return {'count':0}