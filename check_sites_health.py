import os
import requests
import whois
from datetime import date, timedelta


DAYS_TO_EXPIRE = 30


def load_urls4check(path_file):
    if not os.path.exists(path_file):
        return None
    with open(path_file, 'r', encoding="utf-8") as file_handler:
        for line in file_handler.readlines():
            yield line


def is_server_respond_with_200(url):
    ok_status = 200
    if requests.get(url).status_code is ok_status:
        return True


def get_domain_expiration_date(domain_name):
    info_request = whois.query(domain_name)
    return info_request.expiration_date


def paid_at_least_a_month(expiration_date):
    expiration_prediction = date.today() + timedelta(days=DAYS_TO_EXPIRE)
    if expiration_date > expiration_prediction:
        return True


if __name__ == '__main__':
    pass