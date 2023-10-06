const hamburger = document.querySelector("#hamburger")
const menu = document.querySelector("#menu")
const logo = document.querySelector("#logo")
const menuLinks = document.querySelectorAll("#menu-link")


document.querySelectorAll("#close-modal")[0].addEventListener("click", () => {
    document.querySelector("#modal").classList.toggle("hidden")
})


hamburger.addEventListener("click", () => {
    menu.classList.toggle("hidden")
    hamburger.classList.toggle("text-gray-200")
    logo.classList.toggle("text-blue-950")
    logo.classList.toggle("text-gray-200")
})

menuLinks.forEach((link) => {
    link.addEventListener("click", () => {
        menu.classList.toggle("hidden")
        hamburger.classList.toggle("text-gray-200")
        logo.classList.toggle("text-blue-950")
        logo.classList.toggle("text-gray-200")
    })
})

