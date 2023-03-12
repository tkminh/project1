from . import client

def test_home_page(client):
    '''Test'''
    response = client.get('/')
    html = response.data.decode('utf-8')
    assert response.status_code == 200
    assert 'F.A.B' in html



