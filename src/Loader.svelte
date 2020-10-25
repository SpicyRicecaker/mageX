<script lang="ts">
  import { fade } from 'svelte/transition';
  export let message = '';
</script>

<style lang="scss">
  main {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .loader {
    // background-color: #2b2b2b;
    width: 1rem;
    height: 1rem;
    border-radius: 50%;
    border: 0.2rem #bababa solid;
    border-top: 0.2rem #2b2b2b solid;
    animation: spin 2s linear infinite;
  }
  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
</style>

<main>
  <div transition:fade class="loader" />
  <div transition:fade>{message}</div>
</main>
