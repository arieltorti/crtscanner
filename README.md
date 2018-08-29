### Crtscanner - HTTPS Subdomain Scanner

Retrieves the list of subdomains from a given domain by
looking at HTTPS Certificates Fingerprint on https://crt.sh 

## Installation
```
$ git clone https://github.com/maks500/crtscanner
$ cd crtscanner
$ pip install -r requirements.txt
```

## Usage
```
$ cd crtscanner
$ python crtscanner.py [-h] [-d DOMAIN_NAMED] [-v LOGGING_LEVEL]
                     [domain [domain ...]]
```

## License
MIT
