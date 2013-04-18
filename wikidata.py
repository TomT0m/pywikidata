# -*- coding: utf-8 -*-

from item import Item # So that wikidata.Item can be used.

from configReader import Config
from api import API

import errors
import xdg.BaseDirectory

import os

configfile_path = xdg.BaseDirectory.load_first_config("wp/config.py")

if (os.path.exists(configfile_path)):
	config = Config(configfile_path)
else:
	config = Config('config.py')


if not config["api"]:
	raise errors.ConfigurationError("An API url needs to be defined in config.py")

api = API(config)

