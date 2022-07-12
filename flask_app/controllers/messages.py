
# Import app
from flask_app import app
# Import modules from flask
from flask_app import Flask, render_template, request, redirect, session, url_for, flash, bcrypt

# Import models class
from flask_app.models import user, message

@app.route('/wall')
def display_to_send_and_received_messages():
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
    # Get users received messages to display
    data_m = { 'receivers_id': session['id'] }
    user_messages = message.Message.get_users_message(data_m)
    all_users = user.User.get_all_users()
    return render_template('wall.html', one_user=one_user, user_messages=user_messages, all_users=all_users)

@app.route('/wall/send_message')
def send_message():
    """Send message to user"""
    pass

@app.route('/delete_message/<int:message_id>')
def delete_message(message_id):
    """Delete message by message_id"""
    data = { 'id': message_id }
    message.Message.delete_message(data)
    return redirect('/wall')

