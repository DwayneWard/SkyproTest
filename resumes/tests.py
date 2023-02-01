from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from resumes.models import Resume
from resumes.serializers import ResumeSerializer


class ResumeTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(username='testuser', password='testpassword')
        self.another_user = User.objects.create(username='testuser2', password='testpassword')

        Resume.objects.create(experience='testexperience', portfolio='https://github.com/', title='testitle',
                              phone='+79999999999', email='testemail', owner_id=self.user.id)
        Resume.objects.create(experience='testexperience2', portfolio='https://github.com/', title='testitle2',
                              phone='+79999999999', email='testemail2', owner_id=self.another_user.id)
        Resume.objects.create(experience='testexperience3', portfolio='https://github.com/', title='testitle3',
                              phone='+79999999999', email='testemail3', owner_id=self.user.id)

    def test_get_user_resumes_no_authentication(self):
        response = self.client.get('/resume/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {"detail": "Учетные данные не были предоставлены."})

    def test_get_user_resume_by_number_no_authentication(self):
        response = self.client.get('/resume/2/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {"detail": "Учетные данные не были предоставлены."})

    def test_update_resumes_no_authentication(self):
        response = self.client.patch('/resume/2/', data={"education": "higher"})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {"detail": "Учетные данные не были предоставлены."})

    def test_get_user_resumes_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/resume/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(Resume.objects.filter(owner=self.user)))

    def test_get_user_resume_by_number(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/resume/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['experience'], Resume.objects.get(id=1).experience)

    def test_get_user_resume_by_number_not_owning(self):
        self.client.force_authenticate(user=self.another_user)
        response = self.client.get('/resume/1/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {"detail": "У вас недостаточно прав для выполнения данного действия."})

    def test_update_user_resume(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch('/resume/1/', data={"education": "higher", "phone": "+79999999898"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        resume = Resume.objects.get(id=1)
        serializer = ResumeSerializer(resume)
        self.assertEqual(response.data, serializer.data)

    def test_update_resumes_not_owning(self):
        self.client.force_authenticate(user=self.another_user)
        # Заранее вытаскиваем из базы не отредактированное резюме, чтобы проверить, что редактирование не прошло успешно
        not_edited_resume = ResumeSerializer(Resume.objects.get(id=1)).data

        response = self.client.patch('/resume/1/', data={"education": "higher", "phone": "+79999999898"})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {"detail": "У вас недостаточно прав для выполнения данного действия."})
        # Прверка на то, что изменения не записались в базу
        resume = Resume.objects.get(id=1)
        serializer = ResumeSerializer(resume)
        self.assertEqual(not_edited_resume, serializer.data)

    def test_put_hhtp_method_not_allowed(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put('/resume/1/', data={"education": "higher", "phone": "+79999999898"})

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
