# Handle my Handler

A simple Django solution for those who use same one username on all platforms.

## How does it work?

With only a couple of models and pages, this application provides elegant design solution to handle social links in one 
minimalistic space with easy access to mail option. Put a username and wrap it in social sites and mail operator.
A decent way to got your handler memorized!

Social links, provided with urls, are smoothly scrollable (although current interface is not so intuitive — will be
improved later) via CSS, later it will be improved with more options (with more JS and CSS styles).

## Launch options

Only way to launch for now is manually with some settings adjustments (will be updated later):
* Install environment and apply migrations:
```python
pip install -r requirements.txt
```
```python
python manage.py makemigrations
```
```python
python manage.py migrate
```
* Edit `.env` in `handler` app directory with `settings.py` as shown in `.env.example`;
* Run server:
```python
python manage.py runserver
```


## To-do
* Model adjustments;
* Index visual improvements (adding scroll options and direct mail links);
* Template adjustments (adding static pages);
* User authorization system;
* Deployment options (with nginx and docker);
* Example page.


## DIsclaimer
All code done by Serg Blitzen.
<br>Feel free to fork and improve!
