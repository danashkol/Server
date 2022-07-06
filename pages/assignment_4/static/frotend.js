
function myFunction() {

     fetch('https://reqres.in/api/users?page=2').then(
         response => response.json()
     ).then(
         responseOBJECT => createUsersList(responseOBJECT.data)
     ).catch(
         err => console.log(err)
     );
}

function createUsersList(response){

    const currMain = document.querySelector("main")
    for (let user of response){
        console.log(user)
        const section = document.createElement('section')
        section.innerHTML = `
            <img src="${user.avatar}" alt="Profile Picture"/>
            <div>
             <span>${user.first_name} ${user.last_name}</span>
             <br>
             <a href="mailto:${user.email}">Send Email</a>
            </div>
        `
        currMain.appendChild(section)
    }

}
