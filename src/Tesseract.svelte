<script lang="ts">
  // Prevent the default paste action, don't need for images i think
  // e.preventDefault();

  // const

  Tesseract.recognize(
    'https://tesseract.projectnaptha.com/img/eng_bw.png',
    'eng',
    { logger: (m) => console.log(m) }
  ).then(({ data: { text } }) => {
    console.log(text);
  });
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
  <script src="https://unpkg.com/tesseract.js@v2.1.0/dist/tesseract.min.js">
  </script>
</svelte:head>
