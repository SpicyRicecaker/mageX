<script context="module">
  // We're getting an array of strings (or urls), and returning an array of result.data sure!
  // srcArray: string[]
  let worker;
  export const tesseractRecognize = async (srcArray) => {
    // Tesseract.setLogging(true);
    const outArray = [];

    for (let i = 0; i < srcArray.length; ++i) {
      outArray.push((await worker.recognize(srcArray[i])).data);
    }
    return await outArray;
  };

  export const killTesseractWorkers = async () => {
    await worker.terminate();
  };
</script>

<script>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
  import { lang, ready } from './stores.js';

  // DEBUG
  // import { onMount } from 'svelte';
  // let photos = [];

  // onMount(async () => {
  //   console.log('hi');
  //   const res = await fetch(
  //     `https://jsonplaceholder.typicode.com/photos?_limit=20`
  //   );
  //   photos = await res.json();
  // });
  // DEBUG

  export const spawnTesseractWorkers = async () => {
    worker = Tesseract.createWorker({
      logger: (m) =>
        dispatch('work', {
          status: m.status,
          progress: m.progress,
        }),
    });

    await worker.load();
    await worker.loadLanguage($lang);
    await worker.initialize($lang);
    await ready.set(true);
  };
  export const changeWrokerLang = async () => {
    await worker.terminate();
    await spawnTesseractWorkers();
    await ready.set(false);
  };
</script>

<svelte:head>
  <script
    on:load={spawnTesseractWorkers}
    src="https://unpkg.com/tesseract.js@v2.1.0/dist/tesseract.min.js">
  </script>
</svelte:head>
