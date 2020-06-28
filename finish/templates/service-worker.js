const VERSION = '{{ version2 }}';
const staticCachePrefix = 'static';
const staticCacheName = `${staticCachePrefix}-${VERSION}`;
const dynamicCacheName = 'dynamic';


self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                console.log('[SW] Caching app shell');
                // All the pages supplied here will be set in the cache when the service worker installs.
                // If the service worker is updated, these pages will be updated in the cache.
                // So it can be a good idea to inject the version of the project in the template
                // to be sure the SW will be updated (and thus the pre-cached assets) when the project is.
                cache.addAll([
                    '/static/manifest.json',
                    '/',

                ]);
            }),
    );
});

self.addEventListener('fetch', (event) => {
    // Let the browser do its default thing
    // for non-GET requests. It's not safe to cache them anyway.
    if (event.request.method !== 'GET') {
        return;
    }

    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                // If we have the response in the cache, we return it.
                // If not, we try to fetch it.
                return response || fetch(event.request);
            }),
    );
});
