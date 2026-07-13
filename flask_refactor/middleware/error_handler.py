import logging

from flask import request

from werkzeug.exceptions import ( BadRequest, NotFound, MethodNotAllowed )

from utils.response import error_response

logger = logging.getLogger(__name__) # Creates a logger specific to this Python module.

def register_error_handlers(app):

    @app.errorhandler(NotFound)
    def handle_not_found(error):
        logger.warning("404 Route Not Found | %s %s", request.method, request.path )
        return error_response( message="Route not found", status_code=404 )
    
    @app.errorhandler(MethodNotAllowed)
    def handle_method_not_allowed(error):
        logger.warning( "405 Method Not Allowed | %s %s", request.method, request.path )
        return error_response(message="Method not allowed", status_code=405)
    
    @app.errorhandler(BadRequest)
    def handle_bad_request(error):
        logger.warning( "400 Bad Request | %s %s", request.method, request.path )
        return error_response(message="Bad request", status_code=400)

    @app.errorhandler(Exception) # If an unhandled exception occurs anywhere in the application, this function will execute.
    def handle_exception(error): # Flask calls handle_exception(), not us.
        logger.exception( "500 Internal Server Error | %s %s", request.method, request.path )
        return error_response(message="Internal Server Error", status_code=500)

    '''
    app.error_handlers[Exception] = handle_exception # internal Flask mechanism to register error handlers. This line is not needed because the @app.errorhandler decorator already does this.
    '''

    '''
    It work just like this:
        @app.get("/users")
        def get_users():
            ...

    Here we are not calling get_users in route or controller but Flask will call it when a GET request is made to /users. Similarly, we are not calling handle_exception() anywhere in the code but Flask will call it when an unhandled exception occurs.
    '''

    '''
    Its just like this in Node.js:
    const express = require("express");
    const app = express();

    app.get("/users", async (req, res) => { 
        ...
    });
    # Here we are not calling this function (anonymous async arrow function) anywhere in the code but Express will call it when a GET request is made to /users.
    '''