import unittest
import wsgi

class TestHello(unittest.TestCase):

    def setUp(self):
        wsgi.application.testing = True
        self.application = wsgi.application.test_client()

    def test_hello(self):
        rv = self.application.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!')

    def test_hello_rh(self):
        rv = self.application.get('/rh') 
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Red Hat loves linux')

    def test_hello_bo(self):
        rv = self.application.get('/bo')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Thanks Boeing for allowing us to work with you!!')

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner( output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
