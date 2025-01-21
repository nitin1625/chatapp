from django.shortcuts import render,redirect 
from . forms import SignUpForm
from django.contrib.auth import login ,logout

def front_page(request):
    return render(request,'frontpage.html')


def signup_page(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('frontpage')
        
    else :
        form=SignUpForm()
    return render(request,'signup.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('frontpage')



