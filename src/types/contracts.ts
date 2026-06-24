import { z } from "zod";

export const SystemStateEnum = z.enum([
  "LOCKED",
  "SUPERSEDED",
  "PARTIAL",
  "DISCARDED"
]);

export const ComponentSchema = z.object({
  id: z.string().uuid(),
  name: z.string(),
  status: SystemStateEnum,
  definition: z.string(),
  dependencies: z.object({
    relies_on: z.array(z.string()),
    impacts: z.array(z.string())
  }),
  updatedAt: z.date()
});

export type Component = z.infer<typeof ComponentSchema>;