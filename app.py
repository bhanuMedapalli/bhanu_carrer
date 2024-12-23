from flask import Flask,render_template, jsonify

app = Flask (__name__)
JOBS=[
   {'id':1,'title':'Data Analyst','location':'Bengaluru, India','salary':'Rs. 10,00,000'},
  {'id':2,'title':'Data Analyst','location':'Bengaluru, India','salary':'Rs. 12,00,000'},
  {'id':3,'title':'Data Analyst','location':'Channai','salary':'Rs. 13,00,000'},
  {'id':4,'title':'Data Analyst','location':'Remote','salary':'Rs. 10,00,000'},
  {'id':5,'title':'Data Analyst','location':'Bengaluru, India'}]

@app.route('/')
def name():
  return render_template('home.html',
                         jobs=JOBS,
                         company_name='Bhanu')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)
# this shows that main files by using spacial charecter __name__

  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


