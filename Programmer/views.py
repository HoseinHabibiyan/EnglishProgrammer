from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm , WeekPlanForm ,StudentForm , DailyProgramForm ,UserRegistrationForm
from .models import Refrence ,WeekPlan ,Student ,DailyProgram
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

    def get_next_page(self):
        next_page = super().get_next_page()
        # Add any additional logic you need
        return next_page
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            error_message = 'Invalid username or password'
            return render(request, 'auth/login.html', {'error_message': error_message})
    else:
        return render(request, 'auth/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Additional actions (e.g., login the user)
            return redirect('home')  # Redirect to the desired page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form': form})

# ------------------------------------------------#
#                Book views                
# ------------------------------------------------#

def refrence_list(request):
    refrences = Refrence.objects.all()
    return render(request, 'refrence/refrence_list.html', {'refrences': refrences})


def refrence_detail(request, pk):
    refrence = get_object_or_404(Refrence, pk=pk)
    return render(request, 'refrence/refrence_detail.html', {'refrence': refrence})



# ------------------------------------------------#
#                 Week Plan views                
# ------------------------------------------------#

@login_required
def weekplan_list(request):
    current_user = request.user
    current_student = Student.objects.filter(user= current_user).first()
    weekplans = WeekPlan.objects.filter(Student=current_student)
    return render(request, 'weekplans/weekplan_list.html', {'weekplans': weekplans})

@login_required
def weekplan_detail(request, pk):
    weekplan = get_object_or_404(WeekPlan, pk=pk)
    return render(request, 'weekplans/weekplan_detail.html', {'weekplan': weekplan})

@login_required
def weekplan_create(request):
    if request.method == 'POST':
        form = WeekPlanForm(request.POST)
        if form.is_valid():
            weekplan = form.save()
            return redirect('weekplan_detail', pk=weekplan.pk)
    else:
        form = WeekPlanForm()
    return render(request, 'weekplans/weekplan_form.html', {'form': form})

@login_required
def weekplan_update(request, pk):
    weekplan = get_object_or_404(WeekPlan, pk=pk)
    if request.method == 'POST':
        form = WeekPlanForm(request.POST, instance=weekplan)
        if form.is_valid():
            weekplan = form.save()
            return redirect('weekplan_detail', pk=weekplan.pk)
    else:
        form = WeekPlanForm(instance=weekplan)
    return render(request, 'weekplans/weekplan_form.html', {'form': form})

@login_required
def weekplan_delete(request, pk):
    weekplan = get_object_or_404(WeekPlan, pk=pk)
    weekplan.delete()
    return redirect('weekplan_list')


# ------------------------------------------------#
#                 Student views                
# ------------------------------------------------#

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

@login_required
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

@login_required
def student_create(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    return render(request, 'students/student_form.html', {'form': form})

@login_required
def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    return render(request, 'students/student_form.html', {'form': form, 'student': student})

@login_required
def student_delete(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_confirm_delete.html', {'student': student})


# ------------------------------------------------#
#                Daily Program views                
# ------------------------------------------------#

@login_required
def dailyprogram_create(request, weekplan_id):
    weekplanobject = get_object_or_404(WeekPlan, pk=weekplan_id)
     
    form = DailyProgramForm(request.POST or None)
    
    if form.is_valid():
        dailyprogram = form.save(commit=False)
        weekplanobject = get_object_or_404(WeekPlan, pk=weekplan_id)
        dailyprogram.relatedweek = weekplanobject
        dailyprogram.save()
        return redirect('weekplan_detail', weekplanobject.pk)
    return render(request, 'dailyprograms/dailyprogram_create.html', {'form': form, 'weekplan': weekplanobject})

@login_required
def dailyprogram_update(request, weekplan_id, dailyprogram_id):
    weekplan = get_object_or_404(WeekPlan, pk=weekplan_id)
    dailyprogram = get_object_or_404(DailyProgram, pk=dailyprogram_id)
    form = DailyProgramForm(request.POST or None, instance=dailyprogram)
    if form.is_valid():
        form.save()
        return redirect('weekplan_detail', weekplan.pk)
    return render(request, 'dailyprograms/dailyprogram_update.html', {'form': form, 'weekplan': weekplan, 'dailyprogram': dailyprogram})

@login_required
def dailyprogram_detail(request, weekplan_id, dailyprogram_id):
    weekplan = get_object_or_404(WeekPlan, pk=weekplan_id)
    dailyprogram = get_object_or_404(DailyProgram, pk=dailyprogram_id)
    return render(request, 'dailyprograms/dailyprogram_detail.html', {'weekplan': weekplan, 'dailyprogram': dailyprogram})

@login_required
def dailyprogram_delete(request, weekplan_id, dailyprogram_id):
    weekplan = get_object_or_404(WeekPlan, pk=weekplan_id)
    dailyprogram = get_object_or_404(DailyProgram, pk=dailyprogram_id)
    if request.method == 'POST':
        dailyprogram.delete()
        return redirect('weekplan_detail', weekplan.pk)
    return render(request, 'dailyprograms/dailyprogram_delete.html', {'weekplan': weekplan, 'dailyprogram': dailyprogram})