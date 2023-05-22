const card = document.querySelectorAll(".media-content")
const cardContainer = document.querySelector('.card-container')

const LastCardVision = new IntersectionObserver(entries => {
    const lastCard = entries[0]
    console.log(entries[0])
    if (!lastCard.isIntersecting) return
    loadNewCard()
    LastCardVision.unobserve(lastCard.target)
    LastCardVision.observe(document.querySelector(".column:last-child"))
}, {})

LastCardVision.observe(document.querySelector(".column:last-child"))

function loadNewCard() {
    for (let i = 0; i<10; i++){
        const card_block = document.createElement('div')
        card_block.classList.add("column")
        card_block.classList.add('is-4')

        const card = document.createElement('div')
        card.classList.add('card')

        const card_content = document.createElement('div')
        card_content.classList.add('card-content')

        const card_media = document.createElement('div')
        card_media.classList.add('media-content')

        const p_price = document.createElement('p')
        p_price.classList.add('title')
        p_price.classList.add('is-3')
        p_price.textContent = 'test'

        const p_desc = document.createElement('p')
        p_desc.classList.add('subtitle')
        p_desc.classList.add('is-6')
        p_desc.textContent = "15$"
       
        card_media.append(p_price)
        card_media.append(p_desc)
        card_content.append(card_media)
        card.append(card_content)
        card_block.append(card)

        cardContainer.append(card_block)


    }
}