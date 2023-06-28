from selenium.webdriver.common.by import By
class cartPage():
    addBackpack = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    cartBadge = (By.CLASS_NAME,"shopping_cart_badge")
    inventoryItem = (By.CLASS_NAME, "inventory_item_name")