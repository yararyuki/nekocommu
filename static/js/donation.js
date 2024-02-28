let selectForm = document.getElementById('selectForm');
const resultPoint = document.getElementById('resultPoint');
selectForm.elements[1].checked = true;
selectForm.addEventListener('change', valueChange);

function valueChange(event) {
    let checkValue = selectForm.elements['addPoint'].value;
    console.log(checkValue);
    resultPoint.innerHTML = checkValue;
    document.getElementById( "hiddenText" ).value = checkValue ;
}



//モーダル表示
$(".modal-open").modaal({
    overlay_close: true,//モーダル背景クリック時に閉じるか
    before_open: function () {// モーダルが開く前に行う動作
        $('html').css('overflow-y', 'hidden');/*縦スクロールバーを出さない*/
    },
    after_close: function () {// モーダルが閉じた後に行う動作
        $('html').css('overflow-y', 'scroll');/*縦スクロールバーを出す*/
    }
});