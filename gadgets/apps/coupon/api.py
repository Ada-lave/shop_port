from django.http import JsonResponse

from .models import Coupon

def ApiCanUse(request):
    json_resp = {}

    coupon_code = request.GET.get('coupon_code',"")

    try:
        coupon = Coupon.objects.get(code=coupon_code)

        if coupon.can_use():
            json_resp['amount'] = coupon.value
        else:
            json_resp['amount'] = 0
    
    except Exception:
        json_resp['amount'] = 0
    
    return JsonResponse(json_resp)