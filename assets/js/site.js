// Main interactions live in the page layout. Keep reading content visible without JS.
document.querySelectorAll('.timeline-item').forEach(function(item){item.classList.add('in-view');});
