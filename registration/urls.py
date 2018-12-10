from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path
from django.views.generic.edit import CreateView


urlpatterns = [
    path('register/', CreateView.as_view(
        template_name='registration/register.html',
        form_class=UserCreationForm,
        success_url='/',
    ), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
