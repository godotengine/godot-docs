
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
  const scrollTopPixels = 84;
  // The target margin to be applied to the navigation bar when the logo is hidden.
  const menuTopMargin = 70;
  // The max-height offset when the logo is completely visible.
  const menuHeightOffset_default = 162;
  // The max-height offset when the logo is completely hidden.
  const menuHeightOffset_fixed = 80;
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
      // Executed as the page is scrolled and once immediately as the page enters this state.
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
      });

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

    // Default TOC tree has links that immediately navigate to the selected page. Our
    // theme adds an extra button to fold and unfold the tree without navigating away.
    // But that means that the buttons are added after the initial load, so we need to
    // improvise to detect clicks on these buttons.
    const scrollElement = document.querySelector('.wy-menu-vertical');
    const registerLinkHandler = (linkChildren) => {
      linkChildren.forEach(it => {
        if (it.nodeType === Node.ELEMENT_NODE && it.classList.contains('toctree-expand')) {
          it.addEventListener('click', () => {
            // Toggling a different item will close the currently opened one,
            // which may shift the clicked item out of the view. We correct for that.
            const menuItem = it.parentNode;
            const baseScrollOffset = scrollElement.scrollTop + scrollElement.offsetTop;
            const maxScrollOffset = baseScrollOffset + scrollElement.offsetHeight;

            if (menuItem.offsetTop < baseScrollOffset || menuItem.offsetTop > maxScrollOffset) {
              menuItem.scrollIntoView();
            }

            callback();
          });
        }
      });
    }

    const navigationSections = document.querySelectorAll('.wy-menu-vertical ul');
    navigationSections.forEach(it => {
      if (it.previousSibling == null || typeof it.previousSibling === 'undefined' || it.previousSibling.tagName != 'A') {
        return;
      }

      const navigationLink = it.previousSibling;
      registerLinkHandler(navigationLink.childNodes);

      const linkObserverConfig = { childList: true };
      const linkObserverCallback = (mutationsList, observer) => {
        for (let mutation of mutationsList) {
          registerLinkHandler(mutation.addedNodes);
        }
      };

      const linkObserver = new MutationObserver(linkObserverCallback);
      linkObserver.observe(navigationLink, linkObserverConfig);
    });
  };
})();

/**
 * Registers Giscus if there's an #godot-giscus container.
 * @returns {void} Nothing.
 */
const registerGiscus = function () {
  const giscusContainer = document.getElementById("godot-giscus");
  if (giscusContainer == null) {
    return;
  }

  const removeGiscusContainer = function() {
    giscusContainer.remove();
  };

  const pageNameMetaElement = Array.from(document.head.querySelectorAll("meta")).find((meta) => meta.name === "doc_pagename");
  if (pageNameMetaElement == null) {
    removeGiscusContainer();
    return;
  }

  const pageNameDenyList = [
    "search"
  ];
  if (pageNameDenyList.includes(pageNameMetaElement.content)) {
    removeGiscusContainer();
    return;
  }

  // Use https://giscus.app/ to regenerate the script tag if needed.
  // data-term is set to be language-independent and version-independent, so that comments can be centralized for each page.
  // This increases the likelihood that users will encounter comments on less frequently visited pages.
  const scriptElement = document.createElement("script");
  scriptElement.src = "https://giscus.app/client.js";
  scriptElement.crossOrigin = "anonymous";
  scriptElement.async = true;

  const dataset = {
    repo: "godotengine/godot-docs-user-notes",
    repoId: "R_kgDOKuNx0w",
    category: "User-contributed notes",
    categoryId: "DIC_kwDOKuNx084CbANb",
    mapping: "specific",
    term: pageNameMetaElement.content,
    strict: "1",
    reactionsEnabled: "0",
    emitMetadata: "0",
    inputPosition: "bottom",
    theme: "preferred_color_scheme",
    lang: "en",
    loading: "lazy",
  };

  for (const [key, value] of Object.entries(dataset)) {
    scriptElement.dataset[key] = value;
  }

  giscusContainer.append(scriptElement);
};

