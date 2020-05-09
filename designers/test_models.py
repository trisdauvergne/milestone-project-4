# from django.test import TestCase

# from .models import Print


# class TestPrintModel(TestCase):

#     def test_title_is_required(self):
#         form = Print({'title': ''})
#         self.assertFalse(form.is_valid())
#         self.assertIn('title', form.errors.keys())
#         self.assertEqual(form.errors['title'][0], 'This field is required.')

#     def test_description_is_required(self):
#         form = Print({'description': ''})
#         self.assertFalse(form.is_valid())
#         self.assertIn('description', form.errors.keys())
#         self.assertEqual(form.errors['description'][0],
#                                      'This field is required.')
    
#     def test_size_is_required(self):
#         form = Print({'size': ''})
#         self.assertFalse(form.is_valid())
#         self.assertIn('size', form.errors.keys())
#         self.assertEqual(form.errors['size'][0], 'This field is required.')

#     def test_price_is_required(self):
#         form = Print({'price': ''})
#         self.assertFalse(form.is_valid())
#         self.assertIn('price', form.errors.keys())
#         self.assertEqual(form.errors['price'][0], 'This field is required.')
