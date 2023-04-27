
async function loadUsers(query) {
    let x = await fetch(`/api/search/${query}/`);
    let accounts = JSON.parse(await x.text());
    let mainfeed = document.getElementById('main-feed')
    let loading = document.getElementById('loading')

    for (let i in accounts){
        let tweet = `
        <div class="actual-tweet">
            <span class="add-tweet-image">
                <a href="/user/${accounts[i].username}/"><img src="${accounts[i].profile_image}" class="rounded-circle profile-image" width="50px" height="50px" ></a>
            </span>
            <div class="tweet-content">
                <a href="/user/${accounts[i].username}/">${accounts[i].fullname} <span class="side-name">@${accounts[i].username}</span></a>
                <p class="tweet-text">${accounts[i].bio}</p>
            </div>
        </div>`
        mainfeed.innerHTML += tweet
    }

    loading.style.display = 'none'

}