$(document).ready(() => {
  // Remove the search match highlights from the page, and adjust the URL in the
  // navigation history.
  const url = new URL(location.href);
  if (url.searchParams.has('highlight')) {
    Documentation.hideSearchWords();
  }

  window.addEventListener('keydown', function(event) {
    if (event.key === '/') {
        var searchField = document.querySelector('#rtd-search-form input[type=text]');
        if (document.activeElement !== searchField) {
            searchField.focus();
            searchField.select();
            event.preventDefault();
        }
    }
  });

  // Initialize handlers for page scrolling and our custom sidebar.
  const mediaQuery = window.matchMedia('only screen and (min-width: 769px)');

  registerOnScrollEvent(mediaQuery);
  mediaQuery.addListener(registerOnScrollEvent);

  registerSidebarObserver(() => {
    registerOnScrollEvent(mediaQuery);
  });

  // Add line-break suggestions to the sidebar navigation items in the class reference section.
  //
  // Some class reference pages have very long PascalCase names, such as
  //    VisualShaderNodeCurveXYZTexture
  // Those create issues for our layout, as we can neither make them wrap with CSS without
  // breaking normal article titles, nor is it good to have them overflow their containers.
  // So we use a <wbr> tag to insert mid-word suggestions for appropriate splits, so the browser
  // knows that it's okay to split it like
  //    Visual Shader Node Curve XYZTexture
  // and add a new line at an opportune moment.
  const classReferenceLinks = document.querySelectorAll('.wy-menu-vertical > ul:last-of-type .reference.internal');
  for (const linkItem of classReferenceLinks) {
    let textNode = null;
    linkItem.childNodes.forEach(it => {
      if (it.nodeType === Node.TEXT_NODE) {
        // If this is a text node and if it needs to be updated, store a reference.
        let text = it.textContent;
        if (!(text.includes(" ") || text.length < 10)) {
          textNode = it;
        }
      }
    });

    if (textNode != null) {
        let text = textNode.textContent;
        // Add suggested line-breaks and replace the original text.
        // The regex looks for a lowercase letter followed by a number or an uppercase
        // letter. We avoid splitting at the last character in the name, though.
        text = text.replace(/([a-z])([A-Z0-9](?!$))/gm, '$1<wbr>$2');

        linkItem.removeChild(textNode);
        linkItem.insertAdjacentHTML('beforeend', text);
    }
  }

  // Change indentation from spaces to tabs for codeblocks.
  const codeBlocks = document.querySelectorAll('.rst-content div[class^="highlight"] pre');
  for (const codeBlock of codeBlocks) {
    const classList = codeBlock.parentNode.parentNode.classList;
    if (!classList.contains('highlight-gdscript') && !classList.contains('highlight-cpp')) {
      // Only change indentation for GDScript and C++.
      continue;
    }
    let html = codeBlock.innerHTML.replace(/^(<span class="w">)?( {4})/gm, '\t');
    let html_old = "";
    while (html != html_old) {
      html_old = html;
      html = html.replace(/\t( {4})/gm, '\t\t')
    }
    codeBlock.innerHTML = html;
  }

  // See `godot_is_latest` in conf.py
  const isLatest = document.querySelector('meta[name=doc_is_latest]').content.toLowerCase() === 'true';
  if (isLatest) {
    // Add a compatibility notice using JavaScript so it doesn't end up in the
    // automatically generated `meta description` tag.

    const baseUrl = [location.protocol, '//', location.host, location.pathname].join('');
    // These lines only work as expected in the production environment, can't test this locally.
    const fallbackUrl = baseUrl.replace('/latest/', '/stable/');
    const homeUrl = baseUrl.split('/latest/')[0] + '/stable/';
    const searchUrl = homeUrl + 'search.html?q=';

    const noticeLink = document.querySelector('.latest-notice-link');

    // Insert a placeholder to display as we're making a request.
    noticeLink.innerHTML = `
    Checking the <a class="reference" href="${homeUrl}">stable version</a>
    of the documentation...
    `;

    // Make a HEAD request to the possible stable URL to check if the page exists.
    fetch(fallbackUrl, { method: 'HEAD' })
      .then((res) => {
        // We only check the HTTP status, which should tell us if the link is valid or not.
        if (res.status === 200) {
          noticeLink.innerHTML = `
          See the <a class="reference" href="${fallbackUrl}">stable version</a>
          of this documentation page instead.
          `;
        } else {
          // Err, just to fallthrough to catch.
          throw Error('Bad request');
        }
      })
      .catch((err) => {
        let message = `
        This page does not exist in the <a class="reference" href="${homeUrl}">stable version</a>
        of the documentation.
        `;

        // Also suggest a search query using the page's title. It should work with translations as well.
        // Note that we can't use the title tag as it has a permanent suffix. OG title doesn't, though.
        const titleMeta = document.querySelector('meta[property="og:title"]');
        if (typeof titleMeta !== 'undefined') {
          const pageTitle = titleMeta.getAttribute('content');
          message += `
          You can try searching for "<a class="reference" href="${searchUrl + encodeURIComponent(pageTitle)}">${pageTitle}</a>" instead.
          `;
        }

        noticeLink.innerHTML = message;
      });
  }

  // Load instant.page to prefetch pages upon hovering. This makes navigation feel
  // snappier. The script is dynamically appended as Read the Docs doesn't have
  // a way to add scripts with a "module" attribute.
  const instantPageScript = document.createElement('script');
  instantPageScript.toggleAttribute('module');
  /*! instant.page v5.1.0 - (C) 2019-2020 Alexandre Dieulot - https://instant.page/license */
  instantPageScript.innerText = 'let t,e;const n=new Set,o=document.createElement("link"),i=o.relList&&o.relList.supports&&o.relList.supports("prefetch")&&window.IntersectionObserver&&"isIntersecting"in IntersectionObserverEntry.prototype,s="instantAllowQueryString"in document.body.dataset,a="instantAllowExternalLinks"in document.body.dataset,r="instantWhitelist"in document.body.dataset,c="instantMousedownShortcut"in document.body.dataset,d=1111;let l=65,u=!1,f=!1,m=!1;if("instantIntensity"in document.body.dataset){const t=document.body.dataset.instantIntensity;if("mousedown"==t.substr(0,"mousedown".length))u=!0,"mousedown-only"==t&&(f=!0);else if("viewport"==t.substr(0,"viewport".length))navigator.connection&&(navigator.connection.saveData||navigator.connection.effectiveType&&navigator.connection.effectiveType.includes("2g"))||("viewport"==t?document.documentElement.clientWidth*document.documentElement.clientHeight<45e4&&(m=!0):"viewport-all"==t&&(m=!0));else{const e=parseInt(t);isNaN(e)||(l=e)}}if(i){const n={capture:!0,passive:!0};if(f||document.addEventListener("touchstart",function(t){e=performance.now();const n=t.target.closest("a");if(!h(n))return;v(n.href)},n),u?c||document.addEventListener("mousedown",function(t){const e=t.target.closest("a");if(!h(e))return;v(e.href)},n):document.addEventListener("mouseover",function(n){if(performance.now()-e<d)return;const o=n.target.closest("a");if(!h(o))return;o.addEventListener("mouseout",p,{passive:!0}),t=setTimeout(()=>{v(o.href),t=void 0},l)},n),c&&document.addEventListener("mousedown",function(t){if(performance.now()-e<d)return;const n=t.target.closest("a");if(t.which>1||t.metaKey||t.ctrlKey)return;if(!n)return;n.addEventListener("click",function(t){1337!=t.detail&&t.preventDefault()},{capture:!0,passive:!1,once:!0});const o=new MouseEvent("click",{view:window,bubbles:!0,cancelable:!1,detail:1337});n.dispatchEvent(o)},n),m){let t;(t=window.requestIdleCallback?t=>{requestIdleCallback(t,{timeout:1500})}:t=>{t()})(()=>{const t=new IntersectionObserver(e=>{e.forEach(e=>{if(e.isIntersecting){const n=e.target;t.unobserve(n),v(n.href)}})});document.querySelectorAll("a").forEach(e=>{h(e)&&t.observe(e)})})}}function p(e){e.relatedTarget&&e.target.closest("a")==e.relatedTarget.closest("a")||t&&(clearTimeout(t),t=void 0)}function h(t){if(t&&t.href&&(!r||"instant"in t.dataset)&&(a||t.origin==location.origin||"instant"in t.dataset)&&["http:","https:"].includes(t.protocol)&&("http:"!=t.protocol||"https:"!=location.protocol)&&(s||!t.search||"instant"in t.dataset)&&!(t.hash&&t.pathname+t.search==location.pathname+location.search||"noInstant"in t.dataset))return!0}function v(t){if(n.has(t))return;const e=document.createElement("link");e.rel="prefetch",e.href=t,document.head.appendChild(e),n.add(t)}';
  document.head.appendChild(instantPageScript);

  // Make sections in the sidebar togglable.
  let hasCurrent = false;
  let menuHeaders = document.querySelectorAll('.wy-menu-vertical .caption[role=heading]');
  menuHeaders.forEach(it => {
      let connectedMenu = it.nextElementSibling;

      // Enable toggling.
      it.addEventListener('click', () => {
          if (connectedMenu.classList.contains('active')) {
            connectedMenu.classList.remove('active');
            it.classList.remove('active');
          } else {
            connectedMenu.classList.add('active');
            it.classList.add('active');
          }

          // Hide other sections.
          menuHeaders.forEach(ot => {
            if (ot !== it && ot.classList.contains('active')) {
              ot.nextElementSibling.classList.remove('active');
              ot.classList.remove('active');
            }
          });

          registerOnScrollEvent(mediaQuery);
      }, true);

      // Set the default state, expand our current section.
      if (connectedMenu.classList.contains('current')) {
        connectedMenu.classList.add('active');
        it.classList.add('active');

        hasCurrent = true;
      }
  });

  // Unfold the first (general information) section on the home page.
  if (!hasCurrent && menuHeaders.length > 0) {
    menuHeaders[0].classList.add('active');
    menuHeaders[0].nextElementSibling.classList.add('active');

    registerOnScrollEvent(mediaQuery);
  }

  // Giscus
  registerGiscus();
});

