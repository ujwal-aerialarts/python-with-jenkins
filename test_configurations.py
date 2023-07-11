import json
import pytest
import logging

def load_configurations():
    with open("configurations/config.json") as f:
        return json.load(f)

@pytest.mark.parametrize("config", load_configurations())
def test_configuration(config):
    logging.info("Testing configuration: {}".format(config["config_id"]))
    logging.debug("Testing configuration: {}".format(config["config_id"]))
    config_id = config["config_id"]
    version = config["version"]
    input_file = config["input_file"]

    assert config_id == "config_1"