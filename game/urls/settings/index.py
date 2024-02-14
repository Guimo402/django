from django.urls import path, include
from game.views.settings.getinfo import InfoView
from game.views.settings.register import PlayerView
from game.views.settings.ranklist import RanklistView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # 参数：设置访问路径，调用函数名，这条路径的名字
    path("token/", TokenObtainPairView.as_view(), name="settings_token"), # 如果四类请求是用class的写法，一定要用.as_View()，把类封装成一个函数
    path("token/refresh/", TokenRefreshView.as_view(), name="settings_token_refresh"), 
    path("getinfo/", InfoView.as_view(), name="settings_getinfo"),
    path("register/", PlayerView.as_view(), name="settings_register"),
    path("ranklist/", RanklistView.as_view(), name="settings_ranklist"),
    path("acwing/", include("game.urls.settings.acwing.index")),
]
