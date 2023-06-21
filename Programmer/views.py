from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm , WeekPlanForm ,StudentForm , DailyProgramForm
from .models import Book ,WeekPlan ,Student ,DailyProgram
import pdb; pdb.set_trace()

# ------------------------------------------------#
#                Book views                
# ------------------------------------------------#

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'form': form, 'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})



# ------------------------------------------------#
#                 Week Plan views                
# ------------------------------------------------#

def weekplan_list(request):
    weekplans = WeekPlan.objects.all()
    return render(request, 'weekplans/weekplan_list.html', {'weekplans': weekplans})

def weekplan_detail(request, pk):
    weekplan = get_object_or_404(WeekPlan, pk=pk)
    return render(request, 'weekplans/weekplan_detail.html', {'weekplan': weekplan})

def weekplan_create(request):
    if request.method == 'POST':
        form = WeekPlanForm(request.POST)
        if form.is_valid():
            weekplan = form.save()
            return redirect('weekplan_detail', pk=weekplan.pk)
    else:
        form = WeekPlanForm()
    return render(request, 'weekplans/weekplan_form.html', {'form': form})

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

def weekplan_delete(request, pk):
    weekplan = get_object_or_404(WeekPlan, pk=pk)
    weekplan.delete()
    return redirect('weekplan_list')


# ------------------------------------------------#
#                 Student views                
# ------------------------------------------------#

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

def student_create(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    return render(request, 'students/student_form.html', {'form': form})

def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    return render(request, 'students/student_form.html', {'form': form, 'student': student})

def student_delete(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_confirm_delete.html', {'student': student})



# ------------------------------------------------#
#                Daily Program views                
# ------------------------------------------------#


def dailyprogram_create(request, weekplan_id):
    weekplanobject = get_object_or_404(WeekPlan, pk=weekplan_id)
     
    form = DailyProgramForm(request.POST or None)
    
    if form.is_valid():
        dailyprogram = form.save(commit=False)
        weekplanobject = get_object_or_404(WeekPlan, pk=weekplan_id)
        dailyprogram.weekplan = weekplanobject
        dailyprogram.save()
        return redirect('weekplan_detail', weekplanobject.pk)
    return render(request, 'dailyprograms/dailyprogram_create.html', {'form': form, 'weekplan': weekplanobject})

def dailyprogram_update(request, weekplan_id, dailyprogram_id):
    weekplan = get_object_or_404(WeekPlan, pk=weekplan_id)
    dailyprogram = get_object_or_404(DailyProgram, pk=dailyprogram_id)
    form = DailyProgramForm(request.POST or None, instance=dailyprogram)
    if form.is_valid():
        form.save()
        return redirect('weekplan_detail', weekplan.pk)
    return render(request, 'dailyprograms/dailyprogram_update.html', {'form': form, 'weekplan': weekplan, 'dailyprogram': dailyprogram})

def dailyprogram_detail(request, weekplan_id, dailyprogram_id):
    weekplan = get_object_or_404(WeekPlan, pk=weekplan_id)
    dailyprogram = get_object_or_404(DailyProgram, pk=dailyprogram_id)
    return render(request, 'dailyprograms/dailyprogram_detail.html', {'weekplan': weekplan, 'dailyprogram': dailyprogram})

def dailyprogram_delete(request, weekplan_id, dailyprogram_id):
    weekplan = get_object_or_404(WeekPlan, pk=weekplan_id)
    dailyprogram = get_object_or_404(DailyProgram, pk=dailyprogram_id)
    if request.method == 'POST':
        dailyprogram.delete()
        return redirect('weekplan_detail', weekplan.pk)
    return render(request, 'dailyprograms/dailyprogram_delete.html', {'weekplan': weekplan, 'dailyprogram': dailyprogram})