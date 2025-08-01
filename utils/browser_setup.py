from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Remove this line if you want UI
    return webdriver.Chrome(options=options)
