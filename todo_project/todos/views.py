from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Todo
from .serializers import TodoSerializer
# Create your views here.

class TodoList(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
