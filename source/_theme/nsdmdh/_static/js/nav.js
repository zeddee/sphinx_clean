!function(){
// Dropdown event listener
const nav_dropdown_array = document.querySelectorAll('.has-dropdown')

const nav_toggle = (target)=>{
  const nav_event = (event)=>{
    if(event.type==='mouseenter'||event.type==='mouseleave'){
      if(target.classList.contains('is-active')){
        target.classList.remove('is-active')
      } else { target.classList.add('is-active')}
    }
  }
  // Check if hamburger is activated. If activated, then should not trigger menu dropdowns
  if(document.querySelector('.navbar-menu').classList.contains('is-active')){}else{
    target.addEventListener('mouseenter',nav_event)
    target.addEventListener('mouseleave',nav_event)
  }
}

nav_dropdown_array.forEach(nav_toggle)

// Hamburger menu event listener

const nav_burger = document.querySelectorAll('.navbar-burger')

nav_burger.forEach((burger)=>{
    const nav_event = (event)=>{
      const target = document.querySelector('.navbar-menu').classList
      if(event.type==='mousedown'){
        if(target.contains('is-active')){
          target.remove('is-active')
        } else { target.add('is-active')}
      }
    }
    burger.addEventListener('mousedown',nav_event)
})

}()
