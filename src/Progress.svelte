<script lang="ts">
  import { tweened } from 'svelte/motion';
  import { cubicOut } from 'svelte/easing';
  export let status = 'none';
  export let progress = 0;

  const niceProgress = tweened(0, {
    duration: 400,
    easing: cubicOut,
  });

  $: niceProgress.set(progress);
</script>

<style lang="scss">
  main {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  // #wrapper {
  // position: absolute;
  // }

  // @media (min-width: 640px) {
  //   main {
  //     max-width: none;
  //   }
  // }
</style>

<main>
  <div id="wrapper">
    <label for="progress">{status}: {Math.round($niceProgress * 100)}%</label>
    <progress id="progress" value={$niceProgress} />
  </div>
</main>
