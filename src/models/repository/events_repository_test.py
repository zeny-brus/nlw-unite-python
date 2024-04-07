import pytest 
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em BD")
def test_insert_event():
    event = {
        "uuid": "meu-uuid-original",
        "title":"meu title",
        "slug":"meu-slug",
        "maximum_attendees":20
    }

    events_respository = EventsRepository()
    response = events_respository.insert_event(event)
    print(response)

@pytest.mark.skip(reason="Nao necessita")
def test_get_event_by_id():
    event_id = "meu-uuid-original12334"
    events_respository = EventsRepository()
    response = events_respository.get_event_by_id(event_id)
    print (response)
