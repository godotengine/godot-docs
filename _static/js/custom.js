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
    const $sidebar = $('.wy-side-scroll');
    const $search = $sidebar.children('.wy-side-nav-search');
    const $menu = $sidebar.children('.wy-menu-vertical');
    const $ethical = $sidebar.children('.ethical-rtd');

    // This padding is needed to correctly adjust the height of the scrollable area in the sidebar.
    // It has to have the same height as the ethical block, if there is one.
    let $menuPadding = $menu.children('.wy-menu-ethical-padding');
    if ($menuPadding.length == 0) {
      $menuPadding = $('<div class="wy-menu-ethical-padding"></div>');
      $menu.append($menuPadding);
    }

    if (mediaQuery.matches) {
      // Entering the "desktop" state.

      // The main scroll event handler.
      // Executed as the page is scrolled and once immediatelly as the page enters this state.
      const handleMainScroll = (currentScroll) => {
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

      // The sidebar scroll event handler.
      // Executed as the sidebar is scrolled as well as after the main scroll. This is needed
      // because the main scroll can affect the scrollable area of the sidebar.
      const handleSidebarScroll = () => {
        const menuElement = $menu.get(0);
        const menuScrollTop = $menu.scrollTop();
        const menuScrollBottom = menuElement.scrollHeight - (menuScrollTop + menuElement.offsetHeight);

        // As the navigation is scrolled we add a shadow to the top bar hanging over it.
        if (menuScrollTop > 0) {
          $search.addClass('fixed-and-scrolled');
        } else {
          $search.removeClass('fixed-and-scrolled');
        }

        // Near the bottom we start moving the sidebar banner into view.
        if (menuScrollBottom < ethicalOffsetBottom) {
          $ethical.css('display', 'block');
          $ethical.css('margin-top', `-${ethicalOffsetBottom - menuScrollBottom}px`);
        } else {
          $ethical.css('display', 'none');
          $ethical.css('margin-top', '0px');
        }
      };

      $search.addClass('fixed');
      $ethical.addClass('fixed');

      // Adjust the inner height of navigation so that the banner can be overlaid there later.
      const ethicalOffsetBottom = $ethical.height() || 0;
      if (ethicalOffsetBottom) {
        $menuPadding.css('height', `${ethicalOffsetBottom}px`);
      } else {
        $menuPadding.css('height', `0px`);
      }

      $window.scroll(function() {
        handleMainScroll(window.scrollY);
        handleSidebarScroll();
      });

      $menu.scroll(function() {
        handleSidebarScroll();
      })

      handleMainScroll(window.scrollY);
      handleSidebarScroll();
    } else {
      // Entering the "mobile" state.

      $window.unbind('scroll');
      $menu.unbind('scroll');

      $search.removeClass('fixed');
      $ethical.removeClass('fixed');

      $search.css('margin-top', `0px`);
      $menu.css('margin-top', `0px`);
      $menu.css('max-height', 'initial');
      $menuPadding.css('height', `0px`);
      $ethical.css('margin-top', '0px');
      $ethical.css('display', 'block');
    }
  };
})();

// Subscribe to DOM changes in the sidebar container, because there is a
// banner that gets added at a later point, that we might not catch otherwise.
const registerSidebarObserver = (function(){
  return function(callback) {
    const sidebarContainer = document.querySelector('.wy-side-scroll');

    let sidebarEthical = null;
    const registerEthicalObserver = () => {
      if (sidebarEthical) {
        // Do it only once.
        return;
      }

      sidebarEthical = sidebarContainer.querySelector('.ethical-rtd');
      if (!sidebarEthical) {
        // Do it only after we have the element there.
        return;
      }

      // This observer watches over the ethical block in sidebar, and all of its subtree.
      const ethicalObserverConfig = { childList: true, subtree: true };
      const ethicalObserverCallback = (mutationsList, observer) => {
        for (let mutation of mutationsList) {
          if (mutation.type !== 'childList') {
            continue;
          }

          callback();
        }
      };

      const ethicalObserver = new MutationObserver(ethicalObserverCallback);
      ethicalObserver.observe(sidebarEthical, ethicalObserverConfig);
    };
    registerEthicalObserver();

    // This observer watches over direct children of the main sidebar container.
    const observerConfig = { childList: true };
    const observerCallback = (mutationsList, observer) => {
      for (let mutation of mutationsList) {
        if (mutation.type !== 'childList') {
          continue;
        }

        callback();
        registerEthicalObserver();
      }
    };

    const observer = new MutationObserver(observerCallback);
    observer.observe(sidebarContainer, observerConfig);
  };
})();

