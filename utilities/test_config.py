import yaml


class TestConfig:

    @staticmethod
    def get_config(property_name: str):
        data = yaml.safe_load("test_config.yaml")
        if data.get(property_name):
            return data.get(property_name)
        raise RuntimeError("Incorrect Config")
