from django.urls import path
from . import views
from django.urls import include





urlpatterns = [
    
   
#6.1 GET POST from rest framework class based view generics
    path('genericsmsgstype/', views.generics_list.as_view()),
    path('ge/', views.ge.as_view()),
    #6.2 GET PUT DELETE from rest framework class based view generics
    path('genericsmsgstypes/<int:pk>', views.generics_pk_msgstypes.as_view()),
    path('genericsmsgs/<int:pk>', views.pk_msgs.as_view()),
    #2
    path('msgtypes_api/', views.msgtypes_api),
    path('msgsapi/<int:id>' , views.msgsapi),

    ####################

    

    
]