#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'themes/plumage'
# THEME = 'themes/blue-penguin'

AUTHOR = 'by-the-water'
SITENAME = 'By the water'
SITESUBTITLE = 'Geoscience, Oil & Gas, AI'
SITEURL = 'https://by-the-water.github.io'

GOOGLE_ANALYTICS = u'UA-99319293-1'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

AUTHOR_URL = 'pages/about.html'
#AUTHORS_SAVE_AS = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
         # ('Python.org', 'http://python.org/'),
         # ('Jinja2', 'http://jinja.pocoo.org/'),
         # ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
          # ('Another social link', '#'),)
		  
DEFAULT_PAGINATION = 8

# FAVICON = 'url-to-favicon'
                       
DISPLAY_PAGES_ON_MENU = True
#SUMMARY_MAX_LENGTH = None

# DISQUS_SITENAME = 'https-by-the-water-github-io'
DISQUS_SITENAME = "https-by-the-water-github-io"

# all the following settings are *optional*

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
# TAGS_URL           = 'tags'
# TAGS_SAVE_AS       = 'tags/index.html'
# AUTHORS_URL        = 'authors'
# AUTHORS_SAVE_AS    = 'authors/index.html'
# CATEGORIES_URL     = 'categories'
# CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
#    ('Tags', TAGS_URL, TAGS_SAVE_AS),
#    ('Authors', AUTHORS_URL, AUTHORS_SAVE_AS),
#    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)
# additional menu items
MENUITEMS = (
#    ('GitHub', 'https://github.com/'),
#    ('Linux Kernel', 'https://www.kernel.org/'),
	 ('Email Me','mailto:rossxsy@gmail.com'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# URLs
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

# Plugins
PLUGIN_PATHS = [u'plugins']
PLUGINS = [u'sitemap']
# Configuration for the "sitemap" plugin 
SITEMAP = { 
	'format': 'xml', 
	'priorities': { 
		'articles': 1, 
		'indexes': 0.5, 
		'pages': 0.5, 
		}, 
	'changefreqs': { 
		'articles': 'always', 
		'indexes': 'daily', 
		'pages': 'monthly' 
		} 
	}