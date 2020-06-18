from django.test import TestCase
from blog.models import CV

# Simple test to confirm that testing is working
class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/home.html')


# Test to make sure that cv page is reached when using address '<homepage>/cv'
class CVPageTest(TestCase):
    def test_uses_cv_template(self):
        response = self.client.get('/cv')
        self.assertTemplateUsed(response, 'blog/cv.html')


# Test that edit page is reached with corresponding url
class CVEditPageTest(TestCase):
    def test_uses_edit_cv_template(self):
        response = self.client.get('/cv/edit')
        self.assertTemplateUsed(response, 'blog/cv_edit.html')


# Test creating & editing CV.
class CVCreateTest(TestCase):
    def test_create_cv(self):
        CV.objects.create(header="Test header")

        response = self.client.get('/cv')

        self.assertIn("Test header", response.content.decode())

    def test_edit_cv(self):
        cv = CV()
        cv.header = 'Header text'
        cv.experience = 'none'
        cv.save()
        saved_items = CV.objects.all()
        self.assertEqual(saved_items.count(), 1)
        self.assertEqual('Header text', saved_items[0].header)
        cv.header = 'new text'
        cv.save()
        self.assertEqual('new text', saved_items[0].header)