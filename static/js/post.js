let selectForm = document.getElementById('selectForm');
selectForm.elements[1].checked = true;

function valueChange(event) {
    let checkValue = selectForm.elements['tag_name'].value;
    console.log(checkValue);
}
function previewImage(obj) {
    var fileReader = new FileReader();
    fileReader.onload = (function () {
        document.getElementById('preview').src = fileReader.result;
    });
    fileReader.readAsDataURL(obj.files[0]);
}