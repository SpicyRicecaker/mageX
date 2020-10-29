import { writable } from 'svelte/store';

export const lang = writable('chi_sim');

// Blocks, lines, or words
export const hocrDisplay = writable('lines');

export const ready = writable(false);

export const options = writable({
  binarify: { parameters: { threshold: 127 }, isActive: false },
  invert: { isActive: false },
});
