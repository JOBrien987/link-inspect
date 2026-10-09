#!/usr/bin/env python3
"""Offline URL red-flag inspector; never visits URLs."""
import argparse
import ipaddress
from urllib.parse import urlsplit

def inspect(url):
    findings=[]
    try:
        parts=urlsplit(url)
        if parts.scheme.lower() not in ('http','https') or not parts.hostname:
            return ['Not a valid HTTP(S) URL.']
        hostname=parts.hostname
        if parts.scheme.lower()!='https': findings.append('Unencrypted HTTP connection.')
        if parts.username is not None or parts.password is not None: findings.append('URL contains userinfo before @; hostname may be misleading.')
        try:
            ipaddress.ip_address(hostname)
            findings.append('URL uses an IP address instead of a domain name.')
        except ValueError: pass
        if 'xn--' in hostname.lower(): findings.append('Hostname contains internationalized-domain punycode.')
        if len(url)>200: findings.append('Unusually long URL.')
        if parts.port is not None and parts.port not in (80,443): findings.append('Nonstandard network port.')
        return findings or ['No basic URL red flags detected. This does NOT mean the link is safe.']
    except ValueError:
        return ['Malformed URL.']

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Inspect a link without opening it')
    parser.add_argument('url')
    for finding in inspect(parser.parse_args().url):
        print('-',finding)
