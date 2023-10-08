#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    # Your chatbot logic here
    bot_reply = "This is a reply from the bot."
    return bot_reply

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

