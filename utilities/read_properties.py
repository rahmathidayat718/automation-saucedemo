import configparser

class ReadConfig:

    # READ URL  LOGIN FROM |    .\\data\\config.ini
    url_basic = configparser.ConfigParser()
    url_basic.read(".\\data\\config.ini")

    # READ DATA LOGIN FROM |    .\\data\\config.ini
    login_sauce_demo =configparser.ConfigParser()
    login_sauce_demo.read(".\\data\\config.ini")

    #GET_DATA
    @staticmethod
    def get_data_login():
        login_data = []
        for section in ReadConfig.login_sauce_demo.sections():
            if "login" in section.lower():  # section yang ada kata 'login'
                username = ReadConfig.login_sauce_demo.get(section, 'username', fallback=None)
                password = ReadConfig.login_sauce_demo.get(section, 'password', fallback=None)
                login_data.append((username, password, section))
        return login_data

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
    def get_after_logout_url():
        return ReadConfig.url_basic.get("LOGOUT", "after_logout_url")