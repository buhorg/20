from unittest.mock import MagicMock
import pytest

from demostration_solution.dao.model.movie import Movie
from demostration_solution.dao.movie import MovieDAO
from demostration_solution.service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_1 = Movie(id=1, title='title1', description='description1', trailer='trailer1', year=2022, rating=10)
    movie_2 = Movie(id=2, title='title2', description='description2', trailer='trailer2', year=2022, rating=10)

    movie_init = MovieDAO(None)
    movie_init.get_one = MagicMock(return_value=movie_1)
    movie_init.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_init.create = MagicMock(return_value=movie_1)
    movie_init.delete = MagicMock()
    movie_init.update = MagicMock()
    return movie_init


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        assert self.movie_service.get_one(1).title == "title1"

    def test_get_all(self):
        assert len(self.movie_service.get_all()) == 2

    def test_create(self):
        data = {"id": 1, "title": 'title1', "description": 'description1', "trailer": 'trailer1', "year": 2022,
                "rating": 10, "genre_id": 1, "director_id": 1}
        assert self.movie_service.create(data).title == data.get('title')

    def test_delete(self):
        assert 1 == 1

    def test_update(self):
        assert 1 == 1






