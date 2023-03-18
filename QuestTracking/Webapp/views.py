from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import CreateTask, Profiles, File, CreateBug, Projects
from datetime import datetime
from django.contrib.auth.decorators import login_required

#***************************************************HOME PAGE**********************************************************#
def Welcomepage(request):
    user = getuser
    Type = Id
    print(Type)
    if (Type[0] == 'E'):
        if(Type[1] == 'D'):
            return render(request, 'WelcomePageDeveloper.html', {'name': user})
        elif(Type[1] == 'T'):
            return render(request, 'WelcomePageTester.html', {'name': user})
    elif (Type[0] == 'M'):
        return render(request, 'WelcomePageManager.html', {'name': user})
    elif (Type[0] == 'D'):
        return render(request, 'WelcomePageDirector.html', {'name': user})
    elif (Type[0] == 'S'):
        return render(request, 'WelcomePageSupport.html', {'name': user})

def Homepage(request):
    return render(request, 'Homepage.html')

def INVALID(request):
    return render(request,'Invalid.html')
def USER_RESTRICTED(request):
    return render(request,'UserRestricted.html')


#***************************************************REGISTRATION*******************************************************#
@login_required(login_url="/login")
def RegisterPage(request):
    x = Id
    if x[0] == 'S':
        if request.method == 'POST':
            name = request.POST['name']
            employeeid = request.POST['employeeid']
            emailid = request.POST['emailid']
            employeedes = request.POST['employeedes']
            username = request.POST['username']
            password = request.POST['password']
            n = name.split(' ')
            global Newuser
            Newuser = User.objects.create_user(username, emailid, password)
            Newuser.first_name = n[0]
            if len(n) > 1 and len(n) < 3:
                Newuser.last_name = n[1]
            Newuser.EmployeeId = employeeid
            Newuser.EmailId = emailid
            Newuser.Username = username
            Newuser.Password = password
            Newuser.save()
            Pro = Profiles()
            Pro.Name = name
            Pro.EmployeeId = employeeid
            Pro.EmployeeDesignation =employeedes
            Pro.Username = username
            Pro.save()
        return render(request, 'Signin.html')
    else:
        return redirect('/USER_RESTRICTED')

#***************************************************LOGIN**************************************************************#
def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        global details
        s= ' '
        details = authenticate(username=username, password=password)
        if details is not None:
            login(request, details)
            name = Profiles.objects.all().values()
            print(name)
            global Id
            for i in name:
                if i['Username'] == str(details):
                    s = i['Name']
                    Id = i['EmployeeId']
                    break
            global Name
            Name = s
            s = s.split(' ')
            global getuser
            getuser = s[0]
            print(Id)
            return redirect('/Welcome')
        else:
            return redirect('/INVALID')
    return render(request, 'login.html')



#***************************************************TASKS**************************************************************#
@login_required(login_url="/login")
def CreateTaskpage(request):
    x1 = Id
    if x1[0] == 'M':
        x = getuser
        name = Profiles.objects.all().values()
        n = []
        for i in name:
            n.append(i['Name'])
        if request.method == 'POST':
            task_name = request.POST['Taskname']
            task_description = request.POST['Description']
            task_due = request.POST['Duedate']
            task_emp = request.POST['assignedEmp']
            task_file = request.FILES['File']
            task_due = task_due.split('-')
            task_due = task_due[::-1]
            task_due = '-'.join(task_due)
            tsk = CreateTask()
            tsk.TaskName = task_name
            tsk.Description = task_description
            tsk.DueDate = task_due
            tsk.AssignedEmployee = task_emp
            tsk.Status = "Assigned by " + x
            tsk.StatusDescription = "Assigned"
            tsk.file = task_file
            tsk.save()
            fil = File()
            fil.Name = task_name
            fil.Type = "Task"
            fil.EmployeeId = Id
            fil.Date_Time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            fil.file = task_file
            fil.save()
            print(fil)
            return redirect('/Welcome')
        return render(request, 'TaskCreate.html', {'em': n})
    else:
        return redirect('/USER_RESTRICTED')


def TasksList(request):
    useR = Id
    data = None
    if(useR[0]=='M'):
        data = CreateTask.objects.filter(Status= "Assigned by " + Name ).values()
    elif(useR[0]=='E'):
        data = CreateTask.objects.filter(AssignedEmployee=Name).values()
    print(data)
    n = []
    for i in data:
        n1 = []
        for j in i:
            n1.append(i[j])
        if n1[-2] != 1:
            n1[-2] = "INACTIVE"
        else:
            n1[-2] = "ACTIVE"
        n1.pop(-1)
        n1.append(i['file'])
        n.append(n1)
    for i in n:
        i[3] = i[3].split('-')
        i[3] = i[3][::-1]
        i[3] = '-'.join(i[3])
    return render(request, 'EmployeeTasks.html', {'task': n})


