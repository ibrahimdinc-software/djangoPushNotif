// Register event listener for the 'push' event.
self.addEventListener('push', function (event) {
    // Retrieve the textual payload from event.data (a PushMessageData object).
    // Other formats are supported (ArrayBuffer, Blob, JSON), check out the documentation
    // on https://developer.mozilla.org/en-US/docs/Web/API/PushMessageData.
    const eventInfo = event.data.text();
    const data = JSON.parse(eventInfo);
    const head = data.head || 'Yeni Bildirim';
    const body = data.body || 'Burası bildirim içeriği ve sizin içeriğiniz dolu değil.';

    // Keep the service worker alive until the notification is created.
    event.waitUntil(
        self.registration.showNotification(head, {
            body: body,
            icon: data.icon,
            tag: 'renotify',
            renotify: true,
            data:{
                url: data.url
            }
        })
    );
});

self.addEventListener('notificationclick', function (event) {
    let url = event.notification.data.url || location.origin;
    console.log(event)
    event.notification.close(); // Android needs explicit close.
    event.waitUntil(
        clients.matchAll({
            type: 'window'
        }).then(windowClients => {
            // Check if there is already a window/tab open with the target URL
            for (var i = 0; i < windowClients.length; i++) {
                var client = windowClients[i];
                // If so, just focus it.
                if (client.url === url && 'focus' in client) {
                    return client.focus();
                }
            }
            // If not, then open the target URL in a new window/tab.
            if (clients.openWindow) {
                return clients.openWindow(url);
            }
        })
    );
});