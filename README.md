# hello-wur
Hello WURld

Taken from this example: https://devcenter.heroku.com/articles/getting-started-with-python-o

# Run
```bash
git clone https://github.com/fritzvd/hello-wur.git
cd hello-wur
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

run locally with plain ole Python and pip
```
python main.py
```

Or free with/on heroku (Assuming you have heroku credentials). Install [heroku toolbelt](https://toolbelt.heroku.com/).
```
heroku login
heroku create
git push heroku master
```

### Hello *World*
Runs here: http://mysterious-castle-6257.herokuapp.com/?name=fritz

### Distance between points
Runs here: http://mysterious-castle-6257.herokuapp.com/distance?from=53.3,4.4&to=51.4,3.6
