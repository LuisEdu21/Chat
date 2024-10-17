import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_chat_response(client):
    response = client.post('/chat', json={'user': 'user_x', 'message': 'Preciso de ajuda'})
    assert response.status_code == 200
    assert 'Você não tem permissão' in response.get_json()['response']
