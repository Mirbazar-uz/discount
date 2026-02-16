from src.ai.validator import PromotionValidator


class TestPromotionValidator:
    def test_validate_active_promotion(self):
        validator = PromotionValidator()
        data = {
            "title": "Test Product",
            "old_price": 1000000,
            "new_price": 500000,
            "deadline": "2099-12-31",
            "confidence": 0.9,
        }
        result = validator.validate(data)

        assert result["is_active"] is True
        assert result["should_delete"] is False
        assert result["discount_percent"] == 50

    def test_validate_expired_promotion(self):
        validator = PromotionValidator()
        data = {
            "title": "Old Product",
            "old_price": 1000000,
            "new_price": 800000,
            "deadline": "2020-01-01",
            "confidence": 0.8,
        }
        result = validator.validate(data)

        assert result["is_active"] is False
        assert result["should_delete"] is True

    def test_validate_no_deadline(self):
        validator = PromotionValidator()
        data = {
            "title": "No Deadline Product",
            "old_price": 500000,
            "new_price": 400000,
            "confidence": 0.7,
        }
        result = validator.validate(data)

        assert result["is_active"] is True
        assert result["should_delete"] is False

    def test_validate_low_confidence(self):
        validator = PromotionValidator()
        data = {
            "title": "Low Confidence",
            "confidence": 0.3,
        }
        result = validator.validate(data)

        assert result.get("low_confidence") is True

    def test_validate_invalid_deadline(self):
        validator = PromotionValidator()
        data = {
            "title": "Invalid Date",
            "deadline": "not-a-date",
            "confidence": 0.9,
        }
        result = validator.validate(data)

        assert result["deadline"] is None
        assert result["is_active"] is True

    def test_get_status_active(self):
        validator = PromotionValidator()
        assert validator.get_status({"is_active": True}) == "active"

    def test_get_status_expired(self):
        validator = PromotionValidator()
        assert validator.get_status({"is_active": False}) == "expired"

    def test_get_status_deleted(self):
        validator = PromotionValidator()
        assert validator.get_status({"should_delete": True}) == "deleted"
