from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/realtime', defaults={'count':1})
@app.route('/realtime')
def realtime():

    # baca data testfile pertama
    # tampilkan ke graph
    # graph nya dinamis (anggap 1 detik ganti 5 data)
    # ganti data setiap 30 detik
    
    return render_template('realtime.html')

@app.route('/data', defaults={'count': 1})
@app.route('/data/<count>')
def get_data(count):
    base_filename="testfile"
    filename=base_filename+str(count)+".csv"
    data = {}
    ch1 = []; ch2 = []; ch3 = []; ch4 = []
    ch_list = ['Channel1', 'Channel2', 'Channel3', 'Channel4']

    try:
        with open('c:/Users/user/Downloads/' + filename, 'r') as file:
            if file:
                csv_reader = csv.DictReader(file)
                cnt = 1
                for row in csv_reader:
                    cnt += 1
                    ch1.append(row[ch_list[0]])
                    ch2.append(row[ch_list[1]])
                    ch3.append(row[ch_list[2]])
                    ch4.append(row[ch_list[3]])

                data[ch_list[0]] = ch1
                data[ch_list[1]] = ch2
                data[ch_list[2]] = ch3
                data[ch_list[3]] = ch4

    except (FileNotFoundError):
        print('file not found')
        print(filename)
        return get_data(int(count)-1)

    return jsonify({'count': count, 'data': data})

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/diagram')
def diagram():
    return render_template('diagram.html')

@app.route('/configuration')
def configuration():
    return render_template('configuration.html')

if __name__ == '__main__':
    app.run(debug=True)
