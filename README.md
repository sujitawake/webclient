# Python-based Webclient

This project is developed to have a tiny web-client handy to perform domain crawling in an automated fashion. The primary intention of this project is to generate baseline traffic by crawling Alexa's top 500 domains.

## Modules requirement
* requests
* eliot
* eliot-tree
* schedule
* colored

## Usage
```sh
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

## View logs

```
$cat logs | eliot-tree
# OR
$eliot-tree logs
```
