from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserRegistrationForm
from .models import Refrence ,WeekPlan ,Student ,RefrenceSeri , Language, Category, Skill_level , Keyword
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required



def home(request):
    refrenceSeri = RefrenceSeri.objects.all()
    refrences = Refrence.objects.all()
    context = {
        'refrenceSeri': refrenceSeri,
        'refrences': refrences,
    }
    return render(request, 'home.html',context)

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
            username = request.POST['username']
            password = request.POST['password1']
            print(request.POST['password1'])
            user = authenticate(request, username=username, password=password)
            login(request, user)
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

def refrence_series(request):
    series = RefrenceSeri.objects.all()
    return render(request, 'refrence/series_list.html', {'series': series})

def language_list(request):
    languages = Language.objects.all()
    return render(request, 'refrence/language_list.html', {'languages': languages})

def refrence_category(request):
    categories = Category.objects.all()
    return render(request, 'refrence/refrence_category.html', {'categories': categories})

def refrence_skill_level(request):
    skill_level = Skill_level.objects.all()
    return render(request, 'refrence/refrence_skill_level.html', {'skill_level': skill_level})

def refrence_keyword(request):
    keywords = Keyword.objects.all()
    return render(request, 'refrence/refrence_keyword.html', {'keywords': keywords})

def language_detail(request, pk ):
    language = get_object_or_404(Language, pk=pk)
    refrences = language.refrence_set.all()
    context = {
        'language': language,
        'refrences': refrences,
    }
    return render(request, 'refrence/language_detail.html', context)

def category_detail(request, pk ):
    category = get_object_or_404(Category, pk=pk)
    refrences = category.refrence_set.all()
    context = {
        'category': category,
        'refrences': refrences,
    }
    return render(request, 'refrence/category_detail.html', context)

def keyword_detail(request, pk ):
    keyword = get_object_or_404(Keyword, pk=pk)
    refrences = keyword.refrence_set.all()
    context = {
        'keyword': keyword,
        'refrences': refrences,
    }
    return render(request, 'refrence/keyword_detail.html', context)


def skill_level_detail(request, pk ):
    skill_level = get_object_or_404(Skill_level, pk=pk)
    refrences = skill_level.refrence_set.all()
    context = {
        'skill_level': skill_level,
        'refrences': refrences,
    }
    return render(request, 'refrence/skill_level_detail.html', context)

def refrence_detail(request, slug):
    refrence = get_object_or_404(Refrence, slug=slug)
    return render(request, 'refrence/refrence_detail.html', {'refrence': refrence})

def refrence_seri_detail(request, slug ):
    refrenceSeri = get_object_or_404(RefrenceSeri, slug=slug)
    refrences = refrenceSeri.refrence_set.all()
    context = {
        'refrenceSeri': refrenceSeri,
        'refrences': refrences,
    }
    return render(request, 'refrence/refrence_seri_detail.html', context)


def search_refrences(request):
    query = request.GET.get('query', '')
    refrences = Refrence.objects.filter(name__icontains=query)
    return render(request, 'refrence/search_results.html', {'query': query, 'refrences': refrences})

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
