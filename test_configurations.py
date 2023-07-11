import json
import pytest
import logging

def load_configurations():
    with open("configurations/config.json") as f:
        configurations = json.load(f)
        # loop dictionary and store in list of tuples
        list_tuples = []
        for config in configurations:
            tuple_config = (config["config_id"], config["version"], config["input_file"])
            list_tuples.append(tuple_config)

        return list_tuples




@pytest.mark.parametrize("config_id, version, input_file", load_configurations())
def test_configuration(config_id, version, input_file, caplog):
    # logging.info("Testing configuration: {}".format(config["config_id"]))
    # logging.debug("Testing configuration: {}".format(config["config_id"]))
    # config_id = config["config_id"]
    # version = config["version"]
    # input_file = config["input_file"]

    assert config_id == "config_1"