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
        self.sender = data['sender']
        self.receiver_id = data['receiver_id']
        self.receiver = data['receiver']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def get_users_message(cls,data):
        """Get messages from db for user logged in (receiver)"""
        query = "SELECT users.first_name AS sender, users2.first_name AS receiver, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users AS users2 ON users2.id = messages.receiver_id WHERE users2.id = %(id)s;" 
        results = connectToMySQL(cls.db).query_db(query,data)
        received_messages = []
        for m in results:
            received_messages.append(cls(m))
        return received_messages

    def create_message(cls,data):
        """Send message; create record in messages"""
        query = "INSERT INTO messages (message, sender_id, receiver_id) VALUES (%(message)s, %(sender_id)s, %(receiver_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    def delete_message(cls,data):
        """delete message"""
        query = "DELETE FROM messages WHERE message.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)


