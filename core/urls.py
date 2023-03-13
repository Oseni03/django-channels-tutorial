from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path("chat/", include("chat.urls", namespace="chat")),
    path("timer/", include("timer.urls", namespace="timer")),
    path("graph/", include("graph.urls", namespace="graph")),
]
