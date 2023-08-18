from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
from .aicontent import openAIQuery, generatecontentTopics, generatecontentSections, contentSectionExpander


views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def home():
    
    return render_template("home.html", **locals())

@views.route('/about')
def about():
    return render_template("about.html", **locals())



# Functional methods for interacting 

@views.route('/product-description', methods=["GET", "POST"] )
@login_required
def Product_Descriptions():
    if request.method == 'POST':
        submission = request.form['productDescription']
        query = "Generate a detailed production description for: {}".format(submission)
        openAIAnswer = openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)
      

    return render_template('product-description.html', user=current_user,  **locals())


@views.route('/videoideas',methods=["GET", "POST"])
@login_required
def video_Ideas():

    if request.method == 'POST':
        submission = request.form['videoIdeas']
        query = "Generate a detailed Video Ideas for: {}".format(submission)
        openAIAnswer = openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)
        
        
        

    return render_template('videoideas.html',user=current_user,  **locals())


@views.route('/tweet-ideas', methods=["GET", "POST"])
@login_required
def tweetIdeas():
    
    if request.method == 'POST':
        submission = request.form['tweetIdeas']
        query = "Generate a tweet ideas for: {}".format(submission)
        openAIAnswer = openAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)
        
    
    return render_template('tweet-ideas.html',user=current_user,  **locals())

  



@views.route('/generate-question', methods=["GET", "POST"])
@login_required
def content_title():
    
    if request.method == 'POST':
        if 'form1' in request.form:
            prompt = request.form['contentTopic']
            contentT = generatecontentTopics(prompt)
            contentTopicIdeas = contentT.replace('\n', '<br>')
    
    return render_template('generate-question.html',user=current_user,  **locals())







@views.route('/content-section', methods=["GET", "POST"])
@login_required
def content_section():
    
    if request.method == 'POST':
         if 'form2' in request.form:
            prompt = request.form['contentSection']
            contentT = generatecontentSections(prompt)
            contentSectionIdeas = contentT.replace('\n', '<br>')
    
    return render_template('content-section.html',user=current_user,  **locals())





@views.route('/Expand-content', methods=["GET", "POST"])
@login_required
def content():
    if request.method == 'POST':
         if 'form3' in request.form:
            prompt = request.form['contentExpander']
            contentT = contentSectionExpander(prompt)
            contentExpanded = contentT.replace('\n', '<br>')
    
    
    return render_template("content.html",user=current_user,  **locals())