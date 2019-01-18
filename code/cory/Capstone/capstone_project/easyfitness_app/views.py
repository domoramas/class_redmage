from django.shortcuts import (
    render, 
    get_object_or_404, 
    get_list_or_404, 
    redirect
)
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from .models import Exercise, Workout
from django.contrib.auth.models import User
from .forms import WorkoutForm
from django.forms import modelformset_factory


import itertools

from django.views.generic import(
    ListView, 
    CreateView, 
    DetailView,
    UpdateView,
    DeleteView
)

def indexView(request):
    return render(request, "home.html")

class AllExerciseView(ListView):
    model = Exercise
    template_name = "all_exercise_muscles.html"

    def get_queryset(self):
        
        out_list = set(
            Exercise.objects.values_list('workout_muscle', flat=True)
        )

        out_list = sorted(out_list, key=lambda tup: (tup[0]))

        return out_list

class AllExerciseListView(ListView):
    model = Exercise
    template_name = "all_exercise_muscles_list.html"

    def get_queryset(self):
        out_list = Exercise.objects.filter(workout_muscle=self.kwargs['muscle'])
        return out_list

def AllExerciseDetail(request, pk, slug):
    # WorkoutFormSet = modelformset_factory(Workout, fields=('name',))
    # if request.method == 'POST': # If the form has been submitted...
    #     formset = WorkoutFormSet(request.POST, request.FILES) # A form bound to the POST data
    #     if formset.is_valid(): # All validation rules pass
    #         formset.save()
    #     return redirect('home') # Redirect after POST
    # else:
    #     formset = WorkoutForm() # An unbound form


    exercise = Exercise.objects.get(pk=pk)
    context = {
        'object': exercise
    }

    return render(request, 'all_exercise_details.html', context)

# class AllExerciseDetail(DetailView):
#     model = Exercise
#     template_name = 'all_exercise_details.html'



# ------------------------------------------------------------------------------


#  USER VIEWS

# Lists Workouts
class WorkoutUserView(LoginRequiredMixin, ListView): 
    model = Workout
    template_name = 'user_workout.html'

    def get_queryset(self):
       
        out_var = Workout.objects.filter(user__username=self.kwargs['user']).order_by('-date_created')
        
        return out_var

# Lists Exercises in Workouts
class WorkoutUserExerciseView(LoginRequiredMixin, ListView): 
    model = Exercise
    template_name = 'user_workout_exercises.html'

    def get_queryset(self):
        return Exercise.objects.filter(workout__pk=self.kwargs['pk'])

class WorkoutUserExerciseDetail(LoginRequiredMixin, DetailView):
    model = Exercise
    template_name = 'user_workout_exercise_detail.html'

class WorkoutUserCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ['name']
    template_name = "user_workout_creation.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user-workout', kwargs = {'user': self.request.user})

def AddToWorkout(request, pk, user):

    if request.method == 'POST': # If the form has been submitted...
        form = WorkoutForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            print('Test1')
        return HttpResponseRedirect(reverse('user-workout', kwargs = {'user': request.user })) # Redirect after POST
    else:
        form = WorkoutForm() # An unbound form

    return render(request, 'home')
    

# ------------------------------------------------------------------------------


# DEFAULT CARDIO VIEWS
def defaultCardioInitView(request):
    return render(request, "default_cardio_init.html" )

def defaultCardioView(request):
    return render(request, "default_cardio.html")

# Slicing changed, gits rid of some N/A
class DefaultCardioDay1(ListView):
    model = Exercise
    template_name = "default_cardio_day1.html"

    def get_queryset(self):
        cardio_exercise = Exercise.objects.filter(workout_type="Cardio")
        cardio_day1 = cardio_exercise.order_by('-rating_number')[2:7]
        return cardio_day1

class DefaultCardioDay2(ListView):
    model = Exercise
    template_name = "default_cardio_day2.html"

    def get_queryset(self):
        cardio_exercise = Exercise.objects.filter(workout_type="Cardio")
        cardio_day2 = cardio_exercise.order_by('-rating_number')[7:12]
        return cardio_day2

