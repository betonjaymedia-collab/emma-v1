import { v4 as uuidv4 } from "uuid";
import { ComponentSchema } from "./types/contracts";

const testComponent = {
  id: uuidv4(),
  name: "Test Component",
  status: "LOCKED",
  definition: "Initial test definition",
  dependencies: {
    relies_on: [],
    impacts: []
  },
  updatedAt: new Date()
};

const result = ComponentSchema.safeParse(testComponent);

console.log(result);