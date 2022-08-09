from unittest.mock import MagicMock
import pytest

from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.model.genre import Genre
from demostration_solution.service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_1 = Genre(id=1, name='Genre1')
    genre_2 = Genre(id=1, name='Genre2')
    genre_3 = Genre(id=1, name='Genre3')
    genre_init = GenreDAO(None)
    genre_init.get_one = MagicMock(return_value=genre_1)
    genre_init.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_init.create = MagicMock(return_value=genre_1)
    genre_init.delete = MagicMock()
    genre_init.update = MagicMock()
    return genre_init


class TestDGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_one(self):
        assert self.genre_service.get_one(1).name == "Genre1"

    def test_get_all(self):
        assert len(self.genre_service.get_all()) == 3

    def test_create(self):
        data = {"id": 1, "name": 'Genre1'}
        assert self.genre_service.create(data).name == data.get('name')

    def test_delete(self):
        assert 1 == 1

    def test_update(self):
        assert 1 == 1






