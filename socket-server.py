#!/usr/bin/python3
import socket

import json

import re

import logging

from json2xml import json2xml, readfromstring, readfromjson

import requests

from requests.exceptions import HTTPError

#import xmltodict

#import ctypes #allow python to bind to port

#import asyncio

#import datetime # process time calculation

#ctypes.windll.shell32.IsUserAnAdmin()





#global variables



port = 15012

host = '' # convert this to localhost to outline outsiders

data_holder = '' # json data holder

tomconn_post_data = '' # final data holder, using this variable to resend final data

dest_url = 'http://192.168.1.6:8082' # desired final url

api_key = ''

logging.basicConfig(filename= 'latest-socket-server.log', filemode='a', format='%(asctime)s - %(process)d- %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logging.debug("Starting program...")









def socket_test():

    logging.debug("entering socket_test function")

    # OPEN SOCKET STREAM

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    # BIND SOCKET TO PORT AND HOST

    sock.bind((host,port))



    #SOCKET IS IN LISTENING MODE

    sock.listen()



    logging.debug(sock.getpeername)

    #print(sock.getpeername)



    while True:

        #SOCKET IS ACCEPTING DATA FROM INCOMING CONN

        conn,addr = sock.accept()

        print("connected by",addr)

        logging.debug("socket is accepting data")



        #CONVERT DATA from bytestream to string

        data=conn.recv(1024)

        data = data.decode("utf-8")

        logging.debug("data is deserialized to utf-8")

        print("received data:",data)



        #scrape data that fits the regex rule which is only json

        print ("\n regex step \n")

        only_json_data = regex_test(data)

        print(only_json_data)

        logging.debug("data is parsed to scrape only json data from post request")



        #after regexing, our data is converted to list, we need to convert it back to string to parse it again to xml

        print("\n list to string conversion step")

        only_json_data_str = list_to_string_after_regex(only_json_data)

        print(only_json_data_str)

        logging.debug("list is converted to str \n")



        # convert string json to pretty xml to work with it

        print("\n json to xml conversion step \n")

        final_data = readfromstring(only_json_data_str)

        final_data_xml = json2xml.Json2xml(final_data).to_xml()

        print(final_data_xml)



        #final data is assigned to variable

        tomconn_post_data = final_data_xml

        print("\n final data is converted to xml and assigned to global variable \n")



        print("\n TESTTTT !!! \n")

        print(tomconn_post_data,dest_url,api_key)

        api_caller(tomconn_post_data,dest_url,api_key)

        conn.close()





#conversion list to string after regex transformed our json to list

def list_to_string_after_regex(only_json_data):

    tmp_str = ''



    for tmp in only_json_data:

        tmp_str += tmp

        return tmp_str



# scape json data from html body as list

def regex_test(data):

    pattern = re.compile('\{.*\".*\:\{.*\:.*\}')

    json_data = re.findall(pattern,data)

    return json_data



# making post call to another server with parsed xml

def api_caller(tomconn_post_data,dest_url,api_key):

        try:
                req = requests.post(url = dest_url, data = tomconn_post_data)
                if req:
                        print("data is sent to desired location succesfully")
                        logging.debug("data is resend as xml to desired url")
        except HTTPError as he:
                print(f'HTTP error occured: {he}')
        except Exception as err:
                print(f'other type of error occured: {err}')


#RUNNING FUNCTIONS

socket_test()
