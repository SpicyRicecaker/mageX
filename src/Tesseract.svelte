<script context="module">
  // We're getting an array of strings (or urls), and returning an array of result.data sure!
  // srcArray: string[]
  let scheduler;
  export const tesseractRecognize = async (srcArray) => {
    // Tesseract.setLogging(true);
    const outArray = [];

    for (let i = 0; i < srcArray.length; ++i) {
      outArray.push((await scheduler.addJob('recognize', srcArray[i])).data);
    }

    return await outArray;

    // for (let i = 0; i < srcArray.length; ++i){
    //   outArray.push(worker.recognize(srcArray[i]))
    // }

    // await Promise.all(outArray);

    // for (let i = 0; i < srcArray.length; ++i) {
    //   outArray[i] = outArray[i].data;
    // }
    // return outArray;
  };

  export const killTesseractWorkers = async () => {
    await worker.terminate();
  };
</script>

<script>
  // import { createEventDispatcher } from 'svelte';
  // const dispatch = createEventDispatcher();
  import { lang, ready, work } from './stores';

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
  // const shouldSpawnTesseract = () => {
  //   if(!$ready){
  //     spawnTesseractWorkers
  //   }
  // }
  
  const init = async () => {
    await createScheduler();
    scheduler.addWorker(await spawnTesseractWorker());
    await ready.set(true);
  }
  
  export const createScheduler = async () => {
    scheduler = Tesseract.createScheduler();
  }

  export const spawnTesseractWorker = async () => {
    console.log('spawning new workers...');
    let worker;
    // worker = Tesseract.createWorker({
    //   logger: (m) =>
    //     dispatch('work', {
    //       status: m.status,
    //       progress: m.progress,
    //     }),
    // });

    worker = Tesseract.createWorker({
      logger: (m) => {
        $work.status = m.status;
        $work.progress = m.progress;
      },
    });

    await worker.load();
    await worker.loadLanguage($lang);
    await worker.initialize($lang);
    // // Remove spaces between words for chinese & japanese
    switch ($lang) {
      case 'chi_sim': // FALLTHROUGH
      case 'jp': //FALLTHROUGH
        await worker.setParameters({
          preserve_interword_spaces: '1',
        });
        break;
      default:
        break;
    }
    return await worker;
  };

  // export const changeWorkerLang = async () => {
  //   await Promise.all([worker.terminate(), spawnTesseractWorkers()]);
  //   await ready.set(false);
  // };
</script>

<svelte:head>
  <script
    on:load={init}
    src="https://unpkg.com/tesseract.js@v2.1.0/dist/tesseract.min.js">
  </script>
</svelte:head>
