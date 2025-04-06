from flask import Blueprint, render_template, request, jsonify
import random
import string

# Membuat Blueprint untuk 'main'
bp_main = Blueprint('main', __name__)


@bp_main.route('/generate-code', methods=['POST'])
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

