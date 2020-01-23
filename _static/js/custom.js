// The number of pixels the user must scroll by before the logo is hidden.
const scrollTopPixels = 40;

// Hide the navigation bar logo when scrolling down on desktop platforms.
// The logo is quite tall, so this helps make the rest of the navigation bar
// more readable.
function registerOnScrollEvent(mediaQuery) {
  // The navigation bar that contains the logo.
  const $navbar = $('.wy-side-scroll');

  // The anchor that contains the logo. This element will be hidden
  // (instead of hiding just the logo), otherwise, a small clickable area
  // would remain visible.
  const $logo = $('.wy-side-nav-search > a');

  if (mediaQuery.matches) {
    // We're on desktop; register the scroll event.
    $navbar.scroll(function() {
      if ($(this).scrollTop() >= scrollTopPixels) {
        $logo.hide();
      } else {
        $logo.show();
      }
    });
  } else {
    // We're on mobile; unregister the scroll event so the logo isn't hidden
    // when scrolling.
    $logo.show();
    $navbar.unbind('scroll');
  }
}

$(document).ready(() => {
  const mediaQuery = window.matchMedia('only screen and (min-width: 768px)');
  registerOnScrollEvent(mediaQuery);
  mediaQuery.addListener(registerOnScrollEvent);
});
