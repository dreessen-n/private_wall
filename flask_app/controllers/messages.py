
# Import app
from flask_app import app
# Import modules from flask
from flask_app import Flask, render_template, request, redirect, session, url_for, flash, bcrypt

# Import models class
from flask_app.models import user

@app.route('/wall')
def display_send_messages():
    """Display page of received message ability to send messages"""
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Create data set to query user based on id to get name to display
    data = {
        'id': session['id']
    }
    # Pass the data dict to create_user method in class
    one_user = user.User.get_user_by_id(data)
    if one_user:
        session['email'] = one_user.email
        session['first_name'] = one_user.first_name
        session['last_name'] = one_user.last_name
    return render_template('wall.html')
