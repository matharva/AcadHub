from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'postandcomment_app'

urlpatterns = [
    # path('comment/', views.registerPage, name="comment"),
	path('post/<int:post_id>', views.postView, name="post"),  
    path('projectPost/<int:ppost_id>', views.projectPostView, name="projectPost"),  
    path('createPost/<slug:community_name>', views.postCreateView, name="createPost"),
    path('createProject/', views.createProjectPost, name="createProjectPost"),
    path('community/<slug:community_name>', views.communityView, name="community"),
    path('createCommunity/', views.communityCreateView, name='createCommunity'),
    path('community/', views.communityListView, name='com'),
    path('projects/', views.projectListView, name='proj'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)