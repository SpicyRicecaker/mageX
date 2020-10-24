<script context="module">
  // We're getting an array of strings (or urls), and returning an array of result.data sure!
  // srcArray: string[]
  export const tesseractRecognize = async (srcArray) => {
    const worker = Tesseract.createWorker({
      logger: (m) => console.log(m),
    });
    // Tesseract.setLogging(true);
    (async () => {
      const outArray = [];
      await worker.load();
      await worker.loadLanguage('eng');
      await worker.initialize('eng');

      for (let i = 0; i < srcArray.length; ++i) {
        outArray.push((await worker.recognize(srcArray[i])).data);
      }
      console.log(outArray);

      await worker.terminate();
    })();
  };
</script>

<script>
</script>

<svelte:head>
  <script src="https://unpkg.com/tesseract.js@v2.1.0/dist/tesseract.min.js">
  </script>
</svelte:head>
