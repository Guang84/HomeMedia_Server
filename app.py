import os
from flask import Flask, jsonify, send_from_directory, abort, render_template, request, send_file, Response
from werkzeug.utils import secure_filename
import zipfile
import io

app = Flask(__name__)

MEDIA_FOLDER = 'media'

# Utility to list folders and files in a directory, with pagination
def list_directory(directory, page=1, items_per_page=10):
    files = []
    folders = []
    try:
        entries = list(os.scandir(directory))
        entries = sorted(entries, key=lambda e: e.name)  # Sort by name
        total_items = len(entries)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        for entry in entries[start:end]:
            if entry.is_file():
                files.append(entry.name)
            elif entry.is_dir():
                folders.append(entry.name)

        return {
            "folders": folders,
            "files": files,
            "total_items": total_items,
            "page": page,
            "items_per_page": items_per_page
        }
    except FileNotFoundError:
        abort(404, description=f"Directory {directory} not found")


# Route to serve the frontend HTML page
@app.route('/')
def index():
    return render_template('index.html')


# Route to list directories and media files with pagination
@app.route('/browse/<path:subpath>', methods=['GET'])
@app.route('/browse/', methods=['GET'])
def browse_media(subpath=""):
    page = request.args.get('page', 1, type=int)
    directory = os.path.join(MEDIA_FOLDER, subpath)
    if not os.path.isdir(directory):
        abort(404, description=f"Directory {subpath} not found")
    return jsonify(list_directory(directory, page=page))


# Route to stream or download media files with byte-range support for large files
@app.route('/media/<path:filename>', methods=['GET'])
def stream_media(filename):
    file_path = os.path.join(MEDIA_FOLDER, filename)
    if not os.path.isfile(file_path):
        abort(404)

    # Handle video streaming with byte-range requests
    def generate():
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(1024 * 8)  # Read in chunks
                if not data:
                    break
                yield data

    return Response(generate(), content_type='video/mp4', direct_passthrough=True)


# Search route to find media by name with pagination
@app.route('/search', methods=['GET'])
def search_media():
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    items_per_page = 10
    result = []

    # Walk through the media folder and collect search results
    for root, dirs, files in os.walk(MEDIA_FOLDER):
        for file in files:
            if query.lower() in file.lower():
                relative_path = os.path.relpath(root, MEDIA_FOLDER)
                result.append(os.path.join(relative_path, file))

    # Pagination for search results
    total_items = len(result)
    start = (page - 1) * items_per_page
    end = start + items_per_page
    paginated_results = result[start:end]

    return jsonify({
        "results": paginated_results,
        "total_items": total_items,
        "page": page,
        "items_per_page": items_per_page
    })


# Route to download an entire folder as a zip
@app.route('/download_folder/<path:foldername>', methods=['GET'])
def download_folder(foldername):
    directory = os.path.join(MEDIA_FOLDER, foldername)
    if not os.path.isdir(directory):
        abort(404, description=f"Folder {foldername} not found")
    
    zip_io = io.BytesIO()
    with zipfile.ZipFile(zip_io, mode='w') as zip_file:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, directory))
    zip_io.seek(0)
    return send_file(zip_io, mimetype='application/zip', as_attachment=True, download_name=f"{foldername}.zip")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
