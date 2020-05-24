# JiangYunDemo

A program that handles HTTP GET requests, takes in parameters in URL using Django, and then returns it in uppercase in JSON format. The project's code and the app itself are located inside of the src folder to make it organized

### Prerequisites

Django is used in a python virtual environment. Before running the program, make sure you have Django installed using pip and a virtual environment


### Running the program

Once you are done with the setup, run the following to start the virtual environment
```
source bin/activate
```
In order to run the server, type the following command to start running the server
```
python manage.py runserver 
```
Next open up your browser, copy and paste the response when the command above is typed

### RESTful API

We are using RESTful API here, by calling the response.GET(), we are able to get the parameter value inside our my_api views and then change them to upper case and return a JSON response format.

An example of such HTTP request is 

```
http://127.0.0.1:8000/api/?name=crystal&info=yes 
```

