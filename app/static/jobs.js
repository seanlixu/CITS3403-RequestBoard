function loadJobs(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            displayJobs(JSON.parse(this.responseText));
        }
    }
}

function displayJobs(response){
    const wrapper = document.createElement('div');
    let title = '';
    let content = '';
    let id ='';

    response.forEach(function(job){
        id = job.id;
        title = job.title;
        content = job.content;
        part = document.createElement('div');
        idSection = document.createElement('div');
        idSection.createTextNode(id);
        part.appendChild(idSection);
        titleSection = document.createElement('div');
        titleSection.createTextNode(title);
        part.appendChild(titlesection);
        contentSection = document.createElement('div');
        contentSection.createTextNode(content);
        part.appendChild(contentSection);
        wrapper.appendChild(part);
        console.log("added job : " + id);
    })

}
