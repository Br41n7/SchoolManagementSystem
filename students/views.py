from django.contrib.auth import get_user_model
from students.models import Student

# create linked user
User = get_user_model()
# Create your views here.
user = User.objects.create_user(
    username=app.email,
    email=app.email,
    password=User.objects.make_random_password(),
)
student = Student.objects.create(
    user=user,
    full_name=app.full_name,
    program=app.program,
)
app.student_created = True
app.save()
messages.success(request, f"Student profile created for {app.full_name}")
