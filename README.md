Sentence mining video games for audio and video is extremely easy. First use textractor to get text, the search text in dictionary to get definition. Get visuals from a screenshot, and audio from screen recorder.

The one problem I have right now is that some games cannot be hooked onto using textractor. Therefore, the following post is mostly about *getting the text from the game as efficiently as possible using image recognition*.

### imageX

- Probably does not require screenshot capabilities
  - Screenshot
    - Alt+PrtSc
    - ShareX
    - OBS
    - Shadowplay
  - Audio
    - ShareX
    - OSB
    - Shadowplay

#### Process
  - A static webpage (can be deployed to netlify)
  - Paste image from clipboard into browser
  - Load and Draw image onto canvas
  - Browser calls tesseract.js
    - NEED progress bar 100%%%%%%%%%%%%%%%. We can probably have the process emit their current event and listen to it from progress.svelte
  - For every textobject
    - store in array, onmousemove if it hits one of these objects then change color and expand rectangle (CSS ANIMATIONS BB), onmouseclick copy to clipboard
  - IT SOUNDS REALLY, REALLY FUN