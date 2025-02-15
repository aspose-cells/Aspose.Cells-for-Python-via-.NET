# This is a demo to show how to use GridJs .
import configparser
import gzip
import io
import mimetypes
import os
from aspose.cellsgridjs import *
import requests
# from aspose.cells import Workbook, SaveFormat, CellsHelper


from flask import Flask, render_template, jsonify, request, send_from_directory, Response, send_file, abort

config = configparser.ConfigParser()
config.read('config.ini')
app=Flask(__name__)
# your working file directory which has spreadsheet files inside wb directory，
FILE_DIRECTORY = os.path.join(os.getcwd(),'wb')
UPLOAD_FOLDER = os.path.join(os.getcwd(),'upload')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def index():
    filename=config.get('DEFAULT', 'FileName')
    return render_template('uidload.html',filename= filename,uid=GridJsWorkbook.get_uid_for_file(filename))

@app.route('/list')
def list():
    files = os.listdir(FILE_DIRECTORY)
    return render_template('list.html', files=files)

@app.route('/Uidtml', methods=['GET'])
def uidtml():
    filename = request.args.get('filename')
    uid = request.args.get('uid')
    return render_template('uidload.html',filename= filename,uid= uid)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    try:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return render_template('uidload.html',filename= file.filename,uid=GridJsWorkbook.get_uid_for_file(file.filename),fromupload=1)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# get json info from  /GridJs2/DetailJson?filename=
@app.route('/GridJs2/DetailJson', methods=['GET'])
def detail_file_json():
    filename = request.args.get('filename')
    if not filename:
        return jsonify({'error': 'filename is required'}), 400
    gwb = GridJsWorkbook()
    # the full path of the file
    file_path = os.path.join(FILE_DIRECTORY, filename)

    # check if the file exists
    if not os.path.isfile(file_path):
        return jsonify({'error': 'file not found'}), 404
    try:
        gwb.import_excel_file(file_path)
        ret = gwb.export_to_json(filename)
        # create a response object, passing in the response body, status code, headers, etc.
        response = Response(ret, status=200, mimetype='text/plain')

        # set the character encoding of the response to UTF-8 
        response.headers['Content-Type'] = 'text/plain; charset=utf-8'

        return response

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@app.route('/GridJs2/DetailStreamJson', methods=['GET'])
def detail_stream_json():
    filename = request.args.get('filename')
    if not filename:
        return Response("Missing filename parameter", status=400)

    file_path = os.path.join(FILE_DIRECTORY, filename)
    try:
        wbj = GridJsWorkbook()
        wbj.import_excel_file(file_path)

        output = io.BytesIO()
        with gzip.GzipFile(fileobj=output, mode='wb', compresslevel=9) as gzip_stream:
            wbj.json_to_stream(gzip_stream, filename)

        response = Response(output.getvalue(), mimetype='application/json')
        response.headers['Content-Encoding'] = 'gzip'

        return response
    except Exception as e:
        return Response(str(e), status=500)

@app.route('/GridJs2/DetailStreamJsonWithUid', methods=['GET'])
def detail_stream_json_with_uid():
    filename = request.args.get('filename')
    uid = request.args.get('uid')
    fromUpload = request.args.get('fromUpload')
    if not filename:
        return jsonify({'error': 'filename is required'}), 400
    if not uid:
        return jsonify({'error': 'uid is required'}), 400
    if not fromUpload:
        file_path = os.path.join(FILE_DIRECTORY, filename)
    else:
        file_path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        wbj = GridJsWorkbook()


        output = io.BytesIO()
        with gzip.GzipFile(fileobj=output, mode='wb', compresslevel=9) as gzip_stream:
            is_done  = wbj.json_to_stream_by_uid(gzip_stream,uid, filename)
            if not is_done:
                wbj.import_excel_file(uid,file_path)
                wbj.json_to_stream(gzip_stream, filename)

        response = Response(output.getvalue(), mimetype='application/json')
        response.headers['Content-Encoding'] = 'gzip'

        return response
    except Exception as e:
        return Response(str(e), status=500)


@app.route('/GridJs2/LazyLoading', methods=['POST'])
def lazy_loading():
    sheet_name = request.form.get('name', '')
    uid = request.form.get('uid', '')
    if not sheet_name:
        return jsonify({'error': 'sheet_name is required'}), 400
    if not uid:
        return jsonify({'error': 'uid is required'}), 400

    wbj = GridJsWorkbook()
    try:

        output = io.BytesIO()
        with gzip.GzipFile(fileobj=output, mode='wb', compresslevel=9) as gzip_stream:
            wbj.lazy_loading_stream(gzip_stream, uid, sheet_name)

        response = Response(output.getvalue(), mimetype='application/json')
        response.headers['Content-Encoding'] = 'gzip'

        return response
    except Exception as e:
        return Response(str(e), status=500)

