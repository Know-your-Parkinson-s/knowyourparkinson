# Know Your Parkinson
![Banner](https://raw.githubusercontent.com/Know-your-Parkinson-s/knowyourparkinson/master/Know%20Your%20Parkinson's-logo/cover.png)
A web application to help you detect your Parkinson's Symptoms early

## Steps to start:
1. Fork this repository to your own GitHub
2. Clone your fork onto your machine
3. Install Python (Duh!)
   - I'd suggest installing _PyPy_ and using that because it's way faster, but regular _Python3_ works too.
   - MacOS comes with _Python2_ by default and that absolutely **won't** work with Flask
4. Setup Virtual Environment
   - Open a terminal and:
   - `pypy3 -m venv venv` -> for PyPy
   - `py -m venv venv` -> python3
   - `python3 -m venv venv` -> MacOS
5. Activate Virtual Environment <- _You'll have to repeat this step everytime_
   - `venv\Scripts\activate` -> Windows _Yes, the **S** is uppercase_
   - `venv/bin/activate` -> MacOS
   - Your terminal should say _venv_ at the start of the PATH
   - ``` python
         if you see venv:
            proceed
         else:
          debug until you see venv
     ```
6. Install requirements <- _You'll have to install requirements everytime there's a change in the requirements.txt file_
   - ```pip install -r requirements.txt```
7. Do some magic shit
   - To run the server and check the app:
     - ```set FLASK_APP=park.py``` <- _Repeat everytime you have a new terminal_
     - ```flask run``` <- _If using python3_
     - ```pypy3 -m flask run``` <- _If using pypy_
     - Open a browser tab and go to ```localhost:5000```
   - When you make changes to code, most of the changes should be _hotpluggable_ i.e refresh the page to see them
   - If a refresh doesn't work, just use ```CTRL+C``` and run the appropriate version of _flask run_ 
   - If you have to install a new dependency:
     - ```pip freeze > requirements.txt```

## Workflow:
- Once you have everything setup, commit things to your own repository
- Send pull requests to the main org repo, this will check if merges are compatible
- Everytime before starting work, it's good practice to pull and check if someone has made changes to the repo
- I know using Git can be difficult and I'm no expert either, but using GitHub desktop will make life easy if you don't already know Git. 
> I myself use GH Desktop because it's faster and easier to use.