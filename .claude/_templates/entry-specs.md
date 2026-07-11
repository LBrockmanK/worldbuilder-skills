<%*
const type = "spec";
const name = await tp.system.prompt("Note name", "", true);
const slug = name.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
await tp.file.rename(moment.utc().format("YYYY-MM-DD") + "-" + slug);
let content = await tp.file.include("[[type-" + type + "]]");
// tp.file.title binds before the rename; stamp the real name
const safe = name.replace(/'/g, "''");
content = content.replace(/^title: .*$/m, () => "title: '" + safe + "'");
content = content.replace(/^# .*$/m, () => "# " + name);
tR += content;
-%>
