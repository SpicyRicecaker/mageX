<script lang="ts">
  import { hocrDisplay } from './stores';
  interface hocrType {
    hocr: string;
    blocks: [
      {
        bbox: {
          x0: number;
          y0: number;
          x1: number;
          y1: number;
        };
        baseline: {
          y0: number;
        };
        text: string;
      }
    ];
    lines: [
      {
        bbox: {
          x0: number;
          y0: number;
          x1: number;
          y1: number;
        };
        baseline: {
          y0: number;
        };
        text: string;
      }
    ];
    words: [
      {
        bbox: {
          x0: number;
          y0: number;
          x1: number;
          y1: number;
        };
        baseline: {
          y0: number;
        };
        text: string;
      }
    ];
  }
  export let ocrdImage: hocrType;
  // debug
  console.log(ocrdImage);
</script>

<!--<style lang="scss">
  // main {
  // text-align: center;
  // max-width: 240px;
  // margin: 0 auto;
  // width: 100%;
  // height: 100%;
  // }
</style>-->

<!-- Really inefficient but can't find any other way to make it typescript compatible -->
{#if $hocrDisplay === 'lines'}
  {#each ocrdImage.lines as block}
    <style lang="scss">
      g {
        &:hover rect {
          fill: white;
          opacity: 1;
        }
        &:hover text {
          display: block;
        }
      }
      rect {
        opacity: 0.3;
        fill: lightgreen;
      }
      text {
        fill: black;
        display: none;
      }
    </style>
    <g>
      <rect
        x={block.bbox.x0}
        y={block.bbox.y0}
        width={block.bbox.x1 - block.bbox.x0}
        height={block.bbox.y1 - block.bbox.y0}
        on:click={() => {
          navigator.clipboard.writeText(block.text);
        }} />
      <text x={block.bbox.x0} y={block.baseline.y0}>
        {block.text}
      </text>
    </g>
  {/each}
{:else if $hocrDisplay === 'blocks'}
  {#each ocrdImage.blocks as block}
    <rect
      x={block.bbox.x0}
      y={block.bbox.y0}
      width={block.bbox.x1 - block.bbox.x0}
      height={block.bbox.y1 - block.bbox.y0} />
  {/each}
{:else}
  {#each ocrdImage.words as block}
    <rect
      x={block.bbox.x0}
      y={block.bbox.y0}
      width={block.bbox.x1 - block.bbox.x0}
      height={block.bbox.y1 - block.bbox.y0} />
  {/each}
{/if}
