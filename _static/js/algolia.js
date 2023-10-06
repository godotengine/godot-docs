
(function() {

    var doc_version = document.querySelector('meta[name="doc_version"]').getAttribute('content');

    // If the current page uses tabs, we will need this small patch
    if (typeof(docsearch) == 'undefined') {
        docsearch = exports['docsearch'];
    }

    // Initialize the Algolia search widget
    docsearch({
        apiKey: 'c39cb614363a2a156811478bc2d0573b',
        indexName: 'godotengine',
        inputSelector: '#rtd-search-form input[type=text]',
        algoliaOptions: {
            facetFilters: ["version:" + (doc_version || 'stable')]
        },
    });

    window.addEventListener('keydown', function(event) {
        if (event.key === '/') {
            document.querySelector('#rtd-search-form input[type=text]').focus();
            event.preventDefault();
        }
    })
})();
