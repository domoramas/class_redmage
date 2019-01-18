from django.urls import path, include
from . import views

# app_name = 'easyfittness'

urlpatterns = [
    path('', views.indexView, name="home"),

    path('all-exercises/', views.AllExerciseView.as_view(), name="all-exercise-muscles"),

    path('all-exercises/<str:muscle>', views.AllExerciseListView.as_view(), name="all-exercise-muscles-list"),

    path('all-exercises/details/<int:pk>/<str:slug>', views.AllExerciseDetail, name="all-exercise-details"),

    # path('all-exercises/details/<int:pk>/<str:slug>', views.AllExerciseDetail.as_view(), name="all-exercise-details"),

    # --------------------------------------------------------------------------
    
    # USER
    path('user/<str:user>/', views.WorkoutUserView.as_view(), name="user-workout"),

    path('user/<str:user>/<int:pk>/', views.WorkoutUserExerciseView.as_view(), name="user-workout-exercises"),

    path('user/details/<int:pk>/<str:slug>/', views.WorkoutUserExerciseDetail.as_view(), name="user-workout-exercise-detail"),

    path('user/<str:user>/create-workout/', views.WorkoutUserCreateView.as_view(), name="user-workout-creation"),

    # --------------------------------------------------------------------------

    # CARDIO
    path('default/cardio/init', views.defaultCardioInitView, name="default-cardio-init"),

    path('default/cardio/', views.defaultCardioView, 
    name="default-cardio"),

    path('default/cardio/day1', views.DefaultCardioDay1.as_view(), name="default-cardio-day1"),

    path('default/cardio/day2', views.DefaultCardioDay2.as_view(), name="default-cardio-day2"),

    path('default/cardio/day3', views.DefaultCardioDay3.as_view(), name="default-cardio-day3"),

    path('default/cardio/detail/<int:pk>/<str:slug>', views.DefaultCardioDetail.as_view(),name="default-cardio-detail"),

    # --------------------------------------------------------------------------
    
    # STRENGTH
    path('default/strength/init', views.defaultStrengthInitView, name="default-strength-init"),

    path('default/strength/', views.defaultStrengthView, 
    name="default-strength"),

    path('default/strength/day1', views.DefaultStrengthDay1.as_view(), name="default-strength-day1"),

    path('default/strength/day2', views.DefaultStrengthDay2.as_view(), name="default-strength-day2"),

    path('default/strength/day3', views.DefaultStrengthDay3.as_view(), name="default-strength-day3"),

    path('default/strength/detail/<int:pk>/<str:slug>', views.DefaultStrengthDetail.as_view(),name="default-strength-detail"),

    # --------------------------------------------------------------------------

    # STRETCH
    path('default/stretch/init', views.defaultStretchInitView, name="default-stretch-init"),

    path('default/stretch/', views.defaultStretchView, 
    name="default-stretch"),

    path('default/stretch/day1', views.DefaultStretchDay1.as_view(), name="default-stretch-day1"),

    path('default/stretch/day2', views.DefaultStretchDay2.as_view(), name="default-stretch-day2"),

    path('default/stretch/day3', views.DefaultStretchDay3.as_view(), name="default-stretch-day3"),

    path('default/stretch/detail/<int:pk>/<str:slug>', views.DefaultStretchDetail.as_view(),name="default-stretch-detail"),

]
