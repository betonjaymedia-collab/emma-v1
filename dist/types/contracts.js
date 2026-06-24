"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ComponentSchema = exports.SystemStateEnum = void 0;
const zod_1 = require("zod");
exports.SystemStateEnum = zod_1.z.enum([
    "LOCKED",
    "SUPERSEDED",
    "PARTIAL",
    "DISCARDED"
]);
exports.ComponentSchema = zod_1.z.object({
    id: zod_1.z.string().uuid(),
    name: zod_1.z.string(),
    status: exports.SystemStateEnum,
    definition: zod_1.z.string(),
    dependencies: zod_1.z.object({
        relies_on: zod_1.z.array(zod_1.z.string()),
        impacts: zod_1.z.array(zod_1.z.string())
    }),
    updatedAt: zod_1.z.date()
});
