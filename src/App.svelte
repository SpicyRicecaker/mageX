<script lang="ts">
  let pastedImageSrc = '';
  const handleImagePaste = (e: ClipboardEvent) => {
    // Code inspired by https://www.techiedelight.com/paste-image-from-clipboard-using-javascript/

    // Focus on first item in the clipboard
    const item = e.clipboardData.items[0];
    console.log(item);

    // Then determine if the image is on top?
    switch (item.type.split('/')[0]) {
      case 'text': {
        console.log('text');
        // Get the blob of the image
        // const blob = await item.getAsFile();
        // console.log(await blob, '123');
        break;
      }
      case 'image': {
        console.log('image');
        // Get the blob of the image
        const blob = item.getAsFile();
        const reader = new FileReader();
        reader.onload = (e) => {
          pastedImageSrc = e.target.result as string;
        };
        reader.readAsDataURL(blob);
        break;
      }
      default: {
        console.log('you pasted not an image lol');
        break;
      }
    }
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

  #image-actual {
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
      <img
        id="image-actual"
        src={pastedImageSrc}
        alt="your-pasted-stuff-here" />
    </div>
  </div>
</main>
