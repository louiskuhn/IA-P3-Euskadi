function upload_img() {
    var canvas = document.getElementById("canvas");
    var dataURL = canvas.toDataURL("image/png");
    document.getElementById('data').value = dataURL;
};