from playwright.sync_api import Page, expect

def test_user_can_log_in(db_connection, page, test_web_address):
    db_connection.seed("seeds/chitter.sql")
    page.goto(f"http://{test_web_address}/")
    page.fill("input[name=email]", "marklovejoy@gmail.com")
    page.fill("input[name=password]", "Test123")
    page.click("text='Log In'")
    div_element = page.locator("h1")
    expect(div_element).to_have_text("HOME")
    
def test_user_can_create_account_and_log_in(db_connection, page, test_web_address):
    db_connection.seed("seeds/chitter.sql")
    page.goto(f"http://{test_web_address}/")
    page.click("text='Sign Up'")
    page.fill("input[name=name]", "another")
    page.fill("input[name=username]", "anothertest")
    page.fill("input[name=email]", "another@gmail.com")
    page.fill("input[name=password]", "Test123")
    page.click("text='Create'")
    page.fill("input[name=email]", "another@gmail.com")
    page.fill("input[name=password]", "Test123")
    page.click("text='Log In'")
    div_element = page.locator("h1")
    expect(div_element).to_have_text("HOME")