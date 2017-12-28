from flask import render_template, request
from datetime import datetime

from realty_app import app
from realty_app.models import Real_estate, db
from realty_app.proc_json import add_real_estate_content


PER_PAGE = 15


@app.route('/')
@app.route('/<int:page>')
def ads_list(page=1):
    oblast_district = request.args.get('oblast_district',
                                       type=str,
                                       default=None)
    min_cost = request.args.get('min_price',
                                 type=str,
                                 default=None)
    max_cost = request.args.get('max_price',
                                type=str,
                                default=None)
    new_building = request.args.get('new_building',
                                    type=bool,
                                    default=None)
    ads = Real_estate.query.filter_by(active=True)

    if new_building:
        year_now = datetime.today().year
        diff_between_the_new_old_build = 2
        year_built = Real_estate.construction_year
        check_new_building = year_now - year_built
        ads = ads.filter(check_new_building <= diff_between_the_new_old_build)
    if oblast_district:
        ads = ads.filter_by(oblast_district=oblast_district)
    if min_cost:
        ads = ads.filter(Real_estate.price >= min_cost)
    if max_cost:
        ads = ads.filter(Real_estate.price <= max_cost)

    ads = ads.paginate(page, per_page=PER_PAGE, error_out=False)

    return render_template('ads_list.html', ads=ads,
                           oblast_district=oblast_district,
                           max_price=max_cost,
                           min_price=min_cost,
                           new_building=new_building)
