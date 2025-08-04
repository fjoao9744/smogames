document.querySelector("#points__options").onclick = () => {
    document.querySelector(".header-buttons__small-screen").classList.add("active")
  }
  
  document.querySelector(".small-close__button").onclick = () => {
    document.querySelector(".header-buttons__small-screen").classList.remove("active")
  }