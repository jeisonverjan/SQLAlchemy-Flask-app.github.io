from flask import Blueprint, render_template, request, redirect
from models.contact import Contact
from utils.db import db
import json

contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def home():
    return render_template("index.html")


@contacts.route("/new", methods=['POST'])
def add_contact():
    
    full_name = request.form['full_name']
    email = request.form['email']
    phone = request.form['phone']
    
    new_contact = Contact(fullname=full_name, email=email, phone=phone)
    
    db.session.add(new_contact)
    db.session.commit()
    
    return redirect('/')


@contacts.route("/update")
def update():
    return "Updating contact"


@contacts.route("/delete")
def delete():
    return "Deleting contact"
