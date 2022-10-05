# VehiclesMarket
Full Stack web application

# Requirements
## Purpose
Visualize the vehicles on responsive Heat Map. <br />
New user can upload his vehicles and they would be added to the Heat Map or merely observe and search for vehicles. <br />
The Heat Map allows you to find out which areas include the biggest number of vehicles (red = many, green = less). <br />
The Heat map and the search vehilces process are available for all users.
## Features - must
1) Responsive Heat Map - 3 layers one on top of another (Polygon of Israel state, Heat map, Points of existing vehicles).
2) Create and edit personal profile.
3) Upload new vehicle.
4) Search for vehicles manually, finding their specifications and pointing out their location on the map.
## Features - optional
1) Public chat with the vehicle's owner (who have been traced during the search process).
2) Additional information about specific vehicle from free API.
3) Deploy to Cloud

# Design
## Description
FrontEnd with HTML, BackEnd with Flask (Python 3) and Database with SQLite (SQLAlchemy).
The package 'website' includes all application. The main file (main.py) imports website and the function create_app(), which creates the package, the database and initializes the blueprints. The application is divided into 2 Blueprints: auth and views. <br />
auth handles the operations: login, signup and logout. <br />
views handles the operations: Display/Delete user profile, Upload/Delete vehicle, Search vehicles, Display analytics (Heat Map page).

## Database diagram
<img width="431" alt="image" src="https://user-images.githubusercontent.com/58309185/193948888-cbfe583a-2bd4-4a97-b8b6-9ae058bb8c6d.png">

## Sequence diagrams
![image](https://user-images.githubusercontent.com/58309185/194046989-753f2444-1566-4907-8e2b-5668c48cf647.png)

![image](https://user-images.githubusercontent.com/58309185/194046901-2f435ac9-104d-473b-a16a-c6581ba51b60.png)

![image](https://user-images.githubusercontent.com/58309185/194046803-8e3b3248-c0b4-4413-a079-19a6c88c7cb0.png)

![image](https://user-images.githubusercontent.com/58309185/194046721-95391b7a-4d8b-4a24-88b5-641116032ab6.png)

![image](https://user-images.githubusercontent.com/58309185/194046660-2f08db1b-b7ba-4e28-903b-92661b4fe5c8.png)

## Use case diagram
![image](https://user-images.githubusercontent.com/58309185/194046542-e0929610-7c0d-4620-99d1-003893e99beb.png)

# Deployment - run in CMD:
** copy the lines below to cmd in this order! <br />
python -m set_up.py <br />
python -m pip install --upgrade pip <br />
![Requirements_FIona_GDAL](https://user-images.githubusercontent.com/58309185/194172318-833268ed-28a3-4111-a615-d43a038b5e36.png)

python -m venv env <br />
\venv\Scripts\activate <br />
python -m pip install --upgrade pip <br />
python -m pip install -r requirements.txt --force-reinstall <br />
python -m main
