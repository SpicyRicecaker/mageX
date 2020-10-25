import { writable } from 'svelte/store';

export const lang = writable('chi_sim');

export const ready = writable(false);

export const options = writable({ binary: false, invert: false });
