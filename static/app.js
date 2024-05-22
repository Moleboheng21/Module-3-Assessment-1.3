function goToLandingPage1( ) {
    // Replace the URL "/landing-page" with the actual URL or route of the landing page
   window.location.href = "http://127.0.0.1:5000/add";
   }


   function goToLandingPage2( ) {
    // Replace the URL "/landing-page" with the actual URL or route of the landing page
   window.location.href = "http://127.0.0.1:5000/added";
   }
   function goToLandingPage3( ) {
    // Replace the URL "/landing-page" with the actual URL or route of the landing page
   window.location.href = "http://127.0.0.1:5000/added2";
}


document.addEventListener("DOMContentLoaded", function() {
    fetchNewsfeed();
  });
  
  function fetchNewsfeed() {
    // Replace the URL with your actual API endpoint for fetching recipe news
    fetch("https://api.example.com/recipe-news")
      .then(response => response.json())
      .then(data => {
        renderNewsfeed(data);
      })
      .catch(error => {
        console.error("Error fetching recipe news:", error);
      });
  }
  
  function renderNewsfeed(newsfeedData) {
    const newsfeedContainer = document.getElementById("newsfeed-container");
  
    newsfeedData.forEach(news => {
      const card = createNewsCard(news);
      newsfeedContainer.appendChild(card);
    });
  }
  
  function createNewsCard(news) {
    const card = document.createElement("div");
    card.classList.add("news-card");
  
    const title = document.createElement("h2");
    title.textContent = news.title;
    card.appendChild(title);
  
    const image = document.createElement("img");
    image.src = news.image;
    card.appendChild(image);
  
    const description = document.createElement("p");
    description.textContent = news.description;
    card.appendChild(description);
  
    const link = document.createElement("a");
    link.href = news.url;
    link.textContent = "Read more";
    card.appendChild(link);
  
    return card;
  }