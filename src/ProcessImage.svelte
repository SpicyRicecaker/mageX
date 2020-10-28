<script lang="ts">
  import { options } from './stores.js';
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');
  // Takes in an array of srcs and calls process on all of them
  export const processImageAll = async (
    rawArray: HTMLImageElement[]
  ): Promise<HTMLImageElement[]> => {
    // Add operations based off of what we want
    let queuedOps: pixelProcessor[] = [];
    Object.entries($options).forEach(([key, value]) => {
      if (value.isActive) {
        switch (key) {
          case 'binarify': {
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
    // If we have no queued ops just return
    if (queuedOps.length === 0) {
      return [];
    }
    // Now actually process the images
    let processed:Promise<HTMLImageElement>[] = [];
    for (let i = 0; i < rawArray.length; i++) {
      processed.push(processImage(HTMLImageElement[i]));
    }
    return await Promise.all(processed);
  };

  // Takes in an image source, does some processing on it, and then returns the resulting image source
  export const processImage = async (raw: HTMLImageElement): Promise<HTMLImageElement> => {
    // const rawImage = await createImage(raw);
    // Onload we can do canvas stuff
    // Set canvas width and height
    canvas.width = raw.naturalWidth;
    canvas.height = raw.naturalHeight;

    // Then draw the image
    ctx.drawImage(raw, 0, 0);
    // Get the image data
    let imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    // Then loop through, modify and return image data
    const d = imageData.data;


    // await modifyImgData(imageData.data, queuedOps);
    await Promise.resolve().then(() => {
      for (let i = 0; i < d.length; i += 4) {
        // [imageData.data[i], imageData.data[i+1], imageData.data[i+2]] = invertImage([imageData.data[i], imageData.data[i+1], imageData.data[i+2]]);

        const gray =
          0.2126 * imageData.data[i] +
          0.7152 * imageData.data[i + 1] +
          0.0722 * imageData.data[i + 2];
        // Now we cross check it with our threshold
        // < for only grayscale
        // > for invert + grayscale
        if (gray > $options.binarify.parameters.threshold) {
          imageData.data[i] = 0;
          imageData.data[i + 1] = 0;
          imageData.data[i + 2] = 0;
        } else {
          imageData.data[i] = 255;
          imageData.data[i + 1] = 255;
          imageData.data[i + 2] = 255;
        }
        // d[i] = 255 - d[i];
        // d[i + 1] = 255 - d[i + 1];
        // d[i + 2] = 255 - d[i + 2];
      }
    });
    // Draw onto canvas
    ctx.putImageData(imageData, 0, 0);
    // Append canvas DEBUGGGGGGGGGGGGGGGGG
    document.body.appendChild(canvas);
    // Canvas to base64
    const dataURL = canvas.toDataURL();
    // base64 to image
    return await createImage(dataURL);
  };

  // DEBUGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGg

  const modifyImgData = async (
    imageData: ImageData['data'],
    queuedOps: pixelProcessor[]
  ) => {
    for (let i = 0; i < imageData.length; i += 4) {
      // [imageData.data[i], imageData.data[i+1], imageData.data[i+2]] = invertImage([imageData.data[i], imageData.data[i+1], imageData.data[i+2]]);

      // const gray =
      //   0.2126 * imageData.data[i] +
      //   0.7152 * imageData.data[i + 1] +
      //   0.0722 * imageData.data[i + 2];
      // // Now we cross check it with our threshold
      // if (gray < $options.binarify.parameters.threshold) {
      //   imageData.data[i] = 0;
      //   imageData.data[i + 1] = 0;
      //   imageData.data[i + 2] = 0;
      // } else {
      //   imageData.data[i] = 255;
      //   imageData.data[i + 1] = 255;
      //   imageData.data[i + 2] = 255;
      // }
      imageData[i] = 255 - imageData[i];
      imageData[i + 1] = 255 - imageData[i + 1];
      imageData[i + 2] = 255 - imageData[i + 2];
    }
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

  // interface pixelProcessor {
  //   (pixel: number[]): Promise<number[]>
  // }

  type pixelProcessor = (pixel: number[]) => number[];

  const binaryImage: pixelProcessor = (pixel) => {
    // First need to set pixels to grayscale
    // We use the luminosity equation for grayscale conversion
    // from https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale
    const gray = 0.2126 * pixel[0] + 0.7152 * pixel[1] + 0.0722 * pixel[2];
    // Now we cross check it with our threshold
    return gray < $options.binarify.parameters.threshold
      ? [0, 0, 0]
      : [255, 255, 255];
  };

  const invertImage = (pixel) => [
    255 - pixel[0],
    255 - pixel[1],
    255 - pixel[2],
  ];

  // const modifyImgData = async (
  //   imageData: ImageData,
  //   queuedOps: pixelProcessor[]
  // ) => {
  //   let ops = queuedOps.length;
  //   // Loop through all pixels (R,G,B,A)
  //   for (let i = 0; i < imageData.data.length; i += 4) {
  //     // Loop through all required tasks
  //     for (let j = 0; j < ops; ++j) {
  //       // Set pixels equal to the result of the operations
  //       [
  //         imageData.data[i],
  //         imageData.data[i + 1],
  //         imageData.data[i + 2],
  //       ] = queuedOps[j]([
  //         imageData.data[i],
  //         imageData.data[i + 1],
  //         imageData.data[i + 2],
  //       ]);
  //     }
  //   }
  // };
</script>