def EditTaskpage(request, id):
    name = Profiles.objects.all().values()
    n = []
    for i in name:
        if (i['EmployeeId'][0] == 'E'):
            n.append(i['Name'])
    taskdetails = CreateTask.objects.get(id=id)
    if request.method == 'POST':
        task_due = request.POST['DueDate']
        task_emp = request.POST['assignedEmp']
        task_status = request.POST['tskstatus']
        task_status_Des = request.POST['tskstatdes']
        taskdetails.DueDate = task_due
        taskdetails.AssignedEmployee = task_emp
        taskdetails.Status = task_status
        taskdetails.StatusDescription = task_status_Des
        taskdetails.save()
        return redirect('/Welcome')
    return render(request, 'EditTask.html', {'em': n, 'tsk': taskdetails})


def DeleteTask(request,id):
    taskdetails = CreateTask.objects.get(id=id)
    taskdetails.Active = False
    taskdetails.save()
    return redirect('/Welcome')
def ReactivateTask(request,id):
    taskdetails = CreateTask.objects.get(id=id)
    taskdetails.Active = True
    taskdetails.save()
    return redirect('/Welcome')
def ReactivateTask(request,id):
    taskdetails = CreateTask.objects.get(id=id)
    taskdetails.Active = True
    taskdetails.save()
    return redirect('/Welcome')

def ViewActiveTasks(request):
    data = CreateTask.objects.all().values()
    n = []
    for i in data:
        n1 = []
        for j in i:
            n1.append(i[j])
        if n1[-2] == 1:
            n1.pop(-2)
            n1.pop(-1)
            n.append(n1)
    for i in n:
        i[3] = i[3].split('-')
        i[3] = i[3][::-1]
        i[3] = '-'.join(i[3])
    return render(request, 'ViewActiveTasks.html', {'task': n,'x':len(n)})


def ViewInActiveTasksList(request):
    data = CreateTask.objects.all().values()
    n = []
    for i in data:
        n1 = []
        for j in i:
            n1.append(i[j])
        if n1[-2] != 1:
            n1.pop(-2)
            n1.pop(-1)
            n.append(n1)
    for i in n:
        i[3] = i[3].split('-')
        i[3] = i[3][::-1]
        i[3] = '-'.join(i[3])
    return render(request, 'InActiveTasks.html', {'task': n,'x':len(n)})

#***************************************************BUGS***************************************************************#

def CreateBugpage(request):
    name = CreateTask.objects.all().values()
    c = getuser
    n = []
    for i in name:
        n.append(i['TaskName'])
    if request.method == 'POST':
        Bug_name = request.POST['Bugname']
        Bug_description = request.POST['Description']
        Bug_AraiseTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        BuggedTask = request.POST['BugTask']
        Bug_file = request.FILES['File']
        Bug = CreateBug()
        Bug.BugName = Bug_name
        Bug.Description = Bug_description
        Bug.AraiseDate = Bug_AraiseTime
        Bug.In_Task = BuggedTask
        Bug.Status = "Raised by " + c
        Bug.StatusDescription = "Raised"
        Bug.file = Bug_file
        Bug.save()
        fil = File()
        fil.Name = Bug_name
        fil.Type = "Bug"
        fil.EmployeeId = Id
        fil.Date_Time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        fil.file = Bug_file
        fil.save()
        return redirect('/Welcome')
    return render(request, 'CreateBug.html', {'em': n})

def EditBugpage(request, id):
    Bugdetails = CreateBug.objects.get(id=id)
    if request.method == 'POST':
        Bug_status = request.POST['Bugstatus']
        Bug_status_Des = request.POST['Bugstatdes']
        Bug_file = request.POST['BugFile']
        Bugdetails.Status = Bug_status
        Bugdetails.StatusDescription = Bug_status_Des
        Bugdetails.file = Bug_file
        Bugdetails.save()
        fil = File()
        fil.Name = Bugdetails.BugName
        fil.Type = "Bug"
        fil.EmployeeId = Id
        fil.Date_Time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        fil.file = Bug_file
        fil.save()
        return redirect('/Welcome')
    return render(request, 'EditBug.html', {'Bug': Bugdetails})


def ViewActiveBugs(request):
    data = CreateBug.objects.all().values()
    n = []
    for i in data:
        n1 = []
        for j in i:
            n1.append(i[j])
        if n1[-2] == 1:
            n1.pop(-2)
        n.append(n1)
    print(n)
    return render(request, 'ViewActiveBugs.html', {'Bug': n,'x':len(n)})

def ViewInActiveBugs(request):
    data = CreateBug.objects.all().values()
    n = []
    for i in data:
        n1 = []
        for j in i:
            n1.append(i[j])
        if n1[-2] != 1:
            n1.pop(-2)
            n1.pop(-1)
            n.append(n1)
    print(n)
    return render(request, 'InActiveBugs.html', {'Bug': n,'x':len(n)})

def BugsList(request):
    data = CreateBug.objects.all().values()
    print(data)
    n = []
    for i in data:
        n1 = []
        for j in i:
            n1.append(i[j])
        if n1[-2] != 1:
            n1[-2] = "INACTIVE"
        else:
            n1[-2] = "ACTIVE"
        n.append(n1)
    return render(request, 'ViewBugs.html', {'Bug': n})

