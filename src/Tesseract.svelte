<!--<script context="module" ✂prettier:content✂="Cg==" ✂prettier:content✂="e30=">{}</script>-->
<script context="module">
  // We're getting an array of strings (or urls), and returning an array of result.data sure!
  // srcArray: string[]
  let worker;
  export const tesseractRecognize = async (srcArray) => {
    // Tesseract.setLogging(true);
    (async () => {
      const outArray = [];

      for (let i = 0; i < srcArray.length; ++i) {
        outArray.push((await worker.recognize(srcArray[i])).data);
      }
      return await outArray;
    })();
  };

  export const killTesseractWorkers = async () => {
    await worker.terminate();
  };
</script>

<script>
  import { lang } from './stores.js';
  export const spawnTesseractWorkers = async () => {
    worker = Tesseract.createWorker({ logger: (m) => console.log(m) });
    (async () => {
      await worker.load();
      await worker.loadLanguage($lang);
      await worker.initialize($lang);
    })();
  };
  export const changeWrokerLang = async () => {
    await worker.terminate();
    await spawnTesseractWorkers();
  }
</script>

<svelte:head>
  <script
    on:load={spawnTesseractWorkers}
    src="https://unpkg.com/tesseract.js@v2.1.0/dist/tesseract.min.js">
  </script>
</svelte:head>
