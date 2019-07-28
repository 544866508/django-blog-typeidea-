var is_md = document.getElementById("id_is_md");
function change_to_markdown_or_ckeditor() {
    if (is_md && is_md.type && is_md.type == "checkbox") {
        if (is_md.checked == true) {
            document.getElementById("div_id_content_ck").style.display = "none";
            document.getElementById("div_id_content_md").style.display = "block";
        } else {
            document.getElementById("div_id_content_ck").style.display = "block";
            document.getElementById("div_id_content_md").style.display = "none";
        }
    }
}
is_md.onclick = change_to_markdown_or_ckeditor;
window.onload = change_to_markdown_or_ckeditor;
