declare type Synth      = any;
declare type Oscillator = any;
declare type Frequency  = number;

declare type Waveform   = "sin" | "cos" | "saw" | "tri" | "sq";
declare type SampleRate = 44100 | 48000 | 50000;
declare type BitDepth   = 16 | 32;

declare interface Action { 
  type: string; 
  value: number; 
}

declare var SOCK_PORT: number;
declare var WAVEFORMS: Array<Waveform>;
declare var SYNTH_OPTIONS: Object;

declare var AUDIO_NODES: Array<Oscillator>;

declare function manageEvents<T>(client: T): void;