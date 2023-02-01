from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED

from resumes.models import Resume
from resumes.permissions import IsOwner
from resumes.serializers import ResumeSerializer


class ResumeListView(ListAPIView):
    """
    Представление отдает все резюме авторизованного пользователя.
    """
    model = Resume
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Resume.objects.filter(owner=self.request.user)


class ResumeRetrieveUpdateView(RetrieveUpdateAPIView):
    """
    Представление отображает резюме авторизованного пользователя по HTTP методу GET с передачей id,
    Вносит частичные изменения в резюме авторизованного пользователя по HTTP методу PATCH с передачей id.
    Работает только в случае, если резюме принадлежит пользователю.
    Для обновления доступен только HTTP метод PATCH. При использовании HTTP метода PUT будет выдана ошибка HTTP 405.
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated, IsOwner, ]

    def put(self, request, *args, **kwargs):
        return JsonResponse({'detail': 'Метод \"PUT\" не разрешен.'}, status=HTTP_405_METHOD_NOT_ALLOWED)
