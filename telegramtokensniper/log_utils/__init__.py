import logging
import os

file_dir = os.path.dirname(__file__)

#global logger, alternative approach: https://stackoverflow.com/questions/7621897/python-logging-module-globally
logging = logging

logging.basicConfig(filename=f"{file_dir}/tokensniper.log", format="[%(asctime)s] %(levelname)s: %(message)s",
                    datefmt='%d/%m/%Y %H:%M:%S', level=logging.INFO)
