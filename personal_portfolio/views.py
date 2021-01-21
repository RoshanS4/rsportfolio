def logout(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/')

def account(request):
    auth.account(request)
    return redirect('http://127.0.0.1:8000/admin/')