from django.urls import path
from django.views.generic import TemplateView

from pages import views as page_views
from .views import HomePageView, InviteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('invite/', InviteView.as_view(), name='invite'),
    path('invite-success/', TemplateView.as_view(template_name='account/new_admin_registration_success.html'),
         name='invite-success'),
    path('docs', page_views.DocsView.as_view(), name='docs'),
    path('generate-schedule', page_views.GenerateScheduleView.as_view(), name='generate-schedule'),
    path('check-schedule', page_views.CheckScheduleView.as_view(), name='check-schedule'),
    path('crud', page_views.CrudView.as_view(), name='crud'),
    path('student-form', page_views.StudentFormSuccessView.as_view(), name='student-form-success'),
    path('calendar/<slug:schedule_id>', page_views.CalendarView.as_view(), name='calendar-view'),
    path('schedule-redirect', page_views.ScheduleRedirectView.as_view(), name='schedule-redirect'),
]

app_name = 'pages'
