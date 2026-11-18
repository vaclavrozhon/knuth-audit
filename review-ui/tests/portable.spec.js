import { test, expect } from "@playwright/test";

test("portable catalog, review records, book omission and page coverage", async ({ page }) => {
  const errors = [];
  page.on("pageerror", e => errors.push(e.message));
  await page.goto("/");
  await expect(page.locator(".cards .finding-card")).toHaveCount(817);
  await page.getByRole("textbox", { name: "Search findings" }).fill("F7-C0006");
  await expect(page.locator(".cards .finding-card")).toHaveCount(1);
  await page.locator(".finding-card").click();
  await expect(page.locator(".publication-review")).toContainText("absolute priority is not established");
  await page.getByRole("button", { name: "Read review record" }).click();
  await expect(page.locator(".markdown")).toContainText("F7-C0006");
  await page.getByRole("button", { name: "Back to evidence" }).click();
  await page.getByRole("button", { name: "View page", exact: true }).click();
  await expect(page.getByLabel("Select page")).toHaveCount(0);
  await expect(page.locator(".page-image img")).toHaveCount(0);
  await expect(page.getByRole("dialog")).toContainText("The book is not included");
  await page.getByRole("button", { name: "Close (Esc)", exact: true }).click();
  await page.getByRole("button", { name: "Volume progress", exact: true }).click();
  await expect(page.locator(".volume-progress-card")).toHaveCount(7);
  await expect(page.getByRole("link", { name: "Open book", exact: true })).toHaveCount(0);
  await expect(page.locator(".volume-progress-card").first()).toContainText("Book not included");
  expect(errors).toEqual([]);
});

test("local notes survive reload and can be exported", async ({ page, request }) => {
  await page.goto("/#F014");
  const note = "Portable test note: ε < 1.\n<b>Literal markup</b>";
  await page.getByLabel("Note", { exact: true }).fill(note);
  await expect(page.locator(".save-status")).toHaveText("Saved");
  await page.getByLabel("My verdict", { exact: true }).selectOption("verified");
  await expect(page.locator(".save-status")).toHaveText("Saved");
  await page.reload();
  await expect(page.getByLabel("Note", { exact: true })).toHaveValue(note);
  await expect(page.getByLabel("My verdict", { exact: true })).toHaveValue("verified");
  const exported = await (await request.get("/api/export")).json();
  expect(exported.annotations.F014.note).toBe(note);
});

test("small-screen card and argument stay usable", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/#V1-C0002");
  await expect(page.getByRole("dialog")).toBeVisible();
  await page.getByRole("button", { name: "Read original audit notes" }).click();
  await expect(page.locator(".markdown")).toContainText("V1-C0002");
  await page.locator(".markdown").getByRole("link", { name: "Review record", exact: true }).click();
  await expect(page.locator(".markdown")).toContainText("V1-C0002");
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
});
