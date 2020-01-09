import requests
import configparser


class Update:
    """update a work in Scholar@UC"""

    def __init__(self, attributes):
        parser = configparser.ConfigParser()
        parser.read("config.ini")
        self.headers = {
         "api-key": parser.get("api", "api-key")
        }
        self.root = parser.get("api", "root")
        self.work_type = attributes.pop("work_type")
        self.id = attributes.pop("id")
        self.attributes = attributes

    def update(self):
        r = requests.patch(
            f"{self.root}/api/concern/{self.work_type}/{self.id}",
            headers=self.headers,
            data=self.attributes
        )
        return r
