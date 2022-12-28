from flask import Flask,send_file,request
import os
app = Flask(__name__)


@app.route('/')
def index():
    return '!'

@app.route("/newest")
def new():
  hi = -1
  for file in os.listdir("."):
    if file.startswith("v"):
      try:
        if int(file[1:]) >  hi:
          hi = int(file[1:])
      except:
        pass
  return 'v'+str(hi)
@app.route('/<file>', methods=['GET'])
def ind2(file):
  try: 
    return send_file(f"./{file}", as_attachment=True)
  except:
    return 'file not found',404

@app.route('/add_')
def a():
  if request.args.get("name") == "main.py" or request.args.get("name") == "add.py": return 'files not accepted '
  try:
    with open(f'{request.args.get("name")}','r'):pass
    a = 1
  except FileNotFoundError: 
    a = 0

  if a == 0: 
    with open(f'{request.args.get("name")}','a') as r:
      print(request.args.get("val"))
      r.write(request.args.get("val"))
  if a==1:
    return 'name taken'
  return ''
@app.errorhandler(404)
def handle_404():
  return ' not found',404
  
app.run(host='0.0.0.0', port=81)
