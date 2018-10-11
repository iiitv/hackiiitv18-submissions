"""
auth = firebase.auth()

def singIn(request):
    return render(request, "signIn.html")

def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
    return render(request,"signIn.html",{"msg":message})
    print(use"""
    return render(request, "welcome.html",{"e":email})

