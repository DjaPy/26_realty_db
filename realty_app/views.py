from flask import render_template

from app import app, db
from .models import Real_estate


@app.route('/')
def ads_list():
    return render_template('ads_list.html', ads=[{
            "settlement": "Череповец",
            "under_construction": False,
            "description": '''Квартира в отличном состоянии. Заезжай и живи!''',
            "price": 2080000,
            "oblast_district": "Череповецкий район",
            "living_area": 17.3,
            "has_balcony": True,
            "address": "Юбилейная",
            "construction_year": 2001,
            "rooms_number": 2,
            "premise_area": 43.0,
        }]*10
    )