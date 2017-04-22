
function fancy_fmt(x) {
    console.log('will format', x);
    var size = 0;

    if (x > 1024 * 1024 * 1024)
        size = (Math.round(x * 100 / (1024 * 1024 * 1024)) / 100).toString() + 'GB';

    else if (x > 1024 * 1024)
        size = (Math.round(x * 100 / (1024 * 1024)) / 100).toString() + 'MB';

    else if (x > 1024)
        size = (Math.round(x * 100 / 1024) / 100).toString() + 'KB';

    else 
        size = x.toString() + 'B';

    console.log('formatted as', size);
    return size;
}


function file_selected(files_list) {
    console.log("files_list=", files_list);

    var file = files_list[0];

    if (file) {
        var raw_size = file.size;
        var size     = fancy_fmt(file.size);
        console.log('raw file size', raw_size, 'fancy file size', size);

        /* Reveal the block of file info */
        $('#file-info').css('display', 'block');

        console.log("file name", file.name);
        $('#fileName').text(file.name);
        //document.cookie = "name=" + file.name + "; path=/";

        $('#fileSize').text(size);

        console.log("file type", file.type);
        if (file.type) $("#fileType").text(file.type);
        else  $("#fileType").text('Type: application/octet-stream');

        $('#button_upload').prop('disabled', false);

        return true;

    } else {
        $('#file-info').css('display', 'none');
        $('#button_upload').prop('disabled', true);

        return false;
    }
}


function upload() {
    $('#button_upload').prop('disabled', true);
    $('#fakeFileSelect').hide();

    /* TODO: missing support for multiples
     *       files and directories
     * */
    uploadFile();
}


function uploadFile() {
    console.log('Normal upload');
    var file = document.getElementById('fileToUpload').files[0];

    /* Enable Progress bar */
    $("#progress-main").show();

    /* initialize a form from another */
    var fd = new FormData(document.getElementById('form1'));

    /* event listners */
    var xhr = new XMLHttpRequest();
    xhr.upload.addEventListener("progress", uploadProgress, false);
    xhr.addEventListener("load", uploadComplete, false);
    xhr.addEventListener("error", uploadFailed, false);
    xhr.addEventListener("abort", uploadCanceled, false);

    /* Configuring XHR */
    xhr.open("POST", "/upload", true);
    xhr.setRequestHeader("X-File-Name", file.name);
    xhr.setRequestHeader("X-File-Size", file.size);

    window.uploadStart = new Date();
    xhr.send(fd);
}


function uploadProgress(evt) {
    var file = document.getElementById('fileToUpload').files[0];

    if (evt.lengthComputable) {
        $('#loaded').text(fancy_fmt(evt.loaded));
        $('#total').text(fancy_fmt(file.size));

        /* Percents of progress XXX: use SWORD progress bar*/
        var percentComplete = Math.round(evt.loaded * 100 / evt.total);
        $("#progress-bar").attr('aria-valuenow', percentComplete);
        $("#progress-bar").css("width", (percentComplete.toString() + '%'));
        $("#progress-bar").html(percentComplete.toString() + '%');

        /* Time Remaining */
        var seconds_elapsed = (new Date().getTime() - window.uploadStart.getTime()) / 1000;
        if (seconds_elapsed >= 0)
            $("#elapsed").text(Math.round(seconds_elapsed) + 's');
        else
            $("#elapsed").text('0s');

        var bytes_per_second = seconds_elapsed ? evt.loaded / seconds_elapsed : 0;
        var Kbytes_per_second = bytes_per_second / 1000;
        if (Kbytes_per_second >= 0)
            $('#rate').text(Math.round(Kbytes_per_second) + 'KB/s'); 
        else
            $('#rate').text('0KB/s'); 

        var remaining_bytes = file.size - evt.loaded;
        var seconds_remaining = seconds_elapsed ? remaining_bytes / bytes_per_second : 'calculating';
        if (seconds_remaining >= 0)
            $("#estimated").text(Math.round(seconds_remaining) + 's');
        else
            $("#estimated").text('0s');

    } else {
        $("#progress-bar").html('unable to compute');
    }
}


function uploadComplete(evt) {
    /* This event is raised when the server send back a response */
    $('#results').html(evt.target.responseText);
}


function uploadFailed(evt) {
  console.debug("There was an error attempting to upload the file.");
}


function uploadCanceled(evt) {
  console.debug("The upload has been canceled by the user or the browser dropped the connection.");
}
