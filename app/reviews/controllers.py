from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for,jsonify
from app import db,login_manager
from flask_cors import CORS


from app.reviews.models import Review
mod_reviews = Blueprint('reviews', __name__, url_prefix='/reviews')


@mod_reviews.route('/addReview/<id>',methods=['POST'])
def addreview(id):
        if(request.method=='POST' and g.user.is_authenticated):
                text=request.form['text']
                username=g.user.name
                review=Review(text,id,username)
                db.session.add(review)
                db.session.commit()
                return jsonify(review.revSerialize())


@mod_reviews.route('/showReview/<id>',methods=['GET'])
def showReviewTable(id):
        if(request.method=='GET'):
                review={'Review':[]}
                rw=Review.query.filter(Review.item_id==id).all()
                for i in rw:
                        review['Review'].append(i.revSerialize())
                return jsonify(review)

