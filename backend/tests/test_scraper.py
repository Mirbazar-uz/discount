from src.scraper.telegram_scraper import TelegramScraper
from src.scraper.parser import extract_image_url, clean_price_text, extract_percentage


class TestTelegramScraper:
    def test_is_promotion_post_with_keyword(self):
        scraper = TelegramScraper()
        assert scraper.is_promotion_post("Katta chegirma! 50% off") is True
        scraper.close()

    def test_is_promotion_post_without_keyword(self):
        scraper = TelegramScraper()
        assert scraper.is_promotion_post("Bugungi ob-havo yaxshi") is False
        scraper.close()

    def test_is_promotion_post_russian(self):
        scraper = TelegramScraper()
        assert scraper.is_promotion_post("Большая скидка на товары!") is True
        scraper.close()

    def test_is_promotion_post_cashback(self):
        scraper = TelegramScraper()
        assert scraper.is_promotion_post("10% cashback olasiz") is True
        scraper.close()


class TestParser:
    def test_extract_image_url(self):
        style = "background-image: url('https://example.com/image.jpg')"
        assert extract_image_url(style) == "https://example.com/image.jpg"

    def test_extract_image_url_no_match(self):
        assert extract_image_url("no image here") is None

    def test_clean_price_text(self):
        assert clean_price_text("18 500 000 so'm") == 18500000

    def test_clean_price_text_empty(self):
        assert clean_price_text("no price") is None

    def test_extract_percentage(self):
        assert extract_percentage("Chegirma 50%") == 50

    def test_extract_percentage_no_match(self):
        assert extract_percentage("no percent") is None
