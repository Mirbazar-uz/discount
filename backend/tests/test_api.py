from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


class TestHealthEndpoint:
    def test_health_check(self):
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "timestamp" in data


class TestPromotionsEndpoint:
    def test_get_promotions(self):
        response = client.get("/promotions")
        assert response.status_code == 200
        data = response.json()
        assert "promotions" in data
        assert "total" in data

    def test_get_promotions_with_limit(self):
        response = client.get("/promotions?limit=5")
        assert response.status_code == 200
        data = response.json()
        assert data["limit"] == 5

    def test_get_promotions_with_category(self):
        response = client.get("/promotions?category=electronics")
        assert response.status_code == 200


class TestStoresEndpoint:
    def test_get_stores(self):
        response = client.get("/stores")
        assert response.status_code == 200
        assert isinstance(response.json(), list)


class TestStatsEndpoint:
    def test_get_stats(self):
        response = client.get("/stats")
        assert response.status_code == 200
        data = response.json()
        assert "total_promotions" in data
        assert "active_promotions" in data
        assert "total_stores" in data


class TestRatingEndpoint:
    def test_get_weekly_rating(self):
        response = client.get("/rating/weekly")
        assert response.status_code == 200
        data = response.json()
        assert "stores" in data
        assert data["period"] == "weekly"

    def test_get_monthly_rating(self):
        response = client.get("/rating/monthly")
        assert response.status_code == 200
        data = response.json()
        assert data["period"] == "monthly"
