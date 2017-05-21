from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


@csrf_exempt
def paypal_return(request):
    print request.POST
    # TODO!!
    # find the logged in user
    # find the user's purchase/subscription (last known one at least)
    # it is through the purchase that you have access to coffee details

    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal/paypal_return.html', args)


def paypal_cancel(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal/paypal_cancel.html', args)
