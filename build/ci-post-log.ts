// DEBUG: posts the tail of the CI gate log into a draft release, because Forgejo shows no job logs through its API.
import * as fs from 'node:fs';

const log = fs.readFileSync('.courseware/ci/ci-build.log', 'utf8').slice(-60000);
const fence = '`'.repeat(3);
const response = await fetch(`${process.env.GITHUB_SERVER_URL}/api/v1/repos/${process.env.GITHUB_REPOSITORY}/releases`, {
  method: 'POST',
  headers: { Authorization: `token ${process.env.GITHUB_TOKEN}`, 'Content-Type': 'application/json' },
  body: JSON.stringify({
    tag_name: `ci-debug-${process.env.GITHUB_SHA!.slice(0, 7)}`,
    target_commitish: process.env.GITHUB_SHA,
    name: 'ci debug log',
    body: `${fence}\n${log}\n${fence}`,
    draft: true,
  }),
});
console.log(response.status);
