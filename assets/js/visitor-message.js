(function () {
  'use strict';
  var form = document.getElementById('visitor-message-form');
  if (!form) return;
  var status = document.getElementById('visitor-message-status');
  var button = form.querySelector('button[type="submit"]');
  var mode = form.dataset.mode;
  var recipient = form.dataset.recipient;
  var endpoint = form.getAttribute('action');
  if (mode === 'formspree' && !/^https:\/\/formspree\.io\/f\/[a-z0-9]+$/i.test(endpoint)) return;
  form.hidden = false;

  form.addEventListener('submit', async function (event) {
    event.preventDefault();
    if (!form.reportValidity()) return;
    status.textContent = '';
    var data = new FormData(form);
    if (String(data.get('_gotcha') || '').trim()) return;
    var message = String(data.get('message') || '').trim();
    if (!message) {
      status.textContent = 'Please write a message before sending.';
      document.getElementById('visitor-body').focus();
      return;
    }

    if (mode === 'email') {
      var body = [
        'Name: ' + String(data.get('name') || '').trim(),
        'University / organisation: ' + String(data.get('affiliation') || '').trim(),
        'Reply email: ' + String(data.get('email') || '').trim(),
        '', message
      ].join('\r\n');
      var draft = 'mailto:' + recipient + '?subject=' + encodeURIComponent('Website visitor message — Yifan Tang') + '&body=' + encodeURIComponent(body);
      window.location.href = draft;
      status.textContent = 'Please send the draft in your email app. If it did not open, use the email link below. Your message has not been sent by this website.';
      return;
    }

    button.disabled = true;
    button.textContent = 'Sending…';
    status.textContent = 'Sending your message…';
    var controller = new AbortController();
    var timeout = setTimeout(function () { controller.abort(); }, 20000);
    try {
      var response = await fetch(endpoint, {
        method: 'POST', body: data,
        headers: { Accept: 'application/json' }, signal: controller.signal
      });
      if (!response.ok) throw new Error('Submission was not accepted');
      form.reset();
      status.textContent = 'Thank you. Your message has been submitted privately to Yifan Tang.';
    } catch (error) {
      status.textContent = 'We could not confirm delivery. Your text is still here; please try again or email me directly.';
    } finally {
      clearTimeout(timeout);
      button.disabled = false;
      button.textContent = 'Send message';
    }
  });
}());
