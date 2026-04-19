from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

db = SQLAlchemy()

class DebateSession(db.Model):
    """Store debate session information"""
    __tablename__ = 'debate_sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(50), unique=True, nullable=False)
    mode = db.Column(db.String(20), nullable=False)  # 'coach', 'omniscient', 'none'
    person_a_name = db.Column(db.String(100), default='Person A')
    person_b_name = db.Column(db.String(100), default='Person B')
    max_messages = db.Column(db.Integer, default=10)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    ended_at = db.Column(db.DateTime, nullable=True)
    
    messages = db.relationship('DebateMessage', backref='session', lazy=True, cascade='all, delete-orphan')
    surveys = db.relationship('Survey', backref='session', lazy=True, cascade='all, delete-orphan')

class DebateMessage(db.Model):
    """Store individual debate messages"""
    __tablename__ = 'debate_messages'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('debate_sessions.id'), nullable=False)
    person = db.Column(db.String(50), nullable=False)  # 'person_a' or 'person_b'
    role = db.Column(db.String(50), nullable=False)  # 'user', 'ai', 'system'
    content = db.Column(db.Text, nullable=False)
    ai_reasoning = db.Column(db.Text, default='')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Survey(db.Model):
    """Store survey responses"""
    __tablename__ = 'surveys'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('debate_sessions.id'), nullable=False)
    person = db.Column(db.String(50), nullable=False)  # 'person_a' or 'person_b'
    survey_type = db.Column(db.String(20), nullable=False)  # 'pre' or 'post'
    responses = db.Column(db.JSON, nullable=False)  # Store survey JSON
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

def init_db(app):
    """Initialize database"""
    with app.app_context():
        db.create_all()