# get json info from : /GridJs2/DetailFileJsonWithUid?filename=&uid=
@app.route('/GridJs2/DetailFileJsonWithUid', methods=['GET'])
def detail_file_json_with_uid():
    filename = request.args.get('filename')
    uid = request.args.get('uid')
    if not filename:
        return jsonify({'error': 'filename is required'}), 400
    if not uid:
        return jsonify({'error': 'uid is required'}), 400
    gwb = GridJsWorkbook()
    file_path = os.path.join(FILE_DIRECTORY, filename)

    # check if the file exists
    if not os.path.isfile(file_path):
        return jsonify({'error': 'file not found:'+file_path}), 404
    try:
        sb = gwb.get_json_str_by_uid(uid, filename)
        if sb == None:
            gwb.import_excel_file(uid, file_path)
            sb = gwb.export_to_json(filename)
        # create a response object, passing in the response body, status code, headers, etc.
        response = Response(sb, status=200, mimetype='text/plain')

        # set the character encoding of the response to UTF-8 
        response.headers['Content-Type'] = 'text/plain; charset=utf-8'

        return response

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

# update action :/GridJs2/UpdateCell
@app.route('/GridJs2/UpdateCell', methods=['POST'])
def update_cell():
    # retrieve form data from the request
    p = request.form.get('p')
    uid = request.form.get('uid')

    # create an instance of GridJsWorkbook
    gwb = GridJsWorkbook()

    # call the UpdateCell method and get the result
    ret = gwb.update_cell(p, uid)

    # return a JSON response, as Flask defaults to returning JSON
    return Response(ret, content_type='text/plain; charset=utf-8')

# add image :/GridJs2/AddImage
@app.route('/GridJs2/AddImage', methods=['POST'])
def add_image():
    uid = request.form.get('uid')
    p = request.form.get('p')
    iscontrol = request.form.get('control')
    gwb = GridJsWorkbook()

    if iscontrol is None:
            if 'image' not in request.files:
            # no image upload

                ret = gwb.insert_image(uid, p, None, None)
                return jsonify(ret)

            else:
                file = request.files['image']

                if file.filename == '':
                    return jsonify(gwb.error_json("no file when add image"))
                else:
                    # image upload
                    try:
                    # call InsertImage  method and get the result
                        file_bytes = io.BytesIO(file.read())
                        print('file length  is:'+str(len(file_bytes.getvalue())))
                        ret = gwb.insert_image(uid, p, file_bytes, None)
                        return jsonify(ret)
                    except Exception as e:
                        return jsonify(gwb.error_json(str(e)))

    else:

        try:
            ret = gwb.insert_image(uid, p, None, None)
            return jsonify(ret)
        except Exception as e:
            return jsonify(gwb.error_json(str(e)))

# copy image :/GridJs2/CopyImage
@app.route('/GridJs2/CopyImage', methods=['POST'])
def copy_image():
    uid = request.form.get('uid')
    p = request.form.get('p')
    gwb = GridJsWorkbook()
    ret = gwb.copy_image_or_shape(uid,p)
    return jsonify(ret)

def get_stream_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # if fail,raise HTTPError
    return io.BytesIO(response.content)

# add image by image source url:/GridJs2/AddImageByURL
@app.route('/GridJs2/AddImageByURL', methods=['POST'])
def add_image_by_url():
    uid = request.form.get('uid')
    p = request.form.get('p')
    imageurl = request.form.get('imageurl')
    gwb = GridJsWorkbook()
    if imageurl is not None:
        try:
            stream = get_stream_from_url(imageurl)
            ret = gwb.insert_image(uid, p, stream, imageurl)
        except Exception as e:
            return jsonify(gwb.error_json(str(e)))

        return jsonify(ret)
    else:
        return jsonify(gwb.error_json('image url is null'))


# get image :/GridJs2/Image
@app.route('/GridJs2/Image', methods=['GET'])
def image():
    fileid = request.args.get('id')
    uid = request.args.get('uid')

    if fileid is None or uid is None:
        # if required parameters are missing, return an error response  
        return 'Missing required parameters', 400
    else:
        # retrieve the image stream  
        image_stream = GridJsWorkbook.get_image_stream(uid, fileid)

         # set the MIME type and attachment filename for the response (if needed)
        mimetype = 'image/png'
        attachment_filename = fileid

        #  send the file stream as the response  
        return send_file(
            image_stream,
            as_attachment=False,  # if sending as an attachment  
            download_name=attachment_filename,  # filename for download  
            mimetype=mimetype
        )