// Override the default implementation from doctools.js to avoid this behavior.
Documentation.highlightSearchWords = function() {
  // Nope.
}

// ========
// Tutorial
// ========
const TUTORIAL_VIEW_DYNAMIC_MIN_SIZE = 1036;
const TUTORIAL_VIEW_TYPE_LOCAL_STORAGE_KEY = "tutorialViewType";
const TUTORIAL_VIEW_TYPE_CHANGE_EVENT = "godottutorialviewchange";

const TutorialToggleLabelI18n = Object.freeze({
  "en": "Dynamic view"
});

const TutorialViewType = Object.freeze({
  STATIC: "STATIC",
  DYNAMIC: "DYNAMIC"
});

const TutorialStepType = Object.freeze({
  COMPOUND: "COMPOUND",
  COMMENT: "COMMENT"
});

/** @type {() => (typeof TutorialViewType)[keyof typeof TutorialViewType]} */
function getTutorialViewType() {
  const localStorageType = localStorage.getItem(TUTORIAL_VIEW_TYPE_LOCAL_STORAGE_KEY);
  if (localStorageType === "STATIC") {
    return "STATIC";
  }

  return window.innerWidth < TUTORIAL_VIEW_DYNAMIC_MIN_SIZE
    ? "STATIC"
    : "DYNAMIC";
}

