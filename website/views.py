import json
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user, login_required, current_user
from .models import Note
from . import db 

# bunch of roots here for diffrent states pages (urls) seperated

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        noteData = request.form.get('note')
        if len(noteData) < 1:
            flash('Empty messeges are not allowed!', category='error')
        else:
            new_note = Note(data = noteData, user_id= current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added successfully!', category='success')
    
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    data = json.loads(request.data)  # Use request.json to directly access JSON data
    note_id = data['noteID']
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
        
    return jsonify({})

    
