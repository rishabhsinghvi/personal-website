from website import db

class Message(db.Model):
    m_id = db.Column(db.Integer, primary_key = True)
    m_name = db.Column(db.String(20), nullable = False)
    m_email = db.Column(db.String(100), nullable = False)
    m_msg = db.Column(Text, nullable = False)
    m_msg_time = db.Column(DateTime, nullable=False)

    def __repr__(self):
        return f"Message({self.m_name}, {self.m_email}, {self.m_msg})"
    