$(document).ready(() => {
  const mediaQuery = window.matchMedia('only screen and (min-width: 769px)');

  registerOnScrollEvent(mediaQuery);
  mediaQuery.addListener(registerOnScrollEvent);

  registerSidebarObserver(() => {
    registerOnScrollEvent(mediaQuery);
  });

  // Load instant.page to prefetch pages upon hovering. This makes navigation feel
  // snappier. The script is dynamically appended as Read the Docs doesn't have
  // a way to add scripts with a "module" attribute.
  const instantPageScript = document.createElement('script');
  instantPageScript.toggleAttribute('module');
  /*! instant.page v3.0.0 - (C) 2019 Alexandre Dieulot - https://instant.page/license */
  instantPageScript.innerText = 'let t,e;const n=new Set,o=document.createElement("link"),s=o.relList&&o.relList.supports&&o.relList.supports("prefetch")&&window.IntersectionObserver&&"isIntersecting"in IntersectionObserverEntry.prototype,i="instantAllowQueryString"in document.body.dataset,r="instantAllowExternalLinks"in document.body.dataset,a="instantWhitelist"in document.body.dataset;let c=65,d=!1,l=!1,u=!1;if("instantIntensity"in document.body.dataset){const t=document.body.dataset.instantIntensity;if("mousedown"==t.substr(0,"mousedown".length))d=!0,"mousedown-only"==t&&(l=!0);else if("viewport"==t.substr(0,"viewport".length))navigator.connection&&(navigator.connection.saveData||navigator.connection.effectiveType.includes("2g"))||("viewport"==t?document.documentElement.clientWidth*document.documentElement.clientHeight<45e4&&(u=!0):"viewport-all"==t&&(u=!0));else{const e=parseInt(t);isNaN(e)||(c=e)}}if(s){const n={capture:!0,passive:!0};if(l||document.addEventListener("touchstart",function(t){e=performance.now();const n=t.target.closest("a");if(!f(n))return;h(n.href)},n),d?document.addEventListener("mousedown",function(t){const e=t.target.closest("a");if(!f(e))return;h(e.href)},n):document.addEventListener("mouseover",function(n){if(performance.now()-e<1100)return;const o=n.target.closest("a");if(!f(o))return;o.addEventListener("mouseout",m,{passive:!0}),t=setTimeout(()=>{h(o.href),t=void 0},c)},n),u){let t;(t=window.requestIdleCallback?t=>{requestIdleCallback(t,{timeout:1500})}:t=>{t()})(()=>{const t=new IntersectionObserver(e=>{e.forEach(e=>{if(e.isIntersecting){const n=e.target;t.unobserve(n),h(n.href)}})});document.querySelectorAll("a").forEach(e=>{f(e)&&t.observe(e)})})}}function m(e){e.relatedTarget&&e.target.closest("a")==e.relatedTarget.closest("a")||t&&(clearTimeout(t),t=void 0)}function f(t){if(t&&t.href&&(!a||"instant"in t.dataset)&&(r||t.origin==location.origin||"instant"in t.dataset)&&["http:","https:"].includes(t.protocol)&&("http:"!=t.protocol||"https:"!=location.protocol)&&(i||!t.search||"instant"in t.dataset)&&!(t.hash&&t.pathname+t.search==location.pathname+location.search||"noInstant"in t.dataset))return!0}function h(t){if(n.has(t))return;const e=document.createElement("link");e.rel="prefetch",e.href=t,document.head.appendChild(e),n.add(t)}';
  document.head.appendChild(instantPageScript);
});
