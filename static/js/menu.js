$(".openbtn").click(function () {//ボタンがクリックされたら
    $(this).toggleClass('active');//ボタン自身に activeクラスを付与し
    $("#g-nav").toggleClass('panelactive');//ナビゲーションにpanelactiveクラスを付与
});

$("#g-nav a").click(function () {//ナビゲーションのリンクがクリックされたら
    $(".openbtn").removeClass('active');//ボタンの activeクラスを除去し
    $("#g-nav").removeClass('panelactive');//ナビゲーションのpanelactiveクラスも除去
});


// 表示・非表示を切り替える要素を取得
const showPoint = document.getElementById("pointPop");
// 表示・非表示を切り替える関数
function switchDisplay01() {
    showPoint.classList.remove("p-none");
}
function switchDisplay02() {
    showPoint.classList.add("p-none");
}
// 上記関数を3秒後に実行
setTimeout(() => {
    switchDisplay01();
}, 700);
setTimeout(() => {
    switchDisplay02();
}, 3000);