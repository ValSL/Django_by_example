from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list_url'),
    path('tag/<slug:tag_slug>', views.post_list, name='post_list_by_tag_url'),
    # path('', views.PostListView.as_view(), name='post_list_url'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail_url'),
    path('<int:post_id>/share', views.post_share, name='post_share_url'),

]
