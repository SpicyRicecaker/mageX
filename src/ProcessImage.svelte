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
      if ($options[key].isActive === true) {
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
    // Append canvas DEBUGGGGGGGGGGGGGGGGG
    document.body.appendChild(canvas);

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

  interface pixelProcessor

  const binaryImage = async (pixel: number[]): Promise<number[]> => {};

  const invertImage = async (pixel: number[]): Promise<number[]> => {};

  const modifyImgData = async (
    imageData: ImageData,
    queuedOps: 
  ): Promise<ImageData> => {
    let ops = queuedOps.length;
    console.log(imageData.data);
    // Loop through all pixels (R,G,B,A)
    for (let i = 0; i < imageData.data.length; i += 4) {
      // Loop through all required tasks
      for (let j = 0; j < ops; ++j) {
        // Set pixels equal to the result of the operations
        [imageData[i], imageData[i+1], imageData[i+2]] = queuedOps[j]();
      }
    }
    return imageData;
  };
</script>

<!--<style lang="scss">
  canvas {
    display: none;
  }
</style>-->

<!-- <canvas id="canvas" /> -->
