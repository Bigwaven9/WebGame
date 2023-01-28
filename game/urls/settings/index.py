from django.urls import path, include
from game.views.settings.getinfo import InfoView
from game.views.settings.register import register
from game.views.settings.ranklist import RanklistView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("getinfo/", InfoView.as_view(), name = "settings_getinfo"),
    path("register/", register, name = "settings_register"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('ranklist/', RanklistView.as_view(), name="settings_ranklist"),
]
