from app import app

  def test_hello():
      client = app.test_client()
      response = client.get('/')
      assert response.status_code == 200
      assert b"QuakeWatch: Welcome" in response.data

  def test_health():
      client = app.test_client()
      response = client.get('/health')
      assert response.status_code == 200
      assert response.data == b"OK"