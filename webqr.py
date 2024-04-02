from tempfile import TemporaryFile

from flask import Flask, request
import qrcode


app = Flask(__name__)


@app.route("/qr/encode", methods=["GET"])
def qr_encode():
    data = request.args.get("data")

    kwargs = {}

    for arg_name in ["version", "error_correction", "box_size", "border"]:
        if arg_name in request.args:
            arg_value = request.args.get(arg_name, -1, type=int)
            if arg_value < 0:
                print(f"Invalid {arg_name}: {arg_value}")
            else:
                kwargs[arg_name] = arg_value

    qr = qrcode.QRCode(**kwargs)
    qr.add_data(data)
    img = qr.make_image(
        # fill_color="black",
        # back_color="white",
    )

    with TemporaryFile() as fp:
        img.save(fp, "PNG")
        fp.seek(0)
        imgdata = fp.read()
        return imgdata, 200, {"Content-Type": "image/png"}
