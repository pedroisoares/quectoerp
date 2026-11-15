// Render the PNG icons and favicon.ico from the SVGs written by build.py.
// Needs Node 18+ and Playwright with Chromium: `npm i -D playwright && npx playwright install chromium`.
// Usage: node brand/scripts/rasterize.mjs
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");
const fav = join(dirname(fileURLToPath(import.meta.url)), "..", "favicon");

const jobs = [
  ["favicon.svg", 16, "favicon-16.png"],
  ["favicon.svg", 32, "favicon-32.png"],
  ["favicon.svg", 48, "favicon-48.png"],
  ["favicon.svg", 192, "icon-192.png"],
  ["favicon.svg", 512, "icon-512.png"],
  ["src/apple-touch-icon.svg", 180, "apple-touch-icon.png"],
  ["src/maskable.svg", 512, "icon-maskable-512.png"],
];

const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 1 });
const out = {};
for (const [src, size, name] of jobs) {
  const svg = readFileSync(join(fav, src), "utf8");
  await page.setViewportSize({ width: size, height: size });
  await page.setContent(
    `<style>html,body{margin:0;background:transparent}svg{display:block;width:${size}px;height:${size}px}</style>${svg}`
  );
  const png = await page.screenshot({ omitBackground: true, clip: { x: 0, y: 0, width: size, height: size } });
  writeFileSync(join(fav, name), png);
  out[name] = png;
  console.log("wrote favicon/" + name);
}
await browser.close();

// favicon.ico with PNG-encoded 16, 32 and 48 px images.
const images = [[16, out["favicon-16.png"]], [32, out["favicon-32.png"]], [48, out["favicon-48.png"]]];
const header = Buffer.alloc(6 + 16 * images.length);
header.writeUInt16LE(0, 0); header.writeUInt16LE(1, 2); header.writeUInt16LE(images.length, 4);
let offset = header.length;
images.forEach(([size, png], i) => {
  const e = 6 + 16 * i;
  header.writeUInt8(size, e); header.writeUInt8(size, e + 1);
  header.writeUInt16LE(1, e + 4); header.writeUInt16LE(32, e + 6);
  header.writeUInt32LE(png.length, e + 8); header.writeUInt32LE(offset, e + 12);
  offset += png.length;
});
writeFileSync(join(fav, "favicon.ico"), Buffer.concat([header, ...images.map(([, p]) => p)]));
console.log("wrote favicon/favicon.ico");
