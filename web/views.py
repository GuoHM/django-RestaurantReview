from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .util import *

from .models import *
# Create your views here.


def list(request):
    restaurants = Restaurant.objects.all();
    return render(request, 'list.html', {'restaurantlist':restaurants})


def login_page(request):
    return render(request, 'login.html')


def login_action(request):
    user = User.objects.get(user_name=request.POST['username'])
    if user.password == request.POST['password']:
        request.session['userid'] = user.user_id
        return list(request)
    else:
        return render(request, 'login.html', {'message': 'Invalid login attempt!'})


def logout(request):
    del request.session['userid']
    return render(request, 'login.html')


def restaurant(request, name):
    restaurant = Restaurant.objects.get(name=name)
    reviews = Review.objects.filter(restaurant=restaurant)
    return render(request, 'restaurant.html', {'restaurant': restaurant,'reviews':reviews})


def review_page(request, name):
    restaurant = Restaurant.objects.get(name=name)
    return render(request, 'review.html', {'restaurant':restaurant})


def reveiw_detail(request, review_id):
    review = Review.objects.get(review_id=review_id)
    comments = Comment.objects.filter(review=review).order_by('-date')
    return render(request, 'detail.html', {'review': review,'comments':comments,'range':range(review.rating)})


def like(request, comment_id):
    if is_login(request):
        comment = Comment.objects.get(comment_id=comment_id)
        comment.likes +=1
        comment.save()
        return HttpResponseRedirect('/detail/'+str(comment.review.review_id))
    return HttpResponseRedirect('/login')


def comment(request, review_id):
    if is_login(request):
        user = get_current_user(request)
        review = Review.objects.get(review_id=review_id)
        comment = Comment(user=user,review=review,content=request.POST['comment'],likes=0)
        comment.save()
        return HttpResponseRedirect('/detail/'+str(review_id))
    return HttpResponseRedirect('/login')


@csrf_exempt
def subcomment(request, comment_id):
    if is_login(request):
        user = get_current_user(request)
        comment = Comment.objects.get(comment_id=comment_id)
        subcomment = Comment(user=user, content=request.POST['comment'], likes=0, master_comment=comment)
        subcomment.save()
        return HttpResponseRedirect('/detail/' + str(comment.review.review_id))
    return HttpResponseRedirect('/login')


def submit_review(request,restaurant_id):
    if is_login(request):
        user = get_current_user(request)
        restaurant = Restaurant.objects.get(restaurant_id=restaurant_id)
        review = Review(user=user,restaurant=restaurant,rating=request.POST['rating'], price=request.POST['price'], description=request.POST['description'])
        review.save()
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/login')




