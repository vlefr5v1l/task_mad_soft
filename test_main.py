from fastapi.testclient import TestClient
from app.src.main import app

client = TestClient(app)

def test_get_memes():
    response = client.get("/memes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_meme_by_id():

    response = client.get("/memes/1")
    assert response.status_code == 200
    assert "id" in response.json()
    assert "text" in response.json()
    assert "image_url" in response.json()

def test_create_meme():
    meme_data = {
        "text": "Test meme",
        "image_url": "https://24warez.ru/uploads/posts/2015-11/1447172520_3.gif"
    }
    response = client.post("/memes", json=meme_data)
    assert response.status_code == 201
    response_json = response.json()
    assert "id" in response_json
    assert response_json["text"] == meme_data["text"]
    assert response_json["image_url"] == meme_data["image_url"]

def test_update_meme():
    meme_update_data = {
        "text": "Updated meme text",
        "image_url": "https://abrakadabra.fun/uploads/posts/2021-12/1640224698_1-abrakadabra-fun-p-stikeri-marmoka-1.jpg"
    }
    response = client.put("/memes/1", json=meme_update_data)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["text"] == meme_update_data["text"]
    assert response_json["image_url"] == meme_update_data["image_url"]

def test_delete_meme():

    response = client.delete("/memes/1")
    assert response.status_code == 204

    response = client.get("/memes/1")
    assert response.status_code == 404
