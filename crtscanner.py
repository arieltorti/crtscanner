# -*- coding: utf-8 -*-
# @Author: Ariel Torti
# @Date:   2018-08-23 13:42:02
# @Last Modified by:   Ariel Torti
# @Last Modified time: 2018-08-23 13:57:40
# @GitHub: github.com/maks500
"""
Simple script to retrieve a subdomains from websites.

Retrieves the list of subdomains from a given domain by
looking at HTTPS Certificates Fingerprint on https://crt.sh
"""

import json
import argparse
import requests
import logging

__author__ = "Ariel Torti"

# Logger setup
logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

def parse_arguments(parser):
    """Parse arguments from the command line."""
    parser.add_argument("domain", type=str, nargs="*", help="Domain name")
    parser.add_argument("-d", "--domain", type=str, action="append",
        dest="domain_named", help="Domain name")
    parser.add_argument("-v", "--verbose", type=int, help="Logging level",
        dest="logging_level", default=1)
    return parser.parse_args()

def clean_url(url):
    """
    Remove unnecessary stuff from the url.

    TODO: TLD inspection for more complex urls.
    """
    return url.replace("www.", "").strip("/")

def main(domain_list):
    """
    Print the subdomains of each domain in `domain_list`.

    Keyword arguments:
    domain_list -- A list of domains to target.
    """
    crt_url = "https://crt.sh/?q=%.{}&output=json"
    for d in domain_list:
        subdomains = set()

        logger.debug("\n ------ SCANNING {} ------\n".format(d))

        res = requests.get(crt_url.format(clean_url(d)))

        if res.status_code != 200:
            logger.info("{}'s information is not available.".format(d))

        json_res = res.text.replace("}{", "},{").encode("utf8")
        data = json.loads("[{}]".format(json_res))

        for k in data:
            subdomains.add(k['name_value'])

        for index, s in enumerate(subdomains):
            print("[{}] - {}".format(index, s))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parse_arguments(parser)
    
    logger.setLevel(args.logging_level)

    # If no domains were passed exit.
    if not args.domain and not args.domain_named:
        parser.print_help()
        exit(1)

    if args.domain_named is not None:
        main(args.domain + args.domain_named)
    else:
        main(args.domain)
