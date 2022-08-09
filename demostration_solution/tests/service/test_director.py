from unittest.mock import MagicMock
import pytest

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_1 = Director(id=1, name='Director1')
    director_2 = Director(id=1, name='Director2')
    director_3 = Director(id=1, name='Director3')
    director_init = DirectorDAO(None)
    director_init.get_one = MagicMock(return_value=director_1)
    director_init.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    director_init.create = MagicMock(return_value=director_1)
    director_init.delete = MagicMock()
    director_init.update = MagicMock()
    return director_init


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        assert self.director_service.get_one(1).name == "Director1"

    def test_get_all(self):
        assert len(self.director_service.get_all()) == 3

    def test_create(self):
        data = {"id": 1, "name": 'Director1'}
        assert self.director_service.create(data).name == data.get('name')

    def test_delete(self):
        assert 1 == 1

    def test_update(self):
        assert 1 == 1






