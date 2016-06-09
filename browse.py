#!/usr/bin/env python

import sys
import webbrowser
import argparse

def browser(url):
    webbrowser.get("firefox").open_new(url)

def main():
    try:
        parser = argparse.ArgumentParser("Python Browser Launcher")
        parser.add_argument("-u", "--url", type=str, help = "URL to connect to")
        args = parser.parse_args()
        
        url = "http://"
        link = url + args.url
        browser(link)
    except Exception, e:
    	print " \n[*] An Error Occured, Exiting Program...\n"
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
