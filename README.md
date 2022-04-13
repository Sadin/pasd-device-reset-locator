# possible reset devices
Find possible reset student devices using latest exports from Prime(wireless) and Endpoint(Intune).

### Setup
If running from source a little setup is required

Prereqs: `Python >= 3.7`, `git`


From powershell:
```
$ git clone https://github.com/Sadin/pasd-device-reset-locator.git

$ virtualenv venv

$ ./venv/scripts/activate

$ pip install -r requirements.txt
```

### Usage

#### Python
```
$ python app.py PrimeCSVPath IntuneCSVPath
```

#### Exe
