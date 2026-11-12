import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./tests",
  testMatch: "*.spec.js",
  workers: 1,
  retries: 0,
  use: {
    baseURL: "http://127.0.0.1:4319",
    viewport: { width: 1440, height: 1000 },
    trace: "retain-on-failure",
  },
  webServer: {
    command: "python3 tests/browser_server.py",
    url: "http://127.0.0.1:4319",
    reuseExistingServer: false,
    timeout: 15000,
  },
});
