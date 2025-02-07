from django.test import TestCase
from users.models import User
from services.models import Category, Service, ServiceAttachment


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        """Тест создания категории"""
        category = Category.objects.create(name="Test Category")
        self.assertEqual(category.name, "Test Category")

    def test_category_str_representation(self):
        """Тест строкового представления категории"""
        category = Category.objects.create(name="Test Category")
        self.assertEqual(str(category), "Test Category")


class ServiceAttachmentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(name='testuser', email='testuser@gmail.com', password='12345')

    def test_service_attachment_creation(self):
        """Тест создания вложения"""
        attachment = ServiceAttachment.objects.create(
            image='test_image.jpg',
            created_by=self.user
        )
        self.assertEqual(attachment.image.name, 'test_image.jpg')
        self.assertEqual(attachment.created_by, self.user)

    def test_get_image_method(self):
        """Тест метода get_image"""
        attachment = ServiceAttachment.objects.create(
            image='test_image.jpg',
            created_by=self.user
        )
        self.assertIn('http://127.0.0.1:8000', attachment.get_image())


class ServiceModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(name='testuser', email='testuser@gmail.com', password='12345')
        self.category = Category.objects.create(name="Test Category")
        self.attachment = ServiceAttachment.objects.create(
            image='test_image.jpg',
            created_by=self.user
        )

    def test_service_creation(self):
        """Тест создания услуги"""
        service = Service.objects.create(
            title="Test Service",
            price=100.0,
            descr="Test Description",
            isActive=True,
            category=self.category,
            created_by=self.user
        )
        service.photos.add(self.attachment)

        self.assertEqual(service.title, "Test Service")
        self.assertEqual(service.price, 100.0)
        self.assertEqual(service.descr, "Test Description")
        self.assertTrue(service.isActive)
        self.assertEqual(service.category, self.category)
        self.assertEqual(service.created_by, self.user)
        self.assertIn(self.attachment, service.photos.all())

    def test_service_str_representation(self):
        """Тест строкового представления услуги"""
        service = Service.objects.create(
            title="Test Service",
            price=100.0,
            descr="Test Description",
            isActive=True,
            created_by=self.user
        )
        self.assertEqual(str(service), "Test Service")
