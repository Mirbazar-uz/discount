from datetime import datetime
from typing import Dict


class PromotionValidator:
    def __init__(self):
        self.today = datetime.now().date()

    def validate(self, data: Dict) -> Dict:
        result = {**data}

        if result.get("deadline"):
            try:
                deadline = datetime.fromisoformat(result["deadline"]).date()
                result["is_active"] = deadline >= self.today

                if not result["is_active"]:
                    days_expired = (self.today - deadline).days
                    result["should_delete"] = days_expired > 30
                else:
                    result["should_delete"] = False

            except ValueError:
                result["deadline"] = None
                result["is_active"] = True
                result["should_delete"] = False
        else:
            result["is_active"] = True
            result["should_delete"] = False

        if result.get("old_price") and result.get("new_price"):
            if result["old_price"] > 0 and result["new_price"] > 0:
                discount = (
                    (result["old_price"] - result["new_price"])
                    / result["old_price"]
                ) * 100
                result["discount_percent"] = round(discount)

        if result.get("confidence", 0) < 0.5:
            result["low_confidence"] = True

        return result

    def get_status(self, data: Dict) -> str:
        if data.get("should_delete"):
            return "deleted"
        elif not data.get("is_active"):
            return "expired"
        return "active"
