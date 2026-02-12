from selenium.webdriver.common.by import By

class Locators:

    # Basic Auth Locators
    username_id = (By.ID, "user-name")
    password_id = (By.ID, "password")
    btn_login_id = (By.ID, "login-button")
    #validasi error xpath
    username_empty_xpath = (By.XPATH, "//h3[normalize-space()='Epic sadface: Username is required']")
    password_empty_xpath = (By.XPATH, "//h3[normalize-space()='Epic sadface: Password is required']")
    locked_xpath = (By.XPATH, "//h3[@data-test='error']")
    fail_username_xpath = (By.XPATH, "//h3[@data-test='error']")
    fail_password_xpath = (By.XPATH, "//h3[@data-test='error']")

    # Logout Locators
    open_menu_xpath = (By.XPATH, "//button[normalize-space()='Open Menu']")
    btn_logout_xpath = (By.XPATH, "//a[@id='logout_sidebar_link']")

    #Fiter Products
    btn_filter = (By.XPATH, "//select[@class='product_sort_container']")
    click_Name_A_Z = (By.XPATH, "//select[@class='product_sort_container']/option[@value='az']")
    click_Name_Z_A = (By.XPATH, "//select[@class='product_sort_container']/option[@value='za']")
    click_Price_Low_High = (By.XPATH, "//select[@class='product_sort_container']/option[@value='lohi']")
    click_Price_High_Low = (By.XPATH, "//select[@class='product_sort_container']/option[@value='hilo']")

    #About
    btn_about_xpath = (By.XPATH, "//a[@id='about_sidebar_link']")

    #Chart
    icon_chart = (By.XPATH, "(//*[name()='path'][@fill='currentColor'])[1]")
    product1 = (By.XPATH, "//div[@class='inventory_list']//div[1]//div[3]//button[1]")
    product2 = (By.XPATH, "//body//div[@id='page_wrapper']//div[@id='inventory_container']//div[@id='inventory_container']//div[2]//div[3]//button[1]")
    product3 = (By.XPATH, "//div[3]//div[3]//button[1]")
    product4 = (By.XPATH, "//div[5]//div[3]//button[1]")

