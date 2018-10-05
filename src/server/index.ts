import "../globals";

import net = require("net");
import Sy  = require("nodesynth");

const ns: Synth = new Sy.Synth(SYNTH_OPTIONS);

var vco:  Oscillator = new Sy.Oscillator("sin", 0x000);
var lfo1: Oscillator = new Sy.Oscillator("sin", 0x000);
var lfo2: Oscillator = new Sy.Oscillator("sin", 0x000);

ns.source = vco.mix(lfo1).mix(lfo2);

net.createServer((client: any): void => {
  console.log("client connect -->", client.address().address);
  ns.play();
  manageEvents(client);

  client.on("end", () => {
    console.log("client disconnected -->", client.address().address);
    ns.stop();
  });
})
.on("error", (err: any) => {
  throw new Error(err);
})
.listen(SOCK_PORT);

function manageEvents(client: net.Socket): void {
  client.on("data", (chunk: Buffer): void => {
    var event: Action = JSON.parse(chunk.toString("utf8"));

    switch (event.type) {
      case "vco:freq:set":
        vco.freq = <Frequency>event.value;
      break;
      case "vco:function:set":
        vco.setFunction(WAVEFORMS[event.value]);
      break;
      case "lfo1:freq:set":
        lfo1.freq = <Frequency>event.value;
      break;
      case "lfo1:function:set":
        lfo1.setFunction(WAVEFORMS[event.value]);
      break;
      case "lfo2:freq:set":
        lfo2.freq = <Frequency>event.value;
      break;
      case "lfo2:function:set":
        lfo2.setFunction(WAVEFORMS[event.value]);
      break;
      default:break;
    }
  });
}

// ns.play();