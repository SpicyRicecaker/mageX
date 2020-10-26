<script lang="ts">
  import Tesseract, { tesseractRecognize } from './Tesseract.svelte';
  import { ready } from './stores.js';
  import Progress from './Progress.svelte';
  import Loader from './Loader.svelte';
  import Square from './Square.svelte';
  import Options from './Options.svelte';
  import ProcessImage from './ProcessImage.svelte';
  // DEBUG
  import { beg, end } from './Timing.svelte';
  let tim = 0;

  let processImageComponent;
  const work = {
    status: 'none',
    progress: 0,
  };

  let images: string[] = [];
  let ocrdImages: any;
  const handleImagePaste = async (e: ClipboardEvent) => {
    // Code inspired by https://www.techiedelight.com/paste-image-from-clipboard-using-javascript/
    tim = beg();
    // const raw = await Promise.resolve().then(
    //   async () => await getClipboardImageSources(e.clipboardData.items)
    // );
    const raw = await getClipboardImageSources(e.clipboardData.items);
    end(tim, 'get clipboard image sources');
    if (raw.length > 0) {
      // Have to garbage collect the dataToBlobURL
      Promise.resolve().then(() => destroyBlobURLs(images));
      // We can update images with the link
      tim = beg();
      images = await raw;
      end(tim, 'await raw');
      // However, we want to preprocess the image if needed
      tim = beg();
      // const processed = await processImageComponent.processImageAll(raw);
      // end(tim, 'process all images');
      // if (processed.length === 0) {
      //   tim = beg();
      //   ocrdImages = await tesseractRecognize(processed);
      //   end(tim, 'recog all images');
      // } else {
      //   tim = beg();
      //   ocrdImages = await tesseractRecognize(images);
      //   end(tim, 'recog all images');
      // }
    }
  };

  const dataToBlobURL = (data: DataTransferItem): Promise<string> =>
    new Promise((resolve, reject) =>
      resolve(URL.createObjectURL(data.getAsFile()))
    );

  // const dataToFile = (data: DataTransferItem): Promise<File> =>
  //   Promise.resolve(data.getAsFile());

  const destroyBlobURLs = async (blobURLs: string[]) => {
    const temp: Promise<void>[] = [];
    for (let i = 0; i < blobURLs.length; i++) {
      temp.push(destroyBlobURL(blobURLs[i]));
    }
    await Promise.all(temp);
  };

  const destroyBlobURL = async (blobURL: string) =>
    Promise.resolve(URL.revokeObjectURL(blobURL));

  const getClipboardImageSources = async (
    clipboardImages: DataTransferItemList
  ): Promise<string[]> => {
    const tempImageSources: Promise<string>[] = [];
    for (let i = 0; i < clipboardImages.length; i++) {
      if (clipboardImages[i].type.match(/image/)) {
        const b = clipboardImages[i];
        return [URL.createObjectURL(b.getAsFile())];
        // from clipboard format into file
        // const imageFile = await dataToFile(clipboardImages[i]);
        // form file into base 64 i think
        // const imageText = await fileToText(imageFile);
        const tim = beg();
        tempImageSources.push(
          // await fileToText(await dataToFile(clipboardImages[i]))
          dataToBlobURL(clipboardImages[i])
        );
        end(tim, 'convert to blob');
      }
    }
    return Promise.all(tempImageSources);
  };

  // const fileToText = (file: File): Promise<string> => {
  //   const reader = new FileReader();
  //   return new Promise((resolve, reject) => {
  //     reader.onerror = () => {
  //       reader.abort();
  //       reject('error gg ffs');
  //     };

  //     reader.onload = () => {
  //       resolve(reader.result as string);
  //     };
  //     reader.readAsDataURL(file);
  //   });
  // };

  // Prevent the default paste action, don't need for images i think
  // e.preventDefault();
</script>

<style lang="scss">
  main {
    max-width: 240px;
    width: 100%;
    height: 100%;
  }

  .wrapper {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #cacaca;
  }
  .image-actual {
    max-width: 100%;
    max-height: 100%;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>

<main on:paste={handleImagePaste}>
  <div class="wrapper">
    {#if !$ready}
      <Loader bind:message={work.status} />
    {/if}
    {#each images as image, i}
      <img class="image-actual" src={image} alt="pasted clipboard item {i}" />
      {#await ocrdImages}
        <Progress bind:status={work.status} bind:progress={work.progress} />
      {:then ocrdImage}
        <!-- <Square ocrdImage={ocrdImage[i]} /> -->
      {:catch error}
        <div>Decent{error}</div>
      {/await}
    {/each}
  </div>
  <Tesseract
    on:work={(event) => {
      work.status = event.detail.status;
      work.progress = event.detail.progress;
    }} />
</main>
<Options />
<ProcessImage bind:this={processImageComponent} />
