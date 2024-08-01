const fileForm = document.getElementById('file-form');
const fileInput = document.getElementById('file-input');
const uploadButton = document.getElementById('upload-button');
const fileList = document.getElementById('file-list');

fileForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const files = fileInput.files;
    const formData = new FormData();

    for (const file of files) {
        formData.append('files[]', file);
    }

    fetch('/upload', {
        method: 'POST',
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            fileList.innerHTML = '';
            data.files.forEach((file) => {
                const fileItem = document.createElement('div');
                fileItem.classList.add('file-item');
                fileItem.textContent = file.name;
                fileList.appendChild(fileItem);
            });
        })
        .catch((error) => console.error(error));
});