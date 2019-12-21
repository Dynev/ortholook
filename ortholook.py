import os
import re
import sys
import xml
import copy
import gzip
import time
import shutil
import operator
import subprocess

import numpy
import pandas
import requests
from bs4 import BeautifulSoup as soup
from Bio.Blast.Applications import NcbitblastnCommandline as tblastn
from Bio.Blast.Applications import NcbimakeblastdbCommandline as makeblastdb

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from source import app
from source import load
from source import misc
from source import blast
from source import learn
from source import parse
from source import handle
from source import interpret

def main():
    pass

if __name__ == "__main__":
    main()
