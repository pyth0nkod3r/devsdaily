from django.test import TestCase, SimpleTestCase 
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        #print(str(response))
        self.assertEqual(response.status_code, 200)
    def test_view_url_by_name(self):
        response = self.client.get(reverse('pagesapphome'))
        #print(str(response))
        self.assertEqual(response.status_code, 200)
    def test_view_used_correct_template(self):
        response = self.client.get(reverse('pagesapphome'))
        self.assertTemplateUsed(response, 'newsapphome.html')
        
class SignUpViewTest(TestCase):
    username = 'testuser'
    email = 'test@email.com'
    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
     #   print(str(response))
        self.assertEqual(response.status_code, 200)
    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
       # print(str(response))
        self.assertEqual(response.status_code, 200)
    def test_view_used_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        #print(get_user_model().objects.all()[0].email == self.username)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)