# from flask import send_from_directory
# from flask import Flask, flash, request, redirect, url_for
# from werkzeug.utils import secure_filename
# from flask import render_template
# from url_utils import get_base_url
# import os
# import torch
# import shutil
# import logging
# import pandas
# from PIL import Image

# # setup the webserver
# # port may need to be changed if there are multiple flask servers running on same server
# port = int(os.environ.get("PORT", 8000))
# base_url = get_base_url(port)

# # if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
# if base_url == '/':
#     app = Flask(__name__)
# else:
#     app = Flask(__name__, static_url_path=base_url+'static')

# UPLOAD_FOLDER = 'static/uploads'
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024
# app.jinja_options['comment_start_string'] = "##"

# # Increase the request timeout (e.g., to 60 seconds)
# app.config['TIMEOUT'] = 120  # This sets the timeout to 60 seconds

# # Add this line to configure logging
# app.logger.setLevel(logging.DEBUG)


# # Configure a log file handler
# file_handler = logging.FileHandler('app.log')
# file_handler.setLevel(logging.DEBUG)
# app.logger.addHandler(file_handler)


# try: 
#     model = torch.hub.load("ultralytics/yolov5", "custom", path = 'best.pt', force_reload=False, trust_repo=True)
#     app.logger.error(f"Successful loading of model!")
#     app.logger.error(f"model: {model}")
# except Exception as e:
#         app.logger.error(f"Error loading model: {str(e)}")

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route(f'{base_url}', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)

#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)

#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))

#     return render_template('home.html')

# @app.route(f'{base_url}/fripen_index.html', methods=['GET', 'POST'])
# def fripen_index():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)

#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)

#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))

#     return render_template('fripen_index.html')


# @app.route(f'{base_url}/uploads/<filename>')
# def uploaded_file(filename):
#     here = os.getcwd()
#     image_path = os.path.join(here, app.config['UPLOAD_FOLDER'], filename)
#     app.logger.debug(f"Current location!: {here}")
#     app.logger.debug(f"Image path: {image_path}")
    
#     try:
#         results = model(image_path, size=416)
#     except Exception as e:
#         app.logger.error(f"Error processing image: {str(e)}")
#         return "An error occurred while processing the image."

#     app.logger.debug(f"Ran through results")

#     if len(results.pandas().xyxy) > 0:
#         results.print()
#         app.logger.debug(f"Image path: {results.print()}")
#         app.logger.debug(f"Image path entered into if loop")


#         save_dir = os.path.join(here, app.config['UPLOAD_FOLDER'], filename)
#         os.remove(image_path)
#         app.logger.debug(f"old image removed")

#         results.save(save_dir=save_dir)
#         app.logger.debug(f"Results saved into: {save_dir}")

#         def and_syntax(alist):
#             if len(alist) == 1:
#                 alist = "".join(alist)
                
#                 return alist
#             elif len(alist) == 2:
#                 alist = " and ".join(alist)
               
#                 return alist
#             elif len(alist) > 2:
#                 alist[-1] = "and " + alist[-1]
#                 alist = ", ".join(alist)
                
#                 return alist
#             else:
#                 return
#         confidences = list(results.pandas().xyxy[0]['confidence'])
#         # confidences: rounding and changing to percent, putting in function
        
#         format_confidences = []
#         for percent in confidences:
#             format_confidences.append(str(round(percent*100)) + '%')
#         format_confidences = and_syntax(format_confidences)

#         labels = list(results.pandas().xyxy[0]['name'])
#         # labels: sorting and capitalizing, putting into function
#         labels = set(labels)
#         labels = [emotion.capitalize() for emotion in labels]
#         labels = and_syntax(labels)
        
        
#         # when u don't use Docker (local development, just python3 -m main) use:
#     # return render_template('results.html', confidences=format_confidences, labels=labels, old_filename=filename, filename=filename[:-4]+"/"+filename[:-4]+".jpg")
        
#         app.logger.debug(f"AT the RETURN STATEMENT")
#         #return render_template('results.html', confidences=format_confidences, labels=labels, old_filename=filename, filename=filename[:-4]+"/"+filename[:-4]+".jpg")


#         return render_template('results.html', confidences=format_confidences, labels=labels,
#                                old_filename=filename,
#                                filename=filename)
#     else:
#         found = False
#         app.logger.debug(f"AT the RETURN STATEMENT")

#         return render_template('results.html', labels='1', old_filename=filename, filename=filename)


# @app.route(f'{base_url}/uploads/<path:filename>')
# def files(filename):
#     return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

# ## CUSTOM ROUTES
# @app.route(f'{base_url}/data.html')
# def data():
#     return render_template('data.html')
# @app.route(f'{base_url}/aboutus.html')
# def aboutus():
#     return render_template('aboutus.html')
# @app.route(f'{base_url}/aimodel.html')
# def aimodel():
#     return render_template('aimodel.html')
# @app.route(f'{base_url}/ourjourney.html')
# def ourjourney():
#     return render_template('ourjourney.html')
# @app.route(f'{base_url}/miscellaneous.html')
# def miscellaneous():
#     return render_template('miscellaneous.html')


# ## CUSTOM REDIRECTS
# @app.route(f'{base_url}/home.html')
# def redirect_home():
#     return redirect(url_for('home'))

# @app.route(f'{base_url}/uploads/home.html')
# def redirect_uploads_home():
#     return redirect(url_for('home'))

# @app.route(f'{base_url}/uploads/aboutus.html')
# def redirect_uploads_aboutus():
#      return redirect(url_for('aboutus'))

# @app.route(f'{base_url}/uploads/data.html')
# def redirect_uploads_data():
#      return redirect(url_for('data'))

# @app.route(f'{base_url}/uploads/ourjourney.html')
# def redirect_uploads_journey():
#      return redirect(url_for('ourjourney'))

