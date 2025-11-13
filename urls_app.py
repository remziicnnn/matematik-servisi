from django.urls import path
from views import (
    AddView, SubtractView, MultiplyView, DivideView,
    FactorialView, IsPrimeView, GcdView, LcmView,
    PowerView, MatrixMultiplyView
)

urlpatterns = [
    path('add/', AddView.as_view()),
    path('subtract/', SubtractView.as_view()),
    path('multiply/', MultiplyView.as_view()),
    path('divide/', DivideView.as_view()),
    path('factorial/', FactorialView.as_view()),
    path('is_prime/', IsPrimeView.as_view()),
    path('gcd/', GcdView.as_view()),
    path('lcm/', LcmView.as_view()),
    path('power/', PowerView.as_view()),
    path('matrix_multiply/', MatrixMultiplyView.as_view()),
]
