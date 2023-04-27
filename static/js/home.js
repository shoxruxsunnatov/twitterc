let textarea = document.getElementById('textarea-control')
let tweetbtn = document.getElementById('tweet-btn')

setInterval(function() {
    textarea.rows = Math.ceil(textarea.value.length / 30)
}, 500)

async function loadTweets() {
    let x = await fetch('/api/home/');
    let tweets = JSON.parse(await x.text());
    let mainfeed = document.getElementById('main-feed')
    let loading = document.getElementById('loading')
    let now = new Date()

    for (let i in tweets){
        let tweetdate = new Date(tweets[i].date)
        let date;

        if (now.getDay() - tweetdate.getDay() > 0){
            date = now.getDay() - tweetdate.getDay() + 'd'
        } else if (now.getHours() - tweetdate.getHours() > 0){
            date = now.getHours() - tweetdate.getHours() + 'h'
        } else {
            date = now.getMinutes() - tweetdate.getMinutes() + 'm'
        }
        let tweet = `
        <div class="actual-tweet">
            <span class="add-tweet-image">
                <a href="/user/${tweets[i].account.username}/"><img src="${tweets[i].account.profile_image}" class="rounded-circle profile-image" width="50px" height="50px" ></a>
            </span>
            <div class="tweet-content">
                <a href="/user/${tweets[i].account.username}/">${tweets[i].account.fullname} <span class="side-name">@${tweets[i].account.username} · ${date}</span></a>
                <p class="tweet-text">${tweets[i].text}</p>
            </div>
        </div>`
        mainfeed.innerHTML += tweet
    }

    loading.style.display = 'none'

}
loadTweets()