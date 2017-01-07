import os
import requests
import whois
import argparse
from datetime import datetime, timedelta


DAYS_TO_EXPIRE = 30


def load_urls4check(path_file):
    if not os.path.exists(path_file):
        return None
    with open(path_file, 'r', encoding="utf-8") as file_handler:
        url_units = file_handler.read().split()
        return url_units


def is_server_respond_with_200(url):
    ok_status = 200
    return requests.get(url).status_code == ok_status


def get_domain_expiration_date(domain_name):
    info_request = whois.whois(domain_name)  # can be a list of datetimes
    return info_request.expiration_date


def input_wrapper():
    parser = argparse.ArgumentParser(description='Checking availability of urls list')
    parser.add_argument('file', default='urls.txt', type=str, help='file with urls')
    return parser.parse_args().file


def paid_at_least_a_month(expiration_date):
    expiration_prediction = datetime.today() + timedelta(days=DAYS_TO_EXPIRE)
    if type(expiration_date) is list:
        for possible_unit in expiration_date:
            return possible_unit > expiration_prediction
    else:
        return expiration_date > expiration_prediction


def complex_check(url_):
    if is_server_respond_with_200(url_):
        print("{} has status OK and ... ".format(url_))
    else:
        print("Something wrong with {} and ...".format(url_))

    if paid_at_least_a_month(get_domain_expiration_date(url_)):
        print('domain name paid at least a month forward . \n ')
    else:
        print("domain name expires less then a month! \n ")


if __name__ == '__main__':
    list_to_check = load_urls4check(input_wrapper())
    if list_to_check:
        for item in list_to_check:
            complex_check(item)
    else:
        print('None of urls in specified file!')
