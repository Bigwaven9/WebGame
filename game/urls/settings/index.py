from django.urls import path, include
from game.views.settings.getinfo import InfoView
from game.views.settings.register import PlayerView
from game.views.settings.ranklist import RanklistView
from game.views.settings.github import github_login, github_callback
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("getinfo/", InfoView.as_view(), name = "settings_getinfo"),
    path("register/", PlayerView.as_view(), name = "settings_register"),
    path('token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('ranklist/', RanklistView.as_view(), name = "settings_ranklist"),
    path('login/', github_login, name = "github_login"),
    path('callback/', github_callback, name = "github_callback"),
]
