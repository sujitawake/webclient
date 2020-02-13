# Python-based Webclient

This project is developed to have a tiny web-client handy to perform domain crawling in an automated fashion. The primary intention of this project is to generate baseline traffic by crawling Alexa's top 500 domains.

## Modules requirement
* requests
* eliot
* eliot-tree
* schedule
* colored

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

## View logs

```
$cat logs | eliot-tree
# OR
$eliot-tree logs
```

## Logs output

```bash
$eliot-tree logs # Output pasted below
```

```
42f305eb-39fe-409e-ae62-ff5dbe8b985b
└── domains_iterator/1 ⇒ started 2020-02-13 15:49:28 ⧖ 41.863s
    ├── root_domain/2/1 ⇒ started 2020-02-13 15:49:28 ⧖ 1.682s
    │   ├── source: http://youtube.com/
    │   ├── redirect_url/2/2/1 ⇒ started 2020-02-13 15:49:29 ⧖ 1.304s
    │   │   ├── target: http://youtube.com/
    │   │   └── redirect_url/2/2/2 ⇒ succeeded 2020-02-13 15:49:30
    │   └── root_domain/2/3 ⇒ succeeded 2020-02-13 15:49:30
    ├── root_domain/16/1 ⇒ started 2020-02-13 15:49:57 ⧖ 0.557s
    │   ├── source: http://en.wikipedia.org/
    │   ├── redirect_url/16/2/1 ⇒ started 2020-02-13 15:49:57 ⧖ 0.381s
    │   │   ├── target: http://en.wikipedia.org/
    │   │   └── redirect_url/16/2/2 ⇒ succeeded 2020-02-13 15:49:57
    │   └── root_domain/16/3 ⇒ succeeded 2020-02-13 15:49:57
    ├── root_domain/19/1 ⇒ started 2020-02-13 15:50:01 ⧖ 0.144s
    │   ├── source: http://bp.blogspot.com/
    │   └── root_domain/19/2 ⇒ failed 2020-02-13 15:50:01
    │       ├── errno: None
    │       ├── exception: requests.exceptions.ConnectionError
    │       └── reason: HTTPConnectionPool(host='bp.blogspot.com', port=80): Max retries exceeded with url: / (Caused by New…
    ├── root_domain/20/1 ⇒ started 2020-02-13 15:50:01 ⧖ 0.143s
    │   ├── source: http://googleusercontent.com/
    │   └── root_domain/20/2 ⇒ failed 2020-02-13 15:50:01
    │       ├── errno: None
    │       ├── exception: requests.exceptions.ConnectionError
    │       └── reason: HTTPConnectionPool(host='googleusercontent.com', port=80): Max retries exceeded with url: / (Caused …
    ├── root_domain/21/1 ⇒ started 2020-02-13 15:50:01 ⧖ 2.116s
    │   ├── source: http://maps.google.com/
    │   ├── redirect_url/21/2/1 ⇒ started 2020-02-13 15:50:02 ⧖ 1.380s
    │   │   ├── target: http://maps.google.com/
    │   │   └── redirect_url/21/2/2 ⇒ succeeded 2020-02-13 15:50:03
    │   └── root_domain/21/3 ⇒ succeeded 2020-02-13 15:50:03
    
```
