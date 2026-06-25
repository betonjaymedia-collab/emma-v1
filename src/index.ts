import crypto from "crypto";
import { insertComponent } from "./db/componentRepository";

const testComponent = {
  id: crypto.randomUUID(),
  name: "TestComponent",
  status: "LOCKED",
  definition: "Test definition",
  dependencies: {
    relies_on: [],
    impacts: [],
  },
  updatedAt: new Date(),
};

async function run() {
  try {
    await insertComponent(testComponent);
    console.log("✅ Component inserted into DB");
  } catch (err) {
    console.error("❌ Insert Error:", err);
  }
}

run();