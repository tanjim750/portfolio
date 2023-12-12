const domain = "http://127.0.0.1:8000";
function Sidebar(){

    const endpoint = "/get-sidebar"
    let name = document.querySelectorAll("span.name");
    let menus = document.querySelectorAll("ul.menus");
    let social = document.querySelectorAll("ul.social_links");
    let profile = document.querySelectorAll("div.profileImg");
    let logo = document.querySelector("img#logo");
    let copyright = document.querySelectorAll("p.copyrightText")

    $.getJSON(domain+endpoint)
    .done(function(response) {

        name.forEach(element => {
            element.innerHTML = `${response.name}<span class="back">${response.name}</span>`;
        });

        profile.forEach(element => {
            element.style.backgroundImage = "url(" + domain+response.profile + ")"
        });

        menus.forEach(element => {
            element.innerHTML = "";
            response.menus.forEach(menu => {
                element.innerHTML += '<li id='+menu.name+'><a href="'+menu.link+'">'+menu.name+'</a></li>';
            });
        });

        social.forEach(element => {
            console.log(response.social);
            element.innerHTML = "";
            response.social.forEach(s => {
                element.innerHTML += '<li><a href="'+s.link+'" target="_blank" ><img class="" src="'+domain+s.logo+'" alt /></a></li>';
            })
        });

        copyright.forEach(element => {
            element.textContent = response.copyright;
        });
    })
    .fail(function(jqXHR, textStatus, errorThrown) {
        console.error('Error:', textStatus, errorThrown);
    });
}

function Home(){
    const endpoint = "/get-home";

    let title = document.querySelector("div#hometitle");
    let subtitle = document.querySelector("div.subtitle");
    let image = document.querySelector("img#heroImg");
    let buttons = document.querySelector("div.buttons");
    let contact = document.querySelector("ul.contact-info");

    $.getJSON(domain+endpoint)
    .done(function(response) {
        let pages = document.querySelectorAll("li#Home");
        pages.forEach(page => {
            page.setAttribute("class", "current");
        });

        title.innerHTML = response.title;
        subtitle.innerHTML = response.subtitle;
        image.src = domain+response.image;

        buttons.innerHTML = "";
        response.buttons.forEach( element => {
            buttons.innerHTML += `
                <div class="elisc_tm_button">
                    <a class="anchor" href="${element.url}">${element.text}</a>
                </div>
            `
        });

        contact.innerHTML = "";
        response.contact.forEach( element => {
            contact.innerHTML += '<li><a href="#">'+element.contact+'</a></li>';
        });
    })
    .fail(function(jqXHR, textStatus, errorThrown) {
        console.error('Error:', errorThrown);
    });
}

function About(){
    const endpoint = "/get-about";

    let title = document.querySelector("div#about-title");
    let skills = document.querySelector("ul#skills");
    let description = document.querySelector("div#about-text");
    let buttons = document.querySelector("div.about-btn");
    let contact = document.querySelector("ul#about-info");

    $.getJSON(domain+endpoint)
    .done(function(response) {
        let pages = document.querySelectorAll("li#About");
        pages.forEach(page => {
            page.setAttribute("class", "current");
        });

        title.innerHTML = response.title;
        description.innerHTML = response.description;
        buttons.innerHTML = '<a class="anchor" href="'+response.btn_link+'">'+response.btn_text+'</a>';

        contact.innerHTML = "";
        response.contact.forEach( element => {
            contact.innerHTML += `<li>
            <span>${element.media}</span>
            <span><a class="href_location" href="">${element.contact}</a></span>
            </li>`;
        });

        skills.innerHTML = "";
        response.skills.forEach(element => {
            skills.innerHTML += `<li>
            <div class="list_inner">
            <div class="short">
            <div class="job">
            <span class="yellowColor">${element.date}</span>
            <h3>${element.field}</h3>
            </div>
            <div class="place">
            <span>${element.subtitle}</span>
            </div>
            </div>
            <div class="text">
            <p>${element.text}</p>
            </div>
            <span class="yellowColor">${element.skill}</span>
            </div>
            </li>`;
        })
    })
    .fail(function(jqXHR, textStatus, errorThrown) {
        console.error('Error:', errorThrown);
    });
}


Sidebar()
