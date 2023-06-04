import cherrypy as cherrypy
from models import *

with db:
    db.create_tables([Lab6])

db.connect()


class WebPage(object):

    @cherrypy.expose
    def index(self):
        lab6 = Lab6()
        columns = lab6.get_columns()
        rows = lab6.get_rows()

        output = "<table>"
        output += "<tr>"
        for column in columns:
            output += "<th>{}</th>".format(column)
        output += "</tr>"
        for row in rows:
            output += "<tr>"
            for column in columns:
                output += "<td>{}</td>".format(row[columns.index(column)])
            output += "</tr>"
        output += "</table>"
        output += "<form method='POST' action='/add'>"
        output += "<input type='text' name='name' placeholder='Name'>"
        output += "<input type='text' name='count' placeholder='Count'>"
        output += "<input type='text' name='price' placeholder='Price'>"
        output += "<button type='submit'>Add</button>"
        output += "</form>"
        output += "</table>"
        output += "<form method='POST' action='/update'>"
        output += "<input type='text' name='id' placeholder='Id'>"
        output += "<input type='text' name='name' placeholder='Name'>"
        output += "<input type='text' name='count' placeholder='Count'>"
        output += "<input type='text' name='price' placeholder='Price'>"
        output += "<button type='submit'>Update</button>"
        output += "</form>"

        return output

    @cherrypy.expose
    def add(self, name, count, price):
        lab6 = Lab6()
        lab6.add_item(name, count, price)
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def update(self, id, name, count, price):
        lab6 = Lab6()
        lab6.update_item(article=id, name=name, count=count, price=price)
        raise cherrypy.HTTPRedirect("/")


cherrypy.quickstart(WebPage())
