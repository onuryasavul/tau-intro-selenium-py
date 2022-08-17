import pytest
import selenium.webdriver

@pytest.fixture
def browser():

    # ChromeDriver objesini oluşturma
    b = selenium.webdriver.Chrome()

    # Elementlerin ekranda belirmesi için 10sn bekleme
    b.implicitly_wait(10)

    # Setup için WebDriver objesini döndürme(return)
    yield b

    # Cleanup için WebDriver objesini sonşandırma
    b.quit()