def DeleteBug(request,id):
    Bugdetails = CreateBug.objects.get(id=id)
    Bugdetails.Active = False
    Bugdetails.save()
    return redirect('/Welcome')
def ReactivateBug(request,id):
    Bugdetails = CreateBug.objects.get(id=id)
    Bugdetails.Active = True
    Bugdetails.save()
    return redirect('/Welcome')

#***************************************************PROJECTS**********************************************************#
def CreateProjectpage(request):
    x = getuser
    name = Profiles.objects.all().values()
    n = []
    for i in name:
        if(i['EmployeeId'][0]=='M'):
            n.append(i['Name'])
    if request.method == 'POST':
        project_name = request.POST['Projectname']
        project_description = request.POST['Description']
        project_due = request.POST['Duedate']
        project_Man = request.POST['assignedMan']
        project_file = request.FILES['File']
        project_due = project_due.split('-')
        project_due = project_due[::-1]
        project_due = '-'.join(project_due)
        pro = Projects()
        pro.ProjectName = project_name
        pro.ProjectDescription = project_description
        pro.ProjectDeadline = project_due
        pro.AssignedManager = project_Man
        pro.Status = "Assigned by " + x
        pro.StatusDescription = "Assigned"
        pro.file = project_file
        pro.save()
        fil = File()
        fil.Name = project_name
        fil.Type = "Project"
        fil.EmployeeId = Id
        fil.Date_Time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        fil.file = project_file
        fil.save()
        print(fil)
        return redirect('/Welcome')
    return render(request, 'ProjectCreate.html', {'em': n})

def ProjectsList(request):
    useR = Id
    if useR[0] == 'D':
        data = Projects.objects.all().values()
        print(data)
        n = []
        for i in data:
            n1 = []
            for j in i:
                n1.append(i[j])
            if n1[-2] != 1:
                n1[-2] = "INACTIVE"
            else:
                n1[-2] = "ACTIVE"
            n1.pop(-1)
            n1.append(i['file'])
            n.append(n1)
        for i in n:
            i[3] = i[3].split('-')
            i[3] = i[3][::-1]
            i[3] = '-'.join(i[3])
        print(n)
        return render(request, 'DirectorProjects.html', {'task': n})
    else:
        return redirect('/USER_RESTRICTED')


def EditProjectpage(request, id):
    name = Profiles.objects.all().values()
    n = []
    for i in name:
        if (i['EmployeeId'][0] == 'M'):
            n.append(i['Name'])
    Prodetails = Projects.objects.get(id=id)
    if request.method == 'POST':
        Pro_due = request.POST['DueDate']
        Pro_emp = request.POST['assignedMan']
        Pro_status = request.POST['prostatus']
        Pro_status_Des = request.POST['prostatdes']
        Prodetails.DueDate = Pro_due
        Prodetails.AssignedEmployee = Pro_emp
        Prodetails.Status = Pro_status
        Prodetails.StatusDescription = Pro_status_Des
        Prodetails.save()
        return redirect('/Welcome')
    return render(request, 'EditProject.html', {'em': n, 'tsk': Prodetails})


def DeleteProject(request,id):
    Prodetails = Projects.objects.get(id=id)
    Prodetails.Active = False
    Prodetails.save()
    return redirect('/Welcome')
def ReactivateProject(request,id):
    Prodetails = Projects.objects.get(id=id)
    Prodetails.Active = True
    Prodetails.save()
    return redirect('/Welcome')

def ViewActiveProjects(request):
    data = Projects.objects.all().values()
    print(data)
    n = []
    if data is not None:
        for i in data:
            n1 = []
            for j in i:
                n1.append(i[j])
            if n1[-2] == 1:
                n1.pop(-2)
                n1.pop(-1)
                n.append(n1)
        for i in n:
            i[3] = i[3].split('-')
            i[3] = i[3][::-1]
            i[3] = '-'.join(i[3])
    print(n)
    return render(request, 'ViewActiveProjects.html', {'task': n,'x':len(n)})


def ViewInActiveProjects(request):
    data = Projects.objects.all().values()
    n = []
    if data is not None:
        for i in data:
            n1 = []
            for j in i:
                n1.append(i[j])
            if n1[-2] != 1:
                n1.pop(-2)
                n1.pop(-1)
                n.append(n1)
        for i in n:
            i[3] = i[3].split('-')
            i[3] = i[3][::-1]
            i[3] = '-'.join(i[3])
    return render(request, 'InActiveProjects.html', {'task': n,'x':len(n)})





#***************************************************FILES**************************************************************#
def ViewFiles(request):
    data = File.objects.all().values()
    n = []
    for i in data:
        n1 = []
        for j in i:
            n1.append(i[j])
        n.append(n1)
    return render(request, 'FileView.html', {'task': n,'x':len(n)})


#***************************************************LOGOUT*************************************************************#
def logoutt(request):
    logout(request)
    return redirect('/')