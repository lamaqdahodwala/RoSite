from django.shortcuts import render, redirect
import ro_py

# Create your views here.

client = ro_py.Client()
async def byId(req, uid):
    user = await client.get_user(uid)
    name = user.display_name
    followers = await user.get_followers_count()
    following = await user.get_followings_count()
    status = await user.get_status
    banned = user.is_banned
    created = user.created
    friendcount = await user.get_friends_count()
    return render(req, 'user.html', {
        'name': name,
        'followers': followers,
        'following': following,
        'status': status, 
        'banned': banned,
        'created': created,
        'friendcount': friendcount
    })