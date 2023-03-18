from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Homepage),
    path('login', views.loginpage),
    path('INVALID', views.INVALID),
    path('Register', views.RegisterPage),
    path('USER_RESTRICTED',views.USER_RESTRICTED),
    path('Welcome', views.Welcomepage),
    path('InactiveTasksList', views.ViewInActiveTasksList),
    path('Assigned-Tasks', views.TasksList),
    path('CreateTasks', views.CreateTaskpage),
    path('ReactivateT/<int:id>/',views.ReactivateTask),
    path('ReportBug', views.CreateBugpage),
    path('editT/<int:id>/',views.EditTaskpage),
    path('editB/<int:id>/',views.EditBugpage),
    path('deleteT/<int:id>/',views.DeleteTask),
    path('deleteB/<int:id>/',views.DeleteBug),
    path('ViewTasks', views.ViewActiveTasks),
    path('ViewBugs', views.BugsList),
    path('ViewActiveBugs', views.ViewActiveBugs),
    path('ViewInActiveBugs', views.ViewInActiveBugs),
    path('ReactivateB/<int:id>/',views.ReactivateBug),
    path('ViewFiles', views.ViewFiles),
    path('CreateProjects', views.CreateProjectpage),
    path('Projects', views.ProjectsList),
    path('editP/<int:id>/', views.EditProjectpage),
    path('deleteP/<int:id>/',views.DeleteProject),
    path('ReactivateP/<int:id>/',views.ReactivateProject),
    path('ViewActiveProjects', views.ViewActiveProjects),
    path('ViewInActiveProjects', views.ViewInActiveProjects),
    path('logout',views.logoutt)
]