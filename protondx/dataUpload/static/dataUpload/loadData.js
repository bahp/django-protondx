let dropArea = document.getElementById('drop-area')

;['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false)
})

function preventDefaults (e) {
    e.preventDefault()
    e.stopPropagation()
}

;['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false)
})

;['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false)
})

function highlight(e) {
    dropArea.classList.add('highlight')
}

function unhighlight(e) {
    dropArea.classList.remove('highlight')
}


dropArea.addEventListener('drop', handleDrop, false)

function handleDrop(e) {
    let dt = e.dataTransfer
    let files = dt.files

    handleFiles(files)
}

function handleFiles(fileList) {
    for (const file of fileList) {
        const name = file.name ? file.name : 'NOT SUPPORTED';
        const type = file.type ? file.type : 'NOT SUPPORTED';
        const size = file.size ? file.size : 'NOT SUPPORTED';
        console.log({name, type, size});
        readFile(file);
    }
}


let uploadList = document.getElementById('upload-list');
let viewPanel = document.getElementById('view-panel');

function readFile(file) {
    const reader = new FileReader();
    let newDiv = document.createElement('div');
    uploadList.appendChild( newDiv );
    let newBar = document.createElement('button');
    let content = document.createTextNode(file.name)
    newBar.appendChild(content);
    newDiv.appendChild(newBar);


    newBar.addEventListener('click', function () {
        let content = document.createTextNode(file.name);
        viewPanel.appendChild(content);
    });

    reader.addEventListener('load', (event) => {
        const result = event.target.result;
        viewPanel.appendChild( document.createTextNode(result.toString()));
        JSZipUtils.getBinaryContent(result, function(err, data) {
            if(err) {
                throw err; // or handle err
            }

            JSZip.loadAsync(data).then(function (contents) {
                Object.keys(contents.files).forEach(function(filename) {
                    console.log(filename)
                });
            });
        });
        // Do something with result

    });


    reader.addEventListener('progress', (event) => {
        if (event.loaded && event.total) {
            const percent = (event.loaded / event.total) * 100;
            newBar.style.width = percent + '%';
            if (percent === 100){
                newBar.style.overflowX = 'auto';
            }
        }

    });

    reader.readAsDataURL(file);
}

