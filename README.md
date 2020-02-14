# Python-based Webclient

This project is developed to have a tiny web-client handy to perform domain crawling in an automated fashion. The primary intention of this project is to generate baseline traffic by crawling Alexa's top 500 domains.

## Modules requirement
* requests
* eliot
* eliot-tree
* schedule

## Modules installation (automated)
```bash
$mkdir -p ~/tools && cd ~/tools
$git clone https://github.com/sujitawake/webclient.git
$cd webclient
$pipenv install request eliot eliot-tree schedule
```

## Usage
```sh
$cd ~/tools/webclient
$pipenv shell # You should be inside a virtualenv now
$chmod +x run.py
$python run.py
```

## Execution/Debug logs

This program generates ASCII logs during the program execution. This would aid to further debugging if any of the program execution goes wrong. Eliot module has been integrated to generate the log files on-the-fly. You need to follow the below steps to walkthrough the logs. This log file would give detailed information for the followings:

* When program execution had started and ended
* Details about each domain, consisting of:
  * Source domain address
  * Redirection domain address (whenever applicable)
  * Start/End time, took to crawl each URL
* Exceptions are handled and logged internally into the log file (logs)

## View execution logs

```
$cat logs | eliot-tree --local-timezone
# OR
$eliot-tree logs --local-timezone
```

## Logs screenshot

This is a glimpse of the output which you would see when you want to debug if any of the crawling event went wrong in case of errors.

![alt text](https://github.com/sujitawake/webclient/blob/master/screen.png "Debug logs screenshot")


**NOTE:**
<br>
Generated logs are overwritten each time when the program starts. So if you want to debug any previously generated errors, **don't forget to take backup** of the previously generated log file.
