import json


class Config:
    def __init__(self):
        self.server_conf = json.load(open("econf.json", "r"))
        self.site_config = {}

    def load_siteconf(session):
        pass
