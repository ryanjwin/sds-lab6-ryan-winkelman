# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Lab 6 Partners:

# Ryan Winkelman
# Hiram Lopez


# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from state_info import capitals
from model import grade_answers
# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    states = capitals.keys()
    return render_template('quiz.html', states=states)

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        redirect('/')
    # take in answers and build dictionary
    guesses = {}
    states = capitals.keys()
    for state in states:
        if len(request.form[''.join(state.split())]) > 0:
            guesses[state] = request.form[''.join(state.split())]
    answers = grade_answers(guesses)
    return render_template('results.html', answers=answers, capitals=capitals)