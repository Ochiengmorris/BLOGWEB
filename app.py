from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

POSTS = [
  {
    'id': 1,
    'date': 'February 29,2023',
    'title': 'Autopsy Shows Missing UoN Lecturer Died by Strangulation.',
    'content': 'The daily covered the mysterious death of Samuel Mbutu, a University of Nairobi political science lecturer who was reported missing earlier this month.'
  },
  {
    'id': 2,
    'date': 'February 26,2023',
    'title': 'Nairobi Man Becomes a Millionaire After Winning Sportpesa Mega Jackpot Bonus',
    'content': 'A man in Nairobi named Peter-Kiboi is the latest SportPesa Mega Jackpot bonus winner after clinching a staggering KSh 5.4 million.'
  },
  {
    'id': 3,
    'date': 'February 2,2023',
    'title': 'Raila Odingas Bid for AU Top Seat in Limbo New Rules that Might Lock Him out',
    'content': 'Former prime ministers fate now lies in the heads of state and governments who will have the final say on the proposed changes.'
  },
  {
    'id': 4,
    'date': 'Backend Engineer',
    'title': 'Embarambamba, William Getumbes Songs to Be Pulled Down, ',
    'content': 'He announced that Embarambamba and Getumbe may face suspension from MCSK for five years and expulsion if they repeat such offences.'
  }
]

@app.route('/')
def hello():
  return render_template("base.html", posts=POSTS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080,   debug=True)
