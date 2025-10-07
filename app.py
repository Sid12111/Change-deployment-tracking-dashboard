from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

EXCEL_PATH = "" #path to your data file

# Columns to return
COLUMNS_TO_RETURN = [
    "Change Id",
    "Status",
    "Change Description",
    "Change Migrated On",
    "Owner Name"
]

# ✅ Serve the index.html file
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')


# ✅ Return sheet names for dropdown
@app.route('/clients', methods=['GET'])
def get_client_sheet_names():
    try:
        xl = pd.ExcelFile(EXCEL_PATH, engine='openpyxl')
        return jsonify(xl.sheet_names)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ✅ Filter and return results
@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        client = data['client'].strip()
        start_date = pd.to_datetime(data.get('start'), errors='coerce')
        end_date = pd.to_datetime(data.get('end'), errors='coerce')

        xls = pd.read_excel(EXCEL_PATH, sheet_name=None, engine="openpyxl")

        if client not in xls:
            return jsonify({"error": f"No sheet named '{client}' found."})

        df = xls[client]

        if 'Change Migrated On' not in df.columns:
            return jsonify({"error": "No 'Change Migrated On' column found in sheet."})

        df['Change Migrated On'] = pd.to_datetime(df['Change Migrated On'], errors='coerce')

        if not pd.isna(start_date) and not pd.isna(end_date):
            df = df[(df['Change Migrated On'] >= start_date) & (df['Change Migrated On'] <= end_date)]

        valid_columns = [col for col in COLUMNS_TO_RETURN if col in df.columns]
        df = df[valid_columns]
        df = df.where(pd.notnull(df), None)

        for col in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df[col]):
                df[col] = df[col].apply(lambda x: x.strftime('%Y-%m-%d') if pd.notna(x) else '')

        result = {
            "count": len(df),
            "data": df.to_dict(orient='records')
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


