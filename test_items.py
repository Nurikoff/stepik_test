from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_cart_add_button_exists(browser):
    browser.get(link)
    try:
        browser.find_element_by_class_name("btn-add-to-basket")
        exists = True
    except NoSuchElementException:
        exists = False
    assert exists == True ,  "No element found"
