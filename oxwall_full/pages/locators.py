from selenium.webdriver.common.by import By


class CommonPageLocators:
    MESSAGE = (By.CLASS_NAME, "ow_message_node")


class SignInPageLocators:
    USERNAME_FIELD = (By.NAME, "identity")
    PASSWORD_FIELD = (By.NAME, "password")
    SIGN_IN_BUTTON = (By.NAME, 'submit')


class InternalPageLocators:
    # Right menu elements:
    SIGN_IN_MENU = (By.CSS_SELECTOR, ".ow_signin_label")
    SIGN_UP_MENU = (By.CLASS_NAME, 'ow_console_item_link')
    USER_BOARD = (By.CLASS_NAME, 'ow_notification_list')
    USER_MENU = (By.CSS_SELECTOR, '.ow_dropdown_menu_item.ow_cursor_pointer')
    SIGN_OUT = (By.XPATH, ".//a[contains(@href, 'sign-out')]")
    USER_ICON = (By.CSS_SELECTOR, ".ow_console_items_wrap > div:nth-child(5)")
    # Left menu elements:
    ACTIVE_MENU = (By.CSS_SELECTOR, ".ow_responsive_menu .ow_main_menu .active")
    MAIN_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_main_menu_index a")
    DASHBOARD_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_dashboard a")
    JOIN_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_base_join_menu_item a")
    MEMBERS_MENU = (By.CSS_SELECTOR, ".ow_site_panel .base_users_main_menu_item a")
    PHOTO_MENU = (By.CSS_SELECTOR, ".ow_site_panel .photo_photo a")
    VIDEO_MENU = (By.CSS_SELECTOR, ".ow_site_panel .video_video ")

    MESSAGE = (By.CLASS_NAME, "ow_message_node")

class DashboardPageLocators:
    TITLE = (By.CSS_SELECTOR, "h1.ow_stdmargin.ow_ic_house")
    POST_TEXT = (By.CSS_SELECTOR, ".ow_newsfeed_content")
    POST_LIST = (By.XPATH, '//*[contains(@id, "action-feed1-")]')

    STATUS_FIELD = (By.NAME, 'status')
    SAVE_BT = (By.NAME, 'save')

    COMMENTS_LIST = (By.CSS_SELECTOR, '.ow_comments_item.clearfix')
    COMMENTS_COUNTER = (By.CLASS_NAME, 'newsfeed_counter_comments')
    COMMENT_BT = (By.CSS_SELECTOR, '.ow_miniic_comment.newsfeed_comment_btn ')
    COMMENT_TEXT_FIELD = (By.XPATH, '//div[@class="ow_comments_input"]/textarea')

    POST_BLOCK = (By.CLASS_NAME, "ow_newsfeed_item")
    POST_CONTEX_MENU = (By.CLASS_NAME, "ow_newsfeed_context_menu_wrap")
    CONTEXT_MENU = (By.CSS_SELECTOR, '.ow_context_more')
    DELETE_BT = (By.XPATH, '//ul[@class="ow_context_action_list ow_border"]/li/a')


class PostBlockLocators:
    POST_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string > a")
    POST_TEXT = (By.CLASS_NAME, 'ow_newsfeed_content')
    POST_TIME = (By.CSS_SELECTOR, "a.create_time.ow_newsfeed_date")
    LIKE = (By.CLASS_NAME, "newsfeed_like_btn")
    LIKE_COUNTER = (By.CLASS_NAME, "newsfeed_counter_likes")

