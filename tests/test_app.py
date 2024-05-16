from playwright.sync_api import Page, expect

def test_user_can_log_in(db_connection, page, test_web_address):
    db_connection.seed("seeds/chitter.sql")
    page.goto(f"http://{test_web_address}/sign-in")
    page.fill("input[name=email]", "marklovejoy@gmail.com")
    page.fill("input[name=password]", "Test123")
    page.click("text='Log In'")
    div_element = page.locator("p.nav-text")
    expect(div_element).to_have_text("Welcome lovejoy01")
    
def test_user_can_create_account_and_log_in(db_connection, page, test_web_address):
    db_connection.seed("seeds/chitter.sql")
    page.goto(f"http://{test_web_address}/sign-in")
    page.click("text='Sign Up'")
    page.fill("input[name=name]", "another")
    page.fill("input[name=username]", "anothertest")
    page.fill("input[name=email]", "another@gmail.com")
    page.fill("input[name=password]", "Test123")
    page.click("text='Create'")
    page.fill("input[name=email]", "another@gmail.com")
    page.fill("input[name=password]", "Test123")
    page.click("text='Log In'")
    div_element = page.locator("p.nav-text")
    expect(div_element).to_have_text("Welcome anothertest")
    
    
def test_user_can_not_create_account_and_log_in_email_in_use(db_connection, page, test_web_address):
    db_connection.seed("seeds/chitter.sql")
    page.goto(f"http://{test_web_address}/sign-in")
    page.click("text='Sign Up'")
    page.fill("input[name=name]", "another")
    page.fill("input[name=username]", "anothertest")
    page.fill("input[name=email]", "marklovejoy@gmail.com")
    page.fill("input[name=password]", "Test123")
    page.click("text='Create'")
    error_message = page.locator("body")
    expect(error_message).to_have_text("Email is already in use")
    
    
def test_password_invalid(db_connection, page, test_web_address):
    db_connection.seed("seeds/chitter.sql")
    page.goto(f"http://{test_web_address}/sign-in")
    page.click("text='Sign Up'")
    page.fill("input[name=name]", "another")
    page.fill("input[name=username]", "anothertest")
    page.fill("input[name=email]", "lovejoy@gmail.com")
    page.fill("input[name=password]", "Test")
    page.click("text='Create'")
    error_message = page.locator("body")
    expect(error_message).to_have_text("Password must have at least 1 capital letter, 1 number, and be greater than 4 in length")
    
    
#test for create peep

#test for homepage no log in 

#test correct user logged in 