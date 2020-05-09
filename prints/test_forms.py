from django.test import TestCase

from .forms import UploadPic


class TestUploadPic(TestCase):

    def test_title_is_required(self):
        form = UploadPic({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_description_is_required(self):
        form = UploadPic({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0],
                                     'This field is required.')

    def test_size_is_required(self):
        form = UploadPic({'size': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('size', form.errors.keys())
        self.assertEqual(form.errors['size'][0], 'This field is required.')

    def test_price_is_required(self):
        form = UploadPic({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = UploadPic()
        self.assertEqual(form.Meta.fields, ['designer',
                                            'title',
                                            'description',
                                            'size',
                                            'price',
                                            'image'])
