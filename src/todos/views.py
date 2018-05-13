from rest_framework import permissions, viewsets

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Todo.objects
    serializer_class = TodoSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

    # def get_queryset(self):
    #     search = self.request.query_params.get('search', None)
    #     queryset = Todo.objects.filter(
    #         public_only=not self.request.user.is_staff, search=search)
    #     return queryset
