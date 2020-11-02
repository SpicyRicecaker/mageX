<script lang="ts">
  // OCR component
  import { tesseractRecognize } from './Tesseract.svelte';
  // Are workers ready for new task, stored in store
  import { images, ocrdImages, processed, ready, work } from './stores';
  // The initial loading circle for Tesseract
  import Loader from './Loader.svelte';
  // Progress bar based off of worker progress (dispatched event progress)
  import Progress from './Progress.svelte';
  // [WIP] Our resulting bounding boxes from OCR
  import Square from './Square.svelte';
  // Takes in image and processes it for better OCR results
  import ProcessImage from './ProcessImage.svelte';
  // Debugs time it takes to complete func. First const start = beg(); then end(start, [message])
  import { fade, fly } from 'svelte/transition';
  // import { beg, end } from './Timing.svelte';

  // We bind this to process image because we need to access $store variables
  // context="module" makes it so that you can't access $store for some reason
  let processImageComponent;

  // Work responds to the worker progress being dispatched in './Tesseract.svelte'

  // The resulting hocr object from tesseract OCRing an image
  const handleImagePaste = async (e: ClipboardEvent) => {
    $ocrdImages = undefined;
    // Code inspired by https://www.techiedelight.com/paste-image-from-clipboard-using-javascript/
    // Get our clipboardImages as an array of blobs
    const raw = await getClipboardImageSources(e.clipboardData.items);
    // Convert them to images
    const tempImages = await loadNewImages(raw);
    if (tempImages.length > 0) {
      // Have to garbage collect the dataToBlobURL
      Promise.resolve().then(() => destroyBlobURLs($images));
      // We can update images with the link
      $images = tempImages;
      $processed = await processImageComponent.processImageAll(tempImages);
      // However, we want to preprocess the image if needed
      if ($processed.length === 0) {
        $ocrdImages = tesseractRecognize($images);
      } else {
        $ocrdImages = tesseractRecognize($processed);
      }
    }
  };

  const dataToBlobURL = (data: DataTransferItem): Promise<string> =>
    new Promise((resolve, reject) =>
      resolve(URL.createObjectURL(data.getAsFile()))
    );

  const destroyBlobURLs = async (blobURLs: string[]) => {
    const temp: Promise<void>[] = [];
    for (let i = 0; i < blobURLs.length; i++) {
      temp.push(destroyBlobURL(blobURLs[i]));
    }
    await Promise.all(temp);
  };

  const destroyBlobURL = async (blobURL: string) =>
    Promise.resolve(URL.revokeObjectURL(blobURL));

  // Takes in clipboard image sources and returns them as blob
  const getClipboardImageSources = async (
    clipboardImages: DataTransferItemList
  ): Promise<string[]> => {
    const tempImageSources: Promise<string>[] = [];
    for (let i = 0; i < clipboardImages.length; i++) {
      if (clipboardImages[i].type.match(/image/)) {
        tempImageSources.push(dataToBlobURL(clipboardImages[i]));
      }
    }
    return Promise.all(tempImageSources);
  };

  const loadNewImages = async (
    srcArr: string[]
  ): Promise<HTMLImageElement[]> => {
    // First define out
    const out: Promise<HTMLImageElement>[] = [];
    // Load all srces into array and promise.all of them
    for (let i = 0; i < srcArr.length; ++i) {
      out.push(loadNewImage(srcArr[i]));
    }
    return await Promise.all(out);
  };

  const loadNewImage = (src: string): Promise<HTMLImageElement> =>
    new Promise((resolve) => {
      const image = new Image();
      image.onload = () => resolve(image);
      image.src = src;
    });
</script>

<style lang="scss">
  main {
    width: 100%;
    height: 100%;
    position: relative;
    overflow: hidden;
  }

  .wrapper {
    background-color: aliceblue;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  // Absolutely cannot have display: flex on chrome
  // Maybe display block needed?
  .imageWrapper {
    // flex: 1;
    // display: flex;
    overflow: auto;
  }

  .bigwrapper {
    background-color: rgba(255, 255, 255, 0.5);
    position: absolute;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
</style>

<main on:paste={handleImagePaste}>
  {#if $ocrdImages}
    {#await $ocrdImages}
      {@debug $ocrdImages}
      <div class="bigwrapper" transition:fly={{ y: 500, duration: 2000 }}>
        <Progress bind:status={$work.status} bind:progress={$work.progress} />
      </div>
    {/await}
  {/if}
  <div class="wrapper">
    {#if !$ready}
      <Loader bind:message={$work.status} />
    {/if}
    {#each $images as image, i}
      <div class="imageWrapper" transition:fade|local>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          viewBox="0 0 {image.naturalWidth} {image.naturalHeight}">
          <image
            width={image.naturalWidth}
            height={image.naturalHeight}
            xlink:href={image.src} />
          {#if $ocrdImages}
            {#await $ocrdImages then ocrdImage}
              <!-- {@debug ocrdImage} -->
              <Square ocrdImage={ocrdImage[i]} />
            {/await}
          {/if}
        </svg>
      </div>
    {/each}
  </div>
  <ProcessImage bind:this={processImageComponent} />
</main>
