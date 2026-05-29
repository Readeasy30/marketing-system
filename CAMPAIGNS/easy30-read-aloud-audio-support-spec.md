# Easy30 Read-Aloud Audio Support Spec

Last updated: 2026-05-29

## Purpose

Plan free read-aloud support for ReadEasy30 and optional audio support for MathEasy30.

The default approach should be lightweight, free, and compatible with a static GitHub and Cloudflare setup.

## Recommended default: browser Web Speech API

Use the browser's built-in speech synthesis for read-aloud help.

Why this fits:

- free
- no server needed
- no external audio dependency
- no API key
- fast to load
- works well with static HTML, CSS, and JavaScript

## ReadEasy30 read-aloud goals

- Let learners hear the story text.
- Use a slower calm pace.
- Give the learner a clear Stop button.
- Avoid autoplay.
- Avoid loud audio or surprise sound.
- Keep learner control visible.

## Basic read-aloud function concept

Use this only after reviewing the current ReadEasy30 `app.js` structure.

```javascript
function readAloud(textId) {
  window.speechSynthesis.cancel();

  const textElement = document.getElementById(textId);
  if (!textElement) return;

  const utterance = new SpeechSynthesisUtterance(textElement.innerText);
  utterance.rate = 0.85;
  utterance.pitch = 1.0;

  window.speechSynthesis.speak(utterance);
}
```

## Floating audio control concept

A floating Stop Audio button gives learners control when speech is active.

This is especially important for learners who may become overwhelmed by sound.

Production version should use external CSS and classes.

### Suggested HTML

```html
<div id="audio-control-float" class="audio-control-float" hidden>
  <span>📢 Bubbles is reading...</span>
  <button type="button" onclick="stopReadingAloud()">Stop</button>
</div>
```

### Suggested JavaScript

```javascript
function readAloud(textId) {
  window.speechSynthesis.cancel();

  const textElement = document.getElementById(textId);
  const audioControls = document.getElementById('audio-control-float');

  if (!textElement) return;

  const utterance = new SpeechSynthesisUtterance(textElement.innerText);
  utterance.rate = 0.85;
  utterance.pitch = 1.0;

  utterance.onstart = function () {
    if (audioControls) audioControls.hidden = false;
  };

  utterance.onend = function () {
    if (audioControls) audioControls.hidden = true;
  };

  utterance.onerror = function () {
    if (audioControls) audioControls.hidden = true;
  };

  window.speechSynthesis.speak(utterance);
}

function stopReadingAloud() {
  window.speechSynthesis.cancel();

  const audioControls = document.getElementById('audio-control-float');
  if (audioControls) audioControls.hidden = true;
}
```

### Suggested CSS

```css
.audio-control-float {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
  z-index: 1000;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.55rem 0.8rem;
  border: 2px solid #e2e8f0;
  border-radius: 999px;
  background: #ffffff;
  box-shadow: 0 0.25rem 0.8rem rgba(15, 23, 42, 0.12);
}

.audio-control-float span {
  color: #475569;
  font-size: 0.9rem;
  font-weight: 700;
}

.audio-control-float button {
  border: 0;
  border-radius: 999px;
  padding: 0.4rem 0.75rem;
  background: #dc2626;
  color: #ffffff;
  font-weight: 700;
}
```

## Optional future: pre-recorded Bubbles audio

Pre-recorded audio can be considered later for Bubbles.

Possible tools to review later:

- ElevenLabs free tier
- Microsoft Clipchamp text-to-speech

Rules before adding hosted audio files:

- keep file sizes small
- do not autoplay
- confirm commercial/license terms
- use simple filenames
- avoid adding many audio files before performance review

## Accessibility notes

- Do not rely on audio only.
- Keep all text visible.
- Make Stop button easy to tap.
- Avoid autoplay.
- Keep speech rate adjustable later if possible.
- Use clear button labels.

## Launch blocker

Before production, check browser behavior on:

- Chrome desktop
- Chrome mobile
- Safari/iPhone if possible
- Edge desktop

Speech voices vary by browser and device.
