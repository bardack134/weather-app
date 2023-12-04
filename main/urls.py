

from django.urls import path


from . import views




app_name='Main'
# Define las URL de tu aplicación

urlpatterns = [
    # path('', Registrar.as_view(), name='registrar'),

    # # pasamos el id del objeto que queremos aeliminar como un str en nuestra url
    # path('Delete/<str:item_id>', views.Delete, name='Delete'),
    path('', views.index, name='index'),
  

]