const IP = 'http://192.168.203.49:8000';
function serverCall(mode,data, url){
    let http = new XMLHttpRequest();
    http.onreadystatechange = function(){
        if(this.readyState == 4){
           return http.responseText;
        }
    }
    http.open(mode,url,true);
    http.send(JSON.stringify(data));
}
function getEmailAdrr() {
    let emails = new Set();
    const spans = document.querySelectorAll('.yP');
    for (let i = 0; i < spans.length; ++i) {
        emails.add(spans[i].getAttribute('email'));
    }
    return emails;
}
function markEmails(emailArr) {
    const spans = document.querySelectorAll('.yP');
    let item;
    for (let i = 0; i < spans.length; ++i) {
        if(emailArr.includes(spans[i].getAttribute('email'))){
            item = spans[i];
            while(item.tagName != 'TR'){
                item = item.parentElement;
            }
            item.style.backgroundColor = 'red';
        }
    }
}
function getEmailContent() {
    const list = document.getElementsByClassName('ii');
    let text = [];
    for (var i = 0; i < list.length; ++i) {
        text=[...text,list[i].innerText];
    }
    console.log(text.join('').replaceAll('\n',' '));
}
function createReportButton() {
    let button = document.createElement('button');
        button.innerText = '!';
        button.style.width = '40px';
        button.style.height = '40px';
        button.style.borderRadius = '50%';
        button.style.color = 'white';
        button.style.backgroundColor = 'red';
        button.style.marginLeft = '8px';
        button.style.fontSize = '24px';
        button.title = 'report email as scam!';
        button.id = 'eeeeeeeee';
        button.addEventListener('click', () => {
            const namecards = document.querySelectorAll('.ajn');
            const sender = namecards[namecards.length-1].getAttribute('jid');
            const content = getEmailContent();
            serverCall('POST',{"email":sender, "body": content}, IP + '/report/');
            window.alert('Email successfully reported!');
        });
    const items = document.getElementsByClassName('brC-bsf-aT5-aOt');
    items[items.length-1].insertAdjacentElement('beforeend',button);
}



async function main() {
    document.getElementById('eeeeeeeee')?.remove();
    const url = document.URL.split('/');
    if(url[url.length-1] === '#inbox') {
        markEmails(['no-reply@accounts.google.com','noreply@hackjunction.com']);
        const emails = serverCall('GET',{"emails": getEmailAdrr()}, IP + '/email-populate/');
        markEmails(emails);
    }else {
        const body = getEmailContent();
        createReportButton();
        const chance = serverCall('GET',{"body": body}, IP + '/getPrediction/')
        if(chance > 50) {
            window.alert(`\nThis email has a medium (${chance}%) chance of being malicious\n`);
        }else if(chance > 80) {
            window.alert(`\nThis email has a high (${chance}%) chance of being malicious\n`);
        }
    }
}



window.onload = () => {
    main();
}
window.addEventListener('popstate', function (event) {
	main();
});