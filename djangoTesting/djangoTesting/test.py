from django.test import TestCase

class HelloViewTest(TestCase):
    def test_hello_page(self):
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hello.html')

    def test_hello_page_message(self):
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hola a todos desde la app poster en 29 de diciembre')