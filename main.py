from dotenv import load_dotenv
import os
import discord
import pymongo
import datetime
import re
import urllib.request
import requests
from bs4 import BeautifulSoup
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import os
import asyncio
import re
import docx
from pymongo import MongoClient
import tweepy  
load_dotenv()
variable1 = os.getenv("MONGO_URL")


