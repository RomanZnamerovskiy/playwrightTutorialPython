class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def navigate(self): # fixture is better suited for this task
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()