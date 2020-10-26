<script lang="ts">
  interface hocrType {
    blocks: [
      {
        bbox: {
          x0: number;
          y0: number;
          x1: number;
          y1: number;
        };
        page: {
          text: string;
        };
      }
    ];
  }
  export let ocrdImage: hocrType;
  // debug
  // console.log(ocrdImage);
</script>

<style lang="scss">
  // main {
    // text-align: center;
    // max-width: 240px;
    // margin: 0 auto;
    // width: 100%;
    // height: 100%;
  // }
</style>

{@debug ocrdImage}
<main>
  {#each ocrdImage.blocks as block, i}
    <div>{block.page.text}</div>
  {/each}
</main>
