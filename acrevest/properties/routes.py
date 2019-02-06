# posts/routes.py
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from acrevest import db
from acrevest.models import Property
from acrevest.properties.forms import PropertyForm

from flask import Blueprint

properties = Blueprint('property', __name__)

@properties.route("/property/new", methods=['GET', 'POST'])
@login_required
def new_property():
    form = PropertyForm()
    if form.validate_on_submit():
        property = Property(size=form.size.data, city=form.city.data, county=form.county.data, state=form.state.data, postal_code=form.postal_code.data,country=form.country.data, description=form.description.data, listed_by=current_user)
        db.session.add(property)
        db.session.commit()
        flash('Your property has been submitted and will be listed shortly!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_listing.html', title='List Property', form=form, legend='List Property')


@properties.route("/property/<int:property_id>")
def property(property_id):
    property = Property.query.get_or_404(property_id)
    return render_template('property.html', title=property.title, property=property)


@properties.route("/property/<int:property_id>/update", methods=['GET', 'POST'])
@login_required
def update_listing(property_id):
    property = Property.query.get_or_404(property_id)
    if property.listed_by != current_user:
        abort(403)
    form = PropertyForm()
    if form.validate_on_submit():
        property.size = form.size.data
        property.city = form.city.data
        property.county = form.county.data
        property.state = form.state.data
        property.postal_code = form.postal_code.data
        property.country = form.country.data
        property.description = form.description.data
        
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('properties.property', property_id=property.id))
    elif request.method =='GET':
        form.size.data = property.size
        form.city.data = property.city
        form.county.data = property.county
        form.state.data = property.state
        form.postal_code.data = property.postal_code
        form.country.data = property.country
        form.description.data = property.description

    form.size.data = property.size
    form.city.data = property.city
    form.county.data = property.county
    form.state.data = property.state
    form.postal_code.data = property.postal_code
    form.country.data = property.country
    form.description.data = property.description
    return render_template('list_property.html', title='Update Listing', form=form, legend='Update Listing')

@properties.route("/property/<int:property_id>/delete", methods=['POST'])
@login_required
def remove_listing(property_id):
    property = Property.query.get_or_404(property_id)
    if property.listed_by != current_user:
        abort(403)

    db.session.delete(property)
    db.session.commit()
    flash('Your listing has been removed!', 'success')
    return redirect(url_for('main.home'))

