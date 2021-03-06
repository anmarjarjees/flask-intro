# Flask Introduction

#### Dear Students,
This Folder is about Flask Introduction Tutorial.
We will create our first website using Python/Flask Framework + Bootstrap Framework

Regards,
Instructor: Anmar Jarjees

---
To read the full info about working with Flask using VS Code:
https://code.visualstudio.com/docs/python/tutorial-flask

To Start a new project (for the first time):
Make sure to have a folder for this project: "Flask-Intro"
Inside the project folder, create the venv:

You can check the full article:
https://flask.palletsprojects.com/en/2.0.x/installation/

Step1: Create the virtual Env.
(Windows-Powershell-GitBash)=>> py -m venv intro-venv  
(Mac-Terminal or GitBash)==>> python3 -m venv intro-venv
NOTE: 
- python3 (Windows-GitBash) ==> python3: Permission denied

[intro-venv] could be any name you prefer

We need to activate the venv when reopen our application 
(after the activate it. it appears in the command line)


step2: Activate the venv:
- On Windows, run:
(Powershell/Git Bash)=>> intro-venv\Scripts\Activate.ps1
Or: 
just: intro-venv\Scripts\Activate OR intro-venv\scripts\activate
(CMD-command line prompt)==>> intro-venv\Scripts\activate.bat
- On Unix or MacOS, run: source tutorial-env/bin/activate

NOTE: To deactivate the current venv =>> deactivate

Step3: Install the required package "Flask" (inside our venv) 
Run of of the following commands to download and install flask locally:
For the first time =>> pip install flask 
OR for any user after getting our code: =>> pip install -r requirements.txt

Very Important Note:
- After installing all the required packages (pip install package_name)
- We can move/write all installed package into a text file named "requirements.txt"
=>> pip freeze > requirements.txt
- This file "requirements.txt" is used:
-- in your GitHub Repo, so people can see the package(s) that we used 
-- Any one can run this command to install all the packages: pip install -r requirements.txt
-- to deploy your application to Heroku website (it's required)

By the way:
- you can check all the installed package(s) by using any of these two commands:
- =>> pip list
- =>> pip freeze
[or in terminal: py -m pip freeze]

The result:
click==8.0.0
Flask==2.0.0
itsdangerous==2.0.0
Jinja2==3.0.0
MarkupSafe==2.0.0
Werkzeug==2.0.0

=== We finished installing the package and activating the venv ===
=== We will start building our application (app) ===

Step4: create a new python file to be the main file (the major one) 
to run our application, although this Py file could be any name, 
but by default we should name it "app" (it's better and much easier, you will see why)
This file has to be inside the main project folder-  then jump to app.py :-)

Step5: After finishing our initial (required) code in app.py
you can run flask application:
we can test our app on PowerShell:
we can type =>> py -m flask run
OR =>> flask run


The following result should appear inside the terminal window:
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Two things to consider:
- Environment: production == we need to make it ==> Environment: development
- Debug mode: off == we need to make it ==> Debug mode: on

For now every time we need to test/run our web application after any change, we have to do:
1- CTRL + C to break the running our flask application
2- Then agin write: py -m flask run or flask run

Notice that "app.py" is the name of our main python file to launch the application 

Yes, We don't want to always press CTRL+C to stop the flask 
then py -m flask run to run the flask!!!!!!! We will learn another practical way :-)

Flask Help:
Flask Docs: Development Server Command Line:
The link: https://flask.palletsprojects.com/en/2.0.x/server/

Command Line
The flask command line script (Command Line Interface) is strongly recommended for development 
because it provides a superior reload experience due to how it loads the application. 
The basic usage is like this:

$ export FLASK_APP=my_application
$ export FLASK_ENV=development
$ flask run

NOTE: my_application will be the name of your main python file to start your flask website.

export: 
Set an environment variable. 
The supplied names are marked for automatic export to the environment of subsequently executed commands.

Now be carful that these instructions for linux environment (unix shell) 
or if you want to use bash shell commands 
But in our windows OS => VS Code (or other editor) PowerShell 
we have to change the command "export" with "set"

Step5 (more advanced options):
Below, replace "hello"  with your app name which is in our case is "app"

### For Linux and Mac (Bash):
$ export FLASK_APP=hello
$ export FLASK_ENV=development
$ flask run

### For Windows CMD, use set instead of export:
> set FLASK_APP=hello
> set FLASK_ENV=development
> flask run

### For Windows PowerShell (More official for windows users), use $env: instead of export:
> $env:FLASK_APP = "hello"
> $env:FLASK_ENV = "development"
> flask run

In our current application, we can:
*> $env:FLASK_APP = "app"
> $env:FLASK_ENV = "development"
> flask run

* If your main python file to run your flask application named "app"
you can skip this statement (command) = optional

