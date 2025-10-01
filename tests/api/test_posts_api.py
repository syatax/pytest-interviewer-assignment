import time
import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

NEW_POST_DATA = {
    "title": "Test Post Title",
    "body": "This is a test post body content",
    "userId": 1
}


def verify_response_time(start_ts, max_ms):
    elapsed_ms = (time.time() - start_ts) * 1000
    assert elapsed_ms <= max_ms, f"Response time {elapsed_ms:.1f} ms > {max_ms} ms"


@pytest.mark.nondestructive
def test_comprehensive_posts_endpoint_validation():
    # 1. GET /posts
    start_time = time.time()
    resp = requests.get(f"{BASE_URL}/posts")
    assert resp.status_code == 200
    content_type = resp.headers.get("content-type", "")
    assert "application/json" in content_type

    verify_response_time(start_time, 3000)

    posts = resp.json()
    assert isinstance(posts, list)
    assert len(posts) > 0
    assert len(posts) == 100  # JSONPlaceholder возвращает 100 постов

    first_post = posts[0]
    for field in ("id", "title", "body", "userId"):
        assert field in first_post
    assert isinstance(first_post["id"], int)
    assert isinstance(first_post["title"], str)
    assert isinstance(first_post["body"], str)
    assert isinstance(first_post["userId"], int)

    # 2. GET /posts/1
    resp_single = requests.get(f"{BASE_URL}/posts/1")
    assert resp_single.status_code == 200
    single_post = resp_single.json()
    assert isinstance(single_post, dict)
    assert single_post["id"] == 1
    assert single_post["userId"] == 1
    assert "sunt aut facere" in single_post["title"]
    assert single_post["body"] != ""

    # 3. POST /posts
    resp_create = requests.post(f"{BASE_URL}/posts", json=NEW_POST_DATA)
    assert resp_create.status_code == 201
    content_type2 = resp_create.headers.get("content-type", "")
    assert "application/json" in content_type2
    created_post = resp_create.json()
    assert "id" in created_post
    assert created_post["title"] == NEW_POST_DATA["title"]
    assert created_post["body"] == NEW_POST_DATA["body"]
    assert created_post["userId"] == NEW_POST_DATA["userId"]
    # JSONPlaceholder присваивает ID 101
    assert created_post["id"] == 101

    # 4. Error scenario: несуществующий пост
    resp_err = requests.get(f"{BASE_URL}/posts/99999")
    assert resp_err.status_code == 404

    # malformed POST (JSONPlaceholder принимает любой формат)
    resp_invalid = requests.post(f"{BASE_URL}/posts", json={"invalid": "data"})
    assert resp_invalid.status_code == 201

    # Проверка "получения" созданного (симуляция)
    if "id" in created_post:
        resp_retrieved = requests.get(f"{BASE_URL}/posts/{created_post['id']}")
        assert resp_retrieved.status_code in (200, 404)

    # PUT /posts/1
    update_data = {**NEW_POST_DATA, "title": "Updated Title"}
    resp_update = requests.put(f"{BASE_URL}/posts/1", json=update_data)
    assert resp_update.status_code == 200
    updated_post = resp_update.json()
    assert updated_post["title"] == "Updated Title"
    assert updated_post["id"] == 1

    # DELETE /posts/1
    resp_delete = requests.delete(f"{BASE_URL}/posts/1")
    assert resp_delete.status_code == 200

    # Проверка структуры для нескольких объектов
    for post in (first_post, single_post, created_post):
        for required in ("id", "title", "body", "userId"):
            assert required in post, f"Post missing required field: {required}"