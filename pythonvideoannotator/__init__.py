# !/usr/bin/python2
# -*- coding: utf-8 -*-

__version__ = "1.5"
__author__ = ["Ricardo Ribeiro", "Carlos Mao de Ferro", "Hugo Cachitas"]
__credits__ = ["Ricardo Ribeiro", "Carlos Mao de Ferro", "Hugo Cachitas"]
__license__ = "Attribution-NonCommercial-ShareAlike 4.0 International"
__maintainer__ = ["Ricardo Ribeiro", "Carlos Mao de Ferro"]
__email__ = ["ricardojvr at gmail.com", "cajomferro at gmail.com"]
__status__ = "Development"

from pysettings import conf;

conf += 'pythonvideoannotator.settings'

# load the user settings in case the file exists
try:
	import user_settings

	conf += user_settings
except:
	pass
