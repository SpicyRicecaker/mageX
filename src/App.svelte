<script lang="ts">
  import type { SvelteComponent } from 'svelte';
  // The nav module is basically the tabbed view manager
  import Tab from './Tab.svelte';

  // Import OCR tab
  import Translate from './Translate.svelte';
  // Import Options tab for image processing
  import Options from './Options.svelte';

  interface viewItem {
    label: string;
    value: number;
    component: typeof SvelteComponent;
  }

  interface viewItems extends Array<viewItem> {}

  // Views is all of our components that we just imported in an array
  const views: viewItems = [
    {
      label: 'Translate',
      value: 0,
      component: Translate,
    },
    {
      label: 'Options',
      value: 1,
      component: Options,
    },
  ];
</script>

<style lang="scss">
  // The styling in here mostly just adapts for small displays
  // Then maximizes the canvas
  main {
    max-width: 240px;
    width: 100%;
    height: 100%;
  }
  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>

<main>
  <!-- As for functions, we just spread / inject our views into the nav -->
  <Tab {views} />
</main>
