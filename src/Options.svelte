<script lang="ts">
  import { options } from './stores.js';
</script>

<style lang="scss">
</style>

<main>
  <label for="invert">Is text white on black?</label>
  <input bind:checked={$options.invert} id="invert" type="checkbox" />
</main>
