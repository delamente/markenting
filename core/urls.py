import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog

from common.views import (
    bad_request, page_not_found, permission_denied, server_error,
    simulated_error, change_language,
)
from marketing.views import ContactView, home, ServiceDetailView, ServiceListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('hijack/', include('hijack.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('simulated-error/', simulated_error),
    path('change-language/', change_language, name='change-language'),

    path('', home, name='home'),
    path('servicios/', ServiceListView.as_view(), name='service_list'),
    path('servicios/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('contacto/', ContactView.as_view(), name='contact'),
    path('acerca-de/', TemplateView.as_view(template_name='about.html'), name='about'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        path('error400/', bad_request),
        path('error403/', permission_denied),
        path('error404/', page_not_found),
        path('error500/', server_error),
    ]

admin.site.site_header = settings.PROJECT_DISPLAY_NAME

handler400 = 'common.views.bad_request'
handler403 = 'common.views.permission_denied'
handler404 = 'common.views.page_not_found'
handler500 = 'common.views.server_error'
