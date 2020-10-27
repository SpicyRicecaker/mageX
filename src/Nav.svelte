<script lang="ts">
  import type { SvelteComponent } from 'svelte';
  import { slide } from 'svelte/transition';

  interface viewItem {
    label: string;
    value: number;
    component: typeof SvelteComponent;
  }

  interface viewItems extends Array<viewItem> {}

  export let views: viewItems;
  export let activeView;

  let visible = false;
</script>

<style lang="scss">
  $munchingOrange: #f1c232;
  $msTake: #e06666;
  $notGray: #f3f3f3;
  * {
    margin: 0;
    padding: 0;
  }

  main {
    position: sticky;
    z-index: 1;
  }

  nav {
    display: flex;
    flex-direction: row;
    align-items: center;
    background-color: white;
  }
  button {
    background: white;
    outline: none;
    border: none;
    padding: 1rem;
    border-radius: 0;
    transition: 1s;
    &:hover {
      color: $munchingOrange;
      cursor: pointer;
    }
    &:active {
      transition: 0s;
      background: $munchingOrange;
      color: white;
    }
  }
  h1 {
    padding: 0rem 1rem;
    font-family: 'Bebas Neue', cursive;
  }
  a {
    color: black;
    &:hover {
      text-decoration: none;
    }
  }
  .dropdown {
    display: flex;
    flex-direction: column;
    position: absolute;
    width: 100%;
    box-shadow: 0rem 5rem 5rem 0.2rem lightgray;
  }
  .center {
    flex: 1;
  }
</style>

<main>
  <nav>
    <span class="left">
      <h1><a href="/">mageX</a></h1></span>
    <span class="center" />
    <span class="right"><button
        on:click={() => {
          visible = !visible;
        }}><span>|||</span></button>
    </span>
  </nav>
  {#if visible}
    <div
      class="dropdown"
      on:click={() => {
        visible = false;
      }}
      transition:slide|local>
      {#each views as view}
        <button
          on:click={() => {
            activeView = view.value;
          }}><span>{view.label}</span>
        </button>
      {/each}
    </div>
  {/if}
</main>
