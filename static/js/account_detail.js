
async function loadTweets(username) {
    let x = await fetch(`/api/user/${username}/`);
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
        let image = ''
        if (tweets[i].tweet_image){
            image = `<img src="${tweets[i].tweet_image}" width="100%" height="auto" class="tweet-image">`
        }

        let tweet = `
        <div class="actual-tweet">
            <span class="add-tweet-image">
                <a><img src="${tweets[i].account.profile_image}" class="rounded-circle profile-image" width="50px" height="50px" ></a>
            </span>
            <div class="tweet-content">
                <a>${tweets[i].account.fullname} <span class="side-name">@${tweets[i].account.username} · ${date}</span></a>
                <p class="tweet-text">${tweets[i].text}</p>
                ${image}
            </div>
        </div>`
        mainfeed.innerHTML += tweet
    }

    loading.style.display = 'none'

}
