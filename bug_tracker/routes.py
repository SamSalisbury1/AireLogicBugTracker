from flask import render_template, request
from bug_tracker import app, db
from bug_tracker.src.Core_Model import Member, Ticket

@app.route("/")
def home_page_get():
    return render_template("Home_Page.html", model=get_home_page_model())


# Region Members

@app.route("/add_member_form")
def add_member_form_get():
    return render_template("Add_Member_Form.html")


@app.route('/add_member_form', methods=['POST'])
def add_member_form_post():
    member = Member(member_name=get_member_data_from_form())
    with app.app_context():
        db.session.add(member)
        db.session.commit()

    return render_template("Home_Page.html", model=get_home_page_model())

@app.route('/edit_member_form/<int:member_id>')
def edit_member_form_get(member_id): 
    return render_template("Edit_Member_Form.html", model=get_edit_member_model(member_id))


@app.route('/edit_member_form/<int:member_id>', methods=['POST'])
def edit_member_form_post(member_id):
    with app.app_context():
        member = Member.query.get_or_404(member_id)
        member.member_name = get_member_data_from_form()
        db.session.commit()

    return render_template("Home_Page.html", model=get_home_page_model())


@app.route('/delete_member/<int:member_id>')
def delete_member(member_id):
    with app.app_context():
        Member.query.filter_by(id=member_id).delete()
        db.session.commit()

    return render_template("Home_Page.html", model=get_home_page_model())

# End Region

# Region Tickets

@app.route("/add_ticket_form")
def add_ticket_form_get():
    return render_template("Add_Ticket_Form.html", model=get_add_ticket_model())


@app.route('/add_ticket_form', methods=['POST'])
def add_ticket_form_post():
    ticket_data = get_ticket_data_from_form()   
    ticket = Ticket(
        ticket_code = get_ticket_code(),
        ticket_title = ticket_data['ticket_title'],
        ticket_description = ticket_data['ticket_description'],
        ticket_assignee = ticket_data['ticket_assignee'],
        ticket_status = 'Open'
    )

    with app.app_context():
        db.session.add(ticket)
        db.session.commit()

    return render_template("Home_Page.html", model=get_home_page_model())


@app.route('/edit_ticket_form/<ticket_code>')
def edit_ticket_form_get(ticket_code):
    return render_template("Edit_Ticket_Form.html", model=get_edit_ticket_model(ticket_code))


@app.route('/edit_ticket_form/<ticket_code>', methods=['POST'])
def edit_ticket_form_post(ticket_code):
    id = int(ticket_code.split('-')[1])
    ticket_data = get_ticket_data_from_form()

    with app.app_context():
        ticket = Ticket.query.get_or_404(id)
        ticket.ticket_title = ticket_data['ticket_title']
        ticket.ticket_description = ticket_data['ticket_description']
        ticket.ticket_assignee = ticket_data['ticket_assignee']
        ticket.ticket_status = ticket_data['ticket_status']
        db.session.commit()

    return render_template("Home_Page.html", model=get_home_page_model())


@app.route('/delete_ticket/<ticket_code>')
def delete_ticket(ticket_code):
    id = int(ticket_code.split('-')[1])
    with app.app_context():
        Ticket.query.filter_by(ticket_id=id).delete()
        db.session.commit()

    return render_template("Home_Page.html", model=get_home_page_model())


# End Region

def get_ticket_code():
    tickets = Ticket.query.all()

    if tickets == []:
        return 'CA-1'
    else:
        last_element = tickets[len(tickets) - 1]
        latest_code = last_element.ticket_code
        latest_code_num = int(latest_code.split('-')[1])

        return 'CA-' + str(latest_code_num + 1)

def get_home_page_model():
    return {'members': Member.query.all(), 'tickets': Ticket.query.all()} 


def get_edit_member_model(member_id):
    return Member.query.get_or_404(member_id)


def get_add_ticket_model():
    return Member.query.all()


def get_edit_ticket_model(ticket_code):
    id = int(ticket_code.split('-')[1])
    return {'members': Member.query.all(), 'ticket': Ticket.query.get_or_404(id)}


def get_member_data_from_form():
    return request.form.get('member_name')


def get_ticket_data_from_form():
    return {
        'ticket_title': request.form.get('ticket_title'),
        'ticket_description': request.form.get('ticket_description'),
        'ticket_assignee': request.form.get('ticket_assignee'),
        'ticket_status': request.form.get('ticket_status') if request.form.get('ticket_status') else 'Open'
    }