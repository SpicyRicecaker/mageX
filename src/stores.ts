import { writable } from 'svelte/store';

export const lang = writable('chi_sim');

// Blocks, lines, or words
export const hocrDisplay = writable('lines');

export const ready = writable(false);

export const options = writable({
  binarify: { parameters: { threshold: 127 }, isActive: true },
  invert: { isActive: false },
});

export const images = writable([]);

export const ocrdImages: any = writable(undefined);

export const processed = writable([]);

export const work = writable({
  status: 'downloading tesseract.js',
  progress: 0,
});
