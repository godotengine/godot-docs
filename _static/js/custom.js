// Handle page scroll and adjust sidebar accordingly.

// Each page has two scrolls: the main scroll, which is moving the content of the page;
// and the sidebar scroll, which is moving the navigation in the sidebar.
// We want the logo to gradually disappear as the main content is scrolled, giving
// more room to the navigation on the left. This means adjusting the height
// available to the navigation on the fly. There is also a banner below the navigation
// that must be dealt with simultaneously.
const registerOnScrollEvent = (function(){
  // Configuration.

  // The number of pixels the user must scroll by before the logo is completely hidden.
  const scrollTopPixels = 234;
  // The target margin to be applied to the navigation bar when the logo is hidden.
  const menuTopMargin = 90;
  // The max-height offset when the logo is completely visible.
  const menuHeightOffset_default = 338;
  // The max-height offset when the logo is completely hidden.
  const menuHeightOffset_fixed = 102;
  // The distance between the two max-height offset values above; used for intermediate values.
  const menuHeightOffset_diff = (menuHeightOffset_default - menuHeightOffset_fixed);

  // Media query handler.
  return function(mediaQuery) {
    // We only apply this logic to the "desktop" resolution (defined by a media query at the bottom).
    // This handler is executed when the result of the query evaluation changes, which means that 
    // the page has moved between "desktop" and "mobile" states.

    // When entering the "desktop" state, we register scroll events and adjust elements on the page.
    // When entering the "mobile" state, we clean up any registered events and restore elements on the page
    // to their initial state.

    const $window = $(window);
    const $menu = $('.wy-menu-vertical');
    const $search = $('.wy-side-nav-search');
    const $ethical = $('.ethical-rtd');

    if (mediaQuery.matches) {
      // Entering the "desktop" state.

      // The scroll event handler.
      // Executed as the page is scrolled and once immediatelly as the page enters this state.
      const handleScroll = (currentScroll) => {
        if (currentScroll >= scrollTopPixels) {
          // After the page is scrolled below the threshold, we fix everything in place.
          $search.css('margin-top', `-${scrollTopPixels}px`);
          $menu.css('margin-top', `${menuTopMargin}px`);
          $menu.css('max-height', `calc(100% - ${menuHeightOffset_fixed}px)`);
        }
        else {
          // Between the top of the page and the threshold we calculate intermediate values 
          // to guarantee a smooth transition.
          $search.css('margin-top', `-${currentScroll}px`);
          $menu.css('margin-top', `${menuTopMargin + (scrollTopPixels - currentScroll)}px`);

          if (currentScroll > 0) {
            const scrolledPercent = (scrollTopPixels - currentScroll) / scrollTopPixels;
            const offsetValue = menuHeightOffset_fixed + menuHeightOffset_diff * scrolledPercent;
            $menu.css('max-height', `calc(100% - ${offsetValue}px)`);
          } else {
            $menu.css('max-height', `calc(100% - ${menuHeightOffset_default}px)`);
          }
        }
      };

      $search.addClass('fixed');
      $ethical.addClass('fixed');

      // Adjust the inner height of navigation so that the banner can be overlaid there later.
      const ethicalOffsetBottom = $ethical.height() || 0;
      if (ethicalOffsetBottom) {
        $menu.css('padding-bottom', `${ethicalOffsetBottom}px`);
      } else {
        $menu.css('padding-bottom', `0px`);
      }

      $window.scroll(function() {
        handleScroll(window.scrollY);
      });

      $menu.scroll(function() {
        const menuScrollTop = $(this).scrollTop();
        const menuScrollBottom = this.scrollHeight - (menuScrollTop + this.offsetHeight);

        // As the navigation is scrolled we add a shadow to the top bar hanging over it.
        if (menuScrollTop > 0) {
          $search.addClass('fixed-and-scrolled');
        } else {
          $search.removeClass('fixed-and-scrolled');
        }

        // Near the bottom we start moving the sidebar banner into view.
        if (menuScrollBottom < ethicalOffsetBottom) {
          $ethical.css('margin-top', `-${ethicalOffsetBottom - menuScrollBottom}px`);
        } else {
          $ethical.css('margin-top', '0px');
        }
      })

      handleScroll(window.scrollY);
    } else {
      // Entering the "mobile" state.

      $window.unbind('scroll');
      $menu.unbind('scroll');

      $search.removeClass('fixed');
      $ethical.removeClass('fixed');

      $search.css('margin-top', `0px`);
      $menu.css('margin-top', `0px`);
      $menu.css('padding-bottom', `0px`);
      $menu.css('max-height', 'initial');
      $ethical.css('margin-top', '0px');
    }
  }
})();

$(document).ready(() => {
  const mediaQuery = window.matchMedia('only screen and (min-width: 769px)');
  registerOnScrollEvent(mediaQuery);
  mediaQuery.addListener(registerOnScrollEvent);
});
