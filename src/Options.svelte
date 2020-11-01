<script lang="ts">
  import { options } from './stores';
</script>

<style lang="scss">
</style>

<main>
  <div>
    <div>
      <label for="invert">Is text white on black?</label>
      <input
        bind:checked={$options.invert.isActive}
        id="invert"
        type="checkbox" />
    </div>
    <div>
      <label for="binarify">Binarify the image?</label>
      <input
        bind:checked={$options.binarify.isActive}
        id="binarify"
        type="checkbox" />
    </div>
    <div>
      <label for="threshold">Binary threshold {$options.binarify.parameters.threshold}</label>
      <input
        id="threshold"
        type="range"
        min="0"
        max="255"
        bind:value={$options.binarify.parameters.threshold} />
    </div>
  </div>
</main>
