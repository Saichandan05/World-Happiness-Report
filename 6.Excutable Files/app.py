from flask import Flask,request,render_template
import pickle
app=Flask(__name__)
model=pickle.load(open('World happiness report.pkl','rb'))

@app.route('/')
def home():
 return render_template("index.html")

@app.route('/result', methods=['GET','POST'])
def Result():
   if request.method == "POST":
      gdp_per_capita = float(request.form['gdp_per_capita'])
      social_support = float(request.form['social_support'])
      healthy_life_expectancy = float(request.form['healthy_life_expectancy'])
      freedom_to_choose = float(request.form['freedom_to_choose'])
      generosity = float(request.form['generosity'])
      perceptions_of_corruption = float(request.form['corruption_perception'])
      pred = [[gdp_per_capita, social_support, healthy_life_expectancy, freedom_to_choose, generosity, perceptions_of_corruption]]
      print(pred)
      output = model.predict(pred)
      print(output)
      return render_template('result.html', predict = output)
   
   return render_template('pred.html')

if __name__ == '__main__':
  app.run(debug=True)



