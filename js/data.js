const ROOT = new URL('../data/', import.meta.url);
let manifestPromise, indexPromise;
const shardCache = new Map();
export async function getManifest(){return manifestPromise ||= fetch(new URL('manifest.json',ROOT)).then(check).then(r=>r.json())}
export async function getIndex(){return indexPromise ||= fetch(new URL('index.json',ROOT)).then(check).then(r=>r.json())}
export async function getCategory(category){if(!shardCache.has(category)){const promise=fetch(new URL(`${category}.json`,ROOT)).then(check).then(r=>r.json());shardCache.set(category,promise)}return shardCache.get(category)}
export async function getRecord(id){const index=await getIndex();const hit=index.find(x=>x.id===id);if(!hit)return null;const rows=await getCategory(hit.category);return rows.find(x=>x.id===id)||null}
function check(r){if(!r.ok)throw new Error(`Chargement impossible (${r.status})`);return r}
