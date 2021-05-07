from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from ro_py import Client

client = Client()
# Create your views here.
def index(req):
    return render(req, 'index.html')

def redirection(req):
    uid = req.GET.get('idinput')
    return HttpResponseRedirect(f'/userid/{uid}')

async def userid(req, uid):
    #TODO add in the code to get data and template
    user = await client.get_user(uid)
    name =  user.display_name
    status =await user.get_status()
    banned = user.is_banned
    friendcount = await user.get_friends_count()
    following = await user.get_followings_count()
    followers = await user.get_followers_count()
    return render(req, 'user.html', {
        'name': name,
        'status': status,
        'banned': banned
        'friendcount': friendcount,
        'following': following,
        'followers': followers
    })