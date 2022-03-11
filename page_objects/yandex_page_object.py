from selenium.webdriver.common.by import By


class CommentModalYandexPage:
    opinion_star = (
        By.CSS_SELECTOR,
        '[class="inline-image _loaded business-rating-edit-view__icon"] path'
    )
    auth_form = (
        By.CSS_SELECTOR,
        '[class="dialog"] [type="submit"]'
    )

    opinion_description = (
        By.TAG_NAME,
        'textarea'
    )
    file_input = (
        By.CSS_SELECTOR,
        'input[type="file"]'
    )
    uploading_file = (
        By.CSS_SELECTOR,
        'img[class="add-photos-view__photo"]'
    )
    send_btn = (
        By.CSS_SELECTOR,
        '[class="dialog"] [type="button"]'
    )


class LoginFormYandexPage:

    login_input = (
        By.ID,
        'passp-field-login'
    )
    enter_password_btn = (
        By.ID,
        'passp:sign-in'
    )
    password_input = (
        By.ID,
        'passp-field-passwd'
    )
    entrance_btn = (
        By.ID,
        'passp:sign-in'
    )
    skip_phone = (
        By.CSS_SELECTOR,
        '[data-t="phone_skip"]'
    )
