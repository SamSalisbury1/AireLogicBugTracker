from bug_tracker import db

class Ticket(db.Model):
    ticket_id = db.Column(db.Integer, primary_key=True)
    ticket_code = db.Column(db.String(255), unique=True, nullable=False)
    ticket_title = db.Column(db.String(20), nullable=False)
    ticket_description = db.Column(db.Text)
    ticket_status = db.Column(db.String(20), nullable=False)
    ticket_assignee = db.Column(db.String(20))

    def __repr__(self):
        return f"Ticket('{self.ticket_code}', '{self.ticket_title}', '{self.ticket_description}', '{self.ticket_status}', '{self.ticket_assignee}')"

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Member('{self.id}', '{self.member_name}')"

