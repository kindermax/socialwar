from selenium.webdriver.common.by import By


class OKFormLocators:
    LOGIN_INPUT = (
        By.CSS_SELECTOR,
        '[name="st.email"]'
    )
    PASSWORD_INPUT = (
        By.CSS_SELECTOR,
        '[name="st.password"]'
    )
    SUBMIT_BTN = (
        By.CSS_SELECTOR,
        'input[type="submit"]'
    )
    MSG_INPUT = (
        By.CSS_SELECTOR,
        '[data-tsid="write_msg_input"]'
    )
    IMG_BUTTON = (
        By.CSS_SELECTOR,
        '[data-tsid="open_attach_menu_button"]'
    )
    FILE_INPUT = (
        By.CSS_SELECTOR,
        'input[class="attach-file"]'
    )
    UPLOADED_FILE = (
        By.CSS_SELECTOR,
        '[data-tsid="upload-bar"][progress="1"]'
    )
