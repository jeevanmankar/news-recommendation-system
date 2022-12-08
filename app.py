from flask import Flask, render_template, request
from newsSystem import news_search

app = Flask(__name__)


@app.route('/')
def home():
    results = list()
    query = request.form.get("query")
    return render_template("index.html")

@app.route('/results', methods=["GET", "POST"])
def display_description():
    """
    Serve anchor links to pet documents whose description matches the query
    :return: HTML page with Links to pet documents
    """
    if request.method == 'POST':
        results = list()
        try:
            #searchTerm = request.form.getlist("search")
            #search = ' '.join([str(elem) for elem in searchTerm])
            search = request.form['search']
            query_results = news_search(search.lower())
            for i in range(len(query_results)):  # 'Relevance','Title','Description','Link','Keywords'
                results.append([query_results.iloc[i,0],query_results.iloc[i,1],query_results.iloc[i,2],query_results.iloc[i,3],query_results.iloc[i,4]])

            if( len((query_results)) > 0):
                return render_template("link_to_results.html", items=results,count=len(results))
            else:
                return render_template("error.html")
        except Exception as error:
            print("In error" , error)
            return render_template("error.html")


@app.route('/dashboard',methods=["GET", "POST"])
def dashboard():
    return render_template('dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/Contact',methods=['GET','POST'])
def Contact():
        return render_template('contact.html')

@app.route('/feedback',methods=['GET','POST'])
def feedback():
            return render_template('feedback.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)