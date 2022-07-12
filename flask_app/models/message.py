# Import mysqlconnection config
from flask_app.config.mysqlconnection import connectToMySQL

class Message:
    # Use alias for db
    db = 'private_wall'
    def __init__(self,data):
        """Model a message"""
        self.id = data['id']
        self.message = data['message']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



