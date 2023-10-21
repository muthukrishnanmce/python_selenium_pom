import os

import yaml


class TestConfig:

    @staticmethod
    def get_config(property_name: str):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        file_name = "test_config.yaml"
        complete_path = os.path.join(cur_dir, file_name)
        with open(complete_path, 'r') as file:
            data = yaml.safe_load(file)
        if data.get(property_name):
            return data.get(property_name)
        raise RuntimeError("Incorrect Config")
