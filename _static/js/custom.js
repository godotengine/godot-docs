// The number of pixels the user must scroll by before the logo is hidden.
const scrollTopPixels = 234;

// The margin to apply to the menu when the search bar is made fixed.
// Should roughly match the logo's height as to not hide the top menu items
// behind it.
const menuTopMargin = 90;
const menuHeightOffset_default = 338;
const menuHeightOffset_fixed = 102;
const menuHeightOffset_diff = (menuHeightOffset_default - menuHeightOffset_fixed);

// Hide the navigation bar logo when scrolling down on desktop platforms.
// The logo is quite tall, so this helps make the rest of the navigation bar
// more readable.
function registerOnScrollEvent(mediaQuery) {
  const $window = $(window);
  const $menu = $('.wy-menu-vertical');
  const $search = $('.wy-side-nav-search');

  if (mediaQuery.matches) {
    // We're on desktop; register the scroll event.
    const handleEarlyScroll = (currentScroll) => {
      $search.css('margin-top', `-${currentScroll}px`);
      $menu.css('margin-top', `${menuTopMargin + (scrollTopPixels - currentScroll)}px`);

      if (currentScroll > 0) {
        const scrolledPercent = (scrollTopPixels - currentScroll) / scrollTopPixels;
        const offsetValue = menuHeightOffset_fixed + menuHeightOffset_diff * scrolledPercent;
        $menu.css('max-height', `calc(100% - ${offsetValue}px)`);
      } else {
        $menu.css('max-height', `calc(100% - ${menuHeightOffset_default}px)`);
      }
    };

    $search.addClass('fixed');
    $window.scroll(function() {
      const currentScroll = window.scrollY;

      if (currentScroll >= scrollTopPixels) {
        $search.css('margin-top', `-${scrollTopPixels}px`);
        $menu.css('margin-top', `${menuTopMargin}px`);

        $menu.css('max-height', `calc(100% - ${menuHeightOffset_fixed}px)`);
      }
      else {
        handleEarlyScroll(currentScroll);
      }
    });

    $menu.scroll(function() {
      if ($(this).scrollTop() > 0) {
        $search.addClass('fixed-and-scrolled');
      } else {
        $search.removeClass('fixed-and-scrolled');
      }
    })

    handleEarlyScroll(window.scrollY);
  } else {
    // We're on mobile; unregister the scroll event so the logo isn't hidden
    // when scrolling and clean up any changed properties.
    $window.unbind('scroll');
    $search.removeClass('fixed');
    $search.css('margin-top', `0px`);
    $menu.css('margin-top', `0px`);
    $menu.css('max-height', 'initial');
  }
}

$(document).ready(() => {
  const mediaQuery = window.matchMedia('only screen and (min-width: 769px)');
  registerOnScrollEvent(mediaQuery);
  mediaQuery.addListener(registerOnScrollEvent);
});
