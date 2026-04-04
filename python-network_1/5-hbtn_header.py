#!/usr/bin/python3
"""Module that fetches a URL and displays the X-Request-Id header value"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(
        sys.argv[1],
        headers={'cfclearance': 'true'}
    )
    print(response.headers.get('X-Request-Id'))
