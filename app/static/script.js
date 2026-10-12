// Loads the content from the API and fills the page.
// This is the "frontend talks to backend" part: the HTML has empty boxes,
// and JavaScript fills them with JSON from /api/...

async function getJSON(path) {
  const response = await fetch(path);
  if (!response.ok) throw new Error(`${path} returned ${response.status}`);
  return response.json();
}

// Small helper to build elements without writing HTML strings (safer: no injection).
function el(tag, props = {}, children = []) {
  const node = Object.assign(document.createElement(tag), props);
  for (const child of [].concat(children)) {
    if (child) node.append(child);
  }
  return node;
}

function renderLinks(container, links) {
  const labels = { github: "GitHub", linkedin: "LinkedIn", email: "Email" };
  Object.entries(links).forEach(([key, url], i) => {
    container.append(el("a", { className: i % 2 ? "btn alt" : "btn", href: url, textContent: labels[key] || key }));
  });
}

function typeTerminal(lines) {
  const target = document.getElementById("terminal-text");
  const text = lines.join("\n");
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    target.textContent = text;
    return;
  }
  let i = 0;
  const tick = () => {
    target.textContent = text.slice(0, ++i);
    if (i < text.length) setTimeout(tick, text[i - 1] === "\n" ? 220 : 18);
  };
  tick();
}

async function main() {
  document.getElementById("year").textContent = new Date().getFullYear();

  try {
    const [profile, skills, experience, projects] = await Promise.all([
      getJSON("/api/profile"),
      getJSON("/api/skills"),
      getJSON("/api/experience"),
      getJSON("/api/projects"),
    ]);

    document.getElementById("name").textContent = profile.name;
    document.getElementById("nav-name").textContent = profile.name.toLowerCase();
    document.getElementById("title").textContent = profile.title;
    document.getElementById("summary").textContent = profile.summary;
    renderLinks(document.getElementById("links"), profile.links);
    renderLinks(document.getElementById("contact-links"), profile.links);

    typeTerminal([
      "$ whoami",
      `${profile.name.toLowerCase()} — ${profile.title}`,
      "$ kubectl get pods -n portfolio",
      "NAME                         READY   STATUS    AGE",
      "portfolio-api-7c9f6d-x2k4p   1/1     Running   3d",
      `$ echo "${profile.location}"`,
      profile.location,
    ]);

    document.getElementById("skills-list").append(
      ...skills.map((s) =>
        el("div", { className: "card" }, [
          el("h4", { textContent: s.group }),
          el("ul", { className: "tags" }, s.items.map((item) => el("li", { textContent: item }))),
        ])
      )
    );

    document.getElementById("experience-list").append(
      ...experience.map((job) =>
        el("div", { className: "job" }, [
          el("h4", { textContent: `${job.role} · ${job.company}` }),
          el("span", { className: "period mono", textContent: job.period }),
          el("ul", {}, job.highlights.map((h) => el("li", { textContent: h }))),
        ])
      )
    );

    document.getElementById("projects-list").append(
      ...projects.map((p) =>
        el("div", { className: "card" }, [
          el("h4", { textContent: p.name }),
          el("p", { textContent: p.description }),
          el("ul", { className: "tags" }, p.tags.map((t) => el("li", { textContent: t }))),
          p.url ? el("p", {}, el("a", { href: p.url, textContent: "View on GitHub →" })) : null,
        ])
      )
    );
  } catch (err) {
    console.error(err);
  }

  const status = document.getElementById("api-status");
  try {
    const health = await getJSON("/health");
    status.textContent = health.status === "ok" ? "online" : "degraded";
    status.classList.add(health.status === "ok" ? "up" : "down");
  } catch {
    status.textContent = "offline";
    status.classList.add("down");
  }
}

main();
