from flask import Flask, render_template, redirect, url_for, request, jsonify
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/generate_code.html')

@app.route('/test/')
def test():
    return render_template('test.html')


@app.route('/generate-code', methods=['POST'])
def generate_unique_code():
    brand = request.form.get('brand')
    model = request.form.get('model')

    # while True:      
    if brand == 'djoy':
        if model == 'os':
            code = 'D0'
        else:
            code = 'D1'
    else:
        if model == 'os':
            code = 'W0'
        else:
            code = 'W1'
            
    
    # Menambahkan 12 karakter acak yang bisa berupa huruf besar/kecil atau angka
    code += ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    
    print(f"Generated unique code: {code}")
    return jsonify({'code': code})
        # Memeriksa apakah kode sudah ada dalam daftar
        # if code not in generated_codes:
        #     generated_codes.add(code)
        #     return code


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

