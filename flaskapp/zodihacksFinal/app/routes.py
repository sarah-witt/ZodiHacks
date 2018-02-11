import indicoio
import operator
from flask import Flask, request, render_template
indicoio.config.api_key = '03843959a29915829e64e3e5537b4079'

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/capricorn.html')
def capricorn():
    return render_template('capricorn.html')

@app.route('/virgo.html')
def virgo():
    return render_template('virgo.html')

@app.route('/leo.html')
def leo():
    return render_template('leo.html')

@app.route('/taurus.html')
def taurus():
    return render_template('taurus.html')

@app.route('/gemini.html')
def gemini():
    return render_template('gemini.html')

@app.route('/libra.html')
def libra():
    return render_template('libra.html')

@app.route('/scorpio.html')
def scorpio():
    return render_template('scorpio.html')

@app.route('/aquarius.html')
def aquarius():
    return render_template('aquarius.html')

@app.route('/pisces.html')
def pisces():
    return render_template('pisces.html')

@app.route('/aries.html')
def aries():
    return render_template('aries.html')

@app.route('/sagittarius.html')
def sagittarius():
    return render_template('sagittarius.html')

@app.route('/cancer.html')
def cancer():
    return render_template('cancer.html')

def zodiac_finder (myersbriggs):
    a = ''
    if (myersbriggs == 'consul'):
        a = 'libra.html'
    elif (myersbriggs == 'entertainer'):
        a = 'leo.html'
    elif (myersbriggs == 'executive'):
        a = 'capricorn.html'
    elif (myersbriggs == 'logistician'):
        a = 'cancer.html'
    elif (myersbriggs == 'entrepreneur'):
        a = 'aries.html'
    elif (myersbriggs == 'defender'):
        a = 'taurus.html'
    elif (myersbriggs == 'virtuoso'):
        a = 'aries.html'
    elif (myersbriggs == 'adventurer'):
        a = 'sagittarius.html'
    elif (myersbriggs == 'protagonist'):
        a = 'leo.html'
    elif (myersbriggs == 'campaigner'):
        a = 'gemini.html'
    elif (myersbriggs == 'advocate'):
        a = 'aquarius.html'
    elif (myersbriggs == 'mediator'):
        a = 'pisces.html'
    elif (myersbriggs == 'logician'):
        a = 'virgo.html'
    elif (myersbriggs == 'debater'):
        a = 'gemini.html'
    elif (myersbriggs == 'commander'):
        a = 'capricorn.html'
    else:
        a = 'scorpio.html'
    return a

@app.route('/', methods=['POST']) #allow POST request
def my_form_post():
    text = request.form['text']
    if (text == ''):
        return render_template('index.html')
    else:
        matches = indicoio.personas(text)
        myersbriggs = max(matches.items(), key=operator.itemgetter(1))[0]
        zodiac = zodiac_finder(myersbriggs)
        return render_template(zodiac)

if __name__ == '__main__':
  app.run(debug=True)
