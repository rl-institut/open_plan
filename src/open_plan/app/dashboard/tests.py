from django.test import TestCase
import uuid
from .models import Project, Simulation
from io import BytesIO
from django.urls import reverse


class SimulationServiceTest(TestCase):
    fixtures = ['benchmarks_fixture.json',]

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    # def test_results_assets_successfull_creation_after_file_processing(self):
        # project = Project.objects.get(pk=1)
        # associated_simulation = Simulation(request_id=f'{uuid.uuid4()}', project=project, status='RU')
        # associated_simulation.save()
        # with open('test_resources/results.xls', 'rb') as test_file:
        #     mock_file_handler = BytesIO(test_file.read())
        # mock_file_handler.name = "results.xls"
        # xls_to_dict = parse_xl_file(file=mock_file_handler)

        # assets_created = create_results_assets(xls_to_dict, associated_simulation)
        # self.assertTrue(assets_created)
    
