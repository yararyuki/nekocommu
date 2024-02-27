let selectForm = document.getElementById('selectForm');
const resultPoint = document.getElementById('resultPoint');
selectForm.elements[1].checked = true;
selectForm.addEventListener('change', valueChange);

function valueChange(event) {
    let checkValue = selectForm.elements['addPoint'].value;
    console.log(checkValue);
    resultPoint.innerHTML = checkValue;
}