function getTutorialToggleLabel() {
  let documentLang = document.documentElement.lang ?? "en";
  let label = TutorialToggleLabelI18n[documentLang];
  if (label != null) {
    return label;
  }

  // Check if the lang is in the `xx-XX` format.
  if (documentLang.charAt(2) !== "-") {
    // Let's return the default value.
    return TutorialToggleLabelI18n.en;
  }

  label = TutorialToggleLabelI18n[documentLang.substring(0, 1)];
  if (label != null) {
    return label;
  }

  return TutorialToggleLabelI18n.en;
}

let nextTutorialId = 0;

/** @type {(tutorial: HTMLDivElement) => void} */
function setupTutorial(tutorial) {
  let tutorialId = nextTutorialId;
  nextTutorialId++;

  tutorial.classList.remove("tutorial");
  tutorial.classList.add("tutorial-js");

  /**
   * Boolean set each screen refresh to know if the screen has been resized.
   */
  let resized = false;

  /**
   * Current view type
   * @type {(typeof TutorialViewType)[keyof typeof TutorialViewType]}
   */
  let currentViewType;

  /** @type {Array<HTMLElement>} */
  const tutorialChildren = Array.from(tutorial.children);
  /**
   * @typedef {{ type: (typeof TutorialStepType)[keyof typeof TutorialStepType], index: number }} StepBase
   * @typedef {StepBase & { type: "COMPOUND", title: HTMLDivElement, description: HTMLDivElement, content: HTMLDivElement }} StepAdmonition
   * @typedef {StepBase & { type: "COMMENT", comment: HTMLDivElement }} StepComment
   */
  const steps = tutorialChildren.map((step, index) => {
    const type = step.classList.contains("admonition")
      ? "ADMONITION"
      : "COMMENT";

    /** @type {StepComment | StepAdmonition} */
    let returnVal;

    switch (type) {
      case "COMMENT": {
        const comment = document.createElement("div");
        comment.append(...Array.from(step.children));
        /** @type {StepComment} */
        returnVal = {
          type,
          index,
          comment
        };
      } break;

      case "ADMONITION": {
        const title = step.querySelector(".admonition-title");
        if (title == null) throw new Error("error while parsing step: title is null");
        title.classList.add("step-title");
        title.remove();

        const content = step.querySelector(".step-content");
        if (content == null) throw new Error("error while parsing step: content is null");
        content.remove();

        const description = document.createElement("div");
        description.classList.add("step-description");
        description.append(...Array.from(step.children))

        const context = step.query
        /** @type {StepAdmonition} */
        returnVal = {
          type,
          index,
          title,
          description,
          content
        };
      } break;
    }

    return returnVal;
  });

  // Intersection observer
  /** @type {Map<HTMLElement, IntersectionObserverEntry>} */
  const observedEntries = new Map();
  /** @type {HTMLDivElement | null} */
  let activeEntry = null;

  /** @type {IntersectionObserverInit} */
  const observerOptions = {
    root: null,
  };
  /** @type {IntersectionObserverCallback} */
  const observerCallback = (entries, observer) => {
    for (const entry of entries) {
      if (observedEntries.has(entry.target)) {
        observedEntries.delete(entry.target);
      }
      if (entry.isIntersecting) {
        observedEntries.set(entry.target, entry);
      }
    }
  };

  const observer = new IntersectionObserver(observerCallback, observerOptions);

  /**
   * Toggle that handles the static/dynamic style.
   */
  const toggle = document.createElement("input");
  {
    /** @type {(typeof TutorialViewType)[keyof typeof TutorialViewType] | null} */
    let localStorageValue = localStorage.getItem(TUTORIAL_VIEW_TYPE_LOCAL_STORAGE_KEY);
    if (localStorageValue == null) {
      localStorageValue = TutorialViewType.DYNAMIC;
      localStorage.setItem(TUTORIAL_VIEW_TYPE_LOCAL_STORAGE_KEY, localStorageValue);
    }

    toggle.id = `godot-tutorial-${tutorialId}`;
    toggle.type = "checkbox";
    toggle.checked = localStorageValue === "DYNAMIC";
    toggle.addEventListener("change", () => {
      if (toggle.checked) {
        currentViewType = TutorialViewType.DYNAMIC;
      } else {
        currentViewType = TutorialViewType.STATIC;
      }

      localStorage.setItem(TUTORIAL_VIEW_TYPE_LOCAL_STORAGE_KEY, currentViewType);
      window.dispatchEvent(new CustomEvent(TUTORIAL_VIEW_TYPE_CHANGE_EVENT, { detail: { viewType: currentViewType, source: tutorial } }));
      onViewTypeChange();

      toggle.scrollIntoView({ behavior: "smooth", block: "center", inline: "nearest" });
    });
  }

  /** @type {(entry: HTMLDivElement) => void} */
  const switchEntry = (entry) => {
    if (entry === activeEntry || entry == null || currentViewType !== "DYNAMIC") {
      return;
    }

    if (activeEntry !== null) {
      activeEntry.classList.remove("active");
    }
    entry.classList.add("active");
    activeEntry = entry;

    // Let's activate the correct display content.
    const entryIndex = entry.dataset["stepIndex"];
    const displayContainerSteps = tutorial.querySelectorAll(".display-container .step-admonition-content");
    for (const displayContainerStep of Array.from(displayContainerSteps)) {
      if (displayContainerStep.dataset["stepIndex"] === entryIndex) {
        displayContainerStep.classList.add("active");
      } else {
        displayContainerStep.classList.remove("active");
      }
    }
  };

  /** @type {FrameRequestCallback} */
  const animationFrameRequest = (_time) => {
    window.requestAnimationFrame(animationFrameRequest);

    if (resized) {
      handleResize();
      resized = false;
    }

    if (observedEntries.size === 0) {
      return;
    }

    /** @type {Array<{ entry: IntersectionObserverEntry, distance: number }>} */
    let entries = [];
    const clientHeight = document.documentElement.clientHeight;
    const clientHeightQuarter = clientHeight / 4;
    for (const [target, entry] of Array.from(observedEntries)) {
      const entryCenter = (entry.target.getBoundingClientRect().bottom + entry.target.getBoundingClientRect().top) / 2;
      const entryDistance = Math.abs(entryCenter - clientHeightQuarter);
      entries.push({ entry, distance: entryDistance });
    }
    entries = entries.sort((a, b) => {
      return a.distance - b.distance;
    });

    if (entries.length > 0) {
      const firstEntry = entries[0];
      switchEntry(firstEntry.entry.target);
    } else {
      switchEntry(null);
    }
  };
  window.requestAnimationFrame(animationFrameRequest);

  window.addEventListener("resize", () => {
    resized = true;
  });

  const handleResize = () => {
    const oldViewType = currentViewType;
    currentViewType = getTutorialViewType();
    if (oldViewType !== currentViewType) {
      onViewTypeChange();
    }
  };

  const onViewTypeChange = () => {
    toggle.checked = currentViewType === "DYNAMIC";

    // Rebuild the layout.
    clearLayout();

    switch (currentViewType) {
      case "STATIC": {
        buildStaticLayout(steps);
      } break;

      case "DYNAMIC": {
        buildDynamicLayout(steps);
      } break;
    }
  };

  const clearLayout = () => {
    for (const child of Array.from(tutorial.children)) {
      tutorial.removeChild(child);
    }

    tutorial.classList.remove("static");
    tutorial.classList.remove("dynamic");
    observer.disconnect();
    observedEntries.clear();

    buildToggleContainer();
  };

  const buildToggleContainer = () => {
    const toggleContainer = document.createElement("div");
    toggleContainer.classList.add("toggle-container");

    const label = document.createElement("label");
    label.htmlFor = toggle.id;
    label.innerText = getTutorialToggleLabel();

    toggleContainer.append(label, toggle);
    tutorial.append(toggleContainer);
  };

  const buildStaticLayout = () => {
    tutorial.classList.add("static");

    for (const step of steps) {
      const stepContainer = document.createElement("div");
      stepContainer.classList.add("step-container");

      switch (step.type) {
        case "COMMENT": {
          stepContainer.classList.add("step-comment");
          stepContainer.append(step.comment);
        } break;

        case "ADMONITION": {
          stepContainer.classList.add("step-admonition");

          const stepTextContainer = document.createElement("div");
          stepTextContainer.classList.add("step-admonition-box");
          stepTextContainer.append(step.title, step.description);
          stepContainer.append(stepTextContainer);

          const stepContentContainer = document.createElement("div");
          stepContentContainer.classList.add("step-admonition-content");
          stepContentContainer.append(step.content);
          stepContainer.append(stepContentContainer);

          // Resets the "scrolled" tag, as there's no scroll anymore.
          /** @type {HTMLDivElement[]} */
          const scrollableAreas = stepContentContainer.querySelectorAll("div[class^='highlight-'] .highlight");
          for (const scrollableArea of scrollableAreas) {
            delete scrollableArea.dataset["scrolled"];
          }
        } break;
      }

      tutorial.append(stepContainer);
    }
  };

  const buildDynamicLayout = () => {
    tutorial.classList.add("dynamic");

    const topContainer = document.createElement("div");
    topContainer.classList.add("top-container");

    const stepsContainer = document.createElement("div");
    stepsContainer.classList.add("steps-container");

    const bottomContainer = document.createElement("div");
    bottomContainer.classList.add("bottom-container");

    const displayContainer = document.createElement("div");
    displayContainer.classList.add("display-container");

    const displaySticky = document.createElement("div");
    displaySticky.classList.add("display-sticky");
    displayContainer.append(displaySticky);

    for (const step of steps) {
      const stepContainer = document.createElement("div");
      stepContainer.classList.add("step-container");
      stepContainer.dataset["stepIndex"] = step.index;

      switch (step.type) {
        case "COMMENT": {
          stepContainer.classList.add("step-comment");
          stepContainer.append(step.comment);
        } break;

        case "ADMONITION": {
          stepContainer.classList.add("step-admonition");

          const stepTextContainer = document.createElement("div");
          stepTextContainer.classList.add("step-admonition-box");
          stepTextContainer.append(step.title, step.description);
          stepContainer.append(stepTextContainer);

          // Instead of adding "step-admonition-content" to the `stepContainer`
          // (which is being added in `stepsContainer`), let's put it in
          // `displayContainer` instead.
          const stepContentContainer = document.createElement("div");
          stepContentContainer.classList.add("step-admonition-content");
          stepContentContainer.dataset["stepIndex"] = step.index;
          stepContentContainer.append(step.content);
          displaySticky.append(stepContentContainer);

          // Scroll to the mean of the highlighted lines.
          requestAnimationFrame(() => {
            /** @type {HTMLDivElement | null} */
            const scrollContainer = stepContentContainer.querySelector("div[class^='highlight-']");
            if (scrollContainer == null) {
              return;
            }

            /** @type {HTMLDivElement | null} */
            const scrollableArea = scrollContainer.querySelector(".highlight");
            if (scrollableArea == null) {
              throw new Error("scrollableArea is null");
            }

            // Return early if the container has been already "scrolled".
            if (scrollableArea.dataset["scrolled"] != null) {
              return;
            }
            scrollableArea.dataset["scrolled"] = "scrolled";

            // If the browser has remembered the scroll before a refresh, the `scrollTop`
            // value will not be 0.
            // @TODO: Fix (if possible) the bug where the browser remembers that the
            //        scroll was at 0. Currently, we just ignore it and reset the scroll
            //        to the mean.
            if (scrollableArea.scrollTop !== 0) {
              return;
            }

            const { top: scrollableTop, height: scrollableHeight } = scrollableArea.getBoundingClientRect();

            /** @type {[smallest: number, highest: number]} */
            let positions = [0, 0];
            /** @type {HTMLDivElement | null} */
            const codeTab = stepContentContainer.querySelector(".sphinx-tabs");

            if (codeTab == null) {
              return;
            }

            /** @type {HTMLSpanElement[]} */
            const highlightedLines = Array.from(codeTab.querySelectorAll(".highlight .hll"));
            if (highlightedLines.length === 0) {
              return;
            }

            for (const highlightedLine of highlightedLines) {
              const { top, height } = highlightedLine.getBoundingClientRect();
              positions = [
                Math.min(positions[0], top),
                Math.max(positions[1], top + height)
              ];
            }

            const mean = (positions[0] + positions[1]) / 2;
            const targetScrollTop = Math.max((mean - scrollableTop) + (scrollContainer.clientHeight / 2), scrollableHeight);
            scrollableArea.scrollTo({ top: targetScrollTop });
          });

          // Only observe "COMPOUND" steps.
          observer.observe(stepContainer);
        } break;
      }

      stepsContainer.append(stepContainer);
    }

    tutorial.append(topContainer, stepsContainer, bottomContainer, displayContainer);
  };

  /** @type {(event: CustomEvent) => void} */
  const tutorialViewTypeChangeEventListener = (event) => {
    const {
      viewType,
      source
    } = event.detail;

    if (source === tutorial) {
      return;
    }

    const oldViewType = currentViewType;
    currentViewType = viewType;

    if (oldViewType !== currentViewType) {
      onViewTypeChange();
    }
  };
  window.addEventListener(TUTORIAL_VIEW_TYPE_CHANGE_EVENT, tutorialViewTypeChangeEventListener);

  // Initialize the display.
  handleResize();
}

document.addEventListener("DOMContentLoaded", () => {
  /** @type {NodeListOf<HTMLDivElement>} */
  const tutorials = document.querySelectorAll(".tutorial");
  for (const tutorial of Array.from(tutorials)) {
    setupTutorial(tutorial);
  }
});
