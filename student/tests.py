from django.test import TestCase, Client

from .models import Student


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='the_fire',
            sex=1,
            email='body@cc.com',
            profession='程序员',
            qq='123213',
            phone='12331231'
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='huyang',
            sex=1,
            email='afsdf@saf.com',
            profession='程序员',
            qq='21312',
            phone='12312312',
        )
        self.assertEqual(student.sex_show, '男', '性别展示一致')

    def test_filter(self):
        name = 'the_fire'
        student = Student.objects.filter(name=name)
        self.assertEqual(student.count(), 1, '只存在一个{}'.format(name))

    def test_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, '首页存在')

    def test_post_student(self):
        client = Client()
        data = {
            'name': 'test_for_post',
            'sex': 1,
            'email': 'afsdf@fasdf.com',
            'profession': '程序员',
            'qq': '1232',
            'phone': '12312',
        }
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'post-status_code 为302')

        response = client.get('/')
        self.assertTrue(b'test_for_post' in response.content, 'test_for_post in content')
