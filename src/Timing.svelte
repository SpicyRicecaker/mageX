<script context="module" lang="ts">
  export const beg = (): number => Date.now();
  export const end = (start: number, msg: string) =>
    console.log(`Took ${beg() - start}ms to ${msg}.`);
</script>