class DefaultCardioDay3(ListView):
    model = Exercise
    template_name = "default_cardio_day3.html"

    def get_queryset(self):
        cardio_exercise = Exercise.objects.filter(workout_type="Cardio")
        cardio_day3 = cardio_exercise.order_by('-rating_number')[12:17]
        return cardio_day3

class DefaultCardioDetail(DetailView):
    model = Exercise
    template_name = "default_cardio_detail.html"


# ------------------------------------------------------------------------------


# DEFAULT STRENGTH VIEWS
def defaultStrengthInitView(request):
    return render(request, "default_strength_init.html" )

def defaultStrengthView(request):
    return render(request, "default_strength.html")

class DefaultStrengthDay1(ListView):
    model = Exercise
    template_name = "default_strength_day1.html"

    def get_queryset(self):
        strength_exercise = Exercise.objects.filter(workout_type="Strength")

        strength_chest = strength_exercise.filter(workout_muscle="Chest")[:3]

        strength_shoulders = strength_exercise.filter(workout_muscle="Shoulders")[:3]

        strength_triceps = strength_exercise.filter(workout_muscle="Triceps")[:3]

        return itertools.chain(strength_chest, strength_shoulders, strength_triceps)

class DefaultStrengthDay2(ListView):
    model = Exercise
    template_name = "default_strength_day2.html"

    def get_queryset(self):
        strength_exercise = Exercise.objects.filter(workout_type="Strength")

        strength_mid_back = strength_exercise.filter(workout_muscle="Middle Back")[:3]

        strength_low_back = strength_exercise.filter(workout_muscle="Lower Back")[:3]

        strength_biceps = strength_exercise.filter(workout_muscle="Biceps")[:3]

        return itertools.chain(strength_mid_back, strength_low_back, strength_biceps)

class DefaultStrengthDay3(ListView):
    model = Exercise
    template_name = "default_strength_day3.html"

    def get_queryset(self):
        strength_exercise = Exercise.objects.filter(workout_type="Strength")

        strength_hamstring = strength_exercise.filter(workout_muscle="Hamstrings")[:3]

        strength_calves = strength_exercise.filter(workout_muscle="Calves")[:3]

        strength_glutes = strength_exercise.filter(workout_muscle="Glutes")[:3]

        return itertools.chain(strength_hamstring, strength_calves, strength_glutes)

class DefaultStrengthDetail(DetailView):
    model = Exercise
    template_name = "default_strength_detail.html"


# ------------------------------------------------------------------------------


# DEFAULT STRETCH VIEWS
def defaultStretchInitView(request):
    return render(request, "default_stretch_init.html" )

def defaultStretchView(request):
    return render(request, "default_stretch.html")

# Slicing changed, gits rid of some N/A
class DefaultStretchDay1(ListView):
    model = Exercise
    template_name = "default_stretch_day1.html"

    def get_queryset(self): 
        stretch_exercise = Exercise.objects.filter(workout_type="Stretching")
        stretch_day1 = stretch_exercise.order_by('-rating_number')[3:8]
        return stretch_day1

class DefaultStretchDay2(ListView):
    model = Exercise
    template_name = "default_stretch_day2.html"

    def get_queryset(self):
        stretch_exercise = Exercise.objects.filter(workout_type="Stretching")
        stretch_day2 = stretch_exercise.order_by('-rating_number')[8:13]
        return stretch_day2

class DefaultStretchDay3(ListView):
    model = Exercise
    template_name = "default_stretch_day3.html"

    def get_queryset(self):
        stretch_exercise = Exercise.objects.filter(workout_type="Stretching")
        stretch_day3 = stretch_exercise.order_by('-rating_number')[13:18]
        return stretch_day3

class DefaultStretchDetail(DetailView):
    model = Exercise
    template_name = "default_stretch_detail.html"
