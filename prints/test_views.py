from django.test import TestCase


class TestPrintViews(TestCase):

    # def test_get_all_prints_page(self):
    #     response = self.client.get('/prints/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'prints/all_prints.html')

    # def test_add_print_page(self):
    #     response = self.client.get('/prints/add-print/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'prints/add_print.html')

    def test_can_add_print(self):
        response = self.client.post('/prints/add-print/',
                                    {'title': 'Test added item'})
        self.assertRedirects(response, '/prints/')
