from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from game.models.player.player import Player
from random import randint

class PlayerView(APIView):
    def post(self, request):
        data = request.POST
        username = data.get("username", "").strip()
        password = data.get("password", "").strip()
        password_confirm = data.get("password_confirm", "").strip()
        if not username or not password:
            return Response({
                'result': "Username and password are required"
            })
        if password != password_confirm:
            return Response({
                'result': "The passwords you entered do not match"
            })
        if User.objects.filter(username=username).exists():
            return Response({
                'result': "The username has already existed"
            })
        user = User(username = username)
        user.set_password(password)
        user.save()
        Player.objects.create(user = user, photo = "https://www.bgvw.org/static/image/initial_image/" + str(randint(1, 37)) + ".png")
        return Response({
            'result': "success",
        })

def register(username, password, photo):
    user = User(username = username)
    user.set_password(password)
    user.save()
    Player.objects.create(user = user, photo = photo)