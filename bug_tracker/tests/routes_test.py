from flask import Flask
import datetime
from sqlalchemy import DateTime
import unittest
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase
from unittest import mock
from unittest.mock import MagicMock, Mock, patch
from bug_tracker.src.Core_Model import Member, Ticket
from bug_tracker import app, db

class Routes_Tests(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ticket_app_test_db.db'
        db.init_app(app)
        app.app_context().push()
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Member(member_name='Jimmy Mgill'))
        db.session.add(Ticket(ticket_code='CA-1', ticket_title='Fix null reference exception', ticket_description='Read Title', ticket_assignee='Jimmy Mgill', ticket_status='Open', ticket_created_at=datetime.datetime(2023, 1, 5)))

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


    # Region HomePage

    def test_home_page_get(self):
        # act 
        self.client.get('/')

        # assert
        model = {'members': Member.query.all(), 'tickets': Ticket.query.all()}

        self.assert_template_used('Home_Page.html')
        self.assert_context("model", model)

    # End Region HomePage

    # Region Members

    def test_add_member_form_get(self):
        # act 
        self.client.get('/add_member_form')

        # assert
        self.assert_template_used('Add_Member_Form.html')


    @patch('bug_tracker.routes.get_member_data_from_form')
    def test_add_member_form_post(self, mock_get):
        mock_get.return_value = 'Chuck Mgill'

        # act 
        self.client.post('/add_member_form')

        # assert
        members = Member.query.all()
        model = {'members': Member.query.all(), 'tickets': Ticket.query.all()}

        assert members
        assert members[0].member_name == 'Jimmy Mgill'
        assert members[1].member_name == 'Chuck Mgill'
        self.assert_template_used('Home_Page.html')
        self.assert_context("model", model)
         

    def test_edit_member_form_get(self):
        # act
        self.client.get('/edit_member_form/1')

        # assert
        model = Member.query.get_or_404(1)

        self.assert_template_used('Edit_Member_Form.html')
        self.assert_context("model", model)


    @patch('bug_tracker.routes.get_member_data_from_form')
    def test_edit_member_form_post(self, mock_get):
        mock_get.return_value = 'Saul Goodman'

        # act
        self.client.post('/edit_member_form/1')

        # assert
        member = Member.query.get_or_404(1)
        model = {'members': Member.query.all(), 'tickets': Ticket.query.all()}

        assert member
        assert member.member_name == 'Saul Goodman'
        self.assert_template_used('Home_Page.html')
        self.assert_context("model", model)

    
    def test_delete_member(self):
        # act
        self.client.get('/delete_member/1')

        # assert
        member = Member.query.all()
        model = {'members': Member.query.all(), 'tickets': Ticket.query.all()}

        assert not member
        self.assert_template_used('Home_Page.html')
        self.assert_context("model", model)


    # End Region Members

    # Region Tickets

    def test_add_ticket_form_get(self):
        #act
        self.client.get('/add_ticket_form')

        # assert
        model = Member.query.all()

        self.assert_template_used('Add_Ticket_Form.html')
        self.assert_context("model", model)


    @patch('bug_tracker.routes.get_ticket_data_from_form')
    def test_add_ticket_form_post(self, mock_get):
        mock_get.return_value = {
            'ticket_title': 'Fix Data Leak',
            'ticket_description': 'The Data is Leaking again',
            'ticket_assignee': 'Jimmy Mgill',
            'ticket_status': 'Closed'
        }

        # act
        self.client.post('/add_ticket_form')

        # assert
        ticket = Ticket.query.get_or_404(2)
        model = {'members': Member.query.all(), 'tickets': Ticket.query.all()}

        assert ticket
        assert ticket.ticket_code == 'CA-2' 
        assert ticket.ticket_title == 'Fix Data Leak' 
        assert ticket.ticket_description == 'The Data is Leaking again' 
        assert ticket.ticket_status == 'Open' 
        assert ticket.ticket_assignee == 'Jimmy Mgill'
        assert ticket.ticket_created_at.year == 2023
        assert ticket.ticket_created_at.month == 1
        assert ticket.ticket_created_at.day == 5
        self.assert_template_used('Home_Page.html')
        self.assert_context("model", model)


    def test_edit_ticket_form_get(self):
        #act
        self.client.get('/edit_ticket_form/CA-1')

        # assert
        model = {'members': Member.query.all(), 'ticket': Ticket.query.get_or_404(1)}

        self.assert_template_used('Edit_Ticket_Form.html')
        self.assert_context("model", model)
    
    @patch('bug_tracker.routes.get_ticket_data_from_form')
    def test_edit_ticket_form_post(self, mock_get):
        mock_get.return_value = {
            'ticket_title': 'Fix Data Leak',
            'ticket_description': 'The Data is Leaking again',
            'ticket_assignee': 'Jimmy Mgill',
            'ticket_status': 'Closed'
        }

        #act
        self.client.post('/edit_ticket_form/CA-1')

        # assert
        ticket = Ticket.query.get_or_404(1)
        model = {'members': Member.query.all(), 'tickets': Ticket.query.all()}

        assert ticket
        assert ticket.ticket_code == 'CA-1' 
        assert ticket.ticket_title == 'Fix Data Leak' 
        assert ticket.ticket_description == 'The Data is Leaking again' 
        assert ticket.ticket_assignee == 'Jimmy Mgill' 
        assert ticket.ticket_status == 'Closed' 
        assert ticket.ticket_created_at.year == 2023
        assert ticket.ticket_created_at.month == 1
        assert ticket.ticket_created_at.day == 5
        self.assert_template_used('Home_Page.html')
        self.assert_context("model", model)


    def test_delete_ticket(self):
        # act
        self.client.get('/delete_ticket/CA-1')

        # arrange
        ticket = Ticket.query.all()
        model = {'members': Member.query.all(), 'tickets': Ticket.query.all()}

        assert not ticket
        self.assert_template_used('Home_Page.html')
        self.assert_context("model", model)

    # End Region Tickets

if __name__ == '__main__':
    unittest.main()