#### NOTES:
1)- The steps above will run our application/code with [Debug mode: on]
2)- Instead of copy and paste the above lines three times, we can write them all in one line with ;
Windows => $env:FLASK_APP = "app"; $env:FLASK_ENV = "development"; flask run 
Mac => export FLASK_APP=app; export FLASK_ENV=development; flask run
3)- If our main application is named "app" which is the default name that is used by Flask Framework,
in such case we can just run these two commands: $env:FLASK_ENV = "development"; flask run 


Step6 (When you close your application and reopen it again):
After closing (quitting) the application, then if you open the project again (in VS Code) and runt it:
- You can just open the main file "app.py" and VSC should activate the venv automatically
(Make sure  your venv is activate before running your file)
just repeat the same the commands =>> step5 (advanced):
- flask run => this will run the application with Debug mode: off 
  => we have to CTRL+C and run it again for any change we make
- $env:FLASK_ENV = "development"; flask run  => this will run the application with Debug mode: on
  => we can just need refresh the browser for any change we make

Notice that this command "flask run" will NOT work if you are using a different name other than "app"
- You have to run first: $env:FLASK_APP = "your_app_name"
- also it's strongly recommended to run $env:FLASK_ENV = "development" then py -m flask run
- in order to have the "lazy mode" on and debug mode also on

#### The End

## Below are more notes, info, and review/summary:
Use the following steps from a terminal (Based on MS VS Code Docs):
1. set an environment variable for FLASK_APP.
On Linux and macOS, use export set FLASK_APP=webapp; on Windows use set FLASK_APP=webapp.
2. Navigate into the hello_app folder, 
then launch the program using python3 -m flask run (Linux/macOS) or python -m flask run (Windows).

## Notice that you will need to change python with py 
Tip: If you want to use a different filename than app.py, such as program.py,
define an environment variable named FLASK_APP and set its value to your chosen file.
Flask's development server then uses the value of FLASK_APP instead of the default file app.py. 

For more information check this link about set command:
https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/set_1

you can check this link also about PowerShell:
https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.x

### Quick Note about: 
### Create a requirements.txt file for the environment:
When you share your app code through source control (Github) or some other means,
it doesn't make sense to copy all the files in a virtual environment 
because recipients can always recreate the virtual environment themselves.

Accordingly, developers typically omit the virtual environment folder from source control 
and instead describe the app's dependencies using a requirements.txt file.

Although you can create the file by hand, 
you can also use the pip freeze command to generate the file based on the exact libraries installed 
in the activated environment:

In the terminal, run =>> pip freeze > requirements.txt 
to create the requirements.txt file in your project folder.

In such case, anyone (or any build server) that receives a copy of the project 
needs only to run the pip install -r requirements.txt command
to reinstall the packages in the original the environment. 
(The recipient still needs to create their own virtual environment, however.)

***************
## Final Summary:
***************

### To summarize, to create a new project :-):
------------------------------------------
Focusing on using Powershell Terminal Only:
First Time (Create a virtual environment):
> py -m venv any-name => let's name it "env" =>>  py -m venv env 
> activate the venv > any-name\scripts\activate =>> env\scripts\activate
> Now we can use pip list to view the packages that we have by default inside the venv
> install our package locally inside the venv: 
=>> pip install flask

NOTE:
- In case if you see this error: Unable to import 'flask'pylint(import-error)
- You can follow these steps on VSC docs starting from piont 4 to point 5:
https://code.visualstudio.com/docs/python/tutorial-flask

NOTE: running pip list command VS running pip freeze command:
1) The result format/layout
2) different results:
- pip list can display the basic default packages that added automatically to our venv + the installed packages
The default packages:
pip        19.2.3
setuptools 41.2.0
- pip freeze can only display the manually installed packages

- Now we can create the requirements.txt file that contains the required packages/dependencies to run our project locally/Heroku:
- pip freeze > requirements.txt (required for heroku deployment)

NOTE: Other people/devs can use this command: =>> pip install requirements.txt

### To summarize, to reopen a project :-):
--------------------------------------
1) Open the project folder in VS Code: File => Open Folder (CTRL+K, CTRL+O)
2) Activate your virtual environment: any-name\Scripts\activate
(in case if you see an error with activation about execution policy please refer to my python note pdf file)
3) Running our application: two ways to run our flask application (For Windows PowerShell):
3.a) Run the flask with development mode (not in production mode): 
> $env:FLASK_APP = "app"; $env:FLASK_ENV = "development"; flask run
> $env:FLASK_ENV = "development"; flask run
> Or with the LMS of Code Institute: $env:FLASK_APP = "run"; $env:FLASK_ENV = "development"; flask run 

NOTE:
> $env:FLASK_APP = "flaskr" => you need to run this command ONLY if your application name is NOT "app.py"

3.b) Run the flask with production mode (not in development mode):
> $env:FLASK_ENV = flask run (CTRL+C to quit flask)
4) Jump to your code and happy coding :-)
