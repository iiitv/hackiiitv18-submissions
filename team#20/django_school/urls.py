from  classroom.views import classroom , students , teachers
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('classroom.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('admin/', admin.site.urls),
]
