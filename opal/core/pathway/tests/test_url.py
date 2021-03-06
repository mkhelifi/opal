from opal.core.test import OpalTestCase
from django.core.urlresolvers import reverse


class PathwayReverseUrlTests(OpalTestCase):

    def test_reverse_pathway_url_with_numbers(self):
        self.assertEqual(
            '/pathway/templates/numerical10.html',
            reverse('pathway_template', kwargs={'name': 'numerical10'})
        )
