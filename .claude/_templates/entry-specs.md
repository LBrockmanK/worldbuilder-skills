<%*
const type = "spec";
const name = await tp.system.prompt("Note name", "", true);
const slug = name.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
await tp.file.rename(moment.utc().format("YYYY-MM-DD") + "-" + slug);
tR += await tp.file.include("[[type-" + type + "]]");
-%>
