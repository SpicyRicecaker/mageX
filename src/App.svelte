<script lang="ts">
  import Tesseract, { tesseractRecognize } from './Tesseract.svelte';

  let images: string[] = [];
  const handleImagePaste = async (e: ClipboardEvent) => {
    // Code inspired by https://www.techiedelight.com/paste-image-from-clipboard-using-javascript/
    const t = await getClipboardImageSources(e.clipboardData.items);
    if (t.length > 0) {
      images = await t;
      await tesseractRecognize(images);
    }
  };

  const dataToFile = (data: DataTransferItem): Promise<File> =>
    Promise.resolve(data.getAsFile());

  const getClipboardImageSources = async (
    clipboardImages: DataTransferItemList
  ): Promise<string[]> => {
    const tempImageSources: string[] = [];
    for (let i = 0; i < clipboardImages.length; i++) {
      if (clipboardImages[i].type.match(/image/)) {
        tempImageSources.push(
          await fileToText(await dataToFile(clipboardImages[i]))
        );
      }
    }
    return tempImageSources;
  };

  const fileToText = (file: File): Promise<string> => {
    const reader = new FileReader();
    return new Promise((resolve, reject) => {
      reader.onerror = () => {
        reader.abort();
        reject('error gg ffs');
      };

      reader.onload = () => {
        resolve(reader.result as string);
      };
      reader.readAsDataURL(file);
    });
  };

  // Prevent the default paste action, don't need for images i think
  // e.preventDefault();
</script>

<style lang="scss">
  main {
    text-align: center;
    max-width: 240px;
    margin: 0 auto;
    width: 100%;
    height: 100%;
  }

  /* h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  } */

  .wrapper {
    width: 100%;
    height: 100%;
  }
  .container-image {
    flex: 1;
    background-color: #cacaca;
    width: 100%;
    height: 100%;
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
    <div class="container-image">
      {#each images as image, i}
        <img class="image-actual" src={image} alt="pasted clipboard item {i}" />
      {/each}
    </div>
  </div>
  <Tesseract />
</main>
