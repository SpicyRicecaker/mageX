<script lang="ts">
  import type { SvelteComponent } from 'svelte';
  import Nav from './Nav.svelte';

  interface viewItem {
    label: string;
    value: number;
    component: typeof SvelteComponent;
  }

  interface viewItems extends Array<viewItem> {}

  export let views: viewItems;
  export let activeView = 0;
</script>

<svelte:head>
  <link
    href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap"
    rel="stylesheet" />
</svelte:head>

<main>
  <Nav {views} {activeView}/>
  {#each views as view}
    {#if activeView === view.value}
      <svelte:component this={view.component} />
    {/if}
  {/each}
</main>
