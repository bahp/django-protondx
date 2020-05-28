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
        readFile(file);
    }
}

// switch tabs when button is pressed
function openTab(evt, fileName) {
    let i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(fileName + '-tab').style.display = "block";
    document.getElementById(fileName + '-button').classList.add('active');
}
let uploadList = document.getElementById('upload-list');
let viewPanel = document.getElementById('view-content');

let FILE_COUNT = 0;

function readFile(file) {

    // create a new Div which contains a button/loading bar and file name
    let newDiv = document.createElement('div');
    let newBar = document.createElement('button');
    let file_name = file.name + '-(' + FILE_COUNT + ')';
    let content = document.createTextNode(file_name);
    newBar.classList.add('tablinks');
    newBar.id = file_name + '-button';
    newBar.appendChild(content);
    newDiv.appendChild(newBar);
    uploadList.appendChild( newDiv );
    FILE_COUNT += 1;
    // Open the file, exception if not .zip
    // Create a new tab linked to button in list
    // to display any relevant content
    const reader = new FileReader();
    reader.addEventListener('load', (event) => {
        newBar.addEventListener('click', function () {
            openTab(event, file_name);
        });

        const result = event.target.result;
        JSZipUtils.getBinaryContent(result, function(err, data) {
            if(err) {
                throw err; // or handle err
            }

            let zip = new JSZip();
            zip.loadAsync(data).then(function (contents) {
                let newTab = document.createElement('div');
                newTab.classList.add('tabcontent');
                newTab.id = file_name + '-tab';

                let list = document.createElement('ul');
                Object.keys(contents.files).forEach(function(filename) {
                    let item = document.createElement('li');
                    item.appendChild(document.createTextNode(filename));
                    list.appendChild(item);

                    if (filename.endsWith('.json')){
                        zip.file(filename).async("string").then(function (data) {
                            newTab.appendChild(document.createElement('hr'))
                            const jsonobj = JSON.parse(data);
                            const newDiv = document.createElement('div');

                            const count = parseInt($('#id_data-TOTAL_FORMS').attr('value'), 10);
                            const tmplMarkup = $('#upload-template').html();
                            const compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);

                            // update form count
                            $('#id_data-TOTAL_FORMS').attr('value', count+1);

                            newDiv.innerHTML = compiledTmpl;

                            const formFields = [
                                ["test_result","id_data-" + count + "-test_result"],
                                ["date_test",  "id_data-" + count + "-test_date"],
                                ["patient_first_name", "id_data-" + count + "-first_name"],
                                ["patient_last_name", "id_data-" + count + "-last_name"],
                                ["patient_gender", "id_data-" + count + "-gender"],
                                ["patient_dob", "id_data-" + count + "-dob"],
                                ["patient_postcode", "id_data-" + count + "-patient_postcode"],
                                ["testing_centre_type", "id_data-" + count + "-centre_type"],
                                ["testing_centre_long", "id_data-" + count + "-longitude"],
                                ["testing_centre_lat", "id_data-" + count + "-latitude"],
                            ]



                            newTab.appendChild(newDiv);
                            // ADD things to the TAB/JSON file HERE

                            // ...

                            formFields.forEach((fieldNames) => {
                                if (fieldNames[0] in jsonobj) {
                                    document.getElementById(fieldNames[1]).value = jsonobj[fieldNames[0]];
                                }
                            });

                        });
                    }

                });
                newTab.appendChild(list);

                // ADD things to the TAB HERE

                // ...


                newTab.style.display = "none";
                viewPanel.appendChild(newTab);
            }).catch(function (e) {
                console.log(e);
                alert("Please upload a file with a .zip extension");
                newBar.disabled = true;
            });
        });
    });

    // used to update progress bar inside buttons
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

