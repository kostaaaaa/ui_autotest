# Introduction
This repository contains test for https://copenhagencard.com/ using PyTest and Selenium.

# How to run tests
1. Install requirements in your virtual environment
```
pip install -r requirements.txt
```
2. Download Selenium Webdriver:\
Ubuntu
```
wget https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin
``` 
 &emsp;MacOS
```
wget https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_mac64.zip
unzip chromedriver_mac64.zip
sudo mv chromedriver /usr/local/bin
```
3. Run tests
```
pytest --tb=line -v
```

![Screenshot from 2022-11-10 18-04-15](https://user-images.githubusercontent.com/81771740/201160477-b879d25d-dbd6-48bf-8c93-2cd7303f76e6.png)