def guess_mime_type_from_filename(filename):
    # guess the MIME type based on the filename  
    mime_type, encoding = mimetypes.guess_type(filename)
    if mime_type is None:
        # if not found, return the default binary MIME type  
        mime_type = 'application/octet-stream'
    return mime_type


# get ole file: /GridJs2/Ole?uid=&id=
@app.route('/GridJs2/Ole', methods=['GET'])
def ole():
    oleid = request.args.get('id')
    uid = request.args.get('uid')
    sheet = request.args.get('sheet')
    gwb = GridJsWorkbook()
    filename = None
    filebyte = gwb.get_ole(uid, sheet, oleid, filename)
    if filename != None:

        # retrieve the image stream  
        ole_stream = io.BytesIO(filebyte)

    # set the MIME type and attachment filename for the response (if needed)
        mimetype = guess_mime_type_from_filename(filename)


    # send the file stream as the response 
        return send_file(
            ole_stream,
            as_attachment=True,  # if sending as an attachment  
            download_name=filename,  # filename for download
            mimetype=mimetype
        )
    else:
        # file not find
        abort(400, 'File not found')


# get batch zip image file url : /GridJs2/ImageUrl?uid=&id=
@app.route('/GridJs2/ImageUrl', methods=['GET'])
def image_url():
    id = request.args.get('id')
    uid = request.args.get('uid')
    file = uid + "." + id;
    return  jsonify("/GridJs2/GetZipFile?f="+ file)


# get zip file : /GridJs2/GetZipFile?f=
@app.route('/GridJs2/GetZipFile', methods=['GET'])
def get_zip_file():
    file = request.args.get('f')
    file_path = os.path.join(Config.file_cache_directory, file)
    # check if the file exists
    if os.path.isfile(file_path):
        # set the MIME type application/zip
        mimetype = 'application/zip'

        # use send_file to send a file as a response  
        # as_attachment=True Send the file as an attachment  ，download_name Specify the filename for download  
        return send_file(file_path, as_attachment=True, download_name=file, mimetype=mimetype)
    else:
        # If the file does not exist, return a 404 error  
        abort(404, description='File not found')


# get file: /GridJs2/GetFile?id=&filename=
@app.route('/GridJs2/GetFile', methods=['GET'])
def get_file():
    id = request.args.get('id')
    filename = request.args.get('filename')
    if filename != None:
        mimetype=guess_mime_type_from_filename(filename)
        file_path = os.path.join(Config.file_cache_directory, id.replace('/', '.')+"."+filename)
        # check if the file exists
        if os.path.isfile(file_path):
            # set the MIME type application/zip
            # use send_file to send a file as a response  
            # as_attachment=True Send the file as an attachment，download_name Specify the filename for download  
            return send_file(file_path, as_attachment=True, download_name=filename, mimetype=mimetype)
    else:
        abort(404, description='FileName is none')

# download file :/GridJs2/Download
@app.route('/GridJs2/Download', methods=['POST'])
def download():
    p = request.form.get('p')
    uid = request.form.get('uid')
    filename = request.form.get('file')
    gwb = GridJsWorkbook()

    try:
        gwb.merge_excel_file_from_json(uid, p)

        gwb.save_to_cache_with_file_name(uid, filename, None);

    except Exception as e:
        return jsonify(gwb.error_json(str(e)))
    if (Config.save_html_as_zip and filename.endswith(".html")):
        filename += ".zip";
    fileurl = "/GridJs2/GetFile?id=" + uid + "&filename=" + filename;
    return jsonify(fileurl)


def do_at_start(name):

    print(f'Hi, {name}  {FILE_DIRECTORY} ')


    # whether to load worksheets with lazy loading
    Config.set_lazy_loading(True)

    # do some init work for GridJS
    # set storage cache directory for GridJs
    Config.set_file_cache_directory(config.get('DEFAULT', 'CacheDir'))
    # set License for GridJs
    if os.path.exists(config.get('DEFAULT', 'LicenseFile')):
        Config.set_license(config.get('DEFAULT', 'LicenseFile'))
    # set Image route for GridJs,correspond with image()
    GridJsWorkbook.set_image_url_base("/GridJs2/Image")
    print(f'{Config.file_cache_directory}')



if __name__ == '__main__':
    do_at_start('hello gridjs')
    app.run(port=2022, host="0.0.0.0", debug=True)

