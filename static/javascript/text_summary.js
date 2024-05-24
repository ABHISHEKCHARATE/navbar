function toggleInput() {
    var inputType = document.getElementById("inputType").value;
    var pdfInput = document.getElementById("pdfInput");
    var textInput = document.getElementById("textInput");
    if (inputType === "pdf") {
        pdfInput.style.display = "block";
        textInput.style.display = "none";
    } else {
        pdfInput.style.display = "none";
        textInput.style.display = "block";
    }
}