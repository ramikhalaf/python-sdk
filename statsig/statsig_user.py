import json

class StatsigUser:
    def __init__(self, user_id):
        self.user_id = user_id
        self.email = None
        self.ip = None
        self.user_agent = None
        self.country = None
        self.locale = None
        self.app_version = None
        self.custom = None
        self.private_attributes = None
        self._statsig_environment = None

    def to_dict(self, forEvaluation = False):
        user_nullable = {
            'userID': self.user_id,
            'email': self.email,
            'ip': self.ip,
            'userAgent': self.user_agent,
            'country': self.country,
            'locale': self.locale,
            'appVersion': self.app_version,
            'custom': self.custom,
            'statsigEnvironment': self._statsig_environment,
        }

        if forEvaluation and self.private_attributes is not None:
            user_nullable["privateAttributes"] = self.private_attributes
        
        return {k: v for k, v in user_nullable.items() if v is not None}
