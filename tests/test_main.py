from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_memes():
    response = client.get("/memes")
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, dict)
    assert "memes" in response_json
    assert isinstance(response_json["memes"], list)


def test_create_meme():
    image_name = "1.png"
    meme_data = {
        'text': (None, 'meme1'),
        "image": open(f"tests/test_images/1.png", 'rb')
    }
    response = client.post("/memes", files=meme_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "id" in response_json
    assert response_json["image_url"].split(
        "/memes/")[1] == image_name



def test_get_meme_by_id():
    response = client.get("/memes/1")
    assert response.status_code == 200
    assert "id" in response.json()
    assert "text" in response.json()
    assert "image_url" in response.json()


def test_update_meme():
    image_name = "1.png"
    meme_update_data = {
        'text': (None, 'meme1'),
        "image": open(f"tests/test_images/{image_name}", 'rb')
    }

    response = client.put("/memes/1", files=meme_update_data)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["image_url"].split(
        "/memes/")[1] == image_name


def test_delete_meme():
    response = client.delete("/memes/1")
    assert response.status_code == 200
    response = client.get("/memes/1")
    assert response.status_code == 404
