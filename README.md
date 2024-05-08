pyExploitDb (https://gotham-security.com)
==

[![Build Status](https://travis-ci.com/GoVanguard/pyExploitDb.svg?branch=master)](https://travis-ci.com/GoVanguard/pyExploitDb)
[![Known Vulnerabilities](https://snyk.io/test/github/GoVanguard/pyExploitDb/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/GoVanguard/pyExploitDb?targetFile=requirements.txt)
[![Maintainability](https://api.codeclimate.com/v1/badges/c718eabcdd4b815698db/maintainability)](https://codeclimate.com/github/GoVanguard/pyExploitDb/maintainability)


## Authors:
Shane William Scott

## About pyExploitDb
An optimized Python3 library to fetch the most recent exploit-database, create searchable indexes for CVE->EDBID and EDBID -> CVE, and provide methods to perform searches.

## Upcoming features
> CPE database, indexes and mappings

## Installation
pip install pyExploitDb
> Note: This assumes pip is for your python3 environment. Use pip3 if pip is for your python2 environment.

## Example Usage
```python
from pyExploitDb import PyExploitDb
pEdb = PyExploitDb()
pEdb.debug = False
pEdb.openFile()
results = pEdb.searchCve("CVE-2018-14592")
print(results)
```

## Example debug/verbose output
CVE-2018-1459
Found
Exploit DB Id: 45447
File: ./exploit-database/exploits/php/webapps/45447.txt
Date: 2018-09-24
Author: Haboob Team
Platform: webapps
Type: php
Port: 80
{'edbid': '45447', 'exploit': './exploit-database/exploits/php/webapps/45447.txt', 'date': '2018-09-24', 'author': 'Haboob Team', 'platform': 'webapps', 'type': 'php', 'port': '80'}

## Credits
Originally based on fork of cve_searchsploit by Andrea Fioraldi.
