# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
import logging
from my_pokemon_api import *
from db_accessor import *

logger = logging.getLogger('worker')

class Config:
    pass


# Create your views here.

def add_crawl_point(request):
    
    logger.info("I'm in add_crawl_point")
    #1 get ceil_id from request
    request_obj = json.loads(request.body)
    cell_id = request_obj["cell_id"]
    # call api
    config = Config() 
    config.auth_service = "ptc"
    config.username = "testuser"
    config.password = "testuser"
    config.proxy = "socks5://127.0.0.1:9050"
    api = init_api(config)
    search_response = search_point(cell_id, api)
    result = parse_pokemon(search_response)
    logger.info("Crawl result: {0}".format(json.dumps(result, indent=2)))
    for pokemon in result:
        add_pokemon_to_db(pokemon["encounter_id"],
                          pokemon["expiration_timestamp_ms"],
                          pokemon["pokemon_id"],    
                          pokemon["latitude"],
                          pokemon["longitude"])

    return HttpResponse("Result")