# @app.route(f'{base_url}/uploads/miscellaneous.html')
# def redirect_misc():
#      return redirect(url_for('miscellaneous'))


# # define additional routes here
# # for example:
# # @app.route(f'{base_url}/team_members')
# # def team_members():
# #     return render_template('team_members.html') # would need to actually make this page

# if __name__ == '__main__':
#     # IMPORTANT: change url to the site where you are editing this file.
#     website_url = 'fripen-ai.onrender.com'
    
#     #print(f'Try to open\n\n    {website_url}' + base_url + '\n\n')
#     print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')   
#     port = int(os.environ.get("PORT", 8000))
#     app.run(host = '0.0.0.0', port=port, debug=False)
from flask import send_from_directory
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import render_template
from url_utils import get_base_url
import os
import torch
import shutil
import logging
import pandas
from PIL import Image

# setup the webserver
port = int(os.environ.get("PORT", 8000))
base_url = get_base_url(port)

if base_url == '/':
    app = Flask(__name__)
else:
    app = Flask(__name__, static_url_path=base_url+'static')

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024
app.jinja_options['comment_start_string'] = "##"
app.config['TIMEOUT'] = 120

# Configure logging
app.logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

try:
    model_path = os.path.join(os.path.dirname(__file__), 'best.pt')
    model = torch.hub.load("ultralytics/yolov5", "custom", path=model_path, force_reload=False, trust_repo=True)
    app.logger.error(f"Successful loading of model!")
    app.logger.error(f"model: {model}")
except Exception as e:
    app.logger.error(f"Error loading model: {str(e)}")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route(f'{base_url}', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            try:
                file.save(file_path)
                return redirect(url_for('uploaded_file', filename=filename))
            except Exception as e:
                app.logger.error(f"Error saving file: {str(e)}")
                return "Error saving file"
    return render_template('home.html')

@app.route(f'{base_url}/fripen_index.html', methods=['GET', 'POST'])
def fripen_index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            try:
                file.save(file_path)
                return redirect(url_for('uploaded_file', filename=filename))
            except Exception as e:
                app.logger.error(f"Error saving file: {str(e)}")
                return "Error saving file"
    return render_template('fripen_index.html')

@app.route(f'{base_url}/uploads/<filename>')
def uploaded_file(filename):
    here = os.path.dirname(__file__)
    image_path = os.path.join(here, app.config['UPLOAD_FOLDER'], filename)
    app.logger.debug(f"Current location!: {here}")
    app.logger.debug(f"Image path: {image_path}")
    
    try:
        results = model(image_path, size=416)
    except Exception as e:
        app.logger.error(f"Error processing image: {str(e)}")
        return "An error occurred while processing the image."
    
    app.logger.debug(f"Ran through results")
    
    if len(results.pandas().xyxy) > 0:
        results.print()
        app.logger.debug(f"Image path: {results.print()}")
        app.logger.debug(f"Image path entered into if loop")
        
        save_dir = os.path.join(here, app.config['UPLOAD_FOLDER'], filename)
        os.remove(image_path)
        app.logger.debug(f"old image removed")
        results.save(save_dir=save_dir)
        app.logger.debug(f"Results saved into: {save_dir}")
        
        def and_syntax(alist):
            if len(alist) == 1:
                return "".join(alist)
            elif len(alist) == 2:
                return " and ".join(alist)
            elif len(alist) > 2:
                alist[-1] = "and " + alist[-1]
                return ", ".join(alist)
            return ""
        
        confidences = list(results.pandas().xyxy[0]['confidence'])
        format_confidences = [str(round(percent*100)) + '%' for percent in confidences]
        format_confidences = and_syntax(format_confidences)
        
        labels = list(results.pandas().xyxy[0]['name'])
        labels = set(labels)
        labels = [emotion.capitalize() for emotion in labels]
        labels = and_syntax(labels)
        
        app.logger.debug(f"AT the RETURN STATEMENT")
        return render_template('results.html', confidences=format_confidences, labels=labels, old_filename=filename, filename=filename)
    else:
        found = False
        app.logger.debug(f"AT the RETURN STATEMENT")
        return render_template('results.html', labels='1', old_filename=filename, filename=filename)

@app.route(f'{base_url}/uploads/<path:filename>')
def files(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route(f'{base_url}/data.html')
def data():
    return render_template('data.html')

@app.route(f'{base_url}/aboutus.html')
def aboutus():
    return render_template('aboutus.html')

@app.route(f'{base_url}/aimodel.html')
def aimodel():
    return render_template('aimodel.html')

@app.route(f'{base_url}/ourjourney.html')
def ourjourney():
    return render_template('ourjourney.html')

@app.route(f'{base_url}/miscellaneous.html')
def miscellaneous():
    return render_template('miscellaneous.html')

@app.route(f'{base_url}/home.html')
def redirect_home():
    return redirect(url_for('home'))

@app.route(f'{base_url}/uploads/home.html')
def redirect_uploads_home():
    return redirect(url_for('home'))

@app.route(f'{base_url}/uploads/aboutus.html')
def redirect_uploads_aboutus():
    return redirect(url_for('aboutus'))

@app.route(f'{base_url}/uploads/data.html')
def redirect_uploads_data():
    return redirect(url_for('data'))

@app.route(f'{base_url}/uploads/ourjourney.html')
def redirect_uploads_journey():
    return redirect(url_for('ourjourney'))

@app.route(f'{base_url}/uploads/miscellaneous.html')
def redirect_misc():
    return redirect(url_for('miscellaneous'))

if __name__ == '__main__':
    website_url = 'fripen-ai.onrender.com'
    print(f'Try to open\n\n https://{website_url}' + base_url + '\n\n')
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port, debug=False)
