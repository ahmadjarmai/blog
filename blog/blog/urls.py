from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blogapp.sitemaps import PostSiteMap

sitemaps ={
    'sitemaps':PostSiteMap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
 name='django.contrib.sitemaps.views.sitemap')
]

"""if settings.DEDUG :
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
"""
