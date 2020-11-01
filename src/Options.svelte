<script lang="ts">
  import { options, images, processed } from './stores';
  import ProcessImage from './ProcessImage.svelte';

  let processImageComponent;

  const updateProcessed = async () => {
    $processed = await processImageComponent.processImageAll($images);
  };
</script>

<style lang="scss">
  .main {
    width: 100%;
    height: 100%;
    position: relative;
    overflow: hidden;
  }

  .wrapper {
    background-color: aliceblue;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .imageWrapper {
    flex: 1;
    display: flex;
    overflow: auto;
  }
</style>

<main>
  <div>
    <div>
      <label for="invert">Is text white on black?</label>
      <input
        bind:checked={$options.invert.isActive}
        on:change={updateProcessed}
        id="invert"
        type="checkbox" />
    </div>
    <div>
      <label for="binarify">Binarify the image?</label>
      <input
        bind:checked={$options.binarify.isActive}
        on:change={updateProcessed}
        id="binarify"
        type="checkbox" />
    </div>
    <div>
      <label for="threshold">Binary threshold
        {$options.binarify.parameters.threshold}</label>
      <input
        id="threshold"
        type="range"
        min="0"
        max="255"
        bind:value={$options.binarify.parameters.threshold}
        on:change={updateProcessed} />
    </div>
  </div>
</main>

<div class="main">
  <div class="wrapper">
    {#each $processed as process}
      <div class="imageWrapper">
        <img src={process.src} alt="processed_image" />
      </div>
    {/each}
  </div>
</div>

<ProcessImage bind:this={processImageComponent} />
