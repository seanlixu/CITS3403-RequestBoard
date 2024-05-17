function loadJobs(){
    var xhttp = new XMLHttpRequest();

    // once the information required is obtained, and dectected call displayJobs
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            displayJobs(JSON.parse(this.responseText));
        }
    }
    //the URL must be the endpoint url for which the function that will call the python function for extracting job db information will be.
    xhttp.open("GET", "URL", true);
    xhttp.send();
}

// displayJobs is used to grab the extracted information, and create individual divs to store the job informations
function displayJobs(response){
    const wrapper = document.createElement('div');
    let title = '';
    let content = '';
    let id ='';
    
    // for each job, put all the information in a wrapper div (the outside of the card)
    response.forEach(function(job){
        id = job.id;
        title = job.title;
        content = job.content;

        part = document.createElement('div');

        idSection = document.createElement('div');
        idSection.appendChild(document.createTextNode(id));
        part.appendChild(idSection);

        titleSection = document.createElement('div');
        titleSection.appendChild(document.createTextNode(title));
        part.appendChild(titleSection);

        contentSection = document.createElement('div');
        contentSection.appendChild(document.createTextNode(content));
        part.appendChild(contentSection);

        wrapper.appendChild(part);
        console.log("added job : " + id);
    })
    
    // the dashboard html will have a div with id jobContent which would hold the wrapper div
    section = document.getElementById('jobContent');
    section.appendChild(wrapper);

}

document.getElementById("uploaded-jobs").addEventListener("click", function(){
    var button1 = document.createElement("a");
    button1.className = "nav-link active";

    var button2 = document.createElement("svg");
    button2.className = "bi pe-none me-2";
    button2.setAttribute("width", "16");
    button2.setAttribute("height", "16");

    var useElement = document.createElement("use");
    useElement.setAttribute("xlink:href", "#grid");
    button2.appendChild(useElement);

    var textNode = document.createTextNode("New Posting");
    button1.appendChild(textNode);

    button1.appendChild(button2);
    document.getElementById("index").appendChild(button1);
});