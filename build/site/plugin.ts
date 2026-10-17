import * as path from 'path';

export function wordlePlugin({ courseDir }: { courseDir: string }) {
  return {
    styles: [path.join(courseDir, 'build/site/assets/wordle.css')],
    scripts: [path.join(courseDir, 'build/site/assets/wordle.js')],
  };
}
