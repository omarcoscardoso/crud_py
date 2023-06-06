from flask_table import Table, Col, LinkCol
 
class Results(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    email = Col('Email')
    password = Col('Password', show=False)
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='id'))
    