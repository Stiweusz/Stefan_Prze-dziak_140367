from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/kredyt', methods=['GET'])
def decyzja_kredytowa():
    try:
        wiek = int(request.args.get('wiek'))
        dochod = float(request.args.get('dochod'))

        if wiek >= 18 and dochod > 3000:
            decyzja = "Kredyt przyznany"
        else:
            decyzja = "Kredyt nieprzyznany"

        return jsonify({
            "wiek": wiek,
            "dochod": dochod,
            "decyzja": decyzja
        })
    except (ValueError, TypeError):
        return jsonify({"error": "Błędne dane wejściowe"}), 400

if __name__ == '__main__':
    app.run(debug=True)
