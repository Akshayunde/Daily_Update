from flask import Flask, render_template
app=Flask(__name__)

post = [
{
'Item_name': 'pen',
'Item_date': '20/02/2020',
'Item_prise': '50'
},
{
'Item_name': 'book',
'Item_date': '25/02/2020',
'Item_prise': '454'
}
]


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', post=post)

@app.route('/about')
def about():
	return render_template('aout.html')

@app.route('/contactus')
def contactus():
	return render_template('contact.html')

if __name__ == '__main__':
	app.run(debug=True)


