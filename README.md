# [![Build Status](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT25cWKvJzO6NPpJ7SU-FQy6SYetdL3_6mdqLWV45V0xH2U6HGu&s)](https://github.com/rupesh-biswas/WhatsApp_Web_Contacts)WhatsApp Web Contact List Fetcher

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/rupesh-biswas/WhatsApp_Web_Contacts)

WhatsApp Web Contact List Fetcher is selenium based webscraper which gives a list of people in your contact list using WhatsApp.

  - [Requirements](https://github.com/rupesh-biswas/WhatsApp_Web_Contacts#Requirements)
  - [How to run](https://github.com/rupesh-biswas/WhatsApp_Web_Contacts#How-to-run)

# Requirements
  - Python3 (https://www.python.org/downloads/)
  - Selenium python package (https://pypi.org/project/selenium/)
  - chromedriver (https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver)
  - Pandas python package (https://pypi.org/project/pandas/)

# How to run
  1. Open terminal window in the python filelocation.
  2. In the terminal window type the below line:
        - Windows: python bot.py
        - Others: python3 bot.py
  3. A csv named **peoples.csv** will be generated in the same direcory. 

**Note:**
> You will need to scan the initial WhatsApp Web QR code scanner.

**Cons:**
 1. Webdriver cannot be run on headless mode due to QR code scan step.
 2. Contacts having exactly the same name will be skipped.