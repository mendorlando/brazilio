import unittest
from app import app


class CompilerTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def compile(self, source, octave=4):
        return self.client.post('/api/compile', json={'source': source, 'octave': octave})

    def test_teacher_melody(self):
        response = self.compile('Main { C4 D4 E4 C4 B3 A3 }')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual([n['midi'] for n in data['notes']], [60, 62, 64, 60, 59, 57])
        self.assertIn('(programa', data['tree'])
        self.assertEqual(data['compiler'], 'ANTLR4')

    def test_octave_accidentals_and_rest(self):
        data = self.compile('Main { C F# Bb R }', 5).get_json()
        self.assertEqual([n.get('midi') for n in data['notes']], [72, 78, 82, None])
        self.assertTrue(data['notes'][-1]['rest'])

    def test_errors(self):
        for source, stage in [('Main { H4 }', 'léxico'),
                              ('Main { C4', 'sintáctico'),
                              ('Main { C0 }', 'semántico'),
                              ('Main { C4 } C4', 'sintáctico')]:
            with self.subTest(source=source):
                response = self.compile(source)
                self.assertEqual(response.status_code, 422)
                self.assertIn(stage, [e['stage'] for e in response.get_json()['errors']])

    def test_invalid_requests(self):
        for payload in [None, [], {}, {'source': 'Main {}', 'octave': True},
                        {'source': 'Main {}', 'octave': 9}, {'source': 'x' * 16001}]:
            self.assertEqual(self.client.post('/api/compile', json=payload).status_code, 400)
        self.assertEqual(self.client.post('/api/compile', data='x' * 33000,
                                         content_type='application/json').status_code, 413)

    def test_public_routes(self):
        with self.client.get('/') as response:
            self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.get('/health').get_json()['compiler'], 'ANTLR4')
        self.assertEqual(self.client.get('/app.py').status_code, 404)


if __name__ == '__main__':
    unittest.main()
