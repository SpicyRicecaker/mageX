# mageX

Now live at (prompurr.org)[prompurr.org]!

## why?

Sentence mining video games for audio and video is extremely easy. First use textractor to hook text and copy, then search said text in dictionary to get definition. Get visuals from a screenshot, and audio from a screen recorder.

However, issues arise when some game cannot be hooked onto using textractor. Therefore, mageX aims to *get the text from the game as efficiently as possible using image recognition*.

## current usage
  - [x] go to prompurr.org
  - [ ] upload image
    - [x] paste from clipboard
    - [ ] browse file
    - [ ] drag file
  - [x] change image processing settings 
    - [x] if text is white, must select corresponding option
  - [ ] select desired block of text in image and enjoy!

## new features
- [ ] fix new image not uploading after image is already there
- [ ] mobile first options UI
  - navbar with ||| menu on top
    - OCR
    - Processing
  - when processing, overlay canvas on top of current image, then have a tap menu on the bottom (similar to the navbar) to change options
- [ ] text bounding boxes

## implementation
- !!For options UI
  - Move Nav.svelte over from Lampest
  - If view of Nav is processing (in processImage)
    - Overlay canvas on top of other pic
      - Make sure to edit dimensions using css
      - While await canvas have loading
    - Create Bot.svelte
      - Nav except position is bottom
      - Contains all image options
      - Upon any modification, show three buttons
        - Reprocess image (golden)
          - Shifts view back into OCR (with fade in transition)
          - Calls translate function again on the canvas
        - Cancel all changes (x, red)
        - Persist changes (purple cookies, lights up if different from current)
    - Canvas is live edit, reacts to any user change
- !For main 
  - If past pref cookies is modified
    - Load ProcessImage.svelte canvas
    - ALWAYS Process based off of that 
- Bounding boxes
  - #Option 1
    - Draw image onto canvas
    - For textbox in textboxes
      - ctx.drawRect
      - onMouseMove
        - for(all textboxes)
          - if mouse.x > textboxes.left && mouse.x < textboxes.right
          - && mouse.y > textboxes.bot && mouse.y < textboxes.top
          - ctx.writeText(textboxes.text)
    - Pros
      - Relatively easy to implement
      - Will easily scale up and down with canvas
    - Cons
      - Will have to image with canvas
  - #Option 2
    - Draw rects onto SVG BBBBBBBBBBB
    - SVGs ARE OP WTF
    - CAN DRAW DOM ELEMENTS STRAIGHT ONTO CANVAS WITH SPECIFIC DIMENSIONS, INCLUDING IMAGES AND RECTS
    - CLEARLY THE WINNER HERE
    - Ok actual implementation
      - Slight refactoring of existing OCR to have image enclosed in svg
      - $$$$Profit
      - Ok actual actual implementation
        - Watch video on svg html5
        <!-- - Probably need to make an image component actuaylly. 
        - inside svg, under image, call squares -->
