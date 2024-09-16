from django.shortcuts import render

#Create a function to render the CV template

def cv_view(request):
    return render(request, 'rc_portfolio_cv/cv.html')
