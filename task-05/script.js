class Header extends HTMLElement {
    connectedCallback() {
      this.innerHTML = `
      <header>
      <div class="logo">
          <a href="index.html" class="logo"><img src="assets/navbar/logo.png" alt="logo" width="30px"></a>   
      </div>
      <nav>
          <a href="https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q" target="_blank" class="social-link"><img src="assets/navbar/spotify.png" alt="spotify"></a>
          <a href="https://www.youtube.com/user/imaginedragons" target="_blank" class="social-link"><img src="assets/navbar/youtube.svg" alt="youtube"></a>
          <a href="https://twitter.com/Imaginedragons" target="_blank" class="social-link"><img src="assets/navbar/twitter.svg" alt="twitter"></a>
          <a href="https://www.instagram.com/imaginedragons/" target="_blank" class="social-link"><img src="assets/navbar/instagram.svg" alt="instagram"></a>
      </nav>
  </header>
      `;
    }
  }

  customElements.define('main-header', Header);