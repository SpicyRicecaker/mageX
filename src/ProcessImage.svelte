<script lang="ts">
  import { options } from './stores.js';
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');
  // Takes in an array of srcs and calls process on all of them
  export const processImageAll = async (
    rawArray: string[]
  ): Promise<string[]> => {
    let processed = [];
    for (let i = 0; i < rawArray.length; i++) {
      processed.push(await processImage(rawArray[i]));
    }
    return await processed;
  };

  // Takes in an image source, does some processing on it, and then returns the resulting image source
  export const processImage = async (raw: string): Promise<string> => {
    const rawImage = await createImage(raw);
    // Onload we can do canvas stuff
    // Set canvas width and height
    canvas.width = rawImage.naturalWidth;
    canvas.height = rawImage.naturalHeight;

    // Then draw the image
    ctx.drawImage(rawImage, 0, 0);
    // Get the image data
    let imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    // Add operations based off of what we want
    let queuedOps = [];
    Object.entries($options).forEach(([key, value]) => {
      if ($options[key] === true) {
        switch (key) {
          case 'binary': {
            queuedOps.push(binaryImage);
            break;
          }
          case 'invert': {
            queuedOps.push(invertImage);
            break;
          }
        }
      }
    });
    // Then loop through, modify and return image data
    imgData = await modifyImgData(imgData, queuedOps);
    // Draw onto canvas
    ctx.putImageData(imgData, 0, 0);
    // Append canvas 


    // Canvas to base64
    const dataURL = canvas.toDataURL();
    return dataURL;
  };

  const createImage = async (raw: string): Promise<HTMLImageElement> =>
    new Promise((resolve) => {
      // First we've gotta create the image so we can get its dimensions
      const rawImage = new Image();
      // rawImage.onload = async () => resolve(rawImage);
      rawImage.onload = () => {
        resolve(rawImage);
      };
      // Set the src to our base64 string
      rawImage.src = raw;
    });
  const binaryImage = async (imageData: ImageData) => {};

  const invertImage = async (imageData: ImageData) => {};

  const modifyImgData = async (
    imageData: ImageData,
    queuedOps
  ): Promise<ImageData> => {
    const tempImageData = imageData;
    console.log(tempImageData.data);
    for (let i = 0; i < tempImageData.data.length; i += 4) {}
    return await tempImageData;
  };
</script>

<!--<style lang="scss">
  canvas {
    display: none;
  }
</style>-->

<!-- <canvas id="canvas" /> -->
