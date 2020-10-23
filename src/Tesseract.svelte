<script lang="ts">
  declare const Tesseract:any;
  // Prevent the default paste action, don't need for images i think
  // e.preventDefault();

  // const

  const loadTesseract = () => {
    const exampleImage = 'https://tesseract.projectnaptha.com/img/eng_bw.png';

    const worker = Tesseract.createWorker({
      logger: (m) => console.log(m),
    });
    Tesseract.setLogging(true);
    work();

    async function work() {
      await worker.load();
      await worker.loadLanguage('eng');
      await worker.initialize('eng');

      let result = await worker.detect(exampleImage);
      console.log(result.data);

      result = await worker.recognize(exampleImage);
      console.log(result.data);

      await worker.terminate();
    }
  };
</script>

<!--<style lang="scss">
  // main {
  //   text-align: center;
  //   max-width: 240px;
  //   margin: 0 auto;
  //   width: 100%;
  //   height: 100%;
  // }

  /* h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  } */

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>-->

<svelte:head>
  <script
    on:load={loadTesseract}
    src="https://unpkg.com/tesseract.js@v2.1.0/dist/tesseract.min.js">
  </script>
</svelte:head>
