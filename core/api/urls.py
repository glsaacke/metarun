from django.urls import path
from . import views

urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="update",),
    path("user/", views.UserListCreate.as_view(), name="user-view-create"),
    path("user/<int:pk>/", views.UserRetrieveUpdateDestroy.as_view(), name="update"),
    path("activity/", views.ActivityListCreate.as_view(), name="activity-view-create"),
    path("activity/<int:pk>/", views.ActivityRetrieveUpdateDestroy.as_view(), name="update"),
    path("faq/", views.FaqListCreate.as_view(), name="faq-view-create"),
    path("faq/<int:pk>/", views.FaqRetrieveUpdateDestroy.as_view(), name="update"),
]