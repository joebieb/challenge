# Code Challenge

## Run dev server

Install packages with `npm install`

Run `ng serve` for a dev server ( you will need to run API project separately )

## Run projects together

Run `ng build` to build project.

Copy contents of dist/app to the `static` folder of the API

Run the API and it will serve the UI static files as well as the API

# Notes

Just a basic angular app with material ui components.

There are several `TODO:` comments of where I should add further functionality, otherwise it should be pretty straight forward.

The landing page will give you a link to a login page. 

The login page takes a string value of "email" type. Clicking the "Fake Login" button will send a request to the API to get an access token to use on subsequent requests. Upon successfully receiving a token, you will be presented with the quotation page. Entering valid values and clicking the "Get Quote" button will send a request to the API, passing the appropriate headers, including the token and a json body. A successful request should result in displaying a quote below the form. If there are any errors, they should be displayed below the form as well.


