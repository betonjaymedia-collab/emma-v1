"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const uuid_1 = require("uuid");
const contracts_1 = require("./types/contracts");
const testComponent = {
    id: (0, uuid_1.v4)(),
    name: "Test Component",
    status: "LOCKED",
    definition: "Initial test definition",
    dependencies: {
        relies_on: [],
        impacts: []
    },
    updatedAt: new Date()
};
const result = contracts_1.ComponentSchema.safeParse(testComponent);
console.log(result);
