import configparser

class ReadConfig:

    # READ URL  LOGIN FROM |    .\\data\\config.ini
    url_basic = configparser.ConfigParser()
    url_basic.read(".\\data\\config.ini")

    # READ DATA LOGIN FROM |    .\\data\\config.ini
    login_data =configparser.ConfigParser()
    login_data.read(".\\data\\config.ini")

    #GET_DATA
    @staticmethod
    def get_data_login():
        login_data = []
        for section in ReadConfig.login_data.sections():
            if "login" in section.lower():  # section yang ada kata 'login'
                username = ReadConfig.login_data.get(section, 'username', fallback=None)
                password = ReadConfig.login_data.get(section, 'password', fallback=None)
                login_data.append((username, password, section))
        return login_data

    @staticmethod
    def get_data_for_login():
        username = ReadConfig.login_data.get("DataLogin", "username")
        password = ReadConfig.login_data.get("DataLogin", "password")
        return username, password

    @staticmethod
    def get_login_url_page():
        return ReadConfig.url_basic.get("setting", "login_url_page")

    @staticmethod
    def get_after_login_url():
        return ReadConfig.url_basic.get("setting", "after_login_url")

    @staticmethod
    def get_logout_url_page():
        return ReadConfig.url_basic.get("LOGOUT", "logout_url_page")

    @staticmethod
    def get_about_url_page():
        return ReadConfig.url_basic.get("ABOUT", "about_url_page")

    @staticmethod
    def get_after_logout_url():
        return ReadConfig.url_basic.get("LOGOUT", "after_logout_url")

    #validation login
    @staticmethod
    def get_error_locked():
        return ReadConfig.login_data.get("LOGIN-locked_out_user", "error_locked")

    @staticmethod
    def get_error_fail_username():
        return ReadConfig.login_data.get("LOGIN-fail_username", "error_fail_username")

    @staticmethod
    def get_error_fail_password():
        return ReadConfig.login_data.get("LOGIN-fail_password", "error_fail_password")

    @staticmethod
    def get_error_username_empty():
        return ReadConfig.login_data.get("LOGIN-username_empty", "error_username_empty")

    @staticmethod
    def get_error_password_empty():
        return ReadConfig.login_data.get("LOGIN-password_empty", "error_password_empty")
